"""Functional Battleship."""

__author__ = "730463172"


def input_guess(Gridsize: int, spec: str) -> int:
    """Defining Input Guess."""
    assert spec == "row" or spec == "column"
    row_guess: int = int(input(f"Guess a {spec}: "))
    
    run = True 
    while run is True:  
        if row_guess <= 0 or row_guess > Gridsize:
            row_guess = int(input(f"The grid is only {Gridsize} by {Gridsize}. Try again: "))
        else:
            return row_guess
        

BLUE_BOX: str = "\U0001F7E6" 
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
emoji_boxes: str = BLUE_BOX


def print_grid(Gridsize: int, rowguess: int, columnguess: int, userguess: bool) -> None:
    """Printing Grid."""
    row_counter: int = 1
    if userguess is True:
        emoji_boxes = RED_BOX
    else:
        emoji_boxes = WHITE_BOX    

    while row_counter <= Gridsize:
        results = ""
        column_counter = 1 
        if rowguess == row_counter:
            while column_counter <= Gridsize:
                if columnguess == column_counter:
                    results = results + emoji_boxes
                else:
                    results += BLUE_BOX
                column_counter += 1
        else:
            while column_counter <= Gridsize:
                results += BLUE_BOX
                column_counter += 1
        print(results)
        row_counter += 1


def correct_guess(secretrow: int, secretcolumn: int, rowguess: int, columnguess: int) -> bool:
            """Correct guess docstring."""
            if rowguess == secretrow and columnguess == secretcolumn:
                return True
            return False


def main(gridsize: int, secretrow: int, secretcolumn: int) -> None:
    """Defining Main."""
    turn_counter = 1
    while turn_counter <= 5:
        print(f"=== Turn {turn_counter}/5 === ")
        row_guess: int = input_guess(gridsize, "row") 
        column_guess: int = input_guess(gridsize, "column")
        guess: bool = correct_guess(secretrow, secretcolumn, row_guess, column_guess)
        
        if guess is True:
            print_grid(gridsize, row_guess, column_guess, guess)
            print("Hit!")
            print(f"You won in {turn_counter}/5 turns!")
            turn_counter = 6
        else:
            print_grid(gridsize, row_guess, column_guess, guess)
            print("Miss!")
            turn_counter += 1
    print("X/5 - Better luck next time!")