// Given a pivot x, and a list lst, partition the list into three parts.

// The first part contains all elements in lst that are less than x
// The second part contains all elements in lst that are equal to x
// The third part contains all elements in lst that are larger than x
// Ordering within a part can be arbitrary.

// For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14]


function partitionList(lst, x) {
    const lessThanX = lst.filter(n => n < x);
    const equalToX = lst.filter(n => n === x);
    const greaterThanX = lst.filter(n => n > x);
  
    return [...lessThanX, ...equalToX, ...greaterThanX];
  }
  
  const x = 10;
  const lst = [9, 12, 3, 5, 14, 10, 10];
  const result = partitionList(lst, x);
  console.log(result); // Output will be [9, 3, 5, 10, 10, 12, 14]
  