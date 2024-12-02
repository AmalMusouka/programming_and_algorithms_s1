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
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def _repr_(self):
        return str(self.value)

    # gets the leaf name
    def leaf_name_of_value(self, value):
        return 'left' if self.value > value else 'right'

    # gets the leaf name
    def leaf_name_of_node(self, node):
        return self.leaf_name_of_value(node.value)

    def get_leaf_node_for_leaf(self, leaf):
        return getattr(self, leaf)

    def get_leaf_node_for_node(self, node):
        leaf = self.leaf_name_of_node(node)
        return self.get_leaf_node_for_leaf(leaf)

    def add_leaf(self, node):
        leaf = self.leaf_name_of_node(node)
        setattr(self, leaf, node)
        return node


class TreeSet:
    def __init__(self):
        self.root = None
        self.num_of_val = 0

    def increment_size(self):
        self.num_of_val += 1

    def decrement_size(self):
        self.num_of_val -= 1

    def get_parent(self, value):
        parent = None
        current_node = self.root

        while current_node and current_node.value != value:
            next_leaf = current_node.leaf_name_of_value(value)
            parent = current_node
            current_node = current_node.get_leaf_node_for_leaf(next_leaf)

        return parent

    def get_node(self, value):
        parent = self.get_parent(value)

        if not parent and self.root.value == value:
            return self.root

        if not parent:
            return None

        node_leaf = parent.leaf_name_of_value(value)
        return parent.get_leaf_node_for_leaf(node_leaf)

    # recursive get noe
    def get_node_r(self, value, parent):
        if not parent:
            return None

        if parent.value == value:
            return parent

        leaf = parent.leaf_name_of_value(value)
        leaf_node = parent.get_leaf_node_for_leaf(leaf)

        if not leaf_node:
            return None

        if leaf_node.value == value:
            return leaf_node

        return self.get_node_r(value, leaf_node)

    def get_node_from_root(self, value):
        return self.get_node_r(value, self.root)

    def add(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            self.increment_size()
            return True

        parent = self.root

        while parent:
            if parent.value == node.value:
                return False

            parent_leaf = parent.get_leaf_node_for_node(node)

            if parent_leaf:
                parent = parent_leaf
                continue

            parent.add_leaf(node)
            self.increment_size()

        return True


    def min(self):
        smallest = self.root
        if smallest is None:
            return None

        while smallest.left is not None:
                smallest = smallest.left
        return smallest.value

    def max(self):
        largest = self.root
        if largest is None:
            return None

        while largest.right is not None:
            largest = largest.right
        return largest.value

    def contains(self, x):
        n = self.root
        while n is not None:
            if x == n.value:
                return True
            if x < n.value:
                n = n.left
            else:
                n = n.right
        return False

    # smallest node including node and subtree
    def smallest_node(self, node):
        if node.left:
            return self.smallest_node(node.left)
        return node


    def remove(self, value):
        parent = self.get_parent(value)
        node = self.get_node_from_root(value)

        if not node:
            return False

        # handle 2 leafs
        if node.left and node.right:
            smallest_node = self.smallest_node(node.right)
            self.remove(smallest_node.value)

            if parent is None:
                prev_root = self.root
                self.root = smallest_node
                smallest_node.left = prev_root.left
                smallest_node.right = prev_root.right
                return

            parent_leaf = parent.leaf_name_of_node(node)
            setattr(parent, parent_leaf, smallest_node)

            if node.right:
                smallest_node.right = node.right

            if node.left:
                smallest_node.left = node.left

            return

        # handle 1 leaf
        if node.left or node.right:
            node_only_leaf = 'left' if node.left else 'right'

            if node is self.root:
                self.root = getattr(node, node_only_leaf)
                self.decrement_size()
                return node

            parent_leaf = parent.leaf_name_of_node(node)
            setattr(parent, parent_leaf, getattr(node, node_only_leaf))
            self.decrement_size()
            return node

        # handle no leafs
        if node is self.root:
            # root node
            self.root = None
            self.decrement_size()
            return None

        parent_leaf = parent.leaf_name_of_node(node)
        setattr(parent, parent_leaf, None)

        self.decrement_size()

        return node

    def print(self, node, level=0):
        if node is not None:
            self.print(node.right, level + 1)
            print('   ' * 4 * level + '-> ' + str(node.value))
            self.print(node.left, level + 1)

    def print_tree(self):
        self.print(self.root)
        print('\n\n')

    def size(self):
        return self.num_of_val

    def count_helper(self, node, lo, hi):
        count = 0

        if node is None:
            return 0

        if lo <= node.value <= hi:
            count += 1

        if node.left and node.value >= lo:
            count += self.count_helper(node.left, lo, hi)

        if node.right and node.value <= hi:
            count += self.count_helper(node.right, lo, hi)

        return count


    def count(self, lo, hi):
        node = self.root

        if hi < lo:
            return 0

        if node is None:
            return 0

        return self.count_helper(node, lo, hi)


#
# def sample1():
#     t = TreeSet()
#     for x in [10, 30, 25, 40, 28]:
#         t.add(x)
#     print(t.count(0, 30))
#
# sample1()
