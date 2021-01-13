# Smallest Difference
# Example:
# Array One: [-1, 5, 10, 20, 28, 3]
# Array Two: [26, 134, 135, 15, 17]
# Answer: [28, 26]

# ==============================================================

# O(Nlog(N) + Mlog(M)) Time | O(1) Space

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float('inf')
    currentDiff = float('inf')
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        currentDiff = abs(firstNum - secondNum)
        if firstNum < secondNum:
            idxOne += 1
        elif secondNum < firstNum:
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > currentDiff:
            smallest = currentDiff
            smallestPair = [firstNum, secondNum]
    return smallestPair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
