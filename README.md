# Syntactic-Analyzer-OWL
Objetivo: Construir um analisador sintático para verificar formas adequadas de se descrever classes de uma ontologia em OWL Manchester Syntax

Alunos: Vítor Duarte e Ricardo Júnior

Disciplina: Compiladores 

Professor: Dr. Patricio de Alencar Silva

Este é um analisador sintático para a linguagem OWL (Web Ontology Language) implementado em Python usando a biblioteca PLY (Python Lex-Yacc). O código é projetado para analisar expressões OWL presentes em um arquivo de texto e fornecer um resumo estatístico.

Os arquivos parser.out e parsetab.py são gerados com dados baseados no arquivo de teste (dados.txt ou dados2.txt) 

* Instalação:

Certifique-se de ter o Python e o pip instalados em seu sistema. Em seguida, execute os seguintes comandos para instalar as dependências necessárias:

```bash
pip install ply
pip install pandas
pip install matplotlib
```

## Uso

Clone o repositório para o seu sistema ou faça o download do ZIP
```bash
https://github.com/vitordbo/Syntactic-Analyzer-OWL.git
```
* Abrindo no VSCode

Se você estiver usando o VSCode, pode abrir o diretório do projeto diretamente. Certifique-se de ter a extensão do Python instalada. Abra o terminal integrado no VSCode e instale as dependências necessárias, caso ainda não tenha feito.

## Execução

Basta executar o seguinte comando: 
```bash
python App.py
```
ou apertar o botão de Run do VSCode:

![image](https://github.com/vitordbo/Syntactic-Analyzer-OWL/assets/65680799/3efcd8c4-8cc0-4bc8-8a70-be8f6711ed81)

## Visualização do Resumo
Além da saída dos dados via terminal, o código gera uma tabela resumo e a salva como uma imagem. A tabela é salva como "resumo_tabela.png" no diretório do projeto.

