class BST(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


    # O(Log(N)) Time | O(1) Space
	def insert(self, value):
		currentNode = self
		while True:
			if value < currentNode.value:
				if currentNode.left is None:
					currentNode.left = BST(value)
					break
				else:
					currentNode = currentNode.left
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
		return self


    # O(Log(N)) Time | O(1) Space
	def contains(self, value):
		currentNode  = self
		while currentNode is not None:
			if value < currentNode.value:
				currentNode = currentNode.left
			elif value > currentNode.value:
				currentNode = currentNode.right
			else:
				return True
		return False


	def remove(self, value, parentNode = None):
		currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.left
			elif value > currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.right
			else:
				if currentNode.left is not none and currentNode.right is not None:
					currentNode.value = currentNode.right.getMinValue()
					currentNode.right.remove(currentNode.value, parentNode)
				elif parentNode is None:
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						currentNode.left = currentNode.left.left
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else:
						currentNode.value = None
				elif parentNode.left == currentNode:
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
				break

	def getMinValue(self):
		currentNode = self
		while currentNode.left is not None:
			currentNode = currentNode.left
		return currentNode.value 

	def inOrderTraversal(self, tree, array = []):
		# left --> root --> right
		if tree is not None:
			self.inOrderTraversal(tree.left, array)
			array.append(tree.value)
			self.inOrderTraversal(tree.right, array)
		return array

	def preOrderTraversal(self, tree, array = []):
		# root --> left --> right
		if tree is not None:
			array.append(tree.value)
			self.preOrderTraversal(tree.left, array)
			self.preOrderTraversal(tree.right, array)
		return array

	def postOrderTraversal(self, tree, array = []):
		# left --> right --> root
		if tree is not None:
			self.postOrderTraversal(tree.left, array)
			self.postOrderTraversal(tree.right, array)
			array.append(tree.value)
		return array




tree = BST(10)
tree.insert(5).insert(4).insert(1).insert(7).insert(6).insert(22)
print('In-Order: ' + str(tree.inOrderTraversal(tree)))
print('Pre-Order: ' + str(tree.preOrderTraversal(tree)))
print('Post-Order: ' + str(tree.postOrderTraversal(tree)))


              #       10
              #      /  \
              #     6    22
              #    / \
              #   4   7
              #  / \
              # 1   5