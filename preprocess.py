import argparse
import re


def get_input():

    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", help="The name of the LaTeX file to process")
    args = parser.parse_args()
    return args.inputFile


def clean_input_string(string):

    replaced = re.sub(r'^\s*\n$', r'\n', string)
    replaced2 = re.sub(r'(^%|[^\\]\%).*', '', replaced)
    return replaced2


def clean_input_file(inputfile):

    cleaned_string = ''
    start_copying = 0

    for i in open(inputfile, 'r').readlines():
        if i.strip() == r'\end{document}':
            break
        elif i.strip() == r'\begin{document}':
            start_copying = 1
        if start_copying == 1 and not i.lstrip().startswith('%'):
            cleaned_string += clean_input_string(i)
        continue

    # print( cleaned_string )
    return cleaned_string


def clean_input():
    inputfile = get_input()
    cleanedfile = clean_input_file(inputfile)
    return cleanedfile