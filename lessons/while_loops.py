"""Demonstrating While Loops by finding low value in string"""

cards: str= "5235"

card_idx: int= int(cards[0])
low_card= cards(0)
# check if current card is less than low card 
while card_idx < 4:
    current_card: int = cards[card_idx]
    card_idx= card_idx+1
    if (current_card< low_card):
        #update the low card to be current card
        low_card=current_card
   
