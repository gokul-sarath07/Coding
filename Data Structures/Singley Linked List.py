class Node:

	def __init__(self,data):

		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):

		self.head = None

	def append(self,data):
		
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last_node = self.head

		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	def print_list(self):
		curr_node = self.head
		while curr_node:
			print(curr_node.data)
			curr_node = curr_node.next

	def prepend(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def insert_after_node(self,prev_node,data):
		if not prev_node:
			print("Previous node does not present")
		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def delete_node(self,key):
		curr_node = self.head

		if curr_node and curr_node.data == key:
			self.head = curr_node.next
			curr_node = None
			return

		prev = None
		while curr_node and curr_node.data != key:
			prev = curr_node
			curr_node = curr_node.next

		if curr_node is None:
			return

		prev.next = curr_node.next
		curr_node = None

	def delete_node_at_pos(self,pos):
		if self.head:
			curr_node = self.head

			if pos == 0:
				self.head = curr_node.next
				curr_node = None
				return

			prev = None
			count = 0
			while curr_node and count != pos:
				prev = curr_node
				curr_node = curr_node.next
				count += 1

			if curr_node is None:
				return

			prev.next = curr_node.next
			curr_node = None

	def len_iterative(self):
		count = 0
		curr_node = self.head

		while curr_node:
			count += 1
			curr_node = curr_node.next

		return count

	def len_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.len_recursive(node.next)

	def swap_places(self,key_1,key_2):

		if key_1 == key_2:
			return

		prev_1 = None
		curr_1 = self.head
		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1
			curr_1 = curr_1.next

		prev_2 = None
		curr_2 = self.head
		while curr_2 and curr_2.data != key_2:
			prev_2 = curr_2
			curr_2 = curr_2.next

		if not curr_1 or not curr_2:
			return

		if prev_1:
			prev_1.next = curr_2
		else:
			self.head  = curr_2

		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1

		curr_1.next, curr_2.next = curr_2.next, curr_1.next

	def reverse_iterative(self):

		prev = None
		curr_node = self.head

		while curr_node:
			nxt = curr_node.next
			curr_node.next = prev
			prev = curr_node
			curr_node = nxt
		self.head = prev

	def reverse_recursive(self):

		def _reverse_recursive(curr, prev):

			if not curr:
				return prev

			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt
			return _reverse_recursive(curr, prev)

		self.head = _reverse_recursive(curr = self.head, prev = None)

	def merge_sorted(self, other_list):

		p = self.head
		q = other_list.head
		s = None

		if not p:
			return q
		if not q:
			return p

		if p and q:

			if p.data <= q.data:
				s = p
				p = s.next
			else:
				s = q
				q = s.next

			new_head = s

		while p and q:

			if p.data <= q.data:
				s.next = p
				s = p
				p = s.next
			else:
				s.next = q
				s = q
				q = s.next

		if not p:
			s.next = q
		if not q:
			s.next = p

		return new_head

	def remove_duplicates(self):

		curr = self.head
		prev = None
		non_duplicates = dict()

		while curr:
			if curr.data in non_duplicates:
				prev.next = curr.next
				curr = None
			else:
				non_duplicates[curr.data] = 1
				prev = curr
			curr = prev.next

	def print_nth_from_last(self, n):
		
		total_length = self.len_iterative()

		curr = self.head
		while curr:
			if total_length == n:
				print(curr.data)	
			total_length -= 1
			curr = curr.next
		# if curr is None:
		# 	return

	def count_occurences_iterative(self, data):

		count = 0
		curr = self.head
		while curr:
			if curr.data == data:
				count += 1
			curr = curr.next
		return count

	def count_occurences_recursive(self, node, data):

		if not node:
			return 0
		if node.data == data:
			return 1 + self.count_occurences_recursive(node.next, data)
		else:
			return self.count_occurences_recursive(node.next, data)

	def rotate_at_pivot(self, k):

		if self.head and self.head.next:
			p = self.head
			q = self.head
			prev = None
			count = 0

			while p and count < k:
				prev = p
				p = p.next
				q = q.next
				count += 1
			p = prev

			while q:
				prev = q
				q = q.next
			q = prev

			q.next = self.head
			self.head = p.next
			p.next = None