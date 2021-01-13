# Insertion Sort Algorithm
# Example:
# Array: [141, 1, 17, -7, -17, -27, 18, 541, 8 ,7, 7]
# Answer: [-27, -17, -7, 1, 7, 7, 8, 17, 18, 141, 541]

# ==============================================================

# O(N^2) Time | O(1) Space

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(insertionSort([141, 1, 17, -7, -17, -27, 18, 541, 8 ,7, 7]))
