from BST import *



if (__name__== "__main__"):
    tree = Tree("Apple")
    tree.getRoot().setLeftChild(Node("anajna"))
    tree.getRoot().getLeftChild().setLeftChild(Node("Skinny"))
    tree.getRoot().getLeftChild().getLeftChild().setRightChild(Node("alex"))
    tree.getRoot().getLeftChild().getLeftChild().setLeftChild(Node("Mango"))
    tree.getRoot().setRightChild(Node("snivek"))

    print("DFS PreOrder")
    print(DFT_PreOrder(tree))
    print()
    print("PreOrder Recursion")
    print(DFT_PreOrderRecursion(tree))
    print("BFS")
    print(BFS(tree))



