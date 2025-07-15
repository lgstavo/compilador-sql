# Generated from src/SchemaScript.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,135,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,1,1,3,1,39,8,1,1,2,1,
        2,1,2,1,2,1,2,5,2,46,8,2,10,2,12,2,49,9,2,1,2,1,2,1,3,1,3,1,3,1,
        3,5,3,57,8,3,10,3,12,3,60,9,3,1,3,1,3,1,4,1,4,3,4,66,8,4,1,5,1,5,
        1,5,1,5,3,5,72,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,83,8,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,92,8,8,10,8,12,8,95,9,8,1,8,1,
        8,1,9,1,9,1,9,1,9,5,9,103,8,9,10,9,12,9,106,9,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,120,8,11,10,11,12,11,
        123,9,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,
        0,0,14,0,2,4,6,8,10,12,14,16,18,20,22,24,26,0,1,2,0,20,20,23,24,
        132,0,29,1,0,0,0,2,38,1,0,0,0,4,40,1,0,0,0,6,52,1,0,0,0,8,65,1,0,
        0,0,10,67,1,0,0,0,12,73,1,0,0,0,14,82,1,0,0,0,16,84,1,0,0,0,18,98,
        1,0,0,0,20,109,1,0,0,0,22,113,1,0,0,0,24,128,1,0,0,0,26,132,1,0,
        0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,
        1,0,0,0,32,33,1,0,0,0,33,34,5,0,0,1,34,1,1,0,0,0,35,39,3,4,2,0,36,
        39,3,16,8,0,37,39,3,22,11,0,38,35,1,0,0,0,38,36,1,0,0,0,38,37,1,
        0,0,0,39,3,1,0,0,0,40,41,5,1,0,0,41,42,5,2,0,0,42,43,5,22,0,0,43,
        47,5,3,0,0,44,46,3,6,3,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,
        0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,5,4,0,0,51,5,1,
        0,0,0,52,53,5,22,0,0,53,54,5,5,0,0,54,58,3,8,4,0,55,57,3,14,7,0,
        56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,
        0,0,0,60,58,1,0,0,0,61,62,5,6,0,0,62,7,1,0,0,0,63,66,3,10,5,0,64,
        66,3,12,6,0,65,63,1,0,0,0,65,64,1,0,0,0,66,9,1,0,0,0,67,71,5,21,
        0,0,68,69,5,7,0,0,69,70,5,23,0,0,70,72,5,8,0,0,71,68,1,0,0,0,71,
        72,1,0,0,0,72,11,1,0,0,0,73,74,5,9,0,0,74,75,5,7,0,0,75,76,5,22,
        0,0,76,77,5,8,0,0,77,13,1,0,0,0,78,83,5,10,0,0,79,83,5,11,0,0,80,
        81,5,12,0,0,81,83,3,26,13,0,82,78,1,0,0,0,82,79,1,0,0,0,82,80,1,
        0,0,0,83,15,1,0,0,0,84,85,5,13,0,0,85,86,5,14,0,0,86,87,5,22,0,0,
        87,88,5,3,0,0,88,93,3,18,9,0,89,90,5,15,0,0,90,92,3,18,9,0,91,89,
        1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,
        95,93,1,0,0,0,96,97,5,4,0,0,97,17,1,0,0,0,98,99,5,7,0,0,99,104,3,
        20,10,0,100,101,5,15,0,0,101,103,3,20,10,0,102,100,1,0,0,0,103,106,
        1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,104,
        1,0,0,0,107,108,5,8,0,0,108,19,1,0,0,0,109,110,5,22,0,0,110,111,
        5,5,0,0,111,112,3,26,13,0,112,21,1,0,0,0,113,114,5,16,0,0,114,115,
        5,22,0,0,115,116,5,17,0,0,116,121,3,24,12,0,117,118,5,15,0,0,118,
        120,3,24,12,0,119,117,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,
        122,1,0,0,0,122,124,1,0,0,0,123,121,1,0,0,0,124,125,5,18,0,0,125,
        126,3,24,12,0,126,127,5,6,0,0,127,23,1,0,0,0,128,129,5,22,0,0,129,
        130,5,19,0,0,130,131,3,26,13,0,131,25,1,0,0,0,132,133,7,0,0,0,133,
        27,1,0,0,0,10,31,38,47,58,65,71,82,93,104,121
    ]

