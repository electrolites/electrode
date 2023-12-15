"""
Binary tree class for electrode.
"""

class BinTreeNode:
	def __init__(self, data, left: None | BinTreeNode = None, right: None | BinTreeNode = None):
		self.data=data
		self.left=left
		self.right=right

	def addChild(self, data):
		if data==self.data: return
		if data < self.data:
			if self.left is not None: self.left.addChild(data)
			else: self.left=BinTreeNode(data)
		else:
			if self.right is not None: self.right.addChild(data)
			else: self.right=BinTreeNode(data)

	def exists(self, data):
		if data == self.data: return True
		if data<self.data:
			if self.left is not None: return self.left.exists(data)
			else: return False
		if data>self.data:
			if self.right is not None: return self.right.exists(data)
			else: return False

	def inOrderTraversal(self):
		elements=[]
		if self.left is not None:
			elements+=self.left.inOrderTraversal()
		elements.append(self.data)
		if self.right is not None:
			elements+=self.right.inOrderTraversal()
			return elements

	def delete(self, data):
		if data<self.data:
			if self.left is not None: self.left=self.left.delete(data)
		elif data>self.data:
			if self.right is not None: self.right.delete(data)
		else:
			if self.left is None and self.right is None: return None
			elif self.left is None: return self.right
			elif self.right is None: return self.left
			maxValue = self.left.max()
			self.data=maxValue
			self.left=self.left.delete(maxValue)
		return self

	def max(self):
		if self.right is None:
			return self.data
		return self.right.max()

	def min(self):
		if self.left is None:
			return self.data
		return self.left.min()