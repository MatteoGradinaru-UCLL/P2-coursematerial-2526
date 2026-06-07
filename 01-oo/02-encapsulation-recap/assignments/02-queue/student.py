# class Queue:
#     def __init__(self):
#         self.queue_list = []

    
#     def add(self, item):
#         return self.queue_list.append(item)
    
#     def next(self):
#         return self.queue_list.pop(0)

#     def is_empty(self):
#         if len(self.queue_list) <= 0:
#             return True
#         else:
#             return False
        



# queue = Queue()

# queue.add("Alice")
# queue.add("Bob")
# queue.add("Charlie")

# queue.next()
# queue.next()
# queue.next()

# print(queue)





class Queue:
    def __init__(self):
        self.__queue_list = []


    def add(self, item):
        return self.__queue_list.append(item)    
        
    def next(self):
        return self.__queue_list.pop(0)

    def is_empty(self):
        if len(self.__queue_list) <= 0 or len(self.__queue_list) == None:
            return True
        else:
            return False


queue = Queue()

queue.add('Alice')   # Alice arrives first
queue.add('Bob')     # Then Bob
queue.add('Charlie') # And Charlie as third

queue.next()   # Alice arrived first, so she's the first to be served next
queue.next()   # This must return Bob
queue.next()   # Finally, it's Charlie's turn