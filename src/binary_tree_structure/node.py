class TreeNode:
    """
    Representa um nó em uma árvore binária de busca.

    Cada nó contém:
    - Um nome do contato (name).
    - Um número de telefone associado ao contato (number).
    - Referências para o filho à esquerda (left) e o filho à direita (right),
    que também são nós da árvore.

    Args:
        name (str): O nome do contato.
        number (int): O número de telefone do contato.
    
    Attributes:
        name (str): O nome do contato.
        number (int): O número de telefone do contato.
        left (TreeNode | None): Referência para o nó filho à esquerda.
        right (TreeNode | None): Referência para o nó filho à direita.
    """
    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number
        self.left = None
        self.right = None

    def __str__(self):
        return f'Name: {self.name} Number: {self.number}'
