
class TreeAsArray:
    nodes = []

    def add_node(self, new_node):
        """Adds a node to the tree"""
        if len(self.nodes) == 0:
            self.nodes.append(new_node)
            return




class Node:
    id = None
    left = None
    right = None
