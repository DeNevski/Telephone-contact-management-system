import pytest
from src.binary_tree_structure.binary_search_tree import BinarySearchTree

def test_insert_and_ascending_order_traversal(capsys):
    name_1 = 'Rafael'
    number_1 = 34992068746

    name_2 = 'Pedro'
    number_2 = 11991574638
    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(name_1, number_1)
    binary_search_tree.insert(name_2, number_2)

    binary_search_tree.ascending_order()

    captured = capsys.readouterr()

    expected = 'Name: Pedro Number: 11991574638\nName: Rafael Number: 34992068746\n'

    assert captured.out == expected

def test_descending_order_traversal(capsys):
    name_1 = 'Pedro'
    number_1 = 11991574638

    name_2 = 'Rafael'
    number_2 = 34992068746

    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(name_1, number_1)
    binary_search_tree.insert(name_2, number_2)

    binary_search_tree.descending_order()

    captured = capsys.readouterr()

    expected = 'Name: Rafael Number: 34992068746\nName: Pedro Number: 11991574638\n'

    assert captured.out == expected

def test_search():
    name_1 = 'Rafael'
    number_1 = 34992068746

    name_2 = 'Pedro'
    number_2 = 11991574638

    name_3 = 'Fabio'
    number_3 = 75991658743

    name_4 = 'Marcos'
    number_4 = 10992658743

    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(name_1, number_1)
    binary_search_tree.insert(name_2, number_2)
    binary_search_tree.insert(name_3, number_3)
    binary_search_tree.insert(name_4, number_4)

    result = binary_search_tree.search('Fabio')
    expected = 'Name: Fabio Number: 75991658743'

    assert str(result) == expected

def test_update():
    name_1 = 'Fabio'
    number_1 = 75991658743

    name_2 = 'Marcos'
    number_2 = 10992658743

    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(name_1, number_1)
    binary_search_tree.insert(name_2, number_2)

    binary_search_tree.update('Marcos', 22988654973)

    result = binary_search_tree.search('Marcos') 
    expected = 'Name: Marcos Number: 22988654973'

    assert str(result) == expected

def test_remove_root(capsys):
    name_1 = 'Rafael'
    number_1 = 34992068746

    name_2 = 'Pedro'
    number_2 = 11991574638

    name_3 = 'Fabio'
    number_3 = 75991658743

    name_4 = 'Marcos'
    number_4 = 10992658743

    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(name_1, number_1)
    binary_search_tree.insert(name_2, number_2)
    binary_search_tree.insert(name_3, number_3)
    binary_search_tree.insert(name_4, number_4)

    binary_search_tree.remove(name_1)

    binary_search_tree.ascending_order()

    captured = capsys.readouterr()
    expected = 'Name: Fabio Number: 75991658743\nName: Marcos Number: 10992658743\nName: Pedro Number: 11991574638\n'

    assert captured.out == expected

def test_remove_parent(capsys):
    name_1 = 'Rafael'
    number_1 = 34992068746

    name_2 = 'Pedro'
    number_2 = 11991574638

    name_3 = 'Fabio'
    number_3 = 75991658743

    name_4 = 'Marcos'
    number_4 = 10992658743

    name_5 = 'Rodolfo'
    number_5 = 23958748743

    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(name_1, number_1)
    binary_search_tree.insert(name_2, number_2)
    binary_search_tree.insert(name_3, number_3)
    binary_search_tree.insert(name_4, number_4)
    binary_search_tree.insert(name_5, number_5)

    binary_search_tree.remove(name_2)

    binary_search_tree.ascending_order()

    captured = capsys.readouterr()
    expected = 'Name: Fabio Number: 75991658743\nName: Marcos Number: 10992658743\nName: Rafael Number: 34992068746\nName: Rodolfo Number: 23958748743\n'

    assert captured.out == expected

def test_remove_child(capsys):
    name_1 = 'Rafael'
    number_1 = 34992068746

    name_2 = 'Pedro'
    number_2 = 11991574638

    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(name_1, number_1)
    binary_search_tree.insert(name_2, number_2)

    binary_search_tree.remove(name_2)

    binary_search_tree.ascending_order()

    captured = capsys.readouterr()
    expected = 'Name: Rafael Number: 34992068746\n'

    assert captured.out == expected
