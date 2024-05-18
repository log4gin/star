VERSION = "1.0.1"


def now() -> str:
    from datetime import datetime

    return str(datetime.now())


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
    "now": now,
}
