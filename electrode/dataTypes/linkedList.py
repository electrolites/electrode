"""
Singly linked list for electrode.
"""

class Node:
	def __init__(self, data, next: Node | None = None):
		self.data=data
		self.next=next

class linkedList:
	def __init__(self, initialData: tuple):
		self.head=None
		self.tail=None
		self.length=0
		for i in initialData:
			self.append(i)

	def incert(self, data, index):
		if index<0 or index>self.length: raise IndexError('Linked list index out of range.')
		if index==self.length:
			self.append(data)
			return
		if index==0:
			self.head = Node(data, next = self.head)
			self.length+=1
			return
		current = self.head
		node=Node(data)
		for i in range(index -1):
			current=current.next
			if not i==index -1: continue
			node.next=current.next
			current.next=node
		self.length+=1

	def append(self, data):
		node=Node(data)
		if self.head is None: self.head=node
		if self.tail is not None: self.tail.next=node
		else: self.tail=node
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