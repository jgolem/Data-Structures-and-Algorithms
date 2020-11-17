import queue


class Tree:
    root = None

    def print_nodes(self):
        q = queue.Queue()
        q.put(self.root)

        while not q.empty():
            node = q.get()
            print(node.data)

            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

    def add_node(self, new_node):
        """Adds a node to the tree"""
        current = self.root

        while True:

            if current is None:
                current = new_node
                return

            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right


class Node:
    data = None
    left = None
    right = None
