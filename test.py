from electrode.gui.window import Window
from electrode.gui.elements import input
import wx

def main():
	window=Window("test")
	window.show()
	window.adInput("this is a text fealed")
	window.adCheckBox("test your box", initialState=2, threeWay=True)
	window.app.MainLoop()


main()