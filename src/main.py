import sys
import argparse
import os
from antlr4 import *
from generated.SchemaScriptLexer import SchemaScriptLexer
from generated.SchemaScriptParser import SchemaScriptParser
from SemanticVisitor import SemanticVisitor
from CodeGeneratorVisitor import CodeGeneratorVisitor
from ErrorListener import CustomErrorListener

def main():
    arg_parser = argparse.ArgumentParser(description='Compilador SchemaScript para gerar SQL.')
    arg_parser.add_argument('input_file', help='O arquivo .schema a ser compilado.')
    arg_parser.add_argument('-o', '--output', metavar='output_file', help='O nome do arquivo .sql de saída.')
    arg_parser.add_argument('--dialect', default='sqlite', choices=['sqlite', 'mysql', 'postgres'], help='O dialeto SQL a ser gerado.')
    args = arg_parser.parse_args()

    # --- LÓGICA DE DIRETÓRIO DE SAÍDA REMOVIDA ---
    # As linhas que criavam a pasta 'casos-de-teste/saidas/' foram removidas.

    erros_compilacao = []

    try:
        input_stream = FileStream(args.input_file, encoding='utf-8')
    except FileNotFoundError:
        print(f"Erro: Arquivo de entrada não encontrado em '{args.input_file}'")
        return

    lexer = SchemaScriptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SchemaScriptParser(stream)
    
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener(erros_compilacao))

    tree = parser.schema()
    
    if not erros_compilacao:
        print("Análise sintática concluída com sucesso!")
        semantic_visitor = SemanticVisitor(erros_compilacao)
        semantic_visitor.visit(tree)
        print("Análise semântica concluída.")

    if erros_compilacao:
        contador = 1
        # ALTERAÇÃO: O nome do arquivo agora não inclui o caminho da pasta.
        log_filename = f"saida({contador}).txt"
        while os.path.exists(log_filename):
            contador += 1
            log_filename = f"saida({contador}).txt"

        with open(log_filename, "w", encoding="utf-8") as f:
            f.write("Erros de compilação encontrados:\n")
            f.write("=================================\n")
            for error in erros_compilacao:
                f.write(f"- {error}\n")
        print(f"Erros encontrados! Verifique o arquivo de log: {log_filename}")
    else:
        print(f"⚙️ Gerando código para o dialeto '{args.dialect}'...")
        code_generator = CodeGeneratorVisitor(dialect=args.dialect)
        generated_sql = code_generator.visit(tree)
        
        if args.output:
            # ALTERAÇÃO: Salva diretamente no nome do arquivo fornecido, sem adicionar pastas.
            try:
                with open(args.output, "w", encoding="utf-8") as f:
                    f.write(generated_sql)
                print(f"Sucesso! Código SQL salvo em: {args.output}")
            except IOError as e:
                print(f"Erro ao salvar arquivo: {e}")
        else:
            print("\n--- CÓDIGO SQL GERADO ---\n")
            print(generated_sql)

if __name__ == '__main__':
    main()