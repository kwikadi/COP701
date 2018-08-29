import ply.lex as lex

tokens = (
    'BS',  # backslash
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
    'INT'
    # 'WHITESPACE',
    )

# t_WHITESPACE = r'[ \t]+'
t_NEWLINE = r'[\n]+'
t_OB = r'{'
t_CB = r'}'
t_DOLLAR = r'\$'


def t_TEXT(t):
    r'[a-zA-Z0-9_., \t\\]+'
    if t.value == '\\section':
        t.type = 'SECTION'
    elif t.value == '\\subsection':
        t.type = 'SUBSECTION'
    elif t.value == '\\begin':
        t.type = 'BEGIN'
    elif t.value == '\\end':
        t.type = 'END'
    elif t.value == 'document':
        t.type = 'DOC'
    elif t.value == '\\textbf':
        t.type = 'BOLD'
    elif t.value == '\\textit':
        t.type = 'ITALICS'
    elif t.value == '\\par':
        t.type = 'PAR'
    elif t.value == '\\underline':
        t.type = 'UNDERLINE'
    elif t.value == 'enumerate':
        t.type = 'ENUMERATE'
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
        t.type = 'GRAPHICS'
    elif t.value == '\\graphicspath':
        t.type = 'GRAP_PATH'
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = r'''\begin{document}

\section{Introduction}

This is the first section.

Lorem  ipsum  dolor  sit  amet,  consectetuer  adipiscing
elit.   Etiam  lobortisfacilisis sem.  Nullam nec mi et
neque pharetra sollicitudin.  Praesent imperdietmi nec ante.
Donec ullamcorper, felis non sodales...

\section{Second Section}

Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Etiam lobortis facilisissem.  Nullam nec mi et neque pharetra
sollicitudin.  Praesent imperdiet mi necante...

\end{document}'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
