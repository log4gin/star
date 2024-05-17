import os
from lexer import lexer
from complie import parser
from vm import vm
import json

_lexer = lexer()
_parser = parser()
_vm = vm()


# star file_path
# star complie file_path
# star vm file_path


args: list = os.sys.argv[1:]

if len(args) == 2:
    match args[0]:
        case "complie":
            with open(args[1], "r") as f:
                code = f.read()
                tokens = _lexer(code)
                ast = _parser(tokens)

                # convert to json
                with open(args[1] + ".json", "w") as f:
                    json.dump(ast, f)

        case "vm":
            with open(args[1], "r") as f:
                ast = json.load(f)
                _vm(ast)
        case _:
            print("error: unknown option")
            exit(1)

if len(args) == 1:
    with open(args[0], "r") as f:
        code = f.read()
        tokens = _lexer(code)
        ast = _parser(tokens)
        _vm(ast)
