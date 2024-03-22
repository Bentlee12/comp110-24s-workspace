"""One Shot Battleship."""
__author__ = "730463172"

Grid_Size: int = 4
Secret_Row: int = 3
Secret_Column: int = 2

row_guess: int = int(input("Guess a row: "))

while row_guess < 0 or row_guess > Grid_Size:
    row_guess = int(input("The grid is only 4 by 4. Try again: "))

column_guess: int = int(input("Guess a column: "))

while column_guess > Grid_Size or column_guess < 0:
    column_guess = int(input("The grid is only 4 by 4. Try again: "))

BLUE_BOX: str = "\U0001F7E6" 
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
emoji_boxes: str = BLUE_BOX

if row_guess == Secret_Row and column_guess == Secret_Column:
    emoji_boxes = RED_BOX

if row_guess != Secret_Row or column_guess != Secret_Column:
    emoji_boxes = WHITE_BOX


row_counter: int = 1

while row_counter <= Grid_Size:
    results = ""
    column_counter = 1 
    if row_guess == row_counter:
        while column_counter <= Grid_Size:
            if column_guess == column_counter:
                results = results + emoji_boxes
            else: results += BLUE_BOX
            column_counter += 1
    else:
        while column_counter <= Grid_Size:
            results += BLUE_BOX
            column_counter += 1
    print(results)
    row_counter += 1
        

if row_guess == Secret_Row and column_guess != Secret_Column:
    print("Close! Correct row, wrong column.")

if row_guess != Secret_Row and column_guess == Secret_Column:
    print("Close! Correct column, wrong row.")

if column_guess != Secret_Column and row_guess != Secret_Row:
    print("Miss!")

if column_guess == Secret_Column and row_guess == Secret_Row:
    print("Hit!")