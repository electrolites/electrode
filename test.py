from electrode.gui.window import Window
from electrode.gui.elements import input
import wx

def main():
	window=Window("test")
	window.show()
	window.addInput("this is a text fealed")
	window.app.MainLoop()


main()