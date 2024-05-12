import PySimpleGUI as sg
from time import sleep

giveawaycounter = 0
sg.theme('DarkBlue5')
layout = [
            [sg.Text("Bot na giveawaye keydrop!")],
            [sg.Multiline('Liczba giveawayów do których dolaczono:')],
            [sg.Button("Zacznij dolaczac!")], [sg.Button("Wyjdz")],
         ]
window = sg.Window("Keydrop bot", layout)
while True:
    event, value = window.read()
    if event == "Zacznij dolaczac!":
        sleep(5)
        try:
            pos = pyautogui.locateOnScreen('dolacz.png')
            if pos != None:
                sleep(5)
                pyautogui.keyDown("f5")
                pyautogui.keyUp("f5")
                sleep(5)
                print("Ostatnia data dolaczenia do giveaway'u: ")
                print("Ostatnie dolaczenie do giveaway'a - " + datetime.now().strftime("%H:%M:%S"))
                pyautogui.click(pos[0], pos[1])
                sleep(5)
                pyautogui.click(589, 823)
                sleep(80)
                pyautogui.keyDown("browserback")
                pyautogui.keyUp("browserback")
                sleep(5)
                pyautogui.keyDown("f5")
                pyautogui.keyUp("f5")
                giveawaycounter += 1
                sleep(792)
        except:
            print("image not found")

    if event == "Wyjdz" or event == sg.WINDOW_CLOSED:
        break
        window.close()