import pydirectinput
import keyboard
import threading
import time
import random
import pyautogui
import cv2


simulate_spacebar = False
simulate_e = False
simulate_s = False
counter = 0
trade_count= 0
disconnected_count = 0
sign_in_count = 0
refresh_count = 0


def press_spacebar():
    global counter
    global simulate_spacebar
    global simulate_s
    global refresh_count
    global simulate_loot
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
        pydirectinput.press('space')
        pydirectinput.press('space')
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
        counter += 1
        print('counter: ',counter)
        if counter >= 3:
            refresh_count += 1
            print('refresh count: ',refresh_count)
            simulate_s = False
            simulate_spacebar = False
            simulate_loot = False
            pyautogui.hotkey('ctrl', 'r')
            counter = 0
            return counter

def press_loot():
    while simulate_loot:
        pydirectinput.press('e')


def press_e():
    global simulate_spacebar
    global simulate_s  
    global sign_in_count
    global disconnected_count
    global simulate_loot
    while simulate_e:
        if pyautogui.locateOnScreen('disconnected.png', grayscale=True, confidence=0.8) !=None:
            simulate_s = False
            simulate_spacebar = False
            simulate_loot = False
            disconnected_count += 1
            print('disconnected count: ', disconnected_count)
            time.sleep(80)
            pyautogui.hotkey('ctrl', 'r')

        if pyautogui.locateOnScreen('scroll.png', grayscale=True, confidence=0.8) !=None:
            pyautogui.scroll(1)
            print('scrolled')

        if pyautogui.locateOnScreen('Sign-in.png', grayscale=True, confidence=0.8) !=None:
            simulate_s = False
            simulate_spacebar = False
            simulate_loot = False
            pydirectinput.click(272,502)
            pydirectinput.click(272,502) 
            pydirectinput.click(272,502)
            sign_in_count += 1
            print('sign in count: ',sign_in_count)
            pydirectinput.keyDown('d')
            time.sleep(10)
            pydirectinput.keyUp('d')
            time.sleep(1)
            pydirectinput.press('a')
            simulate_s = True
            simulate_spacebar = True
            simulate_loot = True
            threading.Thread(target=press_s).start()
            threading.Thread(target=press_spacebar).start()
            threading.Thread(target=press_loot).start()
            

def press_s():
    global trade_count
    while simulate_s:
        if pyautogui.locateOnScreen('trade.png', grayscale=True, confidence=0.8) !=None:  
            pydirectinput.click(770,257)
            pydirectinput.click(770,257) 
            pydirectinput.click(770,257)
            trade_count += 1
            print('trade count: ',trade_count)



def start_spacebar_simulation(e=None):
    global simulate_loot
    global simulate_spacebar
    global simulate_e
    global simulate_s
    simulate_s = True
    simulate_e = True
    simulate_spacebar = True
    simulate_loot = True
    threading.Thread(target=press_s).start()
    threading.Thread(target=press_e).start()
    threading.Thread(target=press_spacebar).start()
    threading.Thread(target=press_loot).start()



def stop_spacebar_simulation(e):
    global simulate_spacebar
    global simulate_e
    global simulate_s
    global simulate_loot
    simulate_loot = False
    simulate_s = False
    simulate_e = False
    simulate_spacebar = False

keyboard.on_press_key('x', start_spacebar_simulation)
keyboard.on_release_key('c', stop_spacebar_simulation)



while True:
    pass
  
