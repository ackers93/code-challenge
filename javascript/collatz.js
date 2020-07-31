// write a function which takes a positive integer number as an argument and returns it's "Collatz chain". The Collatz chain will stop at one.

// Named after Lothar Collatz, the "Collatz conjecture" defines a sequence of numbers.That sequence is the Collatz "chain".Starting with a positive integer, the Collatz conjecture determines the next integer in the chain until the number 1 is obtained.

// Your Collatz algorithm will evaluate the integer and then, depending on the condition of the integer, perform the following tasks:

// If the integer is even, then halve the number.
// If the integer is not even, then multiply it by 3 and add one.

// An example chain starting from the number 23 looks like this:

// [23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]

// Boldface signifies the odd numbers

// Your function should behave like this:
// console.log(collatzSequence(23));
// // [ 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1 ]

function collatzSequence(n) {
  const sequence = [];
  sequence.push(n);
  while (n !== 1) {
    if (n % 2 === 0) {
      n = n / 2;
      sequence.push(n);
    } else {
      n = n * 3 + 1;
      sequence.push(n);
    }
  }
  return sequence;
}

console.log(collatzSequence(23));
