CREATE TABLE Configuracoes (
    id SERIAL PRIMARY KEY,
    chave_config VARCHAR(50) UNIQUE NOT NULL,
    valor_config TEXT NOT NULL,
    ultima_modificacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo INTEGER DEFAULT 1
);

INSERT INTO Configuracoes (chave_config, valor_config) VALUES ('NOME_DO_SITE', 'Meu Compilador Incrível');
INSERT INTO Configuracoes (chave_config, valor_config) VALUES ('MODO_DEBUG', 'desativado');