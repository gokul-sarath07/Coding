# Monotonic Array
# Example:
# Array: [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
# Answer: True

# ==============================================================

# O(N) Time | O(1) Space

def monotonicArray(array):
    ascending = True
    decending = True
    for num in range(len(array) - 1):
        if array[num] < array[num+1]:
            decending = False
        if array[num] > array[num+1]:
            ascending = False
    return ascending or decending

print(monotonicArray([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
