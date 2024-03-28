import ply.lex as lex
import ply.yacc as yacc
import pandas as pd
import matplotlib.pyplot as plt

# Analisador Sintático para OWL
# Alunos: Vítor Duarte e Ricardo Júnior

# Lendo o arquivo no diretório do projeto, contendo o exemplo a ser analisado.
PATH = 'dados2.txt'

try:
    with open(PATH, 'r') as arquivo:
        file = arquivo.read()
except FileNotFoundError:
    print(f"Arquivo não encontrado '{PATH}' !!!")
except Exception as e:
    print(f"ERRO: '{e}'")

# Abaixo estão as palavras reservadas da linguagem e logo em seguida todos os tokens
reserved = {
    'some': 'SOME',
    'all': 'ALL',
    'value': 'VALUE',
    'min': 'MIN',
    'max': 'MAX',
    'exactly': 'EXACTLY',
    'that': 'THAT',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'only': 'ONLY',
    'class': 'CLASS',
    'equivalento': 'EQUIVALENTTO',
    'individuals': 'INDIVIDUALS',
    'subclassof': 'SUBCLASSOF',
    'disjointclasses': 'DISJOINTCLASSES'
}

tokens = [
    'ID',
    'HAS',
    'IS',
    'OF',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'GT',
    'LT',
    'EQ',
    'COLON',
    'CARDINALITY',
    'DATA_TYPE',
    'PROPERTY',
    'RESERVED'
] + list(reserved.values())

t_SOME = r'SOME'
t_ALL = r'ALL'
t_VALUE = r'VALUE'
t_MIN = r'MIN'
t_MAX = r'MAX'
t_EXACTLY = r'EXACTLY'
t_THAT = r'THAT'
t_NOT = r'NOT'
t_AND = r'AND'
t_OR = r'OR'
t_CLASS = r'Class'
t_EQUIVALENTTO = r'EquivalentTo'
t_INDIVIDUALS = r'Individuals'
t_SUBCLASSOF = r'SubClassOf'
t_DISJOINTCLASSES = r'DisjointClasses'
t_HAS = r'has'
t_IS = r'is'
t_OF = r'Of'
t_ONLY = r'only'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_GT = r'>'
t_LT = r'<'
t_COLON = r':'
t_EQ = r'='

# Abaixo estão as funções para reconhecer cada token ou palavra reservada da linguagem, contendo as expressões regulares para reconhecer as cadeias.
def t_RESERVED(t):
    r'(Class:|Individuals:|EquivalentTo:|SubClassOf:|DisjointClasses:|some|all|and|value|min|max|exactly|only|that|not)'
    t.type = 'RESERVED'
    return t

def t_DATA_TYPE(t):
    r'(owl:|rdfs:|xsd:)\w+'
    t.type = 'DATA_TYPE'
    return t

def t_INDIVIDUAL(t):
    r'[A-Z][a-zA-Z0-9]*\d+'
    t.type = 'INDIVIDUALS'
    return t

def t_PROPERTY(t):
    r'(\bis\w*Of\b)|(\bhas\w*\b)|([a-z]+\w*)'
    t.type = 'PROPERTY'
    return t

def t_CARDINALITY(t):
    r'\d+'
    t.type = 'CARDINALITY'
    return t

def t_Class(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = 'CLASS'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Inicialização do analisador léxico
lexer = lex.lex()

lexer.input(file)

# Declaração de variáveis para contar as ocorrências dos tokens e demais coisas
found_tokens = []
property_count = 0
individual_count = 0
cardinalidade_count = 0
data_type_count = 0
classes_count = 0
reserved_count = 0

# Função principal
while True:
    tok = lexer.token()
    if not tok:
        break
    found_tokens.append((tok.lineno, tok.type, tok.value))
    if tok.type == 'PROPERTY':
        property_count += 1
    elif tok.type == 'INDIVIDUALS':
        individual_count += 1
    elif tok.type == 'CARDINALITY':
        cardinalidade_count += 1
    elif tok.type == 'DATA_TYPE':
        data_type_count += 1
    elif tok.type == 'RESERVED':
        reserved_count += 1
    elif tok.type == 'CLASS':
        classes_count += 1

# Em seguida está o resumo da análise, assim como o valor de cada lexema por linha
for lineno, token_type, token_value in found_tokens:
    print(f'Linha {lineno}: Token: {token_type}, Valor: {token_value}')

print(f"######################################## Resumo #########################################")
print(f"#                           Quantidade de Propriedades: {property_count}\t\t\t\t#")
print(f"#                           Quantidade de Indivíduos: {individual_count}\t\t\t\t#")
print(f"#                           Quantidade de Classes: {classes_count}\t\t\t\t\t#")
print(f"#                           Quantidade de Cardinalidades: {cardinalidade_count}\t\t\t\t#")
print(f"#                           Quantidade de Tipos de dados: {data_type_count}\t\t\t\t#")
print(f"#                           Quantidade de Palavras reservadas: {reserved_count}\t\t\t#")
print(f"#########################################################################################")

# Dados do resumo
data = {
    "Quantidade de Propriedades": [property_count],
    "Quantidade de Indivíduos": [individual_count],
    "Quantidade de Classes": [classes_count],
    "Quantidade de Cardinalidades": [cardinalidade_count],
    "Quantidade de Tipos de dados": [data_type_count],
    "Quantidade de Palavras reservadas": [reserved_count]
}

# Criar um DataFrame (Para imagem)
df = pd.DataFrame(data)

# Criar uma tabela
fig, ax = plt.subplots(figsize=(8, 2))  
ax.axis('off')
table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 cellLoc='center',
                 loc='center')

