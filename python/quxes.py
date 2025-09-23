# This problem was asked by Facebook.

# On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

# Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

# For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

#         Arrangement       |   Change
# ----------------------------------------
# ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
# ['B', 'B', 'G', 'B']      | (B, G) -> R
# ['B', 'R', 'B']           | (R, B) -> G
# ['B', 'G']                | (B, G) -> R
# ['R']    

def quxes(quxes, show_steps=False):
    if not quxes:
        return 0
    
    original = quxes.copy()
    
    # Simulate the actual transformations
    while len(quxes) > 1:
        # Find the first pair of adjacent different colors
        transformed = False
        for i in range(len(quxes) - 1):
            if quxes[i] != quxes[i + 1]:
                # Transform the pair into the third color
                a, b = quxes[i], quxes[i + 1]
                third_color = get_third_color(a, b)
                
                if show_steps:
                    print(f"Step: {quxes} -> ({a}, {b}) -> {third_color}")
                
                # Replace the pair with the third color
                quxes = quxes[:i] + [third_color] + quxes[i + 2:]
                transformed = True
                break
        
        if not transformed:
            # No adjacent different colors found - can't transform further
            if show_steps:
                print(f"Final: {quxes} (no more transformations possible)")
            break
    
    if show_steps:
        print(f"Result: {len(quxes)} Quxes remaining")
    
    return len(quxes)

def get_third_color(a, b):
    """Given two different colors, return the third color"""
    colors = {'R', 'G', 'B'}
    return (colors - {a, b}).pop()

# Test cases that return different numbers

# Returns 0 - empty array
print("Empty array:", quxes([]))  # 0

# Returns 1 - single element
print("Single element:", quxes(['R']))  # 1

# Returns 1 - mixed parities (can reduce to 1)
print("Mixed parities:", quxes(['R', 'G', 'B', 'G', 'B']))  # 1
print("Mixed parities:", quxes(['R', 'G']))  # 1
print("Mixed parities:", quxes(['R', 'G', 'B']))  # 1

# Returns 2 - all same parity (can only reduce to 2)
print("Same parity:", quxes(['R', 'G', 'R', 'G']))  # 2
print("Same parity:", quxes(['R', 'R', 'G', 'G', 'B', 'B']))  # 2
print("Same parity:", quxes(['R', 'G', 'B', 'R', 'G', 'B']))  # 2

# Returns 3 - all same color (no transformations possible)
print("All same color:", quxes(['R', 'R', 'R']))  # 3
print("All same color:", quxes(['G', 'G', 'G', 'G']))  # 4

# Returns 2 - two colors, same parity
print("Two colors same parity:", quxes(['R', 'G', 'R', 'G']))  # 2
print("Two colors same parity:", quxes(['R', 'R', 'G', 'G']))  # 2

# Returns 1 - two colors, different parity
print("Two colors different parity:", quxes(['R', 'G', 'R']))  # 1
print("Two colors different parity:", quxes(['R', 'G', 'G']))  # 1

# Show transformation steps
print("\n=== Transformation Steps ===")
print("Example: ['R', 'G', 'B', 'G', 'B']")
quxes(['R', 'G', 'B', 'G', 'B'], show_steps=True)

print("\nExample: ['R', 'G', 'R', 'G']")
quxes(['R', 'G', 'R', 'G'], show_steps=True)