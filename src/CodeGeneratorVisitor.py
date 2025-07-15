from generated.SchemaScriptVisitor import SchemaScriptVisitor
from generated.SchemaScriptParser import SchemaScriptParser

class CodeGeneratorVisitor(SchemaScriptVisitor):
    
    sqlite_map = { 'chave': 'INTEGER PRIMARY KEY AUTOINCREMENT', 'texto': 'TEXT', 'inteiro': 'INTEGER', 'datahora': 'DATETIME' }
    mysql_map = { 'chave': 'INT PRIMARY KEY AUTO_INCREMENT', 'texto': 'TEXT', 'inteiro': 'INT', 'datahora': 'DATETIME' }
    postgres_map = { 'chave': 'SERIAL PRIMARY KEY', 'texto': 'TEXT', 'inteiro': 'INTEGER', 'datahora': 'TIMESTAMP' }

    def __init__(self, dialect='sqlite'):
        if dialect == 'mysql': self.type_map = self.mysql_map
        elif dialect == 'postgres': self.type_map = self.postgres_map
        else: self.type_map = self.sqlite_map

    def visitSchema(self, ctx:SchemaScriptParser.SchemaContext):
        statements = [self.visit(dec) for dec in ctx.declaracao()]
        return "\n\n".join(filter(None, statements))

    # --- Métodos de Geração de Código (a maioria sem alterações) ---
    def visitDefinicao_tabela(self, ctx:SchemaScriptParser.Definicao_tabelaContext):
        table_name = ctx.ID().getText()
        columns_sql = [self.visit(attr) for attr in ctx.definicao_atributo()]
        columns_str = ",\n".join(columns_sql)
        return f"CREATE TABLE {table_name} (\n{columns_str}\n);"

    def visitBloco_insercao(self, ctx:SchemaScriptParser.Bloco_insercaoContext):
        table_name = ctx.ID().getText()
        if not ctx.linha_dados(): return ""
        insert_lines = []
        for row_ctx in ctx.linha_dados():
            columns = [assign.ID().getText() for assign in row_ctx.atribuicao()]
            values = [self.visit(assign.valor()) for assign in row_ctx.atribuicao()]
            columns_str, values_str = ", ".join(columns), ", ".join(values)
            insert_lines.append(f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str});")
        return "\n".join(insert_lines)
    
    # MÉTODO PARA GERAR 'UPDATE'
    # Método visitDeclaracao_atualizacao ATUALIZADO
    def visitDeclaracao_atualizacao(self, ctx:SchemaScriptParser.Declaracao_atualizacaoContext):
        table_name = ctx.ID().getText()
        
        condicoes = ctx.condicao()
        where_clause_ctx = condicoes[-1]
        set_clauses_ctx = condicoes[:-1]

        set_clauses = [self.visit(cond) for cond in set_clauses_ctx]
        set_str = ", ".join(set_clauses)
        
        where_clause = self.visit(where_clause_ctx)
        
        return f"UPDATE {table_name} SET {set_str} WHERE {where_clause};"

    def visitAtribuicao(self, ctx:SchemaScriptParser.AtribuicaoContext):
        coluna = ctx.ID().getText()
        valor = self.visit(ctx.valor())
        return f"{coluna} = {valor}"
        
    # Este método é usado tanto pelo SET quanto pelo WHERE do 'atualizar'
    def visitCondicao(self, ctx:SchemaScriptParser.CondicaoContext):
        coluna = ctx.ID().getText()
        valor = self.visit(ctx.valor())
        return f"{coluna} = {valor}"

    # --- Métodos Auxiliares ---
    def visitDefinicao_atributo(self, ctx:SchemaScriptParser.Definicao_atributoContext):
        attr_name = ctx.ID().getText()
        type_sql = self.visit(ctx.definicao_tipo())
        constraints = [self.visit(res) for res in ctx.restricao() if self.visit(res) is not None]
        return f"    {attr_name} {type_sql}{' ' if constraints else ''}{' '.join(constraints)}"

    def visitTipo_primitivo(self, ctx:SchemaScriptParser.Tipo_primitivoContext):
        type_name = ctx.NOME_TIPO().getText()
        sql_type = self.type_map.get(type_name, 'TEXT')
        if ctx.NUMBER(): return f"VARCHAR({ctx.NUMBER().getText()})"
        return sql_type

    def visitTipo_chave_estrangeira(self, ctx:SchemaScriptParser.Tipo_chave_estrangeiraContext):
        return f"INTEGER REFERENCES {ctx.ID().getText()}(id)"

    def visitRestricao(self, ctx:SchemaScriptParser.RestricaoContext):
        if ctx.valor(): return f'DEFAULT {self.visit(ctx.valor())}'
        text = ctx.getText()
        if text == 'obrigatorio': return 'NOT NULL'
        if text == 'unico': return 'UNIQUE'
        return None
    
    def visitValor(self, ctx:SchemaScriptParser.ValorContext):
        if ctx.getText() == 'agora': return 'CURRENT_TIMESTAMP'
        if ctx.STRING():
            text = ctx.STRING().getText()
            return f"{text}"
        return ctx.getText()