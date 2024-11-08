// This problem was asked by Google.

// Given the head of a singly linked list, swap every two nodes and return its head.

// For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.


class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

function swapPairs(head) {
  // Create a dummy node to simplify edge cases
  const dummy = new ListNode(0);
  dummy.next = head;
  let prev = dummy;

  while (prev.next && prev.next.next) {
    // Identify the nodes to be swapped
    let first = prev.next;
    let second = prev.next.next;

    // Swap the nodes
    first.next = second.next;
    second.next = first;
    prev.next = second;

    // Move the prev pointer two nodes ahead
    prev = first;
  }

  return dummy.next;
}

// Helper function to print the linked list
function printList(head) {
  let current = head;
  while (current) {
    process.stdout.write(`${current.val} -> `);
    current = current.next;
  }
  console.log("null");
}

// Example usage
let head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
console.log("Original list:");
printList(head);

let swappedHead = swapPairs(head);
console.log("Swapped list:");
printList(swappedHead);
