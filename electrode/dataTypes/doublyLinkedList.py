"""
Doubly linked list for electrode.
"""

class Node:
	def __init__(self, data, next: Node | None = None, prev: None|Node=None):
		self.data=data
		self.next=next
		self.prev=prev

class LinkedList:
	def __init__(self, initialData: tuple):
		self.head=None
		self.tail=None
		self.length=0
		for i in initialData:
			self.append(i)

	def getNode(self, index):
		if index<0 or index>self.length: raise IndexError('Linked list index out of range.')
		if index==0: return self.head
		if index==self.length: return self.tail
		current=self.head
		for i in range(index -1):
			current=current.next
			if not i==index-1: continue
			return current.next

	def incert(self, data, index):
		if index==self.length:
			self.append(data)
			return
		node=Node(data)
		if index==0:
			if self.head is not None:
				node.next=self.head
				self.head.prev=node
			self.head=node
			self.length+=1
			return
		current = self.head
		for i in range(index -1):
			current=current.next
			if not i==index -1: continue
			node.next=current.next
			node.prev=current
			current.next=node
		self.length+=1

	def append(self, data):
		node=Node(data)
		if self.head is None: self.head=node
		if self.tail is not None:
			self.tail.next=node
			node.prev=self.tail
		self.tail=node
		self.length+=1

	def index(self, data):
		current=self.head
		for i in range(self.length):
			if current.data==data: return i
			current=current.next
		raise ValueError(f'{data} is not in linked list.')

	def remove(self, index):
		if index<0 or index>self.length: raise IndexError('Linked list index out of range.')
		if index==0:
			self.head=self.head.next
			return
		current=self.head
		for i in range(index -1):
			if not  i==index -1: continue
			current.next=current.next.next
			current.next.prev=current
			current=current.next
		self.length-=1

	def __str__(self):
		if self.head is None: return '[]'
		llstr=f'[{self.head.data}'
		current=self.head.next
		for i in range(self.length-1):
			llstr+=f',{current.data}'
			current=current.next
		llstr+=f'{self.tail}]'
		return llstr