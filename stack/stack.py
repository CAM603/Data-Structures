"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
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


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = None

    def __len__(self):
        return self.size

    def push(self, value):
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

    def pop(self):
        # Set current
        current = self.storage
        # If None
        if not current:
            return None
        else:
            # reduce size
            self.size -= 1
            # set previous to None
            previous = None
            while current.get_next() is not None:
                # Set new previous node
                # (it will be the current node now)
                previous = current
                # Set new current
                # (Old currents next node)
                current = current.get_next()
            # Make previous the last node by setting its next node to None
            if previous is not None:
                previous.next_node = None
            else:
                self.storage = None
            return current.get_value()

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) is 0:
#             return None
#         else:
#             return self.storage.pop()


# stack = (The) Last (item) In (is the) First (item) Out
# 5 is the pringle closest to the top (last item added)
pringles = [0, 1, 2, 3, 4, 5]
# Someone eats a pringle
pringles.pop()
print(pringles)
# Someone puts a pringle back on
pringles.append(5)
print(pringles)
