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

class Node:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

    # def __repr__(self):
    #     return "Node value: " + str(self.key)

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
        old_table = self.table
        self.table = [None] * self.buckets
        self.rehash(old_table)
        print(f"resizing to {self.buckets} buckets")

    def rehash(self, old_table):
        old_table_size = self.size
        self.size = 0
        count = 0
        if count < old_table_size:
            for i in range(len(old_table)) :
                if old_table[i] is not None:
                    current_node = old_table[i]
                    self.set(current_node.key, current_node.value, True)
                    count += 1
                    while current_node.next is not None:
                        current_node = current_node.next
                        self.set(current_node.key, current_node.value, True)
                        count += 1

    def set(self, key, value=1, rehash=False):
        index = self.my_hash(key)

        if self.table[index] is None:
            self.table[index] = Node(key, value, None)
            self.size += 1
        else:
            current_node = self.table[index]
            prev_node = None

            if not rehash:
                while current_node is not None and current_node.key != key:
                    prev_node = current_node
                    current_node = current_node.next

                if current_node is not None:
                    current_node.value = value
                else:
                    current_node = Node(key, value, None)
                    prev_node.next = current_node
                    self.size += 1

                if self.load_index() > 4:
                    self.buckets *= 2
                    self.resize()
            else:
                new_node = Node(key, value, None)
                new_node.next = current_node
                self.table[index] = new_node
                self.size += 1


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

        return current_node.value

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
    if word != '':
        words.append(word)
    return words


hash_table = HashMap()
input_string = ""
word_occ = []
text_ended = False

for line in sys.stdin:
    if line.strip() == '== END ==':
        text_ended = True
        continue
    if text_ended:
        word_occ.append(line.strip().lower())
    else:
        words = words_from_string(line.strip().lower())
        for word in words:
            if hash_table.get(word) is not None:
                value = hash_table.get(word)
                hash_table.set(word, value + 1)
            else:
                hash_table.set(word)

print(f"unique words = {hash_table.size}")

for word in word_occ:
    print(word, hash_table.get(word))
    if hash_table.get(word) is not None:
        hash_table.remove(word)

