"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # create a list node
        new_node = ListNode(value)
        # Update length
        self.length += 1
        # if there is not a head or tail node
        if not self.head and not self.tail:
            # new node will be head and tail
            self.head = new_node
            self.tail = new_node
        # there is already a node
        else:
            # new nodes next is the current head
            new_node.next = self.head
            # current head will no longer be head so it will have a previous pointer to the new node
            self.head.prev = new_node
            # set new node as the head
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # Capture value of node to remove
        value = self.head.value
        # Use ListNode delete method
        self.delete(self.head)
        # Return the value
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # create new node
        new_node = ListNode(value)
        # update length
        self.length += 1
        # if there is not a head or tail
        if not self.head and not self.tail:
            # new node will be head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # new node previous pointer becomes current tail
            new_node.prev = self.tail
            # current tail will no longer be the tail so it will now have a next pointer to the new node
            self.tail.next = new_node
            # set new node as the tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # Capture value of node to remove
        value = self.tail.value
        # Use ListNode delete method
        self.delete(self.tail)
        # Return value
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # If already the head
        if node is self.head:
            return
        # Create a new head node with the old node's value with add_to_head method
        self.add_to_head(node.value)
        # Delete the old node using this class's delete method
        # to handle the case that the node is head or tail
        self.delete(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # If already the tail
        if node is self.tail:
            return
        # Create a new tail node with the old node's value with add_to_tail method
        self.add_to_tail(node.value)
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # TODO: Error checking if node is not in list
        self.length -= 1
        # Is this the only node?
        if self.head is self.tail:
            # Remove pointer to head
            self.head = None
            # Remove pointer to tail
            self.tail = None
        # If it is the head
        elif node is self.head:
            # Reassign the head to the current heads next pointer
            self.head = node.next
            # Use the delete method on the ListNode class
            node.delete()
        # If it is the tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # If it is in the middle
        else:
            # Rearranges this ListNode's previous and next pointers
            # accordingly, effectively deleting the ListNode
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # How to get max value:
        # Create max variable
        current = self.head
        max = self.head.value
        # Loop through nodes
        while(current is not None):
            # Compare value in node to max found
            if current.value > max:
                max = current.value
            current = current.next
        # Return max found
        return max
