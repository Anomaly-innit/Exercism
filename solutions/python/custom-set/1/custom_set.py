class CustomSet:
    def __init__(self, elements=[]):
        self.elements = set(elements)

    def isempty(self):
        return len(self.elements) == 0

    def __contains__(self, element):
        return element in self.elements

    def issubset(self, other):
        return all(a in other.elements for a in self.elements)

    def isdisjoint(self, other):
        return all(a not in other.elements for a in self.elements)

    def __eq__(self, other):
        return self.elements == other.elements

    def add(self, element):
        return self.elements.add(element)

    def intersection(self, other):
        return CustomSet(self.elements & other.elements)
        
    def __sub__(self, other):
        return CustomSet(self.elements - other.elements)

    def __add__(self, other):
        return CustomSet(self.elements | other.elements)
