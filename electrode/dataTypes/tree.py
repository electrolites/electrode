"""
Tree/tree node class for electrode.
"""

class TreeNode:
	def __init__(self, data, level = 0, parent: None | TreeNode = None):
		self.data=data
		self.level=level
		self.parent=parent
		self.children=[]

	def addChild(self, child: TreeNode):
		child.level=self.level+1
		child.parent=self
		self.children.append(child)

	def removeChild(self, child):
		self.children.remove(child)
		child.parent=None
		child.clearChildren()

	def clearChildren(self):
		for child in self.children:
			if child.children: child.clearChildren()
		self.children.clear()

	def addChildren(self, *childrenToAdd: TreeNode):
		for child in childrenToAdd:
			self.addChild(child)

	def addData(self, data):
		self.children.append(TreeNode(data, level=self.level+1, parent=self))

	def getRootNode(self):
		if self.parent is not None: return self.parent.getRootNode
		return self

	def __str__(self):
		tstr=""
		tstr+=f'{self.getRootNode().data}\n'
		tstr+=self.getRootNode()._getChildrenStr()
		return tstr

	def _getChildrenStr(self):
		cstr=''
		for child in self.children:
			spaces = ' ' * child.level * 2
			cstr+=f'{spaces}{child.data}\n'
			if not child.children: continue
			for c in child.children: cstr+=c._getChildrenStr()