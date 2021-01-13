# Branch Sum
# Example:
# Tree:
#         10
#      4     15
#    2  3  13  22
#
# Branch Sum = [16, 17, 38, 47]

# ==============================================================

# O(N) Time | O(N) Space

def branchSum(tree):
	sumList = []
	calculateBranchSum(tree, 0, sumList)
	return sumList

def calculateBranchSum(node, runningSum, sumList):
    if node is None:
        return
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sumList.append(newRunningSum)

    calculateBranchSum(node.left, newRunningSum, sumList)
    calculateBranchSum(node.right, newRunningSum, sumList)
