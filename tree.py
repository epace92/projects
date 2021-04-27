# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 12:22:41 2018

@author: sylviegibet
"""
#!/usr/bin/env python
# encoding: utf-8

# from pile_list import Pile_List
#%% Exercice 1                  # La chaîne de caractères #%% permet de sélectionner des parties de code

class Node:
    def __init__(self, v):
        self.value = v

    def get_value(self):
        return self.value
    
class Tree:
    
    def __init__(self, root, left, right):
        """ Creates an instance of class Tree
        input   -- self : instance of class Tree
                -- root : instance of class Node, the root of self
                -- right : instance of class Tree, the right of self
                -- left : instance of class Tree, the left of self
        """
        # attributs prives
        self.__root = root   #  racine de l'arbre
        self.__left = left
        self.__right = right
    
    def get_root(self):
        """ Returns the root of the Tree self
        input   -- self : instance of class Tree
        output  -- int, the height of the Tree self
        """
        return self.__root

    
    def root_value(self):
        """ Returns the value of the root of the Tree self
        input   -- self : instance of class Tree
        output  -- int, the height of the Tree self
        """
        return self.__root.get_value()

    def get_left(self):
        """ Returns the left subtree of the Tree self
        input   -- self : instance of class Tree
        output  -- int, the height of the Tree self
        """
        return self.__left
    
    def get_right(self):
        """ Returns the right subtree root of the Tree self
        input   -- self : instance of class Tree
        output  -- instance of class Tree
        """
        return self.__right

    def is_empty(self):
        """ Checks if self is an empty tree or not
        input   -- self : instance of class Tree
        output  -- bool, True if self is empty tree, False otherwise
        """
        return self.__root == None 
    
    def is_leaf(self):
        """ Checks if self is a leaf or not.
        input   -- self : instance of class Tree
        output  -- bool, True if self is a leaf, false otherwise
        """
        return self.__left == None and self.__right==None
    
    def has_left(self):
        """ Checks if self has a left subtree.
        input   -- self : instance of class Tree
        output  -- bool, True if self has a right Tree, false otherwise
        """
        return self.__left != None
 
    def has_right(self):
        """ Checks if self has a right subtree. 
        input   -- self : instance of class Tree
        output  -- bool, True if self has a right Tree, false otherwise
        """
        return self.__right != None
    
    def height(self):
        """ Returns the height of the Tree self
        input   -- self : instance of class Tree
        output  -- int, the height of the Tree self
        """
        if self.is_empty():
            return 0
        elif self.is_leaf():
            return 0
        else:
            if self.has_left():
                if self.has_right():
                    return 1+max(self.get_left().height(), self.get_right().height())
                else:
                    return 1+self.get_left().height()
            else:
                return 1+self.get_right().height()

    def height1(self):
        """ Returns the height of the Tree self
        input   -- self : instance of class Tree
        output  -- int, the height of the Tree self
        """
        if self.is_empty():
            return 0
        elif self.is_leaf():
            return 1
        else:
            if self.get_left():
                if self.get_right():
                    return 1 + max(self.get_left().height1(), self.get_right().height())
                else:
                    return 1 + self.get_left().heigh1()
            else:
                return 1 + self.get_right().height1()

    def count_nodes(self):
        """
        Returns the amount of nodes in the Tree self
        input   -- self : instance of class Tree
        output  -- int, the amount of nodes in the Tree self
        """
        if self.is_empty():
            return 0
        elif self.is_leaf():
            return 1
        else:
            if self.get_left():
                if self.get_right():
                    return 1 + self.get_left().count_nodes() + self.get_right().count_nodes()
                else:
                    return 1 + self.get_left().count_nodes()
            else:
                return 1 + self.get_right().count_nodes()

    def count_leaf(self):
        """Returns the number of leaf in the tree self
        input   --self: an instance of class Tree
        output  --int, amount of leaf in the tree self"""
        if self.is_empty():
            return 0
        elif self.is_leaf():
            return 1
        else:
            if self.get_left():
                if self.get_right():
                    return 0 + self.get_left().count_leaf() + self.get_right().count_leaf()
                else:
                    return 0 + self.get_left().count_leaf()
            else:
                return 0 + self.get_right().count_leaf()

    def sum(self):
        """
        :return: the sum of the nodes' values in the Tree self
        input   -- self : instance of class Tree
        output  -- int, the sum of the nodes' values
        """
        if self.is_empty():
            return 0
        elif self.is_leaf():
            return self.get_root().get_value()
        else:
            if self.get_left():
                if self.get_right():
                    return self.get_root().get_value() + self.get_left().sum() + self.get_right().sum()
                else:
                    return self.get_root().get_value() + self.get_left().sum()
            else:
                return self.get_root().get_value() + self.get_right().sum()

    def increment(self):
        """Increments every single value of the tree's nodes
        input   --self : instance of class Tree
        """
        if self.is_empty():
            return 0
        else:
            self.get_root().value += 1
            if self.get_left():
                self.get_left().increment()
            if self.get_right():
                self.get_right().increment()

    def apply(self, f):
        """ Apply a fucntion f to every values of the tree self
        input   --self: an instance of class Tree
                --f: the function to apply
        """
        if self.is_empty():
            return 0
        else:
            self.get_root().value = f(self.get_root().value)
            if self.get_left():
                self.get_left().apply(f)
            if self.get_right():
                self.get_right().apply(f)

            
    def print_prefix(self):
        """ Returns the prefix description of the Tree self. The value of root is 
        print first. Then the prefix description of the Tree left. And finally the 
        prefix description of the Tree right.
        input   -- self : instance of class Tree
        output  -- str, prefix description of the Tree self
        """
        if self.is_empty():
            return ""
        else:
            ch = str(self.root_value())
            if self.is_leaf():
                return ch
            else:
                if self.has_left():
                    if self.has_right():
                        return ch + " " + self.get_left().print_prefix() + " " + self.get_right().print_prefix()
                    else:
                        return ch + " " + self.get_left().print_prefix()
                else:
                       return ch + " " + self.get_right().print_prefix()

    def print_postfix(self):
        """ Returns the postfix description of the Tree self. The value of root is
        print last. Then the postfix description of the Tree left. And finally the
        postfix description of the Tree right.
        input   -- self : instance of class Tree
        output  -- str, postfix description of the Tree self
        """
        if self.is_empty():
            return ""
        else:
            ch = ""
            if self.is_leaf():
                return ch + str(self.root_value())
            else:
                if self.has_left():
                    if self.has_right():
                        ch = ch + " " + str(self.get_left().print_postfix()) + " " \
                             + str(self.get_right().print_postfix())
                        return ch + " " + str(self.root_value())
                    else:
                        ch = ch + " " + str(self.get_left().print_postfix())
                        return ch + " " + str(self.root_value)
                else:
                    ch = ch + " " + str(self.get_right().print_postfix()) + " " + str(self.root_value)
                    return ch + " " + str(self.root_value())

    def print_infix(self):
        """ Returns the infix description of the Tree self. The value of root is
        print second. First the infix description of the Tree left. And finally the
        infix description of the Tree right.
        input   -- self : instance of class Tree
        output  -- str, infix description of the Tree self
        """
        if self.is_empty():
            return ""
        else:
            if self.is_leaf():
                return str(self.root_value())
            else:
                if self.has_left():
                    if self.has_right():
                        return str(self.get_left().print_infix()) + " " + str(self.root_value()) + " " \
                               + str(self.get_right().print_infix())
                    else:
                        return str(self.get_left().print_infix()) + " " + str(self.root_value())
                else:
                    return str(self.root_value()) + " " + str(self.get_right().print_infix())
 
if __name__ == "__main__":     
    print("Hello Tree !!!")
    # execute only if run as a script
    
    ### 
    # Cette partie du programme joue le rôle de main : elle permet d'effectuer tous les  tests 
    # sur les méthodes de la classe Arbre
    # Lorque vous importez le fichier dans un autre programme, cette partie ne s'exécute pas.