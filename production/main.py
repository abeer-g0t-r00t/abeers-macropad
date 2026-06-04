import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# 3 switches wired direct-to-GND: SW1 -> D10, SW2 -> D9, SW3 -> D8
keyboard.matrix = KeysScanner(
    pins=[board.D10, board.D9, board.D8],
    value_when_pressed=False,
)

# SW1 = Copy (Ctrl+C), SW2 = Paste (Ctrl+V), SW3 = Cut (Ctrl+X)
keyboard.keymap = [
    [KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.X)],
]

if __name__ == "__main__":
    keyboard.go()