class SchemaScriptParser ( Parser ):

    grammarFileName = "SchemaScript.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'criar'", "'tabela'", "'{'", "'}'", "':'", 
                     "';'", "'('", "')'", "'chave_estrangeira'", "'obrigatorio'", 
                     "'unico'", "'padrao'", "'inserir'", "'em'", "','", 
                     "'atualizar'", "'definir'", "'onde'", "'='", "'agora'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NOME_TIPO", "ID", "NUMBER", "STRING", 
                      "COMMENT", "WS" ]

    RULE_schema = 0
    RULE_declaracao = 1
    RULE_definicao_tabela = 2
    RULE_definicao_atributo = 3
    RULE_definicao_tipo = 4
    RULE_tipo_primitivo = 5
    RULE_tipo_chave_estrangeira = 6
    RULE_restricao = 7
    RULE_bloco_insercao = 8
    RULE_linha_dados = 9
    RULE_atribuicao = 10
    RULE_declaracao_atualizacao = 11
    RULE_condicao = 12
    RULE_valor = 13

    ruleNames =  [ "schema", "declaracao", "definicao_tabela", "definicao_atributo", 
                   "definicao_tipo", "tipo_primitivo", "tipo_chave_estrangeira", 
                   "restricao", "bloco_insercao", "linha_dados", "atribuicao", 
                   "declaracao_atualizacao", "condicao", "valor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    NOME_TIPO=21
    ID=22
    NUMBER=23
    STRING=24
    COMMENT=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SchemaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SchemaScriptParser.EOF, 0)

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SchemaScriptParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(SchemaScriptParser.DeclaracaoContext,i)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_schema

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchema" ):
                listener.enterSchema(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchema" ):
                listener.exitSchema(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSchema" ):
                return visitor.visitSchema(self)
            else:
                return visitor.visitChildren(self)




    def schema(self):

        localctx = SchemaScriptParser.SchemaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_schema)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.declaracao()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 73730) != 0)):
                    break

            self.state = 33
            self.match(SchemaScriptParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def definicao_tabela(self):
            return self.getTypedRuleContext(SchemaScriptParser.Definicao_tabelaContext,0)


        def bloco_insercao(self):
            return self.getTypedRuleContext(SchemaScriptParser.Bloco_insercaoContext,0)


        def declaracao_atualizacao(self):
            return self.getTypedRuleContext(SchemaScriptParser.Declaracao_atualizacaoContext,0)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = SchemaScriptParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracao)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.definicao_tabela()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.bloco_insercao()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.declaracao_atualizacao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Definicao_tabelaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SchemaScriptParser.ID, 0)

        def definicao_atributo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SchemaScriptParser.Definicao_atributoContext)
            else:
                return self.getTypedRuleContext(SchemaScriptParser.Definicao_atributoContext,i)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_definicao_tabela

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicao_tabela" ):
                listener.enterDefinicao_tabela(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicao_tabela" ):
                listener.exitDefinicao_tabela(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicao_tabela" ):
                return visitor.visitDefinicao_tabela(self)
            else:
                return visitor.visitChildren(self)




    def definicao_tabela(self):

        localctx = SchemaScriptParser.Definicao_tabelaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_definicao_tabela)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(SchemaScriptParser.T__0)
            self.state = 41
            self.match(SchemaScriptParser.T__1)
            self.state = 42
            self.match(SchemaScriptParser.ID)
            self.state = 43
            self.match(SchemaScriptParser.T__2)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 44
                self.definicao_atributo()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(SchemaScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Definicao_atributoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SchemaScriptParser.ID, 0)

        def definicao_tipo(self):
            return self.getTypedRuleContext(SchemaScriptParser.Definicao_tipoContext,0)


        def restricao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SchemaScriptParser.RestricaoContext)
            else:
                return self.getTypedRuleContext(SchemaScriptParser.RestricaoContext,i)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_definicao_atributo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicao_atributo" ):
                listener.enterDefinicao_atributo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicao_atributo" ):
                listener.exitDefinicao_atributo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicao_atributo" ):
                return visitor.visitDefinicao_atributo(self)
            else:
                return visitor.visitChildren(self)




    def definicao_atributo(self):

        localctx = SchemaScriptParser.Definicao_atributoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_definicao_atributo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SchemaScriptParser.ID)
            self.state = 53
            self.match(SchemaScriptParser.T__4)
            self.state = 54
            self.definicao_tipo()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0):
                self.state = 55
                self.restricao()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(SchemaScriptParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Definicao_tipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo_primitivo(self):
            return self.getTypedRuleContext(SchemaScriptParser.Tipo_primitivoContext,0)


        def tipo_chave_estrangeira(self):
            return self.getTypedRuleContext(SchemaScriptParser.Tipo_chave_estrangeiraContext,0)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_definicao_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefinicao_tipo" ):
                listener.enterDefinicao_tipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefinicao_tipo" ):
                listener.exitDefinicao_tipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefinicao_tipo" ):
                return visitor.visitDefinicao_tipo(self)
            else:
                return visitor.visitChildren(self)




    def definicao_tipo(self):

        localctx = SchemaScriptParser.Definicao_tipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_definicao_tipo)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.tipo_primitivo()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.tipo_chave_estrangeira()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tipo_primitivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOME_TIPO(self):
            return self.getToken(SchemaScriptParser.NOME_TIPO, 0)

        def NUMBER(self):
            return self.getToken(SchemaScriptParser.NUMBER, 0)

        def getRuleIndex(self):
            return SchemaScriptParser.RULE_tipo_primitivo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo_primitivo" ):
                listener.enterTipo_primitivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo_primitivo" ):
                listener.exitTipo_primitivo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo_primitivo" ):
                return visitor.visitTipo_primitivo(self)
            else:
                return visitor.visitChildren(self)




    def tipo_primitivo(self):

        localctx = SchemaScriptParser.Tipo_primitivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tipo_primitivo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(SchemaScriptParser.NOME_TIPO)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 68
                self.match(SchemaScriptParser.T__6)
                self.state = 69
                self.match(SchemaScriptParser.NUMBER)
                self.state = 70
                self.match(SchemaScriptParser.T__7)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tipo_chave_estrangeiraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SchemaScriptParser.ID, 0)

        def getRuleIndex(self):
            return SchemaScriptParser.RULE_tipo_chave_estrangeira

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo_chave_estrangeira" ):
                listener.enterTipo_chave_estrangeira(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo_chave_estrangeira" ):
                listener.exitTipo_chave_estrangeira(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo_chave_estrangeira" ):
                return visitor.visitTipo_chave_estrangeira(self)
            else:
                return visitor.visitChildren(self)




    def tipo_chave_estrangeira(self):

        localctx = SchemaScriptParser.Tipo_chave_estrangeiraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipo_chave_estrangeira)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SchemaScriptParser.T__8)
            self.state = 74
            self.match(SchemaScriptParser.T__6)
            self.state = 75
            self.match(SchemaScriptParser.ID)
            self.state = 76
            self.match(SchemaScriptParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestricaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valor(self):
            return self.getTypedRuleContext(SchemaScriptParser.ValorContext,0)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_restricao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRestricao" ):
                listener.enterRestricao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRestricao" ):
                listener.exitRestricao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRestricao" ):
                return visitor.visitRestricao(self)
            else:
                return visitor.visitChildren(self)




    def restricao(self):

        localctx = SchemaScriptParser.RestricaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_restricao)
        try:
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(SchemaScriptParser.T__9)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(SchemaScriptParser.T__10)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.match(SchemaScriptParser.T__11)
                self.state = 81
                self.valor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bloco_insercaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SchemaScriptParser.ID, 0)

        def linha_dados(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SchemaScriptParser.Linha_dadosContext)
            else:
                return self.getTypedRuleContext(SchemaScriptParser.Linha_dadosContext,i)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_bloco_insercao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco_insercao" ):
                listener.enterBloco_insercao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco_insercao" ):
                listener.exitBloco_insercao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco_insercao" ):
                return visitor.visitBloco_insercao(self)
            else:
                return visitor.visitChildren(self)




    def bloco_insercao(self):

        localctx = SchemaScriptParser.Bloco_insercaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bloco_insercao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(SchemaScriptParser.T__12)
            self.state = 85
            self.match(SchemaScriptParser.T__13)
            self.state = 86
            self.match(SchemaScriptParser.ID)
            self.state = 87
            self.match(SchemaScriptParser.T__2)
            self.state = 88
            self.linha_dados()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 89
                self.match(SchemaScriptParser.T__14)
                self.state = 90
                self.linha_dados()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(SchemaScriptParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Linha_dadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SchemaScriptParser.AtribuicaoContext)
            else:
                return self.getTypedRuleContext(SchemaScriptParser.AtribuicaoContext,i)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_linha_dados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinha_dados" ):
                listener.enterLinha_dados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinha_dados" ):
                listener.exitLinha_dados(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLinha_dados" ):
                return visitor.visitLinha_dados(self)
            else:
                return visitor.visitChildren(self)




    def linha_dados(self):

        localctx = SchemaScriptParser.Linha_dadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_linha_dados)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(SchemaScriptParser.T__6)
            self.state = 99
            self.atribuicao()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 100
                self.match(SchemaScriptParser.T__14)
                self.state = 101
                self.atribuicao()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(SchemaScriptParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SchemaScriptParser.ID, 0)

        def valor(self):
            return self.getTypedRuleContext(SchemaScriptParser.ValorContext,0)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = SchemaScriptParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(SchemaScriptParser.ID)
            self.state = 110
            self.match(SchemaScriptParser.T__4)
            self.state = 111
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_atualizacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SchemaScriptParser.ID, 0)

        def condicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SchemaScriptParser.CondicaoContext)
            else:
                return self.getTypedRuleContext(SchemaScriptParser.CondicaoContext,i)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_declaracao_atualizacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_atualizacao" ):
                listener.enterDeclaracao_atualizacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_atualizacao" ):
                listener.exitDeclaracao_atualizacao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_atualizacao" ):
                return visitor.visitDeclaracao_atualizacao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao_atualizacao(self):

        localctx = SchemaScriptParser.Declaracao_atualizacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_declaracao_atualizacao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(SchemaScriptParser.T__15)
            self.state = 114
            self.match(SchemaScriptParser.ID)
            self.state = 115
            self.match(SchemaScriptParser.T__16)
            self.state = 116
            self.condicao()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 117
                self.match(SchemaScriptParser.T__14)
                self.state = 118
                self.condicao()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
            self.match(SchemaScriptParser.T__17)
            self.state = 125
            self.condicao()
            self.state = 126
            self.match(SchemaScriptParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SchemaScriptParser.ID, 0)

        def valor(self):
            return self.getTypedRuleContext(SchemaScriptParser.ValorContext,0)


        def getRuleIndex(self):
            return SchemaScriptParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicao" ):
                return visitor.visitCondicao(self)
            else:
                return visitor.visitChildren(self)




    def condicao(self):

        localctx = SchemaScriptParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_condicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(SchemaScriptParser.ID)
            self.state = 129
            self.match(SchemaScriptParser.T__18)
            self.state = 130
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SchemaScriptParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(SchemaScriptParser.NUMBER, 0)

        def getRuleIndex(self):
            return SchemaScriptParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor" ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor" ):
                listener.exitValor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = SchemaScriptParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 26214400) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





