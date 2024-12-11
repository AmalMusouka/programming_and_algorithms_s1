#In this exercise you will implement a hash table, and use it to answer queries about word frequencies in the input text.
#
# Write a class HashMap that implements a map (i.e. dictionary) using a hash table. Your class should provide the following methods:
#
# m.set(key, value) - add the mapping (key -> value) to a hash table, replacing any previous value for the given key
#
# m.get(key) - look up a key and returns its value, or None if it is not present
#
# m.remove(key) - remove a key from the hash table if present
import sys


# Hash a string to an unsigned 32-bit integer.



class Node:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

 # def __repr__(self):
    #     return "Node value: " + str(self.value)

class HashMap:
    def __init__(self, buckets=5, size=0):
        self.buckets = buckets
        self.table = [None] * buckets
        self.size = size

    def my_hash(self, s):
        h = 0
        for c in s:
            h = (h * 1_000_003 + ord(c)) % self.buckets
        return h

    def load_index(self):
        return self.size/self.buckets

    def resize(self):
        new_table = [None] * self.buckets
        old_table = self.table
        self.table = new_table
        self.rehash(old_table)
        print(f"resizing to {self.buckets} buckets")


    def rehash(self, old_table):
        self.size = 0
        for i in range(len(old_table)):
            if old_table[i] is not None:
                current_node = old_table[i]
                self.set(current_node.key, current_node.value)
                while current_node.next is not None:
                    current_node = current_node.next
                    self.set(current_node.key, current_node.value)
            else:
                continue

    def set(self, key, value=1):
        index = self.my_hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value, None)
            self.size += 1
        else:
            current_node = self.table[index]
            prev_node = None

            while current_node is not None and current_node.key != key:
                prev_node = current_node
                current_node = current_node.next

            if current_node is not None:
                current_node.value += value
            else:
                current_node = Node(key, value, None)
                prev_node.next = current_node
                self.size += 1


        if self.load_index() > 4:
            self.buckets *= 2
            self.resize()


    def get(self, key):
        index = self.my_hash(key)
        current_node = self.table[index]

        if current_node is None:
            return None

        while current_node.key != key:
            if current_node.next is not None:
                current_node = current_node.next
            else:
                return None

        first_value = current_node.value
        current_node.value = None

        return first_value

    def remove(self, key):
        index = self.my_hash(key)
        current_node = self.table[index]
        prev_node = None

        if current_node is None:
            return None

        while current_node.key != key:
            prev_node = current_node
            current_node = current_node.next

        if prev_node is not None:
            prev_node.next = current_node.next
        else:
            self.table[index] = current_node.next

        self.size -= 1

def words_from_string(string):
    words = []

    word = ''
    for letter in string:

        if ord(letter) > ord("z") or ord(letter) < ord("a"):
            if word != '':
                words.append(word)
                word = ''
                continue
        else:
            word += letter

    return words


hash_table = HashMap()

input_string = ""

while True:
    line = input()
    if line == "== END ==":
        break
    input_string += line + " "

word_occ = []
for line in sys.stdin.readlines():
    word_occ.append(line.lower().strip())

for word in words_from_string(input_string.lower()):
    hash_table.set(word)

print(f"unique words = {hash_table.size}")

for word in word_occ:
    print(word, hash_table.get(word))

