import sys

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def count(self):
        return len(self.queue)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        return (i - 1) // 2

    def up_heap(self, i):
        while i > 0:
            p = self.parent(i)
            if self.queue[p] <= self.queue[i]:
                break
            self.queue[i], self.queue[p] = self.queue[p], self.queue[i]
            i = p

    def insert(self, x):
        self.queue.append(x)
        self.up_heap(len(self.queue) - 1)

    def down_heap(self, i):
        while self.left(i) < len(self.queue):
            if self.right(i) < len(self.queue):
                if self.queue[i] < self.queue[self.left(i)] and self.queue[i] < self.queue[self.right(i)]:
                    break
                if self.queue[self.left(i)] <= self.queue[self.right(i)]:
                    self.queue[i], self.queue[self.left(i)] = self.queue[self.left(i)], self.queue[i]
                    i = self.left(i)
                else:
                    self.queue[i], self.queue[self.right(i)] = self.queue[self.right(i)], self.queue[i]
                    i = self.right(i)
            else:
                if self.queue[i] < self.queue[self.left(i)]:
                    break
                else:
                    self.queue[i], self.queue[self.left(i)] = self.queue[self.left(i)], self.queue[i]
                    i = self.left(i)


    def remove_smallest(self):
        x = self.queue[0]
        if self.count() > 1:
            self.queue[0] = self.queue.pop()
            self.down_heap(0)
        else:
            self.queue.pop()
        return x



pq = PriorityQueue()

dic = {}
count = 0
capacity = int(input())

for line in sys.stdin:
    name, rank = line.strip().split()
    dic[float(rank)] = name
    pq.insert(float(rank))
    count += 1
    if count == capacity:
        leaves = pq.remove_smallest()
        print(dic[leaves], leaves)
        count -= 1

final_keys = []
for rank in pq.queue:
    final_keys.append(rank)

sorted_keys = sorted(final_keys)

for key in sorted_keys:
    print(dic[key], key)










