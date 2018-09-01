from html_strings import *

section_num = 0
subsection_num = 0
body_string = ''
last_node = ''
label_dict = {}
figure_val = 0
ignore_slash_n = False


def get_html_string():
    return start_string + body_string + end_string


def parse_ast(node):
    global body_string, section_num, subsection_num, last_node, label_dict, figure_val, ignore_slash_n
    if node:
        if node.type == 'total':
            parse_ast(node.children[0])

        elif node.type == 'statements':
            for i in node.children:
                parse_ast(i)

        elif node.type == 'section':
            last_node = 'section'
            subsection_num = 0
            section_num += 1
            body_string += section_start.format(str(section_num))
            parse_ast(node.children[0])
            body_string += section_end

        elif node.type == 'newline':
            last_node = 'newline'
            if not ignore_slash_n:
                body_string += break_tag

        elif node.type == 'subsection':
            last_node = 'subsection'
            subsection_num += 1
            body_string += subsection_start.format(str(section_num), str(subsection_num))
            parse_ast(node.children[0])
            body_string += subsection_end
            subsection_num -= 1

        elif node.type == 'paragraph':
            body_string += break_tag

        elif node.type == 'text':
            body_string += str(node.information)

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
            ignore_slash_n = True
            body_string += enumerate_start
            parse_ast(node.children[0])
            body_string += enumerate_end

        elif node.type == 'itemize':
            ignore_slash_n = True
            body_string += itemize_start
            parse_ast(node.children[0])
            body_string += itemize_end

        elif node.type == 'item':
            body_string += item_start
            parse_ast(node.children[0])
            body_string += item_end

        elif node.type == 'image':
            body_string += image_tag.format(str(node.information))

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
            body_string += integral_tag.format(str(node.information[0]), str(node.information[1]))
            parse_ast(node.children[0])

        elif node.type == 'sum':
            body_string += sum_tag.format(str(node.information[0]), str(node.information[1]))
            parse_ast(node.children[0])

        elif node.type == 'caption':
            figure_val += 1
            last_node = 'image'
            body_string += caption_start.format(figure_val)
            parse_ast(node.children[0])
            body_string += caption_end

        elif node.type == 'mathstat':
            body_string += str(node.information)

        elif node.type == 'mathstats':
            parse_ast(node.children[0])

        elif node.type == 'label':
            if last_node == 'section':
                label_dict[node.information] = str(section_num)
            elif last_node == 'subsection':
                label_dict[node.information] = (str(section_num), ".", str(subsection_num))
            elif last_node == 'image':
                label_dict[node.information] = str(figure_val)

        elif node.type == 'ref':
            body_string += str(label_dict[node.information])

        elif node.type == 'tabul':
            body_string += table_start
            parse_ast(node.children[0])
            if body_string.endswith('<tr>'):
                body_string = body_string[:-4]
            body_string += table_end

        elif node.type == 'tableinfo':
            pass

        elif node.type == 'tab':
            parse_ast(node.children[0])

        elif node.type == 'element':
            body_string += element_tag.format(str(node.information))
            parse_ast(node.children[0])

        elif node.type == 'endelement':
            body_string += element_tag.format(str(node.information)) + row_end
            parse_ast(node.children[0])

        elif node.type == 'tabulrecur':
            for i in node.children:
                parse_ast(i)