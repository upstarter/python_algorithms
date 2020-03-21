# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return " ".join([str(i) for i in self.queue])

    # check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == []

    # insert an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # pop an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()


if __name__ == "__main__":
    myQueue = PriorityQueue()
    myQueue.insert(1)
    myQueue.insert(199)
    myQueue.insert(8)
    myQueue.insert(27)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())
