grammar SchemaScript;

schema:
    declaracao+ EOF;

declaracao:
    definicao_tabela
    | bloco_insercao
    | declaracao_atualizacao
    ;

definicao_tabela: 'criar' 'tabela' ID '{' definicao_atributo* '}';
definicao_atributo: ID ':' definicao_tipo restricao* ';';
definicao_tipo: tipo_primitivo | tipo_chave_estrangeira;
tipo_primitivo: NOME_TIPO ('(' NUMBER ')')?;
tipo_chave_estrangeira: 'chave_estrangeira' '(' ID ')';
restricao: 'obrigatorio' | 'unico' | 'padrao' valor;

bloco_insercao: 'inserir' 'em' ID '{' linha_dados (',' linha_dados)* '}';
linha_dados: '(' atribuicao (',' atribuicao)* ')';
atribuicao: ID ':' valor;

declaracao_atualizacao:
    'atualizar' ID 'definir' condicao (',' condicao)* 'onde' condicao ';';

condicao:
    ID '=' valor; // Esta regra já usa o '='

valor: STRING | NUMBER | 'agora';

/* --- TOKENS --- */
NOME_TIPO: 'chave' | 'texto' | 'inteiro' | 'datahora';
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
NUMBER: [0-9]+;
STRING: '\'' ( ~('\\'|'\'') )* '\'';
COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
