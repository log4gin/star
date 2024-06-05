VERSION = "1.1.1"


VERSION_LOG = """
1.0.0 完成 lexer compile vm

1.0.1 修复 深度环境表拷贝导致无法修改外部变量

1.1.1 添加 table
"""


# ---------------------------------------------------------------------------- #
#                                 buid-in table ype                                 #
# ---------------------------------------------------------------------------- #
class table:
    def __init__(self, *arry) -> None:
        self.table = {}
        for i in range(len(arry)):
            self.table[i] = arry[i]

    def __str__(self) -> str:
        return "table:" + str(self.table)

    def get(self, name):
        if name in self.table:
            return self.table[name]
        return None

    def set(self, name, value):
        self.table[name] = value
        return self.table[name]


def _table_init(*arry):
    return table(*arry)


def _table_set(t: table, name, value):
    return t.set(name, value)


def _table_get(t: table, name):
    return t.get(name)


# ---------------------------------------------------------------------------- #
#                                other function                                #
# ---------------------------------------------------------------------------- #


def _now() -> str:
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
    "now": _now,
    "table": _table_init,
    "table_set": _table_set,
    "table_get": _table_get,
}
