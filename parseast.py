section_num = 0
subsection_num = 0


start_string ='''<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <title></title>

</head>

<body>'''

end_string = '''</body>

</html>'''

body_string = ''


def get_html_string():
    return start_string + body_string + end_string


def parse_ast(node):
    global body_string, section_num, subsection_num, inside_section
    if node:
        if node.type == 'total':
            parse_ast(node.children[0])
        elif node.type == 'statements':
            for i in node.children:
                parse_ast(i)
        elif node.type == 'section':
            section_num += 1
            body_string += f'<h2>{section_num} {node.information}</h2>'
        elif node.type == 'newline':
            body_string += '<br>'
        elif node.type == 'subsection':
            subsection_num += 1
            body_string += f'<h3>{section_num}.{subsection_num} {node.information}</h3>'
        elif node.type == 'text':
            body_string += f'{node.information}'
        elif node.type == 'italics':
            body_string += f'<i>{node.information}</i>'
        elif node.type == 'bold':
            body_string += f'<b>{node.information}</b>'
