# Quick Sort
# Example:
# Array: [8,3,7,5,1,6,4,9,10,2]
# Answer: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ==============================================================

# O(Nlog(N)) Time | O(log(N)) Space

def quickSort(array):
	quickSortHelper(array, 0, len(array) - 1)
	return array

def quickSortHelper(array, startIdx, endIdx):

	if startIdx >= endIdx:
		return

	pivotIdx = startIdx
	leftIdx = startIdx + 1
	rightIdx = endIdx

	while rightIdx >= leftIdx:
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			swap(leftIdx, rightIdx, array)
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1
	swap(pivotIdx, rightIdx, array)
	leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
	if leftSubarrayIsSmaller:
		quickSortHelper(array, startIdx, rightIdx - 1)
		quickSortHelper(array, rightIdx + 1, endIdx)
	else:
		quickSortHelper(array, rightIdx + 1, endIdx)
		quickSortHelper(array, startIdx, rightIdx - 1)

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

print(quickSort([8,3,7,5,1,6,4,9,10,2]))
