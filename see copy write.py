import keyboard
import time
import random


def file_write_out(fileName, delay):
    key_presses = []
    f = open(fileName+'.txt', 'r')
    keyboard.wait('esc')
    with open(fileName+'.txt') as fileobj:
        for line in fileobj:
            for ch in line:
                try:
                    if ch == '!' or ch == '"' or ch == '£' or ch == '$' or ch == '(' or ch == ')'or ch == '%'or ch == '^'or ch == '&'or ch == '*'or ch == ':'or ch == '?':
                        keyboard.press('shift')
                        keyboard.press(ch)
                        time.sleep(delay)
                        keyboard.release(ch)
                        keyboard.release('shift')
                    if ch.isupper():
                        keyboard.press('shift')
                        keyboard.press(ch.lower())
                        time.sleep(delay)
                        keyboard.release(ch.lower())
                        keyboard.release('shift')
    ##                if ch == '’':
    ##                    keyboard.press("'")
    ##                    time.sleep(delay)
    ##                    keyboard.release("'")
                    else:
                        keyboard.press(ch)
                        time.sleep(delay)
                        keyboard.release(ch)
                except:
                    print('error:' + ch)
def main():
    wpm = 215
    delay = 1/((wpm/60)*5)
    gogogadget = 1
    while gogogadget:
        fileName = input('please enter the name of the file to write out(Q for quit)')
        if fileName =='Q':
            gogogadget = 0
        else:
            file_write_out(fileName, delay)
    

if __name__ == "__main__":
    main()
