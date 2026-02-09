class Queue:
    def __init__(self):
        self.queue_list = []

    
    def add(self, item):
        return self.queue_list.append(item)
    
    def next(self):
        return self.queue_list.pop(0)

    def is_empty(self):
        if len(self.queue_list) <= 0:
            return True
        else:
            return False
        



queue = Queue()

queue.add("Alice")
queue.add("Bob")
queue.add("Charlie")

queue.next()
queue.next()
queue.next()

print(queue)