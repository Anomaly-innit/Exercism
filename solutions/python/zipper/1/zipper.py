class Zipper:
    def __init__(self, focus, crumbs):
        self.focus = focus
        self.crumbs = crumbs
        
    @staticmethod
    def from_tree(tree):
        return Zipper(tree, [])

    def value(self):
        return self.focus["value"]

    def set_value(self, value):
        new_focus = dict(self.focus)
        new_focus["value"] = value
        return Zipper(new_focus, self.crumbs)

    def left(self):
        if self.focus["left"] is None:
            return None
        crumb = ("left", self.focus["value"], self.focus["right"])
        return Zipper(self.focus["left"], self.crumbs + [crumb])

    def set_left(self, tree):
        new_focus = dict(self.focus)
        new_focus["left"] = tree
        return Zipper(new_focus, self.crumbs)

    def right(self):
        if self.focus["right"] is None:
            return None
        crumb = ("right", self.focus["value"], self.focus["left"])
        return Zipper(self.focus["right"], self.crumbs + [crumb])

    def set_right(self, tree):
        new_focus = dict(self.focus)
        new_focus["right"] = tree
        return Zipper(new_focus, self.crumbs)

    def up(self):
        if not self.crumbs:
            return None
        direction, parent_value, sibling = self.crumbs[-1]
        if direction == "left":
            new_parent = {"value": parent_value, "left": self.focus, "right": sibling}
        else:
            new_parent = {"value": parent_value, "left": sibling, "right": self.focus}
        return Zipper(new_parent, self.crumbs[:-1])

    def to_tree(self):
        while self.crumbs:
            self = self.up()
        return self.focus
