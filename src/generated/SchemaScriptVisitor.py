# Generated from src/SchemaScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SchemaScriptParser import SchemaScriptParser
else:
    from SchemaScriptParser import SchemaScriptParser

# This class defines a complete generic visitor for a parse tree produced by SchemaScriptParser.

class SchemaScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SchemaScriptParser#schema.
    def visitSchema(self, ctx:SchemaScriptParser.SchemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#declaracao.
    def visitDeclaracao(self, ctx:SchemaScriptParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#definicao_tabela.
    def visitDefinicao_tabela(self, ctx:SchemaScriptParser.Definicao_tabelaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#definicao_atributo.
    def visitDefinicao_atributo(self, ctx:SchemaScriptParser.Definicao_atributoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#definicao_tipo.
    def visitDefinicao_tipo(self, ctx:SchemaScriptParser.Definicao_tipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#tipo_primitivo.
    def visitTipo_primitivo(self, ctx:SchemaScriptParser.Tipo_primitivoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#tipo_chave_estrangeira.
    def visitTipo_chave_estrangeira(self, ctx:SchemaScriptParser.Tipo_chave_estrangeiraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#restricao.
    def visitRestricao(self, ctx:SchemaScriptParser.RestricaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#bloco_insercao.
    def visitBloco_insercao(self, ctx:SchemaScriptParser.Bloco_insercaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#linha_dados.
    def visitLinha_dados(self, ctx:SchemaScriptParser.Linha_dadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#atribuicao.
    def visitAtribuicao(self, ctx:SchemaScriptParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#declaracao_atualizacao.
    def visitDeclaracao_atualizacao(self, ctx:SchemaScriptParser.Declaracao_atualizacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#condicao.
    def visitCondicao(self, ctx:SchemaScriptParser.CondicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SchemaScriptParser#valor.
    def visitValor(self, ctx:SchemaScriptParser.ValorContext):
        return self.visitChildren(ctx)



del SchemaScriptParser