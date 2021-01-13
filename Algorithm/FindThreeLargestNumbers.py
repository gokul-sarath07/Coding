# Find Three Largest Numbers
# Example:
# Array: [141, 1, 17, -7, -17, -27, 18, 541, 8 ,7, 7]
# Answer: [18, 141, 541]

# ==============================================================

# O(N) Time | O(1) Space (The result array is small compaired to the input array)

def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateThreeLargest(threeLargest,num)
    return threeLargest

def updateThreeLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        swipeAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        swipeAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        swipeAndUpdate(threeLargest, num, 0)

def swipeAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]

print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8 ,7, 7]))
