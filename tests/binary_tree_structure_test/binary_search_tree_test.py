import pytest
from src.binary_tree_structure.binary_search_tree import BinarySearchTree


def test_insert_and_ascending_order_traversal(capsys):
    name = 'Rafael'
    number = 34992068746

    name2 = 'Pedro'
    number2 = 11991574638
    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(name, number)
    binary_search_tree.insert(name2, number2)

    binary_search_tree.ascending_order()

    captured = capsys.readouterr()

    expected = 'Name: Pedro Number: 11991574638\nName: Rafael Number: 34992068746\n'

    assert captured.out == expected

def test_descending_order_traversal(capsys):
    name = 'Rafael'
    number = 34992068746

    name2 = 'Pedro'
    number2 = 11991574638
    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(name, number)
    binary_search_tree.insert(name2, number2)

    binary_search_tree.descending_order()

    captured = capsys.readouterr()

    expected = 'Name: Rafael Number: 34992068746\nName: Pedro Number: 11991574638\n'

    assert captured.out == expected
