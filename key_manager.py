import datetime
import json
import os
from win32gui import GetWindowText, GetForegroundWindow


class KeyManager:
    def __init__(self, buffer_size:int = 10) -> None:
        self.active_keys = {}
        self.active_buttons = {}
        self.buffer_size = buffer_size
        self.buffer = []
        self.file_name = str(datetime.datetime.now().date())
        self.moves = 0

    def add_move(self, x, y):

        self.moves += 1
        if not (self.moves % 30 == 0):
            return
        
        self.moves = 0
        
        move = {"position":(x, y), "time":str(datetime.datetime.now())}

        if len(self.active_buttons) == 0:
            self.output(move)

        for key in self.active_buttons:
            if not "moves" in self.active_buttons[key]:
                self.active_buttons[key]["moves"] = []
            self.active_buttons[key]["moves"].append(move)

    def add_scroll(self, x, y, dx, dy):

        key_event = {
            "button": "Scroll",
            "start" : str(datetime.datetime.now()),
            "window": GetWindowText(GetForegroundWindow()),
            "start_position": (x, y),
            "scroll_vector": (dx, dy)
        }

        self.output(key_event)

    def add_click(self, button, x, y):

        if button in self.active_keys:
            return
        
        self.active_buttons[button] = {
            "start" : str(datetime.datetime.now()),
            "window": GetWindowText(GetForegroundWindow()),
            "start_position": (x, y)
        }    

    def end_click(self, button, x, y):

        if button in self.active_buttons:
            button_event = self.active_buttons.pop(button)
            button_event["end"] = str(datetime.datetime.now())
            button_event["end_position"] = (x, y)
            button_event["button"] = button

            self.output(button_event)

    def add_key(self, key):

        if key in self.active_keys:
            return
        
        self.active_keys[key] = {
            "start" : str(datetime.datetime.now()),
            "window": GetWindowText(GetForegroundWindow())
        }

    def end_key(self, key):

        if key in self.active_keys:
            key_event = self.active_keys.pop(key)
            key_event["end"] = str(datetime.datetime.now())
            key_event["key"] = key

            self.output(key_event)
        
    def output(self, dictionary:dict):

        self.buffer.append(dictionary)

        if len(self.buffer) >= self.buffer_size:
            self.write_jsonl()

    def write_jsonl(self):
        dicts:list[dict] = self.buffer
        self.buffer = []

        output_dir = f"..\\output"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_path = output_dir + f"\\{self.file_name}.jsonl"    

        with open(output_path, mode="a") as file:
            for item in dicts:
                line = json.dumps(item) + "\n"
                file.write(line)