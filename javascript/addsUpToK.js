function allPairsThatAddUpToK(array, k) {
    const seenNumbers = new Set();
    const pairs = [];
  
    for (const num of array) {
      const complement = k - num;
      if (seenNumbers.has(complement)) {
        pairs.push([complement, num]);
      }
      seenNumbers.add(num);
    }
  
    return pairs.length > 0 ? pairs : null;
  }
  
  // Test the function
  const arr = [10, 15, 3, 7, 7, 10];
  const knumber = 17;
  const result = allPairsThatAddUpToK(arr, knumber);
  
  if (result) {
    console.log(`Pairs that add up to ${knumber}:`, result);
  } else {
    console.log(`No pairs add up to ${knumber}`);
  }
  