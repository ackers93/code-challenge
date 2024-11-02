// Given an array of integers, find if the array contains any duplicates.

// Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

// Example 1:
// Input: [1, 2, 3, 1]
// Output: true

// Example 2:
// Input: [1, 2, 3, 4]
// Output: false
// Example 3:

// Input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
// Output: true

function listDupes(array) {
  let selected_items = []
  for (const num of array){
    if (selected_items.includes(num)){
      return true
    } else {
      selected_items.push(num)
    }
  }
  return false

}
  

// Test cases
const arr1 = [1, 2, 3, 1] // Expected output: true
const arr2 = [1, 2, 3, 4] // Expected output: false
const arr3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] // Expected output: true

console.log(listDupes(arr1))
console.log(listDupes(arr2))
console.log(listDupes(arr3))