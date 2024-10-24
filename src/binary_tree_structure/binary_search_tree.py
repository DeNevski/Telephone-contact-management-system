from .binary_tree import BinaryTree
from .node import TreeNode
from src.utils.helpers import node_search, node_validation
from src.utils.validations import name_and_number_validation, name_verification, root_validation

class BinarySearchTree(BinaryTree):
    
    def insert(self, name: str, number: int) -> None:
        """
        Insere um novo contato (nó) na árvore binária de busca.

        Será feito uma validação do tipo dos dados fornecidos,
        levantando um `TypeError` caso o tipo não for o esperado.

        O novo nó é inserido de acordo com a ordem alfabética do nome.
        Caso já exista um nó com o mesmo nome, uma exceção será lançada.

        - Se a árvore estiver vazia, o novo nó será definido como a raiz.
        - Se a árvore já possuir nós, o algoritmo percorre a árvore 
        comparando o nome do novo nó com os nós existentes:
            - Se o nome for menor, o nó é inserido na subárvore esquerda.
            - Se o nome for maior, o nó é inserido na subárvore direita.
        - A inserção é feita quando se encontra uma folha (nó sem filhos).

        Args:
            name (str): O nome do contato a ser inserido.
            number (int): O número de telefone do contato.

        Raises:
            Exception: Se um contato com o mesmo nome já existir.
            TypeError: Se for passado um tipo de dado não esperado.

        Example:
            >>> ex = BinarySearchTree()
            >>> ex.insert('Diogo', 31991687502)
        """
        name_and_number_validation(name, number)
        
        name_verification(name, self.root)

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

    def search(self, name: str) -> TreeNode:
        """
        Busca um contato (nó) na árvore binária de busca.

        Realiza a busca na árvore baseada no nome fornecido.
        O método válida se é fornecido o tipo correto e se
        a raiz não é None antes de iniciar a busca.

        Returns:
            TreeNode: O nó correspondente ao contato, se encontrado.

        Raises:
            IndexError: Se a raiz da árvore estiver vazia ou se o nome não for encontrado.
            TypeError: Se for passado um tipo de dado não esperado.
        """
        name_and_number_validation(name)

        root = root_validation(self.root)
        node = node_search(name, root)

        node_validation(node)
        return node

    def update(self, name: str, new_number: int) -> None:
        """
        Atualiza o número de telefone de um contato existente na árvore.

        Válida se o tipo de dado fornecido é o esperado. Levanta um `TypeError` caso não for.

        Se o nome fornecido não for encontrado na árvore, levanta um `IndexError`.
        Se for encontrado, o número do contato é atualizado pera o novo valor fornecido.

        Args:
            name (str): O nome do contato a ser atualizado.
            new_number (int): O novo número de telefone a ser atribuído ao contato.

        Raises:
            IndexError: Se a raiz da árvore estiver vazia ou se o nome não for encontrado.
            TypeError: Se for passado um tipo de dado não esperado.
        """
        name_and_number_validation(name, new_number)

        root = root_validation(self.root)
        node = node_search(name, root)
        
        node_validation(node)
        node.number = new_number

    def min(self, node: TreeNode | None = None) -> str:
        """
        Retorna o nó do contato com o menor valor (ordem alfabética) na árvore binária de busca.

        A função percorre a árvore binária de busca à esquerda para encontrar o nó com o menor valor,
        que é o mais à esquerda na árvore.

        Args:
            node (TreeNode | None, opcional): O nó a partir do qual a busca deve começar. Se não for fornecido,
            a busca começa a partir da raiz da árvore.

        Returns:
            str: O nó do contato que possui o menor valor (nome em ordem alfabética).
        """
        if node is None:
            node = self.root

        root_validation(node)

        while node.left:
            node = node.left
        return node
