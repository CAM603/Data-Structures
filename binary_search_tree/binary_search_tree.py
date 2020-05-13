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

        if value < self.value:
            if self.left is not None:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value >= self.value:
            if self.right is not None:
                return self.right.insert(value)
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

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # def do_each(node):
        #     fn(node.value)
        #     if node.right is not None:
        #         do_each(node.right)
        #     if node.left is not None:
        #         do_each(node.left)
        # return do_each(self)
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


def print_them(el):
    print(el)


tree_node = BSTNode(6)

tree_node.insert(2)
tree_node.insert(8)
tree_node.insert(10)
tree_node.insert(3)
tree_node.for_each(print_them)
