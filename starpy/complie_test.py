from pprint import pprint as print


from .lexer import lexer
from .compile import parser

l = lexer()
p = parser()


def Test(code, ast: list):
    tokens = l(code)
    ast = ast
    try:
        assert p(tokens) == ast
    except:
        print("Error!")
        print("Want:")
        print(ast, indent=4)
        print("Get:")
        print(p(tokens), indent=4)


# 字面量
Test("1", ["begin", 1])
Test("1.1", ["begin", 1.1])
Test("'i am string'", ["begin", "'i am string'"])
Test("1 2.1 'i am string'", ["begin", 1, 2.1, "'i am string'"])

# 变量声明
Test("a := 1", ["begin", ["var", "a", 1]])
# 变量修改
Test("a = 2", ["begin", ["assign", "a", 2]])
Test(
    """
a := 2 , a = 3
""",
    ["begin", ["var", "a", 2], ["assign", "a", 3]],
)
# 变量赋值
Test(
    """
a := 2
b := a
""",
    ["begin", ["var", "a", 2], ["var", "b", "a"]],
)

# 函数调用
Test(
    """
    my_func(1, 2)
""",
    ["begin", ["my_func", 1, 2]],
)

# 函数嵌套调用
Test(
    """
    func_one(func_two(1, 2),3)
""",
    ["begin", ["func_one", ["func_two", 1, 2], 3]],
)

# 控制流 while
Test(
    """
    while rt(2,1) {
        print(a)
    }
""",
    [
        "begin",
        [
            "while",
            ["rt", 2, 1],
            ["begin", ["print", "a"]],
        ],
    ],
)


Test(
    """
    (a + b + c - 1)
""",
    ["begin", ["add", "a", ["add", "b", ["sub", "c", 1]]]],
)


Test(
    """
    (a)
""",
    ["begin", "a"],
)


Test(
    """
    (a(1) + 9 + (b)  - 7)
""",
    ["begin", ["add", ["a", 1], ["add", 9, ["sub", "b", 7]]]],
)


print("All Test pass")
