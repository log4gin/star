VERSION = "1.0.0"


interface = {
    "true": True,
    "false": False,
    "version": VERSION,
    "pi": 3.1415926,
    "print": print,  # 宿主语言的函数
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
}
