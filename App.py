import ply.lex as lex
import ply.yacc as yacc

# Lendo o arquivo no diretório do projeto, contendo o exemplo a ser analisado.
PATH = 'dados.txt'

try:
    with open(PATH, 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print(f"Arquivo não encontrado '{PATH}' !!!")
except Exception as e:
    print(f"ERRO: '{e}'")

file = conteudo

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
    'equivalentto': 'EQUIVALENTTO',
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
    'RESERVED',
    'PROPRIEDADE',  # Adicionado
    'value_type'    # Adicionado
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
t_CLASS = r'CLASS'
t_EQUIVALENTTO = r'EQUIVALENTTO'
t_INDIVIDUALS = r'INDIVIDUALS'
t_SUBCLASSOF = r'SUBCLASSOF'
t_DISJOINTCLASSES = r'DISJOINTCLASSES'
t_HAS = r'HAS'
t_IS = r'IS'
t_OF = r'OF'
t_ONLY = r'ONLY'
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
    r'individuals:|equivalentto:|subclassof:|disjointclasses:|some|all|and|value|min|max|exactly|only|that|not'
    if t.value == 'class':
        t.type = 'CLASS'
    else:
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

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'ID')
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

print("Tokens identificados:")
for token in lexer:
    print(token)

print("=======================================")

# Regras de produção sintaticas
def p_ontologia(p):
    '''
    ontologia : descricao_classes descricao_individuals
    '''

def p_descricao_classes(p):
    '''
    descricao_classes : CLASS ID EQUIVALENTTO expression_class COMMA descricao_classes
                      | CLASS ID SUBCLASSOF expression_class COMMA descricao_classes
                      | CLASS ID SUBCLASSOF expression_class propriedades COMMA descricao_classes
                      | CLASS ID DISJOINTCLASSES LPAREN ID COMMA ID COMMA ID RPAREN COMMA descricao_classes
                      | CLASS ID EQUIVALENTTO expression_class propriedades COMMA descricao_classes
                      | CLASS ID SUBCLASSOF expression_class closure_axiom COMMA descricao_classes
                      | CLASS ID SUBCLASSOF expression_class nested_description COMMA descricao_classes
                      | CLASS ID SUBCLASSOF expression_class enumerated_instances COMMA descricao_classes
                      | CLASS ID SUBCLASSOF expression_class covered_class COMMA descricao_classes
                      | 
    '''

# definição de propriedades de uma classe primitiva
def p_propriedades(p):
    '''
    propriedades : PROPERTY expression_class COMMA propriedades
                 | 
    '''

# capturar axioma de fechamento de uma classe
def p_closure_axiom(p):
    '''
    closure_axiom : LPAREN PROPERTY ONLY LPAREN expression_class OR expression_class RPAREN RPAREN
    '''

# capturar as descrições aninhadas de uma classe
def p_nested_description(p):
    '''
    nested_description : LPAREN PROPERTY value_type RPAREN
    '''

def p_expression_class(p):
    '''
    expression_class : ID
                     | ID AND LPAREN expression_class COMMA expression_class RPAREN
                     | ID AND LPAREN expression_class COMMA ID SOME ID RPAREN
                     | ID AND LPAREN ID SOME ID RPAREN
                     | ID AND LPAREN ID COMMA ID SOME ID RPAREN
    '''

def p_descricao_individuals(p):
    '''
    descricao_individuals : CLASS ID COMMA ID descricao_individuals
                          | CLASS ID COMMA descricao_individuals
                          | 
    '''

# capturar as instâncias enumeradas de uma classe
def p_enumerated_instances(p):
    '''
    enumerated_instances : LBRACE ID COMMA ID COMMA ID RBRACE
    '''

# capturar a definição de uma classe coberta
def p_covered_class(p):
    '''
    covered_class : CLASS ID AND LPAREN expression_class COMMA expression_class COMMA expression_class RPAREN
    '''

def p_error(p):
    print("Erro de sintaxe:", p)

# Construção do analisador Sintático
parser = yacc.yacc()

# Lê do arquivo dados.txt
with open("dados.txt", "r") as arquivo:
    dados = arquivo.read()

# Analisa os dados utilizando o parser
parser.parse(dados)