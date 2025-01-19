# class Node:
#     def __init__(self, v, l=None, r=None):
#         self.value = v
#         self.left = l
#         self.right = r
#
#
# def longest_path(tree: Node) -> list[int]:
#     output = [tree.value]
#
#     if tree.right is None and tree.left is None:
#         return output
#
#     if tree.right is None:
#         return output + longest_path(tree.left)
#     elif tree.left is None:
#         return output + longest_path(tree.right)
#
#     return output + max(longest_path(tree.left),
#                         longest_path(tree.right), key=len)
#
#
#
# t = Node(1, l=Node(2, r=Node(3)), r=Node(4))
# print(longest_path(t))
# # output [1,2,3]

#
# from math import floor
#
#
# def has_two_cube_sums(n):
#     limit = floor((n ** (1.0 / 3.0)))
#     count = 0
#
#     for i in range(limit):
#         for j in range(limit, 1, -1):
#             if i ** 3 + j ** 3 == n:
#                 count += 1
#             if count == 2:
#                 return True
#
#     return False
#
# print(has_two_cube_sums())


