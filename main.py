from card import *

game=GameInit()

first_row=game.generate_first_row()

player1=Player()

end_turn=False

while end_turn == False:

    take_action=int(input("Choisissez une action: "))

    if take_action == 1:
        player1.take_card(first_row)
        

    elif take_action == 2:
        player1.take_card_in_hand(first_row)
        
    end_turn= True
