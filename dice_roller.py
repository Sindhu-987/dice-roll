import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown():
    for i in range(3, 0, -1):
        clear()
        print(f"Rolling in... {i}")
        time.sleep(1)

def roll_dice():
    clear()
    print("🎲 Rolling the dice", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()
    result = random.randint(1, 6)
    dice_faces = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }
    print(f"You rolled a {result} {dice_faces[result]}")

while True:
    input("Press Enter to roll the dice (or type 'q' and press Enter to quit): ")
    if input().lower() == 'q':
        print("Goodbye!")
        break
    countdown()
    roll_dice()
