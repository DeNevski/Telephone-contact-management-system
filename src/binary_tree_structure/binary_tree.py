from .node import TreeNode
from src.utils.validations import root_validation

class BinaryTree:

    def __init__(self) -> None:
        self.root = None

    def ascending_order(self, node: TreeNode | None = None) -> None:
        """
        Percorre e imprime os nós da árvore binária de busca em ordem alfabética crescente.

        A travessia é feita em ordem (in-order), ou seja, o método visita primeiro o nó
        mais à esquerda, depois a raiz, e finalmente os nós à direita, imprimindo os
        nós nessa sequência, o que resulta na ordem alfabética crescente dos nomes.

        Se o parâmetro `node` não for fornecido, o método começa a partir da raiz da árvore.

        Args:
            node (TreeNode | None, opcional): O nó de onde a travessia começa. Se não for
            especificado, o método usa a raiz da árvore.

        Example:
            >>> tree = BinarySearchTree()
            >>> tree.insert('Alice', 123)
            >>> tree.insert('Bob', 456)
            >>> tree.insert('Charlie', 789)
            >>> tree.ascending_order()
            Alice
            Bob
            Charlie
        """
        if node is None:
            node = root_validation(self.root)

        if node.left:
            self.ascending_order(node.left)

        print(node, end='\n')

        if node.right:
            self.ascending_order(node.right)

    def descending_order(self, node: TreeNode | None = None) -> None:
        """
        Percorre e imprime os nós da árvore binária de busca em ordem alfabética decrescente.

        A travessia é feita em ordem reversa (reverse in-order), ou seja, o método visita
        primeiro o nó mais à direita, depois a raiz, e finalmente os nós à esquerda, imprimindo
        os nós nessa sequência, o que resulta na ordem alfabética decrescente dos nomes.

        Se o parâmetro `node` não for fornecido, o método começa a partir da raiz da árvore.

        Args:
            node (TreeNode | None, opcional): O nó de onde a travessia começa. Se não for
            especificado, o método usa a raiz da árvore.

        Example:
            >>> tree = BinarySearchTree()
            >>> tree.insert('Alice', 123)
            >>> tree.insert('Bob', 456)
            >>> tree.insert('Charlie', 789)
            >>> tree.descending_order()
            Charlie
            Bob
            Alice
        """
        if node is None:
            node = root_validation(self.root)

        if node.right:
            self.descending_order(node.right)

        print(node, end='\n')
        
        if node.left:
            self.descending_order(node.left)
