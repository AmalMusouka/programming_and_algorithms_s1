# Write a class LinkedList that holds a linked list of values.
#
# Your class should be in a source file named linked_list.py, and should support the following operations:
#
# LinkedList(list) - create a LinkedList that initially holds the values in the given Python list
#
# l.to_list() - return a Python list containing the values in this LinkedList
#
# l.len() - return the number of nodes in a LinkedList
#
# l.get(n) - return the value in the nth node, where nodes are numbered from 0. You may assume that 0 <= n < l.len().
#
# l.has(x) - true if the list includes the value x
#
# l.delete(x) - delete the first occurrence (if any) of the value x
#
# l.rotate() - move the last node in the list to the head of the list; does nothing if the list is empty
#
# l.starts_with(m) - true if the elements of the LinkedList m appear at the beginning of l
#
# l.contains(m) - true if the elements of the LinkedList m appear in succession anywhere in l
#
# l.ends_with(m) - true if the elements of the LinkedList m appear in succession at the end of l
#
# Important: You may not use Python lists anywhere, except in the initializer and the to_list() method.
#
# Your LinkedList class may not store a Python list in any attribute. Also, generators (which we will study later in Programming 1) are not allowed in this assignment.
#
# You do not need to read any input or write any output; simply submit a file linked_list.py containing the class described above.



class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    # def __repr__(self):
    #     return "Node value: " + str(self.value)


class LinkedList:
    def __init__(self, list):
        node_list = [Node(value) for value in list]
        if list == []:
            self.head = None
        else:
            for node_index in range(len(node_list) - 1):
                node = node_list[node_index]
                node.next = node_list[node_index + 1]
            self.head = node_list[0]

    def to_list(self):
        node = self.head
        result = []
        while node is not None:
            result.append(node.value)
            node = node.next

        return result

    def len(self):
        return len(self.to_list())

    def get(self, n):
        node = self.head
        i = 0
        while i != n:
            node = node.next
            i += 1
        return node.value

    def has(self, x):
        node = self.head
        has = False
        while node is not None:
            if node.value == x:
                has = True
                break
            elif node is None:
                has = False
                break
            else:
                node = node.next

        return has


    def delete(self, x):
        node = self.head
        if node is None:
            return
        if x == node.value:
            self.head = node.next
        while node.next is not None:
            if node.next.value == x:
                node.next = node.next.next
                break
            else:
                node = node.next

    def rotate(self):
        node = self.head
        if node is None or node.next is None:
            self.head = node
        else:
            while node is not None:
                if node.next.next is None:
                    node.next.next = self.head
                    self.head = node.next
                    node.next = None
                    break

                else:
                    node = node.next

    # def printer(self, m):
    #     return print(m)

    def starts_with(self, m):
        node = self.head
        node2 = m.head

        while node is not None:
            if node2 is None:
                return True

            if node2.value == node.value:
                node2 = node2.next
                node = node.next
            else:
                return False
        return False



    def contains(self, m):
        node = self.head
        node2 = m.head

        while node2 is not None:
            if node is None:
                return False
            if node.next is None and node2.next is not None:
                return False
            if node.value == node2.value:
                node2 = node2.next
                node = node.next
            else:
                node = node.next

        return True



    def ends_with(self, m):
        node = self.head
        node2 = m.head

        while node is not None:
            if node2 is None:
                return False
            if node.next is None and node2.next is None:
                return True
            if node.value == node2.value:
                node2 = node2.next
                node = node.next
            else:
                node = node.next
        return False

