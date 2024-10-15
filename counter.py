import argparse
import time
import keyboard

def hotkey_pressed():
    print("space pressed")
    global counting
    counting = False

def counter(a):
    global counting
    counting = True
    a=0
    while counting:
      print(a)
      a += 1
      time.sleep(1)

#using a hotkey function
keyboard.add_hotkey(' ', hotkey_pressed)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', type=int, required=True)
    args = parser.parse_args()
    
    counter(args.target)
