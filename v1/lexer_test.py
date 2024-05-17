from lexer import *
from pprint import pprint as print

code = """a := 1 // i am comment
b := 2.1
c := 'hello'
d := "halo"

if a > b {
    print(a)
} else {
    print(b)


def my_func(a, b) {
    a + b
}

my_func(1, 2)

// hi

"""

l = lexer()

print(l(code), indent=4)
