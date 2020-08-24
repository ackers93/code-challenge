# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        l2_list = []
        # need to iterate over both lists,
        # as long as l1 has something in it
        while l1 is not None:
            # we insert each item into the l1_list at the 0th index
            # that way, they end up correctly reversed
            l1_list.insert(0, str(l1.val))
            # this just iterates over the SLL
            l1 = l1.next
        # same as above, but with l2 to l2_list
        while l2 is not None:
            l2_list.insert(0, str(l2.val))
            l2 = l2.next

        # then concatenate each set with the join method
        l1_list_value = "".join(l1_list)
        l2_list_value = "".join(l2_list)

        # add concatenated values together
        end_result = str(int(l1_list_value) + int(l2_list_value))[::-1]
        # then split result into three elements
        # reverse elements in place
        end_result_array = []
        # appends the items in the ListNode format
        for num in end_result:
            end_result_array.append(ListNode(num))
        for node in range(len(end_result_array)):
            if node != len(end_result_array)-1:
                end_result_array[node].next = end_result_array[node+1]
        return end_result_array[0]
