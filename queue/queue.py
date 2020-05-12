"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
    What would that look like? How many Stacks would you need? Try it!
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = None

    def __len__(self):
        return self.size

    def enqueue(self, value):
        # adding to the end or tail
        # wrap value in a new node
        new_node = Node(value)
        # increase size
        self.size += 1
        # if the storage is None
        if not self.storage:
            self.storage = new_node
        else:
            # add new node to the last node
            current = self.storage
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def dequeue(self):
        # removing from the head/beginning
        # if nothing stored
        if not self.storage:
            return None
        else:
            # reduce size
            self.size -= 1
            # capture value we want to return
            # we want value of the current node
            value = self.storage.get_value()
            # remove value at the head
            # update head
            self.storage = self.storage.get_next()
            return value

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         # adding to the end or tail
#         self.storage.append(value)
#         return self.storage


#     def dequeue(self):
#         # removing from the head/beginning
#         if len(self.storage) is 0:
#             return None
#         else:
#             return self.storage.pop(0)

# queue = (The) First (item) In (is the) First (item) Out

# This list is a line of people waiting for coffee
# 0 is first in line, 5 is last in line
waiting_list = [0, 1, 2, 3, 4, 5]
# Someone else gets in line for coffee
waiting_list.append(6)
print(waiting_list)
# The first person leaves after getting coffee
waiting_list.pop(0)
print(waiting_list)
