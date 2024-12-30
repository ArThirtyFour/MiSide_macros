from time import sleep
from pynput.mouse import Listener ,Button
import keyboard


def esc():
    keyboard.press('esc')  
    keyboard.release('esc')
    sleep(0.1)  
    keyboard.press('esc')  
    keyboard.release('esc')


def button_macros(button):
    while True:
        event = keyboard.read_event()  
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == button:
                esc()

def check_mouse(num):
    klavisha = num

    def on_click(x, y, button, pressed):
        if pressed and button == klavisha:
            esc()
    
    with Listener(on_click=on_click) as listener:
        listener.join()

