import ply.yacc as yacc
from latexlexer import tokens, data
from node import Node
from parseast import parse_ast

def p_latex_complete(p):
    """
    totaldoc : begindoc statements enddoc
    """
    p[0] = Node('total', [p[2]])


def p_doc_beginning(p):
    """
    begindoc : BS BEGIN OB DOC CB NEWLINE
    """


def p_doc_ending(p):
    """
    enddoc : BS END OB DOC CB
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
    statement : BS SECTION OB TEXT CB
    """
    p[0] = Node('section', information=p[4])


def p_subsection_statement(p):
    """
    statement : BS SUBSECTION OB TEXT CB
    """
    p[0] = Node('subsection', information=p[4])


def p_newline_statement(p):
    """
    statement : NEWLINE
    """
    p[0] = Node('newline')


def p_text_statement(p):
    """
    statement : TEXT
    """
    p[0] = Node('text', information=p[1])


parser = yacc.yacc()

result = parser.parse(data)

parse_ast(result)