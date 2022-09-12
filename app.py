import os
import speech_recognition as sr
import pyautogui

# get audio from the microphone                                                                       
r = sr.Recognizer()   

while True:
    with sr.Microphone() as source:                                                                       
        print("Speak:")       
        r.adjust_for_ambient_noise(source)                                                                            
        audio = r.listen(source)   

    try:
        txt = r.recognize_google(audio)

        print(">>" + txt)

        if txt == 'right':
            print('go right!!')
            pyautogui.move(30, 0)
        elif txt == 'left' or txt == 'lift':
            print('go left!!')
            pyautogui.move(-30, 0)
        elif txt == 'top' or txt == 'up' or txt == 'stop':
            print('go top!!')
            pyautogui.move(0, -30)
        elif txt == 'down' or txt == 'Darwin':
            print('go Down!!')
            pyautogui.move(0, 30)
        elif txt == 'go left' or txt == 'go lift':
            pyautogui.move(-50, 0)
        elif txt == 'go right':
            pyautogui.move(50, 0)
        elif txt == 'lumos':#Harry potter
            os.system('color 70')
        elif txt == 'nox' or txt == 'Knox':#Harry potter
            os.system('color 07')
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))