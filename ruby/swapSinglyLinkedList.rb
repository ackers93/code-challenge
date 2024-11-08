# This problem was asked by Google.

# Given the head of a singly linked list, swap every two nodes and return its head.

# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.


class ListNode
    attr_accessor :val, :next
  
    def initialize(val = 0, nxt = nil)
      @val = val
      @next = nxt
    end
  end
  
  def swap_pairs(head)
    # Create a dummy node to simplify edge cases
    dummy = ListNode.new(0)
    dummy.next = head
    prev = dummy
  
    while prev.next && prev.next.next
      # Identify the nodes to be swapped
      first = prev.next
      second = prev.next.next
  
      # Swap the nodes
      first.next = second.next
      second.next = first
      prev.next = second
  
      # Move the prev pointer two nodes ahead
      prev = first
    end
  
    dummy.next
  end
  
  # Helper function to print the linked list
  def print_list(head)
    while head
      print "#{head.val} -> "
      head = head.next
    end
    puts "nil"
  end
  
  # Example usage
  head = ListNode.new(1, ListNode.new(2, ListNode.new(3, ListNode.new(4))))
  puts "Original list:"
  print_list(head)
  
  swapped_head = swap_pairs(head)
  puts "Swapped list:"
  print_list(swapped_head)
  