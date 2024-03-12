import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = [
    'CLASS',
    'EQUIVALENTTO',
    'INDIVIDUALS',
    'SUBCLASSOF',
    'DISJOINTCLASSES',
    'SOME',
    'AND',
    'ID',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'COLON',
    'INTEGER',
    'DATA_TYPE',
    'RESERVED'
]

# Expressões regulares para tokens simples
t_SOME = r'some'
t_AND = r'and'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_COLON = r':'
t_RESERVED = r'(Class|Individuals|EquivalentTo|SubClassOf|DisjointClasses|some|and)'
t_ignore = ' \t\n'

# Regra para ID
def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = 'ID'
    return t

# Regra para INTEGER
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para DATA_TYPE
def t_DATA_TYPE(t):
    r'(owl:|rdfs:|xsd:)\w+'
    t.type = 'DATA_TYPE'
    return t

# Função para lidar com quebra de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Função de erro
def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

# Regras de produção
def p_ontologia(p):
    '''
    ontologia : descricao_classes descricao_individuals
    '''

def p_descricao_classes(p):
    '''
    descricao_classes : CLASS ID EQUIVALENTTO expression_class COMMA descricao_classes
                      | CLASS ID SUBCLASSOF expression_class COMMA descricao_classes
                      | CLASS ID DISJOINTCLASSES LPAREN ID COMMA ID COMMA ID RPAREN COMMA descricao_classes
                      | 
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
    descricao_individuals : CLASS ID COLON ID COMMA descricao_individuals
                          | 
    '''

def p_error(p):
    print("Erro de sintaxe:", p)

# Construção do analisador
parser = yacc.yacc()