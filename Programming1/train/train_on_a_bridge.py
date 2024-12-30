import sys
class Bogey:
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight

class Queue:
    def __init__(self, size, capacity, isFull=False):
        self.queue = []
        self.size = size
        self.capacity = capacity
        self.isFull = isFull

    def isFull(self):
        if self.isFull:
            self.remove()
            isFull = False

    def enqueue(self, item, capacity=None):
        self.queue.append(Bogey(item, capacity))
        self.capacity += capacity
        self.size += 1
        if self.size == self.capacity:

    #remove the new bogeys capacity from the leading one
    def remove(self):
        self.queue[0].length = self.queue[0].length - self.queue[self.size - 1].length
        if self.queue[0].length <= 0:
            self.queue.pop(0)
            self.capacity -= self.queue[0].weight
            self.size -= 1


length = 10
cap = 100

list_inp = [(10, 90), (10, 10), (9, 80), (1,10)]

trains = Queue(length, cap)


def add_bogey(x):
    if trains.isFull:
        trains.dequeue()

