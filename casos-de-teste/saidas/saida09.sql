CREATE TABLE Funcionarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cargo VARCHAR(100) DEFAULT 'Colaborador',
    salario INTEGER
);

INSERT INTO Funcionarios (id, nome, salario) VALUES (1, 'Beatriz', 500000);
INSERT INTO Funcionarios (id, nome, cargo, salario) VALUES (2, 'Carlos', 'Analista', 650000);

UPDATE Funcionarios SET salario = 550000 WHERE id = 1;

UPDATE Funcionarios SET cargo = 'Analista Sênior', salario = 720000 WHERE id = 2;