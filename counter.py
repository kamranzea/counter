import argparse
import time
import keyboard

def counter(x):
    for i in range(x):
        if keyboard.is_pressed(' '):
            break
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', type=int, required=True)
    args = parser.parse_args()
    
    counter(args.target)
