import argparse
from lexer import lexer
from compile import parser
from vm import vm
import json


def compile_file(file_path) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
        _lexer = lexer()
        _parser = parser()
        tokens = _lexer(code)
        ast = _parser(tokens)
        return ast


def run_vm(file_path, ast=None):
    _vm = vm()
    if not ast:
        with open(file_path, "r") as f:
            ast = json.load(f)
    _vm(ast)


def run_interpreter(file_path):
    ast = compile_file(file_path)
    run_vm(file_path, ast)


def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(
        description="Star Programming Language Interpreter"
    )
    parser.add_argument("file_path", help="Path to the file to process")
    parser.add_argument("-c", "--compile", action="store_true", help="Compile the file")
    parser.add_argument(
        "-v", "--vm", action="store_true", help="Run the file in the virtual machine"
    )

    # 解析命令行参数
    args = parser.parse_args()

    file_path = args.file_path
    compile_option = args.compile
    vm_option = args.vm

    if compile_option and not vm_option:
        # star file_path --compile
        ast = compile_file(file_path)
        with open(file_path + ".json", "w") as f:
            json.dump(ast, f)
    elif vm_option and not compile_option:
        # star file_path --vm
        run_vm(file_path)
    else:
        # star  file_path
        run_interpreter(file_path)


if __name__ == "__main__":
    main()
