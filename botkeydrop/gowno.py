import pyautogui
import pyperclip
from time import sleep

copy = pyperclip.copy("https://key-drop.com/en/giveaways/list")

pyautogui.click(783, 50)
pyautogui.click(783, 50)
pyautogui.click(783, 50)
sleep(2)
pyautogui.keyDown("backspace")
pyautogui.keyUp("backspace")
sleep(2)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("v")
pyautogui.keyUp("ctrl")
pyautogui.keyUp("v")
pyautogui.keyDown("enter")
pyautogui.keyUp("enter")