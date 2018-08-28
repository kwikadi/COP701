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
    'NEWLINE'
    # 'WHITESPACE',
    )

# t_WHITESPACE = r'[ \t]+'
t_NEWLINE = r'[\n]'
t_OB = r'{'
t_CB = r'}'
t_BS = r'\\'


def t_TEXT(t):
    r'[a-zA-Z0-9_., \t]+'
    if t.value == 'section':
        t.type = 'SECTION'
    elif t.value == 'subsection':
        t.type = 'SUBSECTION'
    elif t.value == 'begin':
        t.type = 'BEGIN'
    elif t.value == 'end':
        t.type = 'END'
    elif t.value == 'document':
        t.type = 'DOC'
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

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)
