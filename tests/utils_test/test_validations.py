import pytest
from src.binary_tree_structure.binary_search_tree import BinarySearchTree
from src.utils.validations import name_verification, root_validation, name_and_number_validation, node_validation
from src.utils.helpers import node_search

def test_name_verification():
    with pytest.raises(Exception):
        binary_search_tree = BinarySearchTree()

        name = 'Fabio'
        number = 119969868746
        binary_search_tree.insert(name, number)

        name_verification('Fabio', binary_search_tree.root)

def test_root_validation():
    with pytest.raises(IndexError):
        binary_search_tree = BinarySearchTree()
        
        root_validation(binary_search_tree.root)
        
def test_invalid_type_name():
    with pytest.raises(TypeError):
        name_and_number_validation(5654, 34992068746)

def test_invalid_type_number():
    with pytest.raises(TypeError):
        name_and_number_validation('Douglas', '34992068746')

def test_node_verifiction():
    with pytest.raises(IndexError):
        binary_search_tree = BinarySearchTree()
        node = node_search('Matheus', binary_search_tree.root)
        node_validation(node)