# Salvar como PNG 
plt.savefig('resumo_tabela.png', bbox_inches='tight', dpi=300)

# Declaração de variáveis para contar as ocorrências dos tokens e demais coisas
found_tokens = []
property_count = 0
individual_count = 0
cardinality_count = 0
data_type_count = 0
reserved_count = 0
disjoint_classes_count = 0
equivalent_classes_count = 0
subclass_count = 0
individual_classes_count = 0

# Regras de produção sintáticas
def p_ontologia(p):
    '''
    ontologia : descricao_classes descricao_individuals
    '''

def p_descricao_classes(p):
    '''
    descricao_classes : CLASS ID equivalencia_classes descricao_classes
                      | CLASS ID subclasso_classes descricao_classes
                      | CLASS ID disjoint_classes descricao_classes
                      | 
    '''
    global classes_count
    classes_count += 1

def p_equivalencia_classes(p):
    '''
    equivalencia_classes : EQUIVALENTTO expressao_classes COMMA
                         | EQUIVALENTTO expressao_classes
    '''
    global equivalent_classes_count
    equivalent_classes_count += 1

def p_subclasso_classes(p):
    '''
    subclasso_classes : SUBCLASSOF expressao_classes propriedades COMMA
                      | SUBCLASSOF expressao_classes propriedades
                      | SUBCLASSOF expressao_classes COMMA
                      | SUBCLASSOF expressao_classes
    '''
    global subclass_count
    subclass_count += 1

def p_disjoint_classes(p):
    '''
    disjoint_classes : DISJOINTCLASSES LPAREN ID COMMA ID COMMA ID RPAREN COMMA
                     | DISJOINTCLASSES LPAREN ID COMMA ID COMMA ID RPAREN
    '''
    global disjoint_classes_count
    disjoint_classes_count += 1

def p_propriedades(p):
    '''
    propriedades : PROPERTY expressao_classes COMMA
                 | PROPERTY expressao_classes
    '''
    global property_count
    property_count += 1

def p_expressao_classes(p):
    '''
    expressao_classes : ID
                      | ID AND LPAREN expressao_classes COMMA expressao_classes RPAREN
                      | ID AND LPAREN expressao_classes COMMA ID SOME ID RPAREN
                      | ID AND LPAREN ID SOME ID RPAREN
                      | ID AND LPAREN ID COMMA ID SOME ID RPAREN
    '''

def p_descricao_individuals(p):
    '''
    descricao_individuals : CLASS ID COMMA ID descricao_individuals
                          | CLASS ID COMMA descricao_individuals
                          | 
    '''
    global individual_classes_count
    individual_classes_count += 1

def p_error(p):
    print("Erro de sintaxe:", p)

# Construção do analisador Sintático
parser = yacc.yacc()

# Analisa os dados utilizando o parser
parser.parse(file)

# Resumo da Análise Sintática
print("==================================== Resumo da Análise Sintática ====================================")
print(f"#                           Quantidade de Disjunções de Classes: {disjoint_classes_count}\t\t\t#")
print(f"#                           Quantidade de Equivalências de Classes: {equivalent_classes_count}\t\t\t#")
print(f"#                           Quantidade de Subclasses: {subclass_count}\t\t\t\t#")
print(f"#                           Quantidade de Classes Individuais: {individual_classes_count}\t\t\t#")
print("=======================================================================================================")