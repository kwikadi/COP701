import ply.lex as lex
from preprocess import clean_input

tokens = (
    'OB',  # open braces
    'CB',  # close braces
    'DOC',  # document
    'BEGIN',
    'END',
    'SECTION',
    'SUBSECTION',
    'TEXT',  # the actual text to be output
    'NEWLINE',
    'ITALICS',
    'BOLD',
    'PAR',
    'UNDERLINE',
    'CAPTION',
    'FRAC',
    'SQRT',
    'DOLLAR',
    'SUM',
    'INT',
    'COMMAND',
    'ENUMERATE',
    'ITEMIZE',
    'ITEM',
    'INCLUDEGRAPHICS',
    'CARET',
    'UNDERSCORE'
    )

t_NEWLINE = r'[\n]+'
t_OB = r'{'
t_CB = r'}'
t_DOLLAR = r'\$'
t_CARET = r'\^'

def t_COMMAND(t):
    r'\\[a-z]+'

    if t.value == '\\section':
        t.type = 'SECTION'

    elif t.value == '\\subsection':
        t.type = 'SUBSECTION'

    elif t.value == '\\begin':
        t.type = 'BEGIN'

    elif t.value == '\\end':
        t.type = 'END'

    elif t.value == '\\textbf':
        t.type = 'BOLD'

    elif t.value == '\\textit':
        t.type = 'ITALICS'

    elif t.value == '\\par':
        t.type = 'PAR'

    elif t.value == '\\underline':
        t.type = 'UNDERLINE'

    elif t.value == '\\item':
        t.type = 'ITEM'

    elif t.value == '\\caption':
        t.type = 'CAPTION'

    elif t.value == '\\frac':
        t.type = 'FRAC'

    elif t.value == '\\sqrt':
        t.type = 'SQRT'

    elif t.value == '\\sum':
        t.type = 'SUM'

    elif t.value == '\\int':
        t.type = 'INT'

    elif t.value == '\\includegraphics':
        t.type = 'INCLUDEGRAPHICS'

    return t


def t_TEXT(t):
    r'[a-zA-Z0-9_., \t=]+'

    if t.value == 'document':
        t.type = 'DOC'

    elif t.value == 'enumerate':
        t.type = 'ENUMERATE'

    elif t.value == 'itemize':
        t.type = 'ITEMIZE'

    elif t.value == '_':
        t.type = 'UNDERSCORE'
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def get_data(inputfile):
    lexer = lex.lex()
    data = clean_input(inputfile)
    lexer.input(data)


    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    return data
