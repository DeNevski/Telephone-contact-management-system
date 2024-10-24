from src.binary_tree_structure.binary_search_tree import BinarySearchTree

if __name__ == '__main__':

    test = BinarySearchTree()
    test.insert('Cafael', 34992068746)
    test.insert('Bedro', 658464968440)
    test.insert('Dico', 1006844566359)
    test.insert('Aino', 336982598548)
    test.insert('Eica', 643960496445)

    test.update('Cafael', 11991574638)
    test.update('Eica', 20986515650)

    test.remove('Cafael')

    test.ascending_order()
    #test.descending_order()
    #print(test.search('Dico'))
