# Write a Python class TreeSet that stores a set of values in a binary search tree.
#
# Your class should support the following operations:
#
# TreeSet() - create a TreeSet
# ts.contains(x) - True if x is in the set
# ts.add(x) - add x to the set if not already present
# ts.remove(x) - remove x from the set if present
# ts.min() - return the smallest value in the set, or None if the set is empty
# ts.max() - return the largest value in the set, or None if the set if empty
# ts.size() - return the total number of values in the set
# ts.count(lo, hi) - return the number of values x in the set such that lo <= x <= hi
# count() should only explore parts of the tree that might contain values between lo and hi. If it always explores the entire tree (i.e. always takes O(N)), it will be not be efficient enough to pass the tests.
#
# size() should run in O(1). All other operations should run in O(h), where h is the height of the binary tree.
#
# If a node has two children, remove() should replace its value with the smallest value in the node's right subtree.

class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class TreeSet:
    def __init__(self):
        self.root = None
        self.num_of_val = 0

    def contains(self, x):
        n = self.root
        while n is not None:
            if x == n.val:
                return True
            if x < n.val:
                n = n.left
            else:
                n = n.right
        return False

    # add a value, or do nothing if already present
    def add(self, x):
        n = Node(x, None, None)  # new node to add
        p = self.root
        if p is None:
            self.root = n
            self.num_of_val = 1
            return

        while True:
            if x == p.val:
                return  # already present
            elif x < p.val:
                if p.left is None:
                    p.left = n
                    self.num_of_val += 1
                    return
                else:
                    p = p.left
            else:  # x > p.val
                if p.right is None:
                    p.right = n
                    self.num_of_val += 1
                    return
                else:
                    p = p.right




    def min(self):
        smallest = self.root
        if smallest is None:
            return None

        while smallest.left is not None:
                smallest = smallest.left
        return smallest.val

    def max(self):
        largest = self.root
        if largest is None:
            return None

        while largest.right is not None:
            largest = largest.right
        return largest.val

    def size(self):
        return self.num_of_val


    def find_next_smallest(self, x):
        if x.right is None and x.left is None:
            return None
        elif x.left is None:
            return x.right
        else:
            return self.find_next_smallest(x.left)


    def remove(self, x):
        n = self.root
        if n is None:
            return

        while n is not None:
            if self.count == 1 and x == n.val:
                self.root = None
                self.count -= 1
            if x == n.right.val:
                new_curr = self.find_next_smallest(n.right)
                n.right = new_curr
                self.num_of_val -= 1
                return
            elif x == n.left.val:
                new_curr = self.find_next_smallest(n.left)
                n.left = new_curr
                self.num_of_val -= 1
                return
            elif x < n.val:
                n = n.left
            else:
                n = n.right


    def count(self, lo, hi):
        p = self.root
        num_of_x = 0

        if p is None:
            return 0

        while p is not None:
            if lo <= p.val <= hi:
                num_of_x += 1
            if p.right is not None:
                if lo <= p.right.val <= hi:
                    p = p.right
                else:
                    p = p.left
            elif p.left is not None:
                if lo <= p.left.val <= hi:
                    p = p.left
            else:
                return num_of_x

        return num_of_x











#
# def sample1():
#     t = TreeSet()
#     print(t.min())
#     print(t.max())
#     for x in [4, 2, 8, 6, 10]:
#         t.add(x)
#     t.add(4)
#     print('size =', t.size())
#     print('min =', t.min())
#     print('max =', t.max())
#     print('t.contains(8) =', t.contains(8))
#
#     t.remove(8)
#     print('t.contains(8) =', t.contains(8))
#     print('size =', t.size())
#     print('t.count(3, 7) =', t.count(3, 7))
#
# sample1()