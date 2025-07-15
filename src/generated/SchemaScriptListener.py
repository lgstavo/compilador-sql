# Generated from src/SchemaScript.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SchemaScriptParser import SchemaScriptParser
else:
    from SchemaScriptParser import SchemaScriptParser

# This class defines a complete listener for a parse tree produced by SchemaScriptParser.
class SchemaScriptListener(ParseTreeListener):

    # Enter a parse tree produced by SchemaScriptParser#schema.
    def enterSchema(self, ctx:SchemaScriptParser.SchemaContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#schema.
    def exitSchema(self, ctx:SchemaScriptParser.SchemaContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#declaracao.
    def enterDeclaracao(self, ctx:SchemaScriptParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#declaracao.
    def exitDeclaracao(self, ctx:SchemaScriptParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#definicao_tabela.
    def enterDefinicao_tabela(self, ctx:SchemaScriptParser.Definicao_tabelaContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#definicao_tabela.
    def exitDefinicao_tabela(self, ctx:SchemaScriptParser.Definicao_tabelaContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#definicao_atributo.
    def enterDefinicao_atributo(self, ctx:SchemaScriptParser.Definicao_atributoContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#definicao_atributo.
    def exitDefinicao_atributo(self, ctx:SchemaScriptParser.Definicao_atributoContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#definicao_tipo.
    def enterDefinicao_tipo(self, ctx:SchemaScriptParser.Definicao_tipoContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#definicao_tipo.
    def exitDefinicao_tipo(self, ctx:SchemaScriptParser.Definicao_tipoContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#tipo_primitivo.
    def enterTipo_primitivo(self, ctx:SchemaScriptParser.Tipo_primitivoContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#tipo_primitivo.
    def exitTipo_primitivo(self, ctx:SchemaScriptParser.Tipo_primitivoContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#tipo_chave_estrangeira.
    def enterTipo_chave_estrangeira(self, ctx:SchemaScriptParser.Tipo_chave_estrangeiraContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#tipo_chave_estrangeira.
    def exitTipo_chave_estrangeira(self, ctx:SchemaScriptParser.Tipo_chave_estrangeiraContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#restricao.
    def enterRestricao(self, ctx:SchemaScriptParser.RestricaoContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#restricao.
    def exitRestricao(self, ctx:SchemaScriptParser.RestricaoContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#bloco_insercao.
    def enterBloco_insercao(self, ctx:SchemaScriptParser.Bloco_insercaoContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#bloco_insercao.
    def exitBloco_insercao(self, ctx:SchemaScriptParser.Bloco_insercaoContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#linha_dados.
    def enterLinha_dados(self, ctx:SchemaScriptParser.Linha_dadosContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#linha_dados.
    def exitLinha_dados(self, ctx:SchemaScriptParser.Linha_dadosContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#atribuicao.
    def enterAtribuicao(self, ctx:SchemaScriptParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#atribuicao.
    def exitAtribuicao(self, ctx:SchemaScriptParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#declaracao_atualizacao.
    def enterDeclaracao_atualizacao(self, ctx:SchemaScriptParser.Declaracao_atualizacaoContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#declaracao_atualizacao.
    def exitDeclaracao_atualizacao(self, ctx:SchemaScriptParser.Declaracao_atualizacaoContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#condicao.
    def enterCondicao(self, ctx:SchemaScriptParser.CondicaoContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#condicao.
    def exitCondicao(self, ctx:SchemaScriptParser.CondicaoContext):
        pass


    # Enter a parse tree produced by SchemaScriptParser#valor.
    def enterValor(self, ctx:SchemaScriptParser.ValorContext):
        pass

    # Exit a parse tree produced by SchemaScriptParser#valor.
    def exitValor(self, ctx:SchemaScriptParser.ValorContext):
        pass



del SchemaScriptParser