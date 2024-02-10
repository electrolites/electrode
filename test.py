from electrode.gui.window import Window
from electrode.events.event import eventManager
import time
from typing import Protocol, runtime_checkable
import asyncio
progress = 0
manager = eventManager()

async def main():
	global progress
	await manager.register("start", startEvent)
	await manager.subscribe("start", onStartEvent)
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
	await manager.postEvent("start", time = time.time(), something = "this is a dumb statement")
	await window.app.MainLoop()


def buttonTest(event):
	print(event)

def sliderTest(event):
	global progress
	value = event.GetEventObject().GetValue()
	print(value)
	progress.SetValue(value)

@runtime_checkable
class startEvent(Protocol):
	time: float
	something: str

async def onStartEvent(event):
	print(f'application started at {event["time"]}, with a string thing of {event["something"]}')


asyncio.run(main())