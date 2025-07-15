from generated.SchemaScriptVisitor import SchemaScriptVisitor
from generated.SchemaScriptParser import SchemaScriptParser

class SemanticVisitor(SchemaScriptVisitor):
    def __init__(self, error_list):
        self.tabela_simbolos = {}
        self.errors = error_list

    @property
    def has_errors(self):
        return len(self.errors) > 0

    def _log_error(self, message):
        if message not in self.errors:
            self.errors.append(message)

    def visitSchema(self, ctx:SchemaScriptParser.SchemaContext):
        # Passo 1: Coleta apenas os nomes das tabelas para criar o mapa do schema
        # e checar por nomes de tabelas duplicados.
        for declaracao in ctx.declaracao():
            if isinstance(declaracao.getChild(0), SchemaScriptParser.Definicao_tabelaContext):
                tabela_ctx = declaracao.getChild(0)
                nome_tabela = tabela_ctx.ID().getText()
                if nome_tabela in self.tabela_simbolos:
                    self._log_error(f"Erro Semântico (linha {tabela_ctx.start.line}): A tabela '{nome_tabela}' já foi declarada.")
                else:
                    self.tabela_simbolos[nome_tabela] = set()
        
        # Passo 2: Faz uma visita completa para todas as outras validações.
        for declaracao in ctx.declaracao():
            self.visit(declaracao)
        
    def visitDefinicao_tabela(self, ctx:SchemaScriptParser.Definicao_tabelaContext):
        nome_tabela = ctx.ID().getText()
        if nome_tabela in self.tabela_simbolos:
            for attr_ctx in ctx.definicao_atributo():
                nome_attr = attr_ctx.ID().getText()
                if nome_attr in self.tabela_simbolos[nome_tabela]:
                    self._log_error(f"Erro Semântico (linha {attr_ctx.start.line}): O atributo '{nome_attr}' já foi declarado na tabela '{nome_tabela}'.")
                else:
                    self.tabela_simbolos[nome_tabela].add(nome_attr)
        
        # CORREÇÃO FINAL: Instruímos o visitante a continuar a análise
        # para dentro dos atributos, o que ativará a checagem de chave estrangeira.
        return self.visitChildren(ctx)
    
    def visitTipo_chave_estrangeira(self, ctx:SchemaScriptParser.Tipo_chave_estrangeiraContext):
        nome_tabela_ref = ctx.ID().getText()
        if nome_tabela_ref not in self.tabela_simbolos:
            self._log_error(f"Erro Semântico (linha {ctx.start.line}): A tabela '{nome_tabela_ref}' referenciada na chave estrangeira não foi definida.")
        return self.visitChildren(ctx)

    def visitBloco_insercao(self, ctx:SchemaScriptParser.Bloco_insercaoContext):
        nome_tabela = ctx.ID().getText()
        if nome_tabela not in self.tabela_simbolos:
            self._log_error(f"Erro Semântico (linha {ctx.start.line}): A tabela '{nome_tabela}' usada no bloco 'inserir' não foi definida.")
            return
        
        atributos_tabela = self.tabela_simbolos[nome_tabela]
        for linha_ctx in ctx.linha_dados():
            for atribuicao_ctx in linha_ctx.atribuicao():
                nome_attr = atribuicao_ctx.ID().getText()
                if nome_attr not in atributos_tabela:
                    self._log_error(f"Erro Semântico (linha {atribuicao_ctx.start.line}): O atributo '{nome_attr}' não existe na tabela '{nome_tabela}'.")
    
    def visitDeclaracao_atualizacao(self, ctx:SchemaScriptParser.Declaracao_atualizacaoContext):
        nome_tabela = ctx.ID().getText()
        if nome_tabela not in self.tabela_simbolos:
            self._log_error(f"Erro Semântico (linha {ctx.start.line}): A tabela '{nome_tabela}' usada no comando 'atualizar' não foi definida.")
            return
        
        atributos_tabela = self.tabela_simbolos[nome_tabela]
        condicoes = ctx.condicao()
        where_cond = condicoes[-1]
        set_conds = condicoes[:-1]

        for cond_ctx in set_conds:
            nome_attr = cond_ctx.ID().getText()
            if nome_attr not in atributos_tabela:
                self._log_error(f"Erro Semântico (linha {cond_ctx.start.line}): O atributo '{nome_attr}' na cláusula 'definir' não existe na tabela '{nome_tabela}'.")
        
        nome_condicao = where_cond.ID().getText()
        if nome_condicao not in atributos_tabela:
            self._log_error(f"Erro Semântico (linha {where_cond.start.line}): O atributo '{nome_condicao}' na cláusula 'onde' não existe na tabela '{nome_tabela}'.")

    def visitDeclaracao(self, ctx:SchemaScriptParser.DeclaracaoContext):
        return self.visitChildren(ctx)