from .node import TreeNode

class BinaryTree:

    def __init__(self, node: TreeNode = None) -> None:
        
        if node:
            self.root = node
        else:
            self.root = None

    # Retorna toda a árvore em ordem crescente
    def ascending_order(self, node: TreeNode = None) -> None:

        if node is None:
            node = self.root

        if node.left:
            self.ascending_order(node.left)

        print(node, end='\n')

        if node.right:
            self.ascending_order(node.right)

    # Retorna toda a árvore em ordem decrescente
    def descending_order(self, node: TreeNode = None) -> None:

        if node is None:
            node = self.root

        if node.right:
            self.descending_order(node.right)

        print(node, end='\n')
        
        if node.left:
            self.descending_order(node.left)
