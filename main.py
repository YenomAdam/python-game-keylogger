from pynput import keyboard
from pynput import mouse
from key_manager import KeyManager

km = KeyManager(5)
keyboard_listener = None
mouse_listener = None

def on_press(key:keyboard.Key):
    if key == keyboard.Key.pause:
        stop_listeners()

    km.add_key(str(key))
    print("Pressing:", key)

def on_release(key:keyboard.Key):
    km.end_key(str(key))
    print("Released:", key)

def on_move(x, y):
    km.add_move(x, y)
    print("Pointing at:", (x, y))

def on_click(x, y, button:mouse.Button, pressed):
    if pressed:
        km.add_click(str(button), x, y)
    else:
        km.end_click(str(button), x, y)
    action = "Pressed" if pressed else "Released"
    print(action, str(button), "at", (x, y))

def on_scroll(x, y, dx, dy):
    km.add_scroll(x, y, dx, dy)
    direction = "up" if dy>0 else "down"
    print("Scrolled", direction, "at", (x, y), "with vector", (dx, dy))

def start_listeners():
    global keyboard_listener, mouse_listener
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    
    keyboard_listener.start()
    mouse_listener.start()

    keyboard_listener.join()
    mouse_listener.join()

def stop_listeners():
    if keyboard_listener:
        keyboard_listener.stop()
    if mouse_listener:
        mouse_listener.stop()

start_listeners()