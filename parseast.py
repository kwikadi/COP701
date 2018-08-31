from html_strings import *

section_num = 0
subsection_num = 0
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
            subsection_num = 0
            section_num += 1
            body_string += section_start.format(section_num)
            parse_ast(node.children[0])
            body_string += section_end

        elif node.type == 'newline':
            body_string += break_tag

        elif node.type == 'subsection':
            subsection_num += 1
            body_string += subsection_start.format(section_num, subsection_num)
            parse_ast(node.children[0])
            body_string += subsection_end
            subsection_num -= 1

        elif node.type == 'paragraph':
            body_string += break_tag

        elif node.type == 'text':
            body_string += f'{node.information}'

        elif node.type == 'italics':
            body_string += italics_start
            parse_ast(node.children[0])
            body_string += italics_end

        elif node.type == 'bold':
            body_string += bold_start
            parse_ast(node.children[0])
            body_string += bold_end

        elif node.type == 'underline':
            body_string += underline_start
            parse_ast(node.children[0])
            body_string += underline_end

        elif node.type == 'enumerate':
            body_string += enumerate_start
            parse_ast(node.children[0])
            body_string += enumerate_end

        elif node.type == 'itemize':
            body_string += itemize_start
            parse_ast(node.children[0])
            body_string += itemize_end

        elif node.type == 'item':
            body_string += item_start
            parse_ast(node.children[0])
            body_string += item_end

        elif node.type == 'image':
            body_string += image_tag.format(node.information)

        elif node.type == 'sqrt':
            body_string += sqrt_start
            parse_ast(node.children[0])
            body_string += sqrt_end

        elif node.type == 'fraction':
            body_string += fraction_start
            parse_ast(node.children[0])
            body_string += fraction_between
            parse_ast(node.children[1])
            body_string += fraction_end

        elif node.type == 'integral':
            body_string += integral_tag

        elif node.type == 'sum':
            body_string += sum_tag

        elif node.type == 'caption':
            body_string += caption_start
            parse_ast(node.children[0])
            body_string += caption_end

