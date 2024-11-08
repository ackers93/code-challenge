# This problem was asked by Google.

# Given the head of a singly linked list, swap every two nodes and return its head.

# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    # Create a dummy node that acts as the previous node of the head node
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        # Identify the nodes to be swapped
        first = prev.next
        second = prev.next.next

        # Swapping the nodes
        first.next = second.next
        second.next = first
        prev.next = second

        # Move the prev pointer two nodes ahead
        prev = first

    return dummy.next

# Helper function to print the linked list
def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print("Original list:")
print_list(head)

swapped_head = swap_pairs(head)
print("Swapped list:")
print_list(swapped_head)
