class Queue(object):

	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		if not self.isempty():
			return self.items.pop()

	def isempty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def __len__(self):
		return self.size()

	def peek(self):
		if not self.isempty():
			return self.items[-1].value

class Stack(object):

	def __init__(self):
		self.items = []

	def push(self, value):
		self.items.append(value)

	def pop(self):
		if not self.isempty():
			return self.items.pop()

	def isempty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def __len__(self):
		return self.size()

	def __str__(self):
		s = ''
		for i in reversed(range(len(self.items))):
			s += str(self.items[i].value) + '-' 
		return s

	def peek(self):
		if not self.isempty():
			return self.items[-1]

class Node(object):

	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):

	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self, traversal_type):

		if traversal_type == 'preorder':
			return self.preorder_print(self.root)
		elif traversal_type == 'inorder':
			return self.inorder_print(self.root)
		elif traversal_type == 'postorder':
			return self.postorder_print(self.root)
		elif traversal_type == 'levelorder':
			return self.levelorder_print(self.root)
		elif traversal_type == 'reverse_levelorder':
			return self.reverse_levelorder_print(self.root)

		else:
			return 'Traversal type ' + str(traversal_type) + ' is not supported'


	def preorder_print(self, start, traversal = ''):
		# root--> left--> right
		if start:
			traversal += (str(start.value) + '-')
			traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
		return traversal

	def inorder_print(self, start, traversal = ''):
		# left --> root --> right
		if start:
			traversal = self.inorder_print(start.left, traversal)
			traversal += (str(start.value) + '-')
			traversal = self.inorder_print(start.right, traversal)
		return traversal

	def postorder_print(self, start, traversal = ''):
		# left --> right --> root
		if start:
			traversal = self.postorder_print(start.left, traversal)
			traversal = self.postorder_print(start.right, traversal)
			traversal += (str(start.value) + '-')
		return traversal

	def levelorder_print(self, start):

		if not start:
			return

		queue = Queue()
		queue.enqueue(start)

		traversal = ''
		while len(queue) > 0:
			traversal += str(queue.peek()) + '-'
			node = queue.dequeue()

			if node.left:
				queue.enqueue(node.left)
			if node.right:
				queue.enqueue(node.right)
		return traversal

	def reverse_levelorder_print(self, start):

		if not start:
			return

		queue = Queue()
		stack = Stack()
		queue.enqueue(start)

		while len(queue) > 0:

			node = queue.dequeue()
			stack.push(node)

			if node.right:
				queue.enqueue(node.right)
			if node.left:
				queue.enqueue(node.left)
		
		return str(stack)


	def height(self, node):
		if node is None:
			return -1

		left_height = self.height(node.left)
		right_height = self.height(node.right)

		return 1 + max(left_height, right_height)

	# def size(self, node):
	# 	count = 0

	# 	if node:
	# 		count += 1
	# 		count += self.size(node.left)
	# 		count += self.size(node.right)
	# 	return count

	def size_(self, node):
		if node is None:
			return 0
		return 1 + self.size_(node.left) + self.size_(node.right)



tree = BinaryTree(10)
tree.root.left = Node(6)
tree.root.right = Node(22)
tree.root.left.left = Node(4)
tree.root.left.right = Node(7)
tree.root.left.left.left = Node(1)
tree.root.left.right.right = Node(5)

print('In-Order: ' + tree.print_tree('inorder'))
print('Pre-Order: ' + tree.print_tree('preorder'))
print('Post-Order: ' + tree.print_tree('postorder'))