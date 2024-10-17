from .binary_tree import BinaryTree
from .node import TreeNode
from src.utils.helpers import node_search, root_validation

class BinarySearchTree(BinaryTree):
    
    def insert(self, name: str, number: int) -> None:
        """
        Insere um novo contato (nó) na árvore binária de busca.

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

        Example:
            >>> ex = BinarySearchTree()
            >>> ex.insert('Diogo', 31991687502)
        """
        self.__name_verification(name)

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

    def __name_verification(self, name: str) -> None:
        """
        Verifica se o nome já existe na árvore binária de busca.

        Este método realiza um busca na árvore binária de busca
        pelo nome fornecido.
        Se o nome for encontrado, uma execeção será levantada.

        Args:
            name (str): Nome do contato a ser verificado.

        Raises:
            Exception: Se o nome já existir na árvore.
        """
        search_name = node_search(name, self.root)

        if search_name:
            raise Exception('Name already existing')

    def search(self, name: str) -> TreeNode:
        """
        Busca um contato (nó) na árvore binária de busca.

        Realiza a busca na árvore baseada no nome fornecido.
        O método valida se a raiz não é None antes de iniciar a busca.

        Returns:
            TreeNode: O nó correspondente ao contato, se encontrado.

        Raises:
            IndexError: Se a raiz da árvore estiver vazia ou se o nome não for encontrado.
        """
        root = root_validation(self.root)
        node = node_search(name, root)

        if not node:
            raise IndexError('Name not found')
        return node

    def update(self, name: str, new_number: int) -> None:
        """
        Atualiza o número de telefone de um contato existente na árvore.

        Se o nome fornecido não for encontrado na árvore, levanta um `IndexError`.
        Se for encontrado, o número do contato é atualizado pera o novo valor fornecido.

        Args:
            name (str): O nome do contato a ser atualizado.
            new_number (int): O novo número de telefone a ser atribuído ao contato.

        Raises:
            IndexError: Se a raiz da árvore estiver vazia ou se o nome não for encontrado.
        """
        root = root_validation(self.root)
        node = node_search(name, root)
        
        if not node:
            raise IndexError('Name not found')
        node.number = new_number
