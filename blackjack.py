def blackjack():

    import random

    cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]

    print("Let's play Blackjack!")

    user_card_1 = random.choice(cards)
    user_card_2 = random.choice(cards)
    user_deck = [user_card_1, user_card_2, ]
    user_deck_sum = sum(user_deck)

    dealer_card_1 = random.choice(cards)
    dealer_card_2 = random.choice(cards)
    dealer_deck = [dealer_card_1, dealer_card_2, ]
    dealer_deck_sum = sum(dealer_deck)

    def draw():
        user_new_card = random.choice(cards)
        user_deck.append(user_new_card)
        user_deck_sum = sum(user_deck)
        print(f"Your new total is {user_deck_sum}.")
        dealer_new_card = random.choice(cards)
        dealer_deck.append(dealer_new_card)
        dealer_deck_sum = sum(dealer_deck)
           
    user_deck_total_message = print(f"You drew a {user_card_1} and a {user_card_2}. Your total is {user_deck_sum}.")
    keep_playing = True
    while keep_playing == True:
        user_draw_ask = input("Would you like to draw a card? y / n: ")
        if user_draw_ask == 'y':
            draw()
            if user_deck_sum > 21:
                keep_playing = False
                print("You lose!")
        if user_draw_ask == 'n':
            keep_playing = False

    if keep_playing == False:
        new_user_deck_sum = sum(user_deck)
        new_dealer_deck_sum = sum(dealer_deck)
        if 11 in user_deck and new_user_deck_sum > 21:
            cards.remove(11)
            cards.append(1)
            new_dealer_deck_sum = sum(dealer_deck)
        elif new_user_deck_sum > 21:
            print(f"Your total is {new_user_deck_sum}. You went over 21. You lose!")
        elif new_dealer_deck_sum > 21:
            print(f"Your total is {new_user_deck_sum}. The dealer's total is {new_dealer_deck_sum}. The dealer went over 21. You win!")
        elif new_user_deck_sum > new_dealer_deck_sum:
            print(f"Your total is {new_user_deck_sum}. The dealer's total is {new_dealer_deck_sum}. You win!")
        elif new_user_deck_sum < new_dealer_deck_sum:
            print(f"Your total is {new_user_deck_sum}. The dealer's total is {new_dealer_deck_sum}. You lose!")
        elif new_user_deck_sum == new_dealer_deck_sum:
            print(f"Your total is {new_user_deck_sum}. The dealer's total is {new_dealer_deck_sum}. It's a draw!")

    play_again = True
    while play_again == True:
        play_again_ask = input("Would you like to play again? y / n: ")
        if play_again_ask == 'y':
            blackjack()
        else:
            play_again = False
            quit()

blackjack()


        
        


    
    
                 
