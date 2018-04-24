from Queue import Queue

queue = Queue()

for i in range(20):
    queue.enqueue(i)

queue.printlist()