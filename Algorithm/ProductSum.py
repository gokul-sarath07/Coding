# Product Sum
# Example:
# Array: [5,2,[7,-1],3,[6,[-13,8],4]]
# Answer: 5 + 2 + ((7+-1)*2) + 3 + ((6 + ((-13+8)*3) +4)*2) = 12

# ==============================================================

# O(N) Time (All elements in the array including elements in subarray) | O(1) Space

def productSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

print(productSum([5,2,[7,-1],3,[6,[-13,8],4]]))
