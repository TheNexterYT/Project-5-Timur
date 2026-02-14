from pygame import *
import json
import os

window_size = 600, 400
window = display.set_mode(window_size)
display.set_caption("Меню зі складностю")
font.init()
main_font = font.Font(None, 36)


filename = "settings.json"
difficulties = ["easy", "normal", "hard"]
current_index = 0

if os.path.exists(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        if data.get("difficulty") in difficulties:
            current_index = difficulties.index(data["difficulties"])
else:
    with open(filename, "w") as f:
        json.dump({"difficulty":  difficulties[0]}, f)

class Button:
    def __init__(self, x, y, width, height, color, text, text_color=(0, 0, 0)):
        self.rect = Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font.Font(None, 28)
