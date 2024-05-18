# ---------------------------------------------------------------------------- #
#                                  Environment                                 #
# ---------------------------------------------------------------------------- #


class Environment:

    def __init__(self, local={}, parent=None) -> None:
        self.local = local
        self.parent = parent

    def __repr__(self) -> str:
        return f"Environment: {self.local}"

    def lookup(self, name):
        if name in self.local:
            return self.local[name]
        if self.parent is not None:
            return self.parent.lookup(name)

        raise Exception(f'"{name}" is not find in Environment')

    def set(self, name, value):
        self.local[name] = value
        return self.local[name]

    def assign(self, name, value):
        if name in self.local:
            return self.set(name, value)
        if self.parent is not None:
            return self.parent.assign(name, value)

        raise Exception(f'"{name}" is not find in Environment')

    def clone(self):
        return Environment(self.local, self.parent)

    def next(self, local={}):
        env = self.clone()

        return Environment(local, env)

    def close(self):
        if self.parent is None:
            return self
        return self.parent


from interface import VERSION, interface

Env = Environment(local=interface)


# ---------------------------------------------------------------------------- #
#                                     tools                                    #
# ---------------------------------------------------------------------------- #


# '"abc"' or "'abc'"
def is_string(exp):
    if not isinstance(exp, str):
        return False
    if (exp[0] == '"' and exp[-1] == '"') or (exp[0] == "'" and exp[-1] == "'"):
        return True


# 123 or 1.23
def is_number(exp):
    return isinstance(exp, (int, float))


# "abc" or 'abc'
def is_var(exp):
    if is_number(exp):
        return False
    if isinstance(exp, list):
        return False
    return True


def is_list(exp):
    return isinstance(exp, list)


def is_dict(exp):
    return isinstance(exp, dict)


# ---------------------------------------------------------------------------- #
#                                    vm                                   #
# ---------------------------------------------------------------------------- #


class vm:

    def __init__(self, Env=Env.clone()) -> None:
        self.Env = Env

    def __call__(self, exp):
        return self.Eval(exp)

    def Eval(self, exp):

        # 自省
        if is_string(exp):
            return exp[1:-1]
        if is_number(exp):
            return exp

        # 变量查找
        if is_var(exp):
            return self.Env.lookup(exp)

        if is_list(exp):

            # 空语句
            if len(exp) == 0:
                return None

            # 变量定义
            if exp[0] == "var":
                _, name, value = exp
                value = self.Eval(value)
                return self.Env.set(name, value)

            # 变量更改
            if exp[0] == "assign":
                _, name, value = exp
                value = self.Eval(value)
                return self.Env.assign(name, value)

            # 代码块
            if exp[0] == "begin":

                self.Env = self.Env.next()
                resoult = None
                for block in exp[1:]:
                    resoult = self.Eval(block)
                self.Env = self.Env.close()
                return resoult

            # 关键字
            if exp[0] == "if":
                _, condition, body, other = exp
                if self.Eval(condition):
                    return self.Eval(body)
                else:
                    return self.Eval(other)

            if exp[0] == "while":
                _, condition, body = exp
                resoult = None
                while self.Eval(condition):
                    resoult = self.Eval(body)
                return resoult

            if exp[0] == "def":
                _, name, params, body = exp
                fn = {
                    "params": params,
                    "body": body,
                }
                return self.Env.set(name, fn)

            # 函数调用
            fn = self.Env.lookup(exp[0])
            args = []
            for arg in exp[1:]:
                args.append(self.Eval(arg))
            # 内置变量函数
            if callable(fn):
                return fn(*args)
            # 用户定义函数
            if is_dict(fn):
                kv = dict(zip(fn["params"], args))
                self.Env = self.Env.next(kv)
                resoult = self.Eval(fn["body"])
                self.Env = self.Env.close()
                return resoult

        raise Exception(f"{exp} with Error")


# ---------------------------------------------------------------------------- #
#                                  interpreter                                 #
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    import time
    import os
    import json

    now = time.time()
    c = vm()
    path = os.sys.argv[1]

    with open(path, "r") as f:
        code: str = json.load(f)
        c(code)
    print(int((time.time() - now) * 1000), "ms")
