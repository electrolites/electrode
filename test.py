from electrode.gui.window import Window
from electrode.gui.elements import input
import wx
progress = 0

def main():
	global progress
	window=Window("test")
	window.adInput("this is a text fealed")
	window.adCheckBox("test your box", initialState=2, threeWay=True)
	window.adButton("test your button", buttonTest)
	window.adSlider("test your slider", 0, 100, 50, onChange=sliderTest)
	window.adComBobox("test", ["ding1", "dong2", "klang3", "clunk4"])
	window.adSpinButton("test your spinner")
	window.adListBox("test your lister", ["ding1", "dong2", "klang3", "clunk4"])
	window.adRadioButtons("test your radios", ["ding1", "dong2", "klang3", "clunk4"])
	progress = window.adProgressBar("test progress")
	tree = window.adTreeView("your a tree climber")
	root=tree.AddRoot("the root of the tree")
	branch1=tree.AppendItem(root,"Branch 1")
	tree.AppendItem(branch1,"leef 1")
	tree.AppendItem(branch1,"leef 2")
	branch2=tree.AppendItem(root,"Branch 2")
	tree.AppendItem(branch2,"leef 3")
	tree.AppendItem(branch2,"leef 4")
	window.show()
	window.app.MainLoop()

def buttonTest(event):
	print(event)

def sliderTest(event):
	global progress
	value = event.GetEventObject().GetValue()
	print(value)
	progress.SetValue(value)


main()