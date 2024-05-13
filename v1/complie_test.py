from complie import *

code = """
:

var ten 10

if > (ten,0) {
    print (ten)
} else {
    ...
}

while > (ten, 0) {
    print ( ten )
    ten = - (ten ,1)
}

def fibo (n) 
:
    if <= (n ,1) {
        1
    } else {
        + (fibo(-(n,1)),fibo(-(n-2))
    }

fibo(8)

"""


def Test(code: str, ast: list):
    tokens = code.replace(",", " ").replace("(", " ( ").replace(")", " ) ").split()
    ast = ast
    try:
        assert parser(tokens) == ast
    except:
        print("Error!")
        print("Want:")
        print(ast)
        print("Get:")
        print(parser(tokens))


# 变量声明
Test("var name 'gin' ", [["var", "name", "'gin'"]])

# 变量修改
Test("name = 123 ", [["assign", "name", 123]])

# 代码块
Test(":", ["begin"])

# 空语句
Test("...", [[]])

# 函数调用
Test(
    """
    sub 123 234
""",
    [["sub", ["sum", 3, 2], 2]],
)
