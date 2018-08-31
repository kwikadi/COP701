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
    statement : SECTION OB statements CB
    """
    p[0] = Node('section', [p[3]])


def p_subsection_statement(p):
    """
    statement : SUBSECTION OB statements CB
    """
    p[0] = Node('subsection', [p[3]])


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
    statement : BOLD OB statements CB
    """
    p[0] = Node('bold', [p[3]])


def p_italics_statement(p):
    """
    statement : ITALICS OB statements CB
    """
    p[0] = Node('italics', [p[3]])


def p_frac_statement(p):
    """
    mathstat : FRAC OB mathstats CB OB mathstats CB
    """
    p[0] = Node('fraction', [p[3], p[6]])


def p_sqrt_statement(p):
    """
    mathstat : SQRT OB mathstats CB
    """
    p[0] = Node('sqrt', [p[3]])


def p_underline_statement(p):
    """
    statement : UNDERLINE OB statements CB
    """
    p[0] = Node('underline', [p[3]])


def p_caption_statement(p):
    """
    statement : CAPTION OB statements CB
    """
    p[0] = Node('caption', [p[3]])


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
              | TEXT
    """
    p[0] = Node('mathstat', [p[1]])


def p_paragraph_statement(p):
    """
    statement : PAR
    """
    p[0] = Node('paragraph')


def p_enumerate_statement(p):
    """
    beginenum : BEGIN OB ENUMERATE CB
    """


def p_itemize_statement(p):
    """
    beginitemize : BEGIN OB ITEMIZE CB
    """


def p_enumerate_statement_end(p):
    """
    endenum : END OB ENUMERATE CB
    """


def p_itemize_statement_end(p):
    """
    enditemize : END OB ITEMIZE CB
    """


def p_enum_statements(p):
    """
    statement : beginenum statements endenum
    """
    p[0] = Node('enumerate', [p[2]])


def p_itemize_statements(p):
    """
    statement : beginitemize statements enditemize
    """
    p[0] = Node('itemize', [p[2]])


def p_item_statement(p):
    """
    statement : ITEM statement
    """
    p[0] = Node('item', [p[1]])


def p_graphics_statement(p):
    """
    statement : INCLUDEGRAPHICS OB TEXT CB
    """
    p[0] = Node('image', information=p[3])


def p_integral_statement(p):
    """
    mathstat : INT UNDERSCORE OB TEXT CB CARET OB TEXT CB mathstat
    """
    p[0] = Node('integral', information=[p[4], p[8]])


def p_sum_statement(p):
    """
    mathstat : SUM UNDERSCORE OB TEXT CB CARET OB TEXT CB mathstat
    """
    p[0] = Node('sum', information=[p[4], p[8]])


parser = yacc.yacc()

result = parser.parse(data)

parse_ast(result)

with open('test.html', 'w') as testfile:
    testfile.write(get_html_string())