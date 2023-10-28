import pydirectinput
import keyboard
import threading
import time
import random

# Flags to control spacebar and movement
simulate_spacebar = False
simulate_e = False
simulate_s = False

# Function to simulate pressing the spacebar repeatedly
def press_spacebar():
    while simulate_spacebar:
        pydirectinput.press('space')
        pydirectinput.keyDown('a')
        time.sleep(0.5)
        pydirectinput.keyUp('a')
        pydirectinput.press('space')
        pydirectinput.keyDown('d')
        time.sleep(0.1)
        pydirectinput.keyUp('d')
        pydirectinput.press('space')
        pydirectinput.keyDown('a')
        time.sleep(0.8)
        pydirectinput.keyUp('a')
        pydirectinput.press('space')
        pydirectinput.press('space')
        pydirectinput.keyDown('a')
        time.sleep(0.5)
        pydirectinput.keyUp('a')
        pydirectinput.press('space')
        pydirectinput.keyDown('d')
        time.sleep(0.1)
        pydirectinput.keyUp('d')
        pydirectinput.press('space')
        pydirectinput.keyDown('a')
        time.sleep(0.8)
        pydirectinput.keyUp('a')
        pydirectinput.press('space')
        pydirectinput.keyDown('d')
        time.sleep(3)
        pydirectinput.keyUp('d')
        pydirectinput.keyDown('w')
        pydirectinput.keyDown('d')
        time.sleep(1.5)
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('d')
        pydirectinput.press('space')
        pydirectinput.keyDown('d')
        time.sleep(0.3)
        pydirectinput.keyUp('d')
        pydirectinput.press('space')
        pydirectinput.keyDown('d')
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        time.sleep(0.5)
        pydirectinput.press('space')
        pydirectinput.press('d')
        pydirectinput.keyDown('d')
        time.sleep(20)
        pydirectinput.keyUp('d')
        pydirectinput.press('space')
        pydirectinput.press('a')
        pydirectinput.press('space')
        pydirectinput.press('a')
        pydirectinput.keyDown('a')
        time.sleep(17)
        pydirectinput.keyUp('a')
        pydirectinput.press('space')
        pydirectinput.press('d')
        pydirectinput.press('space')
        pydirectinput.keyDown('a')
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        time.sleep(2)
        pydirectinput.keyUp('a')
        pydirectinput.keyDown('w')
        pydirectinput.keyDown('a')
        time.sleep(1.8)
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('a')
        pydirectinput.keyDown('d')
        time.sleep(0.5)
        pydirectinput.keyUp('d')
        time.sleep(5)



def press_e():
    while simulate_e:
        pydirectinput.press('e')      
def press_s():
    while simulate_s:
        pydirectinput.click(684,287)
        time.sleep(random.uniform(0.4,3))  

# Start the spacebar simulation when 'x' is pressed
def start_spacebar_simulation(e):
    global simulate_spacebar
    global simulate_e
    global simulate_s
    simulate_s = True
    simulate_e = True
    simulate_spacebar = True
    threading.Thread(target=press_s).start()
    threading.Thread(target=press_e).start()
    threading.Thread(target=press_spacebar).start()


# Stop the spacebar simulation when 'c' is pressed
def stop_spacebar_simulation(e):
    global simulate_spacebar
    global simulate_e
    global simulate_s
    simulate_s = False
    simulate_e = False
    simulate_spacebar = False

# Register the hotkeys
keyboard.on_press_key('x', start_spacebar_simulation)
keyboard.on_release_key('c', stop_spacebar_simulation)


# Run the program indefinitely
while True:
    pass
  
