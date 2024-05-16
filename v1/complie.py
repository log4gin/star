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

    def front(self, setp=1):
        c = self.cursor - setp
        if c < 0:
            raise Exception("front token out of range")
        return self.tokens[c]

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
                # 默认只有自己
                return self.var_self()

            case token_type.KEY:
                if self.current.value == "while":
                    return self.while_loop()
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

    def while_loop(self) -> list:
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
