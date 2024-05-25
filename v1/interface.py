VERSION = "1.1.1"

VERSION_LOG = """
1.0.0 完成 lexer compile vm

1.0.1 修复 深度环境表拷贝导致无法修改外部变量

1.1.1 添加 list
"""


def _now() -> str:
    from datetime import datetime

    return str(datetime.now())


def _list(*a) -> list:
    return list(a)


interface = {
    "true": True,
    "false": False,
    "version": VERSION,
    "pi": 3.1415926,
    "!=": lambda x, y: x != y,
    "==": lambda x, y: x == y,
    ">": lambda x, y: x > y,
    "<": lambda x, y: x < y,
    ">=": lambda x, y: x >= y,
    "<=": lambda x, y: x <= y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "print": print,
    "now": _now,
    "list": _list,
}
