# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Trees.Tree
from Trees import Tree


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    tree = Tree.Tree()
    node = Tree.Node()
    node.data = 5
    tree.add_node(node)
    node1 = Tree.Node()
    node1.data = 1
    tree.add_node(node1)
    node2 = Tree.Node()
    node2.data = 10
    tree.add_node(node2)
    tree.print_nodes()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
