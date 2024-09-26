from .vm import *


# ------------------------------ test4envirment ------------------------------ #
def test4envirment():
    # clone
    env = Env.clone()
    # lookup
    assert env.lookup("version") == VERSION
    # set
    assert env.set("pi", 3.1415926) == 3.1415926
    # next
    env = env.next(local={"next_version": "x.y.z"})
    assert env.lookup("next_version") == "x.y.z"
    # assign
    assert env.assign("version", "0.0.0") == "0.0.0"
    # close
    env = env.close()


# -------------------------------- test4cherry ------------------------------- #


def test4cherry():
    e = vm(Env=Env.clone())
    # 自省
    assert e('"hello"') == "hello"
    assert e(2233) == 2233
    # 变量查看
    assert e("version") == VERSION
    # 变量定义
    assert e(["var", "name", '"gin"']) == "gin"
    # 变量更改
    assert e(["assign", "name", '"mc"']) == "mc"
    # 关键字 if
    assert e(["if", "true", '"yes"', '"no"']) == "yes"
    # 代码块
    e(
        [
            "begin",
            ["var", "times", 10],
            ["if", ["neq", 10, "times"], ["print", '"begin has error"'], "'going'"],
        ]
    )

    # 内置函数变量
    assert e(["var", "ten", 10]) == 10
    assert e(["assign", "ten", ["sub", "ten", 1]]) == 9
    assert not e(["lt", 9, "ten"])
    assert e(["begin", ["assign", "ten", 10]]) == 10

    # 关键字 while
    e(
        [
            "begin",
            [
                "while",
                ["neq", 0, "ten"],
                [
                    "begin",
                    ["assign", "ten", ["sub", "ten", 1]],
                    # ['print', 'ten']
                ],
            ],
        ]
    )

    # 用户函数
    e.Env = Environment(
        {
            "add": lambda x, y: x + y,
            "sub": lambda x, y: x - y,
            "gt": lambda x, y: x > y,
            "lt": lambda x, y: x < y,
        }
    )

    e(["def", "my_add", ["x", "y"], ["add", "x", "y"]])
    assert e(["my_add", 2, 3]) == 5

    e.Env = Environment(
        {
            "add": lambda x, y: x + y,
            "sub": lambda x, y: x - y,
            "gt": lambda x, y: x > y,
            "lt": lambda x, y: x < y,
        }
    )

    e(
        [
            "def",
            "fib",
            ["n"],
            [
                "begin",
                [
                    "if",
                    ["lt", "n", 2],
                    1,
                    ["add", ["fib", ["sub", "n", 1]], ["fib", ["sub", "n", 2]]],
                ],
            ],
        ]
    )

    def fib(n):
        if n < 2:
            return 1
        return fib(n - 1) + fib(n - 2)

    assert e(["fib", 3]) == fib(3)
    e = None

    # 空语句
    b = vm()
    assert (
        b(
            [
                "begin",
            ]
        )
        == None
    )


def test4table():
    # table
    b = vm()
    # print(b.Env)
    b(
        [
            "begin",
            ["var", "table_name", ["table", 0, 1, 2, 3]],
            ["table_set", "table_name", 22, 33],
            ["table_set", "table_name", "'name'", "'gin'"],
            ["print", ["table_get", "table_name", 22]],
            ["print", ["table_get", "table_name", "'gin'"]],
            ["print", ["table_get", "table_name", "'name'"]],
        ]
    )


test4cherry()
test4cherry()
test4table()
