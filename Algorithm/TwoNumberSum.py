# Two Number Sum
# Example:
# Array: [6,2,8,-1,9,-4,-6,3,7], Target: 3
# Answer: [9, -6]

# ==============================================================

# O(N) Time | O(N) Space

def twoNumberSum(array, target):
    potentialResult = {}
    for number in array:
        if (target - number) in potentialResult:
            return [target - number, number]
        else:
            potentialResult[number] = True
    return []

print(twoNumberSum([6,2,8,-1,9,-4,-6,3,7], 3))
