from lexer import token_type


class parser:

    def __call__(self, tokens) -> list:
        self.tokens = tokens
        self.cursor = 0

        return ["begin", *(self.parse())]

    @property
    def current(self):
        if self.cursor >= len(self.tokens):
            return self.tokens[:-1]
        return self.tokens[self.cursor]

    def back(self, setp=1):
        c = self.cursor + setp
        if c > len(self.tokens):
            return self.tokens[-1]
        return self.tokens[c]

    def parse(self) -> list:
        node = []
        while self.current.type != token_type.EOF:
            node.append(self.work())
        return node

    def work(self) -> list | int | str | float:
        match self.current.type:
            case token_type.INT:
                return self.int_literal()
            case token_type.FLOAT:
                return self.float_literal()
            case token_type.STRING:
                return self.string_literal()

            # 变量开头
            case token_type.INDENTIFIER:
                # 变量声明
                if self.back().value == ":=":
                    return self.var_declare()
                # 变量修改
                if self.back().value == "=":
                    return self.var_assign()
                # 函数调用
                if self.back().value == "(":
                    return self.var_call()

                if self.back().value == "[":
                    return self.table_sugar()

                if self.back().value == ".":
                    return self.table_point_sugar()

                if self.back().value == "++":
                    return self.self_add_sugar()

                # 默认只有自己
                return self.var_self()

            case token_type.KEY:
                if self.current.value == "while":
                    return self.while_statment()
                if self.current.value == "if":
                    return self.if_statment()
                if self.current.value == "def":
                    return self.def_statment()

            # 括号开头
            case token_type.BRACKETS:
                if self.current.value == "(":
                    return self.expression_sugar()

            # 操作开头
            case token_type.OPERATOR:
                return self.operator_literal()

            case _:
                raise Exception(f"unknow token {self.current}")

    def int_literal(self) -> int:
        value = int(self.current.value)
        self.cursor += 1
        return value

    def float_literal(self) -> float:
        value = float(self.current.value)
        self.cursor += 1
        return value

    def string_literal(self) -> str:
        value = self.current.value
        self.cursor += 1
        return value

    def operator_literal(self) -> str:
        value = self.current.value
        self.cursor += 1
        return value

    def var_declare(self) -> list:
        name = self.current.value
        self.cursor += 2
        value = self.work()
        return ["var", name, value]

    def var_assign(self) -> list:
        name = self.current.value
        self.cursor += 2
        value = self.work()
        return ["assign", name, value]

    def var_self(self) -> str:
        value = self.current.value
        self.cursor += 1
        return value

    def var_call(self) -> list:
        name = self.current.value
        self.cursor += 2
        args = []
        while self.current.value != ")":
            args.append(self.work())
        self.cursor += 1
        return [name, *args]

    def while_statment(self) -> list:
        self.cursor += 1
        condtion = self.work()
        if self.current.value != "{":
            raise Exception("while loop must be '{'")

        self.cursor += 1
        body = ["begin"]
        while self.current.value != "}":
            body.append(self.work())
        self.cursor += 1
        return ["while", condtion, body]

    def if_statment(self) -> list:
        self.cursor += 1
        condition = self.work()
        if self.current.value != "{":
            raise Exception("if statment must be '{'")

        self.cursor += 1
        body = ["begin"]
        while self.current.value != "}":
            body.append(self.work())
        else_body = ["begin"]
        self.cursor += 1
        if self.current.value == "else":
            self.cursor += 1
            if self.current.value != "{":
                raise Exception("else statment must be '{'")
            self.cursor += 1
            while self.current.value != "}":
                else_body.append(self.work())
            self.cursor += 1
        return ["if", condition, body, else_body]

    def def_statment(self) -> list:
        self.cursor += 1
        if self.current.type != token_type.INDENTIFIER:
            raise Exception("def statment name must be indentifer")
        name = self.current.value
        if self.back().value != "(":
            raise Exception("def statment must be '('")
        self.cursor += 2
        # 参数
        args = []
        while self.current.value != ")":
            arg = self.current
            if arg.type != token_type.INDENTIFIER:
                raise Exception("def statment arg must be indentifer")
            args.append(arg.value)
            self.cursor += 1
        if self.back().value != "{":
            raise Exception("def statment must be '{'")
        self.cursor += 2
        body = ["begin"]
        while self.current.value != "}":
            body.append(self.work())
        self.cursor += 1
        return ["def", name, args, body]

    def table_sugar(self) -> list:
        table_name = self.current.value
        self.cursor += 2
        table_key = self.work()
        if self.current.value != "]":
            raise Exception("table sugar must be ']'")
        # set table
        if self.back().value == "=":
            self.cursor += 2
            table_value = self.work()
            return ["table_set", table_name, table_key, table_value]
        # get table
        self.cursor += 1
        return ["table_get", table_name, table_key]

    def table_point_sugar(self) -> list:
        table_name = self.current.value
        self.cursor += 2

        # 判断key是变量名
        if self.current.type == token_type.INDENTIFIER:
            table_key = "'" + str(self.current.value) + "'"
        else:
            raise Exception("table key must be indentifer or number")

        # set table
        if self.back().value == "=":
            self.cursor += 2
            table_value = self.work()
            return ["table_set", table_name, table_key, table_value]
        # get table
        self.cursor += 1
        return ["table_get", table_name, table_key]

    def expression_sugar(self) -> list:
        self.cursor += 1
        operations = []
        elements = ["("]
        conver_map = {
            "*": "mul",
            "/": "div",
            "-": "sub",
            "+": "add",
            ">": "gt",
            "<": "lt",
            ">=": "gte",
            "<=": "lte",
            "==": "eq",
            "!=": "neq",
        }

        while not (self.current.value == ")" and len(operations) == 0):
            element = self.work()
            if isinstance(element, str) and element in conver_map.keys():
                operations.append(element)
            else:
                elements.append(element)

            # 完成一个函数转换
            if self.current.value == ")":
                while True:

                    if len(elements) == 0:
                        break

                    arg = elements.pop()
                    if arg == "(":
                        break

                    another_arg = elements.pop()
                    if another_arg == "(":
                        elements.append(arg)
                        break

                    elements.append([conver_map[operations.pop()], another_arg, arg])

        self.cursor += 1
        return elements.pop()

    def self_add_sugar(self) -> list:
        value = self.current.value
        self.cursor += 2
        return ["assign", value, ["add", value, 1]]
