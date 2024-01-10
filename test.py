from electrode.gui.window import Window
from electrode.gui.elements import input
import wx


def main():
	window=Window("test")
	window.adInput("this is a text fealed")
	window.adCheckBox("test your box", initialState=2, threeWay=True)
	window.adButton("test your button", buttonTest)
	window.show()
	window.app.MainLoop()

def buttonTest(event):
	print(event)


main()