import re
from enum import Enum


class token_type(Enum):
    KEY = "key"
    INDENTIFIER = "indentifier"
    OPERATOR = "operator"
    BRACKETS = "brackets"
    FLOAT = "float"
    INT = "int"
    STRING = "string"
    BLACK = "black"
    EOF = "eof"


class token:
    def __init__(self, type, value, line="unknow") -> None:
        self.type = type
        self.value = value
        self.line = line

    def __repr__(self) -> str:
        return f"type[{self.type}] --> value[{self.value}] in line {self.line}"


match_token = {
    r"\(|\)|\{|\}|\[|\]": token_type.BRACKETS,
    r"[+-]?\d+\.\d+": token_type.FLOAT,
    r"[+-]?\d+": token_type.INT,
    r"\s+": token_type.BLACK,
    r",": token_type.BLACK,
    r"//(.*)?\n|(\r\n)": token_type.BLACK,
    r"'.*?'": token_type.STRING,
    r'".*?"': token_type.STRING,
    # ---------------------------------- operaor --------------------------------- #
    r":?=": token_type.OPERATOR,
    r"[\+\-\*\/]+": token_type.OPERATOR,
    r"[<>(>=)(<=)]": token_type.OPERATOR,
    # ------------------------------------ key ----------------------------------- #
    "(if)|(while)|(else)|(def)": token_type.KEY,
    # -------------------------------- indetifier -------------------------------- #
    r"[a-zA-Z_]+": token_type.INDENTIFIER,
}


class lexer:

    def is_eof(self):
        return self.cursor >= len(self.code)

    def __call__(self, code):
        # init
        self.code = code
        self.cursor = 0
        self.tokens = []
        self.line = 1
        # work
        while not self.is_eof():
            t = self.lex()
            if t.type != token_type.BLACK:
                self.tokens.append(t)

        self.tokens.append(token(type=token_type.EOF, value="eof", line=self.line))
        return self.tokens

    def lex(self) -> token:

        if self.is_eof():
            return token(type=token_type.EOF, value="eof")

        flag = False
        for regexp, type in match_token.items():
            value = re.match(regexp, self.code[self.cursor :])
            if value:
                flag = True
                self.cursor += len(value.group(0))

                if type == token_type.BLACK:
                    self.line += value.group(0).count("\n")

                return token(type=type, value=value.group(0), line=self.line)

        if not flag:
            raise Exception(
                f"line {self.line} with error \t\t\n current >'{self.code[self.cursor:]}'"
            )
