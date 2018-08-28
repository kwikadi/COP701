class Node:
    def __init__(self, type, children=None, information=None):
        self.type = type
        if information:
            self.information = information
        if children:
            self.children = children
        else:
            self.children = []
