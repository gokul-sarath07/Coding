# Validate Subsequence
# Example:
# Array: [5, 1, 22, 25, 6, -1, 8, 10]
# Sequence: [1, 6, -1, 10]
# Answer: True

# ==============================================================

# O(N) Time | O(1) Space

def validateSubsequence(array, sequence):
    arrayIdx = 0
    sequenceIdx = 0
    while arrayIdx < len(array) and sequenceIdx < len(sequence):
        if array[arrayIdx] == sequence[sequenceIdx]:
            sequenceIdx += 1
        arrayIdx += 1
    return sequenceIdx == len(sequence)

print(validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
