// This problem was asked by Facebook.

// On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

// Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

// For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

//         Arrangement       |   Change
// ----------------------------------------
// ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
// ['B', 'B', 'G', 'B']      | (B, G) -> R
// ['B', 'R', 'B']           | (R, B) -> G
// ['B', 'G']                | (B, G) -> R
// ['R']    

function quxes(quxes, showSteps = false) {
    if (quxes.length === 0) {
        return 0;
    }
    
    // Create a copy to avoid mutating the original array
    let quxesArray = [...quxes];
    
    // Simulate the actual transformations
    while (quxesArray.length > 1) {
        // Find the first pair of adjacent different colors
        let transformed = false;
        for (let i = 0; i < quxesArray.length - 1; i++) {
            if (quxesArray[i] !== quxesArray[i + 1]) {
                // Transform the pair into the third color
                const a = quxesArray[i];
                const b = quxesArray[i + 1];
                const thirdColor = getThirdColor(a, b);
                
                if (showSteps) {
                    console.log(`Step: [${quxesArray.join(', ')}] -> (${a}, ${b}) -> ${thirdColor}`);
                }
                
                // Replace the pair with the third color
                quxesArray = [
                    ...quxesArray.slice(0, i),
                    thirdColor,
                    ...quxesArray.slice(i + 2)
                ];
                transformed = true;
                break;
            }
        }
        
        if (!transformed) {
            // No adjacent different colors found - can't transform further
            if (showSteps) {
                console.log(`Final: [${quxesArray.join(', ')}] (no more transformations possible)`);
            }
            break;
        }
    }
    
    if (showSteps) {
        console.log(`Result: ${quxesArray.length} Quxes remaining`);
    }
    
    return quxesArray.length;
}

function getThirdColor(a, b) {
    // Given two different colors, return the third color
    const colors = new Set(['R', 'G', 'B']);
    colors.delete(a);
    colors.delete(b);
    return colors.values().next().value;
}

// Test cases that return different numbers
console.log("=== Test Cases ===");

// Returns 0 - empty array
console.log("Empty array:", quxes([])); // 0

// Returns 1 - single element
console.log("Single element:", quxes(['R'])); // 1

// Returns 1 - mixed parities (can reduce to 1)
console.log("Mixed parities:", quxes(['R', 'G', 'B', 'G', 'B'])); // 1
console.log("Mixed parities:", quxes(['R', 'G'])); // 1
console.log("Mixed parities:", quxes(['R', 'G', 'B'])); // 1

// Returns 2 - all same parity (can only reduce to 2)
console.log("Same parity:", quxes(['R', 'G', 'R', 'G'])); // 2
console.log("Same parity:", quxes(['R', 'R', 'G', 'G', 'B', 'B'])); // 2
console.log("Same parity:", quxes(['R', 'G', 'B', 'R', 'G', 'B'])); // 2

// Returns 3+ - all same color (no transformations possible)
console.log("All same color:", quxes(['R', 'R', 'R'])); // 3
console.log("All same color:", quxes(['G', 'G', 'G', 'G'])); // 4

// Returns 2 - two colors, same parity
console.log("Two colors same parity:", quxes(['R', 'G', 'R', 'G'])); // 2
console.log("Two colors same parity:", quxes(['R', 'R', 'G', 'G'])); // 2

// Returns 1 - two colors, different parity
console.log("Two colors different parity:", quxes(['R', 'G', 'R'])); // 1
console.log("Two colors different parity:", quxes(['R', 'G', 'G'])); // 1

// Show transformation steps
console.log("\n=== Transformation Steps ===");
console.log("Example: ['R', 'G', 'B', 'G', 'B']");
quxes(['R', 'G', 'B', 'G', 'B'], true);

console.log("\nExample: ['R', 'G', 'R', 'G']");
quxes(['R', 'G', 'R', 'G'], true);
