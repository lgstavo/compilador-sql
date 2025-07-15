CREATE TABLE Usuarios (
    id SERIAL PRIMARY KEY,
    nome_completo VARCHAR(200) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Projetos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    data_inicio TIMESTAMP,
    gerente_id INTEGER REFERENCES Usuarios(id)
);

CREATE TABLE Tarefas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'Pendente',
    projeto_id INTEGER REFERENCES Projetos(id)
);

INSERT INTO Usuarios (nome_completo, email) VALUES ('Ana Pereira', 'ana.p@email.com');
INSERT INTO Usuarios (nome_completo, email) VALUES ('Bruno Costa', 'bruno.c@email.com');

INSERT INTO Projetos (titulo, descricao, gerente_id) VALUES ('Desenvolvimento do Novo Compilador', 'Projeto final da disciplina.', 1);
INSERT INTO Projetos (titulo, gerente_id) VALUES ('Documentação do Usuário', 2);

INSERT INTO Tarefas (titulo, status, projeto_id) VALUES ('Definir a Gramática', 'Concluído', 1);
INSERT INTO Tarefas (titulo, status, projeto_id) VALUES ('Implementar o Gerador de Código', 'Em Andamento', 1);
INSERT INTO Tarefas (titulo, status, projeto_id) VALUES ('Escrever o README', 'Pendente', 2);