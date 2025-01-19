#Write a class CircularQueue that implements a queue of numbers using an array.
#
# Your class should support the following operations:
#
# CircularQueue(size) - create an empty CircularQueue that initially has room for 'size' elements
# q.enqueue(n) - add a number at the tail of the queue
# q.dequeue() - remove a number from the head of the queue, and return it
# q.count() - return the number of values in the queue
# q.avg() - return the average of all values in the queue
# You may assume that q.dequeue() and q.avg() will never be called when the queue is empty.
#
# The enqueue() method should run in O(1) on average. All other methods should always run in O(1).
#
# The array holding the queue elements should always have at least one free slot.
#
# If an enqueue() operation would fill the last slot, then it should expand the structure to make more room.
#
# To do this, replace the array with a newly allocated array that is twice as big, and print a message such as
#
# Resized to 200 elements



class CircularQueue:
    def __init__(self, x):
        self.queue = [None] * x
        self.head = len(self.queue)
        self.tail = len(self.queue) - 1
        self.size = 0
        self.sum = 0

    def __repr__(self):
        return str(self.queue)
    #
    # def head(self):
    #     return self.head
    #
    # def tail(self):
    #     return self.tail

    # checking if the queue is full
    def is_full(self):
        if self.size == len(self.queue):
            self.new_queue()
            return True

        return False

    # to create a new circular queue of twice the size as the original
    def new_queue(self):
        new_queue = [None] * 2 * len(self.queue)
        for i in range(len(self.queue)):
            new_queue[i] = self.queue[(self.head + i) % len(self.queue)]

        self.head = 0
        self.tail = len(self.queue) - 1

        self.queue = new_queue
        return self.queue

    def is_empty(self):
        for i in range(len(self.queue)):
            if self.queue[i] is not None:
                return False

        return True

    def enqueue(self, x):
        if self.is_empty():
            self.head = self.tail = 0
            self.queue[0] = x
            self.size += 1
            self.sum += x
            if self.is_full():
                print(f"Resized to {self.size * 2} elements")
            return

        if self.queue[(self.tail + 1) % len(self.queue)] is None:
            self.tail = (self.tail + 1) % len(self.queue)
            self.queue[self.tail] = x
            self.size += 1
            self.sum += x

        if self.is_full():
            print(f"Resized to {self.size * 2} elements")

        if self.tail == self.head - 1:
            self.tail = self.size - 1


    def dequeue(self):

        value = self.queue[self.head]
        self.sum -= self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % len(self.queue)
        self.size -= 1

        return value

    def count(self):
        return self.size

    def avg(self):
        return self.sum / self.size


# def sample2():
#     q = CircularQueue(1)
#     for x in range(5):
#         q.enqueue(x)
#         q.enqueue(2 * x)
#         q.dequeue()
#     print('count is', q.count())
#     print('avg is', q.avg())
#
#
# sample2()
#
