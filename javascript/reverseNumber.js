// Write a function called reverseNumber that reverses a number.

// Input Example:
// 12345
// 555

// Output Example:
// 54321
// 555

function reverseNumber(num) {
  num = num + "";
  num = Number(num.split("").reverse().join(""));
  return num;
}

reverseNumber(123456);
