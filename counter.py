import time
import keyboard

count = int(input("Enter any integer : "))
#inputint = int(inputint)

def counter (count):

    i = 0
    while i < count:
        
        time.sleep(1)
        i = i + 1
        print(i)
        
        if keyboard.is_pressed(' '):
            break

counter(count)
