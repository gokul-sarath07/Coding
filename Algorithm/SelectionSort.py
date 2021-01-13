# Selection Sort Algorithm
# Example:
# Array: [141, 1, 17, -7, -17, -27, 18, 541, 8 ,7, 7]
# Answer: [-27, -17, -7, 1, 7, 7, 8, 17, 18, 141, 541]

# ==============================================================

# O(N^2) Time | O(1) Space

def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallest = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[i] < array[smallest]:
                smallest = i
        swap(currentIdx, smallest, array)
        currentIdx += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(selectionSort([141, 1, 17, -7, -17, -27, 18, 541, 8 ,7, 7]))
