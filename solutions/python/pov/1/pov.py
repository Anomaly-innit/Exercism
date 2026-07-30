from json import dumps


class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        path = []
        if not find_path(self, from_node, path):
            raise ValueError("Tree could not be reoriented")
        
        new_node = None
        for i in range(len(path)):
            current = path[i]
            if i + 1 < len(path):
                children = [c for c in current.children if c is not path[i + 1]]
            else:
                children = list(current.children)
            if new_node is not None:
                children.append(new_node)
            new_node = Tree(current.label, children)
        
        return new_node

    def path_to(self, from_node, to_node):
        reoriented = self.from_pov(from_node)
        path = []
        if not find_path(reoriented, to_node, path):
            raise ValueError("No path found")
        return [n.label for n in path]
        
def find_path(node, label, path):
    path.append(node)
    if node.label == label:
        return True
    for child in node.children:
        if find_path(child, label, path):
            return True
    path.pop()
    return False
    