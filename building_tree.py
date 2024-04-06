class BuildTree:
    def __init__(self, data, number_of_children):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        

