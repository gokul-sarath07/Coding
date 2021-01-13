# Three Number Sum
# Array: [12, 3, 1, 2, -6, 5, -8, 6], Target: 0
# Answer: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# ==============================================================

# O(N^2) Time | O(N) Space

def threeNumberSum(array, target):
    array.sort()
    sums = []
    for currentIdx in range(len(array) - 2):
        leftIdx = currentIdx + 1
        rightIdx = len(array) - 1
        while leftIdx < rightIdx:
            potentialSum = array[currentIdx] + array[leftIdx] + array[rightIdx]
            if potentialSum == target:
                sums.append([array[currentIdx], array[leftIdx], array[rightIdx]])
                leftIdx += 1
                rightIdx -= 1
            elif potentialSum > target:
                rightIdx -= 1
            elif potentialSum < target:
                leftIdx += 1
    return sums

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
