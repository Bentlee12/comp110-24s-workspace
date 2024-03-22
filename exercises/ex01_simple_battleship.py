"""EX01-Simple Battleship- A cute step toward Battleship."""

__author__ = "730463172"

player1_input: str = input("Pick a secret boat location between 1 and 4:")
player1_number: int = int(player1_input)
if player1_number > 4:
    print("Error!,too high!")
    exit()
if player1_number < 1:
    print("Error!,too low!")
    exit()
player2_input: str = input("Guess a number between 1 and 4:")
player2_number: int = int(player2_input)
if player2_number > 4: 
    print("Error!,too high!")
    exit()
if player2_number < 1:
    print("Error!,too low!")
    exit()   


BLUE_BOX: str = "\U0001F7E6" 
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
emoji_boxes: str = BLUE_BOX

if player2_input == player1_input:
    emoji_boxes = RED_BOX
if player1_input != player2_input:
    emoji_boxes = WHITE_BOX

results = ""

if player2_number == 1:
    results = results + emoji_boxes
else:
    results += BLUE_BOX
if player2_number == 2:
    results = results + emoji_boxes
else:
    results += BLUE_BOX
if player2_number == 3:
     results = results + emoji_boxes
else:
    results += BLUE_BOX
if player2_number == 4:
    results = results + emoji_boxes
else:
    results += BLUE_BOX

print(results)
 
if player2_input != player1_input:
    print("Incorrect! You missed the ship.")
if player2_input == player1_input:
    print("Correct! You hit the ship.")
    

