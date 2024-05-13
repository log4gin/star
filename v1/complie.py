import re


# name
regexp_variable_name = re.compile(r"(\w+)|([/+-/*//])+|_+")

# float
regexp_variable_float = re.compile(r"[+-]?\d+\.\d+")

# int
regexp_variable_int = re.compile(r"[+-]?\d+")

# str
regexp_variable_str = re.compile(r"(^'/w*'$)")


def parser(tokens: list) -> list:
    ast = []
    current = -1

    def walk() -> list | str | int | float:
        nonlocal current
        current += 1
        token = tokens[current]

        # 普通数字
        if regexp_variable_float.fullmatch(token):
            return float(token)
        if regexp_variable_int.fullmatch(token):
            return int(token)
        if isinstance(token, str) and token[0] == "'" and token[-1] == "'":
            return token

        if token == "var":
            current += 1
            name = tokens[current]

            if not regexp_variable_name.fullmatch(name):
                raise Exception(f"Invalid variable name: {name}")

            value = walk()
            return ["var", name, value]

        if token == ":":
            return "begin"

        if token == "...":
            return []

        # name = 'me'
        # print ( name )
        if regexp_variable_name.fullmatch(token):

            name = token

            current += 1
            operator = tokens[current]

            # 变量更改
            if operator == "=":

                current += 1
                value = tokens[current]

                if regexp_variable_float.fullmatch(value):
                    value = float(value)
                    return ["assign", name, value]

                if regexp_variable_int.fullmatch(value):
                    value = int(value)
                    return ["assign", name, value]

                return ["assign", token, value]

            # 函数调用
            # sub(sum(3,2),5)
            # ["sub", ["sum", 3, 2], 5]
            # if operator == "(":
            #     args = []
            #     # Parse function arguments
            #     while tokens[current] != ")":
            #         args.append(walk())
            #         current += 1
            #         # Skip the closing parenthesis
            #         current += 1
            #     return [name, *args]

            return name

    while current < len(tokens) - 1:
        ast.append(walk())
    return ast
