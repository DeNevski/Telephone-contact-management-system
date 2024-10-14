from .binary_tree import BinaryTree
from .node import TreeNode


class BinarySearchTree(BinaryTree):
    
    # Insere um nó na árvore
    def insert(self, name: str, number: int) -> None:
        parent = None
        x = self.root
        
        while x:
            parent = x

            if name < x.name:
                x = x.left
            else:
                x = x.right
        
        if parent is None:
            self.root = TreeNode(name, number)
        elif name < parent.name:
            parent.left = TreeNode(name, number)
        else:
            parent.right = TreeNode(name, number)
