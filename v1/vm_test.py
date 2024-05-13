from vm import *


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
    e = VM(Env=Env.clone())
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
            ["if", ["!=", 10, "times"], ["print", '"begin has error"'], "'going'"],
        ]
    )
    # 内置函数变量
    assert e(["var", "ten", 10]) == 10
    assert e(["assign", "ten", ["-", "ten", 1]]) == 9
    assert not e(["<=", 10, "ten"])
    assert e(["begin", ["assign", "ten", 10]]) == 10

    # 关键字 for
    e(
        [
            "for",
            ["!=", 0, "ten"],
            [
                "begin",
                ["assign", "ten", ["-", "ten", 1]],
                # ['print', 'ten']
            ],
        ]
    )

    # 用户函数
    e.Env = Environment(
        {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
            ">": lambda x, y: x > y,
            "<": lambda x, y: x < y,
        }
    )

    e(["def", "add", ["x", "y"], ["+", "x", "y"]])
    assert e(["add", 2, 3]) == 5

    e.Env = Environment(
        {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            ">": lambda x, y: x > y,
            "<": lambda x, y: x < y,
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
                    ["<", "n", 2],
                    1,
                    ["+", ["fib", ["-", "n", 1]], ["fib", ["-", "n", 2]]],
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


test4cherry()
test4cherry()
