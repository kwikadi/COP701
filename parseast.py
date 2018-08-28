section_num = 0
subsection_num = 0


def parse_ast(node):
    if node:
        if node.type == 'total':
            # create HTML skeleton
            print("At the top")
            parse_ast(node.children[0])
            print("Finishing")
            # close HTML skeleton
        elif node.type == 'statements':
            print("Statements enter")
            for i in node.children:
                parse_ast(i)
            print("Statements exit")
        elif node.type == 'section':
            print("Section enter")
            print (node.information)
            print("Section exit")
            # add heading to file or w/e
        elif node.type == 'newline':
            print("Newline enter, exit")
        elif node.type == 'subsection':
            print("Subsection enter")
            print(node.information)
            print("Subsection exit")
        elif node.type == 'text':
            print(node.information)