# Write a function that receives as input the head node of a linked list and an integer k. Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

# For example, if we have the following linked list:
# (20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

# The head node would refer to the node(20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node(14).

# After the function executes, the state of the linked list should be:
# (20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null

# If k is longer than the length of the linked list, the linked list should not be changed.

# Can you implement a solution that performs a single pass through the linked list and doesn't use any extra space?

# Note: When reading the tests, the linked list contents are enumerated in between square brackets
# this does NOT mean the inputs are arrays.

# For example, a test input of head: [2, 4, 6] indicates that the input is a singly-linked list
# (2) -> (4) -> (6) -> null whose head is the first element in the linked list.

# [execution time limit] 4 seconds(py3)

# [input] linkedlist.integer head

# [input] integer k

# [output] linkedlist.integer

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#


def remove_kth_from_end(head, k):
    # set the original head to a variable so we don't lose it.
    org_head = head
    current_head = head
    length_counter = 1

    if k == 0:
        return head
    # Find the LL length for traversal
    while current_head.next:
        length_counter += 1
        current_head = current_head.next

    if k > length_counter:
        return head

    if k == length_counter:
        head = head.next
        return head
    # subtract k from length to find the kth element
    kth_element = length_counter - k
    k_counter = 1
    prev = head
    current_head = head.next

    while k_counter < kth_element:
        k_counter += 1
        prev = current_head
        current_head = current_head.next
    # continue traversal  with .nexts
    prev.next = current_head.next
    return org_head
