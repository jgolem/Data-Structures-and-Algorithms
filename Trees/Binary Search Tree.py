
# Binary Search tree and it's management
# Notes - Left child is always smaller and right child is always larger


class Tree:
    Nodes = []

    def insert(self, node):
        if len(self.Nodes) == 0:
            self.Nodes.append(node)
            return

        keep_going = True
        current_node = 0

        'while keep_going:

            'if node.data < self.Nodes[current_node]:
                'if self.Nodes[current_node].leftChild is not None:
                    'current_node =



class Node:
    data = None
    leftChild = None
    rightChild = None

