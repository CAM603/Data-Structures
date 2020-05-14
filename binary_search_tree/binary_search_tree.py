"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value  # BinarySearchTree value
        self.left = None  # BinarySearchTree
        self.right = None  # BinarySearchTree

    # Insert the given value into the tree
    def insert(self, value):
        # Recursive function to compare value to the current node value
        # def search(node):
        #     # check if value is less than current node value
        #     if value < node.value:
        #         # If there is a node to the left
        #         # Reinvoke search function
        #         if node.left is not None:
        #             return search(node.left)
        #         # If there is not a node to the left
        #         # Set the left node to a new BSTNode with the new value
        #         else:
        #             node.left = BSTNode(value)
        #     # check if value is greater than or equal to current node value
        #     elif value >= node.value:
        #         # If there is a node to the right
        #         # Reinvoke search function
        #         if node.right is not None:
        #             return search(node.right)
        #         # If there is not a node to the right
        #         # Set the right node to a new BSTNode with the new value
        #         else:
        #             node.right = BSTNode(value)
        # # Invoke recursive function with BSTNode
        # return search(self)

        # Check if incomming value is lesss than current value
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        # recursive function to find if a value exists in the tree
        # def search(node):
        #     # If target is the current node return True
        #     if target == node.value:
        #         return True
        #     # If the target is less than the current node
        #     # Check left
        #     elif target < node.value:
        #         if node.left is not None:
        #             return search(node.left)
        #         else:
        #             return False
        #     # If the target is greater than or equal to the current node
        #     # Check right
        #     elif target >= node.value:
        #         if node.right is not None:
        #             return search(node.right)
        #         else:
        #             return False
        # # Invoke recursive function with BSTNode
        # return search(self)

        if target == self.value:
            return True
        elif target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        elif target >= self.value:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # def search(node):
        #     if node.right is not None:
        #         # Check that node.right
        #         return search(node.right)
        #     else:
        #         # This is the biggest value
        #         return node.value
        # return search(self)

        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    def iterative_get_max(self):
        current_max_value = self.value

        current = self
        # Traverse our structure
        while current is not None:
            if current.value > current_max_value:
                current_max_value = current.value
            # Update current_max_value if we see a larger value
            current = current.right

        return current_max_value

    # Call the function `fn` on the value of each node
    # This is DEPTH FIRST, LIFO
    def for_each(self, fn):
        # def do_each(node):
        #     fn(node.value)
        #     if node.right is not None:
        #         do_each(node.right)
        #     if node.left is not None:
        #         do_each(node.left)
        # return do_each(self)

        # Call passed in function
        # If there is a right child
        fn(self.value)
        if self.right is not None:
            # Call passed in function
            self.right.for_each(fn)
        # If there is a left child
        if self.left is not None:
            # Call passed in function
            self.left.for_each(fn)

    # ITERATIVE FOR EACH (NEEDS A STACK)
    # This is DEPTH FIRST, LIFO
    # def for_each(self, fn):
    #     stack = []
    #     # Add root node
    #     stack.append(self)
    #     # Loop so long as the stack still has elements
    #     while stack:
    #         current = stack.pop()
    #         if current.left:
    #             stack.append(current.left)
    #         if current.right:
    #             stack.append(current.right)
    #         fn(current.value)

    # This is BREADTH FIRST, FIFO
    # def for_each(self, fn):
    #     queue = []
    #     # Add root node
    #     queue.append(self)
    #     # Loop so long as the queue still has elements
    #     while queue:
    #         current = queue.pop(0)
    #         if current.left:
    #             queue.append(current.left)
    #         if current.right:
    #             queue.append(current.right)
    #         fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # Using a STACK visit each node once, one layer at a time
    # Create STACK
    # Add root to STACK
    # while STACK is not empty node = pop top of STACK
    # DO THE THING (PRINT)
    # Add children of node to stack
    def in_order_print(self, node):
        if node is None:
            return
        if node.left:
            node.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # Using a QUEUE visit each node once, one layer at a time
    # Create QUEUE
    # Add root to queue
    # While queue is not empty, node = pop head of queue
    # DO THE THING (PRINT)
    # Add children of root to queue
    # Pop node off the queue

    def bft_print(self, node):
        queue = [node]
        while queue:
            current = queue.pop(0)
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    # Using a STACK visit each node once, one layer at a time
    # Create STACK
    # Add root to STACK
    # while STACK is not empty node = pop top of STACK
    # DO THE THING (PRINT)
    # Add children of node to stack
    def dft_print(self, node):
        stack = [node]
        while stack:
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if self.left is not None:
            # Call passed in function
            self.left.pre_order_dft(self.left)
        if self.right is not None:
            # Call passed in function
            self.right.pre_order_dft(self.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        if self.left is not None:
            # Call passed in function
            self.left.post_order_dft(self.left)
        if self.right is not None:
            # Call passed in function
            self.right.post_order_dft(self.right)
        print(node.value)


def print_them(el):
    print(el)


tree_node = BSTNode(1)

tree_node.insert(8)
tree_node.insert(5)
tree_node.insert(7)
tree_node.insert(6)
tree_node.insert(3)
tree_node.insert(4)
tree_node.insert(2)
# tree_node.for_each(print_them)
# tree_node.in_order_print(tree_node)
# 1,2,3,4,5,6,7,8
# tree_node.bft_print(tree_node)
# 1,8,5,3,7,2,4,6,
# OR
# 1,8,5,7,3,6,4,2,
# tree_node.dft_print(tree_node)
# 1,8,5,7,6,3,4,2,
# OR
# 1,8,5,3,2,4,7,6,
# tree_node.pre_order_dft(tree_node)
# 1,8,5,3,2,4,7,6,
tree_node.post_order_dft(tree_node)
# 2,4,3,6,7,5,8,1,
