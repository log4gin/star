VERSION_LOG = """
1.0.0 完成 lexer compile vm

1.0.1 修复 深度环境表拷贝导致无法修改外部变量

1.1.0 添加 table

1.2.0 添加 table 语法糖 

1.3.0 添加 load 多文件编程 

1.4.0 修改 +-*/ 为表达式而不是函数
"""

VERSION = VERSION_LOG.split("\n")[-2].split()[0]


# ---------------------------------------------------------------------------- #
#                                 build-in table type                           #
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
#                                    package                                   #
# ---------------------------------------------------------------------------- #


def _load(path) -> int | str | float | table:
    from lexer import lexer
    from compile import parser
    from vm import vm

    l = lexer()
    p = parser()
    v = vm()

    with open(path, "r", encoding="utf-8") as f:
        tokens = l(f.read())
        ast = p(tokens)
        resout = v(ast)

        return resout


# ---------------------------------------------------------------------------- #
#                                other function                                #
# ---------------------------------------------------------------------------- #


def _now() -> str:
    from datetime import datetime

    return str(datetime.now())


def _panic(exception):
    raise Exception(exception)


interface = {
    "nil": None,
    "true": True,
    "false": False,
    "version": VERSION,
    "pi": 3.1415926,
    "ne": lambda x, y: x != y,
    "eq": lambda x, y: x == y,
    "rt": lambda x, y: x > y,
    "lt": lambda x, y: x < y,
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "print": print,
    "now": _now,
    "table": _table_init,
    "table_set": _table_set,
    "table_get": _table_get,
    "load": _load,
    "panic": _panic,
}
