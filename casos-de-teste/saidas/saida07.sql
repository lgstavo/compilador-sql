CREATE TABLE Postagens (
    id SERIAL PRIMARY KEY,
    conteudo VARCHAR(280) NOT NULL,
    data_postagem TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    autor_id INTEGER REFERENCES Autores(id)
);

CREATE TABLE Seguidores (
    seguidor_id INTEGER REFERENCES Autores(id),
    seguindo_id INTEGER REFERENCES Autores(id)
);

CREATE TABLE Autores (
    id SERIAL PRIMARY KEY,
    nome_usuario VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Autores (nome_usuario) VALUES ('daniel_luc');
INSERT INTO Autores (nome_usuario) VALUES ('aluno_compiladores');
INSERT INTO Autores (nome_usuario) VALUES ('dev_antlr');

INSERT INTO Postagens (conteudo, autor_id) VALUES ('Acabei de refatorar minha linguagem!', 2);
INSERT INTO Postagens (conteudo, autor_id) VALUES ('Bugs são apenas quebra-cabeças inesperados.', 3);

INSERT INTO Seguidores (seguidor_id, seguindo_id) VALUES (2, 1);
INSERT INTO Seguidores (seguidor_id, seguindo_id) VALUES (2, 3);