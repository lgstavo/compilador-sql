CREATE TABLE Categoria (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Produto (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    preco INTEGER NOT NULL,
    categoria_id INTEGER REFERENCES Categoria(id)
);

INSERT INTO Categoria (nome) VALUES ('Eletrônicos');
INSERT INTO Categoria (nome) VALUES ('Livros');

INSERT INTO Produto (nome, preco, categoria_id) VALUES ('Smart TV 50 polegadas', 350000, 1);
INSERT INTO Produto (nome, preco, categoria_id) VALUES ('O Senhor dos Anéis', 12000, 2);
INSERT INTO Produto (nome, preco, categoria_id) VALUES ('Fone de Ouvido Bluetooth', 25000, 1);