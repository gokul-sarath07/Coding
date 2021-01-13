# Find Three Smallest Numbers
# Example:
# Array: [141, 1, 17, -7, -17, -27, 18, 541, 8 ,7, 67]
# Answer: [-7, -17, -27]

# ==============================================================

# O(N) Time | O(1) Space (The result array is small compaired to the input array)

def findThreeSmallestNumbers(array):
    threeSmallest = [None, None, None]
    for num in array:
        updateThreeSmallest(threeSmallest, num)
    return threeSmallest

def updateThreeSmallest(threeSmallest, num):
    if threeSmallest[2] is None or num < threeSmallest[2]:
        swipeAndUpdate(threeSmallest, num, 2)
    elif threeSmallest[1] is None or num < threeSmallest[1]:
        swipeAndUpdate(threeSmallest, num, 1)
    elif threeSmallest[0] is None or num < threeSmallest[0]:
        swipeAndUpdate(threeSmallest, num, 0)

def swipeAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i+1]

print(findThreeSmallestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8 ,7, 7]))
