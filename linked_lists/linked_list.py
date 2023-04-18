class LinkedList:
    """
    Implements a singly linked list.
    """

    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def add(self, val) -> None:
        next_node = LinkedList(val)
        n = self
        while n.next != None:
            n = n.next
        n.next = next_node

    def remove(self, val) -> None:
        n = self
        while n.next.val != val:
            n = n.next
        n.next = n.next.next
