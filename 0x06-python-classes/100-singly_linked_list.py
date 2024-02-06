#!/usr/bin/python3
"""
A class Node that defines a node of a singly linked list.
"""


class Node:
    """
    Defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        instantiation of the node with data and next_node
        data: the data member of the node.
        next_node: the pointer member of the node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data private instnce attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets data private instance attribute to what value is.
        """
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next_node private instance attribute.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets next_node private instance attribute to what value is.
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


"""
A class SinglyLinkedList that defines a singly linked list.
"""


class SinglyLinkedList:
    """
    This class defines a singly linked list.
    """
    def __init__(self):
        """
        Instantiatoin of the singly linked list
        head: a private instance attribute with no getter or setter.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        This public method inserts a new Node into the correct sorted
        position in the list(increasing order)
        """
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if new_node.data < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        prev = None

        while current and current.data < value:
            prev = current
            current = current.next_node

        prev.next_node = new_node
        new_node.next_node = current

    def __str__(self):
        """
        Returns a human-readable string.
        """
        string = ""
        current = self.__head
        while current is not None:
            string += str(current.data)
            if current.next_node is not None:
                string += '\n'
            current = current.next_node

        return string
