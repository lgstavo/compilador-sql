# Compilador SchemaScript

Este projeto, desenvolvido para a disciplina de **Construção de Compiladores**, consiste em um compilador completo que traduz uma linguagem de alto nível, em português, para scripts SQL funcionais. O objetivo é simplificar e tornar mais segura a criação e manipulação de esquemas de banco de dados.

## Participantes

- Luiz Gustavo da Silva Barros - RA: 800225  


## Vídeo de Demonstração

[Link para o seu vídeo de demonstração no YouTube ou outra plataforma]

## Funcionalidades

### Linguagem de Alto Nível e Intuitiva

A linguagem **SchemaScript** foi projetada para ser clara e legível, utilizando comandos em **português** que abstraem a complexidade do SQL.

- **Definição de Estrutura:**  
  Comandos como `criar tabela`, `chave`, `texto`, `obrigatorio`.

- **Manipulação de Dados:**  
  Comandos como `inserir em` e `atualizar`.

### Validação Sintática e Semântica

O compilador realiza uma análise completa do código-fonte antes de gerar o SQL.

- **Análise Sintática:** Verifica se o código segue as regras da gramática.
- **Análise Semântica:** Detecta erros como:
  - Tabelas ou atributos duplicados.
  - Referências a chaves estrangeiras inválidas.
  - Atributos inexistentes em comandos de `inserir` ou `atualizar`.

- **Log de Erros:** Nenhum código SQL é gerado se erros forem encontrados. Em vez disso, um arquivo `.txt` é criado com os detalhes de cada erro e suas respectivas linhas.

### Geração de Código Multi-Dialeto

Geração de código SQL otimizado para os principais SGBDs:

- PostgreSQL  
- MySQL  
- SQLite

## Requisitos

- Python 3.x  
- Java Development Kit (JDK) 8 ou superior  
- [ANTLR 4.13.1](https://www.antlr.org/)  
- Bibliotecas Python (veja `requirements.txt`):
  - `antlr4-python3-runtime`

## Realizado com

- Python: `3.11`  
- JDK: `22`  
- ANTLR: `4.13.1`

## Como Gerar os Arquivos do Parser

Antes de executar o compilador, gere os arquivos do ANTLR com base na gramática `SchemaScript.g4`:


```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 src/SchemaScript.g4 -visitor -o src/generated
```

### Como executar

```bash

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

## Compilando um arquivo

```bash
python src/main.py casos-de-teste/entradas/entrada08.txt -o saida08.sql --dialect postgres
```


