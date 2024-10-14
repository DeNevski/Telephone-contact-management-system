class TreeNode:

    def __init__(self, name: str, number: int) -> None:
        self.name = name
        self.number = number
        self.left = None
        self.right = None

    def __str__(self):
        return f'Name: {self.name} Number: {self.number}'
