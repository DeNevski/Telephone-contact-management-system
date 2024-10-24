from src.binary_tree_structure.node import TreeNode
from src.utils.helpers import node_search

def name_verification(name: str, node: TreeNode) -> None:
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
    search_name = node_search(name, node)

    if search_name:
        raise Exception('Name already existing')

def root_validation(root: TreeNode) -> None | TreeNode:
    """
    Faz a validação de um nó da árvore.
    - Se for None, levanta um `IndexError`.
    - Se não for, retorna o próprio nó.
    """
    if not root:
        raise IndexError('The tree is empty')
    return root

def name_and_number_validation(name: str, number: int | None = None) -> None:
    """
    Valida o tipo do nome e do número de telefone fornecidos.

    Esta função verifica se o nome é uma string e, caso um número de telefone seja fornecido,
    valida se ele é do tipo inteiro.
    Se os tipos estiverem incorretos, uma exceção `TypeError` será levantada.

    Args:
        name (str): O nome a ser validado.
        number (int | None, opcional): O número de telefone a ser validado, o padrão é None.

    Raises:
        TypeError: Se `name` não for uma string ou se `number` for fornecido e não for um inteiro.
    """
    if not isinstance(name, str):
        raise TypeError('Name must be of type str')
    
    if number and not isinstance(number, int):
        raise TypeError('Number must be of type int')

def node_validation(node: TreeNode) -> None:
    """
    Valida node e levanta um `IndexError` caso for None.
    """
    if not node:
            raise IndexError('Name not found')