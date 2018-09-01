import re


def clean_input_string(string):
    if string.startswith('\graphicspath'):
        return ""
    replaced = re.sub(r'^\s*\n$', r'\n', string)
    replaced2 = re.sub(r'(^%|[^\\]\%).*', '', replaced)
    replaced3 = re.sub(r'\\hline', '', replaced2)
    return replaced3


def clean_input_file(inputfile):

    cleaned_string = ''
    start_copying = 0
    line_count = 0
    line_counting = False
    new_cleaned_string = ''

    for i in open(inputfile, 'r').readlines():
        if i.strip() == r'\end{document}':
            cleaned_string += clean_input_string(i)
            break
        elif i.strip() == r'\begin{document}':
            start_copying = 1
        if start_copying == 1 and not i.lstrip().startswith('%'):
            cleaned_string += clean_input_string(i)
        continue

    for line in cleaned_string.split('\n'):
        if line.startswith('\\begin{tabular}'):
            line_counting = True
            line_count += 1
        elif line_counting and not line.startswith('\\end{tabular}') and line.endswith('\\'):
            line_count += 1
        elif not line.endswith('\\') and line_counting:
            line = line + '\\\\' + '\n'*(line_count+1)
            line_counting = False
            line_count = 0
        new_cleaned_string += line + '\n'

    new_cleaned_string = new_cleaned_string[:-1]
    return new_cleaned_string


def clean_input(inputfile):
    cleanedfile = clean_input_file(inputfile)
    return cleanedfile