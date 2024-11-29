import argparse
from MiniCppContext import Context
from rich import print
from MiniCppCast import MakeDot
from PIL import Image
from MiniCppParser import gen_ast

def parse_args():
    """
    Configura los argumentos del programa usando argparse.
    """
    parser = argparse.ArgumentParser(
        prog="mc.py",
        description="Compiler for MiniC programs",
    )

    # Argumento posicional para el archivo de entrada
    parser.add_argument(
        "input",
        type=str,
        nargs="?",
        help="MiniC program file to compile",
    )

    # Opciones de ejecución
    parser.add_argument(
        "-l", "--lex",
        action="store_true",
        help="Store output of lexer",
    )
    parser.add_argument(
        "-a", "--ast",
        action="store_true",
        help="Print the AST (Abstract Syntax Tree)",
    )
    parser.add_argument(
        "-D", "--dot",
        action="store_true",
        help="Generate AST graph as DOT format",
    )
    parser.add_argument(
        "-p", "--png",
        action="store_true",
        help="Generate AST graph as PNG format",
    )
    parser.add_argument(
        "-s", "--sym",
        action="store_true",
        help="Dump the symbol table",
    )
    parser.add_argument(
        "-R", "--exec",
        action="store_true",
        help="Execute the compiled program",
    )

    return parser.parse_args()

def main():
    # Parsear los argumentos
    args = parse_args()

    # Verificar si se proporcionó un archivo de entrada
    if args.input:
        fname = args.input
        with open(fname, encoding="utf-8") as file:
            source = file.read()

        context = Context()
        context.parse(source)

        if context.have_errors:
            print("Errores encontrados durante el análisis.")
            return

        # Manejo de opciones basadas en los argumentos
        if args.lex:
            print("\n\n\t\t********** TOKENS ********** \n\n")
            tokens = context.lexer.tokenize(source)
            table = [["Type", "Value", "At line"]]
            for tok in tokens:
                table.append([tok.type, tok.value, tok.lineno])
            print(table)

        elif args.ast:
            print("\n\n\t\t********** AST ********** \n\n")
            print(context.ast)

        elif args.dot:
            print("\n\n\t\t********** DOT ********** \n\n")
            dot = MakeDot.render(context.ast)
            print(dot)

        elif args.png:
            base = fname.split('.')[0]
            ast, dot = gen_ast(source, base)
            fdot = base + "_ast.png"
            print(f"Generated PNG: {fdot}")
            image = Image.open(fdot)
            image.show()

        elif args.sym:
            print("\n\n\t\t********** SYMBOL TABLE ********** \n\n")
            print(context.interp.env)

        elif args.exec:
            print("\n Ejecutando... \n")
            context.run()

        else:
            print("No se seleccionó ninguna acción.")
    else:
        context = Context()
        try:
            while True:
                source = input("mc > ")
                context.parse(source)
                if context.have_errors:
                    continue
                for stmt in context.ast.decl:
                    context.ast = stmt
                    context.run()
        except EOFError:
            pass

if __name__ == "__main__":
    main()
