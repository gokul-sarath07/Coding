class Node:

	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:

	def __init__(self):
		self.head = None

	def append(self,data):

		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = new_node
			new_node.prev = curr

	def print_list(self):

		curr = self.head
		while curr:
			print(curr.data)
			curr = curr.next

	def prepend(self,data):

		new_node = Node(data)

		if self.head is None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node


	def insert_after_node(self,key,data):

		curr = self.head
		while curr:
			if curr.next is None and curr.data == key:
				self.append(data)
				return
			elif curr.data == key:
				new_node = Node(data)
				nxt = curr.next
				curr.next = new_node
				new_node.next = nxt
				nxt.prev = new_node
				new_node.prev = curr
				return
			curr = curr.next

	def insert_before_node(self,key,data):
		curr = self.head
		while curr:
			if curr.prev is None and curr.data == key:
				self.prepend(data)
				return
			elif curr.data == key:
				new_node = Node(data)
				prev = curr.prev
				prev.next = new_node
				new_node.next = curr
				curr.prev = new_node
				new_node.prev = prev
				return
			curr = curr.next

	def delete(self, key):

		curr = self.head
		
		while curr:
			if curr.data == key and curr == self.head:
				if not curr.next:
					curr = None
					self.head = None
					return
				else:
					nxt = curr.next
					nxt.prev = None
					curr = None
					self.head = nxt
					return
			elif curr.data == key:
				if curr.next:
					nxt = curr.next
					prev = curr.prev
					curr = None
					prev.next = nxt
					nxt.prev = prev
					return
				else:
					prev = curr.prev
					prev.next = None
					curr = None
					return
			curr = curr.next

	def reverse(self):
		tmp = None
		curr = self.head
		while curr:
			tmp = curr.prev
			curr.prev = curr.next
			curr.next = tmp
			curr = curr.prev
		if tmp:
			self.head = tmp.prev
