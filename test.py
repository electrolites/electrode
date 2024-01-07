from electrode.gui import window, keyboard
from accessible_output2.outputs.auto import Auto

def main():
	w=window.Window("test input")
	speaker=Auto()
	k=keyboard.Keyboard()
	w.show()
	while True:
		k.push()
		if k.keyHolding(k.keyConstants.key_a): speaker.speak("pressed")

main()