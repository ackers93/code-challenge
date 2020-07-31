// Write a function that takes an array of strings and return the longest string in the array.

// For example:
// const strings1 = ['short', 'really, really long!', 'medium'];
// console.log(longestString(strings1)); // <--- 'really, really long!'

// Edge case: If you had an array which had two "longest" strings of equal length, your function should just return the first one.

// For example:
// const strings2 = ['short', 'first long string!!', 'medium', 'abcdefghijklmnopqr'];

function reverseString(str) {
  var array = str.split("");
  str = array.reverse().join("");
  return str;
}

reverseString("LLO");
