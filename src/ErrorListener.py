from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self, output_list):
        # A lista 'output_list' será nossa lista central de erros
        self.errors = output_list

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Formata a mensagem de erro e a adiciona à lista
        error_message = f"Erro de Sintaxe (linha {line}:{column}): {msg}"
        self.errors.append(error_message)

