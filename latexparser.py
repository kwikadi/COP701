import ply.yacc as yacc
from latexlexer import tokens, data
from node import Node
from parseast import parse_ast, get_html_string

def p_latex_complete(p):
    """
    totaldoc : begindoc statements enddoc
    """
    p[0] = Node('total', [p[2]])


def p_doc_beginning(p):
    """
    begindoc : BEGIN OB DOC CB NEWLINE
    """


def p_doc_ending(p):
    """
    enddoc : END OB DOC CB
    """


def p_multiple_statements(p):
    """
    statements : statements statement
    """
    p[0] = Node('statements', [p[1], p[2]])


def p_single_statement(p):
    """
    statements : statement
    """
    p[0] = Node('statements', [p[1]])


def p_section_statement(p):
    """
    statement : SECTION OB TEXT CB
    """
    p[0] = Node('section', information=p[3])


def p_subsection_statement(p):
    """
    statement : SUBSECTION OB TEXT CB
    """
    p[0] = Node('subsection', information=p[3])


def p_newline_statement(p):
    """
    statement : NEWLINE
    """
    p[0] = Node('newline', information=p[1])


def p_text_statement(p):
    """
    statement : TEXT
    """
    p[0] = Node('text', information=p[1])


def p_bold_statement(p):
    """
    statement : BOLD OB TEXT CB
    """
    p[0] = Node('bold', information=p[3])


def p_italics_statement(p):
    """
    statement : ITALICS OB TEXT CB
    """
    p[0] = Node('italics', information=p[3])


def p_frac_statement(p):
    """
    mathstat : FRAC OB TEXT CB OB TEXT CB
    """
    p[0] = Node('fraction', information=[p[3],p[6]])


def p_sqrt_statement(p):
    """
    mathstat : SQRT OB TEXT CB
    """
    p[0] = Node('sqrt', information=p[3])


def p_underline_statement(p):
    """
    statement : UNDERLINE OB TEXT CB
    """
    p[0] = Node('underline', information=p[3])

def p_caption_statement(p):
    """
    statement : CAPTION OB TEXT CB
    """
    p[0] = Node('caption', information=p[3])


def p_math_mode(p):
    """
    statement : DOLLAR mathstats DOLLAR
    """
    p[0] = Node('mathstats', [p[2]])


def p_math_statements(p):
    """
    mathstats : mathstats mathstat
    """
    p[0] = Node('mathstats', [p[1],p[2]])


def p_math_statement(p):
    """
    mathstats : mathstat
    """
    p[0] = Node('mathstat', [p[1]])


parser = yacc.yacc()

result = parser.parse(data)

parse_ast(result)

with open('test.html', 'w') as testfile:
    testfile.write(get_html_string())