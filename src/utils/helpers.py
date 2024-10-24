from src.binary_tree_structure.node import TreeNode

def node_search(name: str, node: TreeNode) -> TreeNode | None:
    """
    Realiza a busca por um contato (nó) na árvore binária de busca.

    A função procura por um nó com o nome fornecido a partir do nó atual da árvore.
    A busca é recursiva, comparando o nome fornecido com o nome armazenado nos nós:
    
    - Se o nome for igual ao nome do nó atual, o nó é retornado.
    - Se o nome for menor, a busca continua na subárvore esquerda.
    - Se o nome for maior, a busca continua na subárvore direita.
    - Se o nó não for encontrado, a função retorna None.

    Args:
        name (str): O nome do contato a ser buscado.
        node (TreeNode): O nó atual da árvore binária a partir do qual a busca é feita.

    Returns:
        (TreeNode | None): O nó que contém o contato buscado, ou None se o nome não for encontrado.
    """
    if node:
        if node.name == name:
            return node
        elif name < node.name:
            return node_search(name, node.left)
        elif name > node.name:
            return node_search(name, node.right)

def node_validation(node: TreeNode) -> None:
    """
    Valida node e levanta um `IndexError` caso for None.
    """
    if not node:
            raise IndexError('Name not found')