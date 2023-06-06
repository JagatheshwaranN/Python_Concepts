class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        Returns the number of nodes in the list takes O(n) time
        """
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a new node containing data at the head of the list takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node  or 'None' if not found
        Takes O(n) time
        """
        current = self.head
        while current is not None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self):
        nodes = []
        current = self.head
        while current is not None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return ' -> '.join(nodes)


n1 = Node(10)
print(n1)
n2 = Node(20)
n1.next_node = n2
print(n1.next_node)
print("=====================================")
lst = LinkedList()
n1 = Node(10)
lst.head = n1
print(lst.size())
print("=====================================")
lst1 = LinkedList()
lst1.add(10)
lst1.add(20)
lst1.add(30)
print(lst1.size())
print(lst1)
ele = lst1.search(20)
print(ele)
