import random
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    picked_card=random.choice(cards)
    return picked_card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score,c_score):
    if u_score==c_score:
        return "It's a Draw, You and computer have same score"
    elif c_score > 21 and u_score > 21:
        return "It's a Draw, You and Computer both went over"
    elif u_score > 21:
        return "Lose, You went over"
    elif c_score > 21:
        return "You won Computer went over"
    elif u_score==0:
        return "Congratulations You won with a Blackjack"
    elif c_score==0:
        return "You Lose computer has a Blackjack"
    elif u_score > c_score:
        return "You Won"
    else:
        return "Computer Won"
def play_game():
    user_cards=[]
    computer_score=-1
    user_score=-1
    computer_card=[]
    is_game_over=False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_card)
        print("Your Cards are",user_cards,"And the current sum is",user_score)
        print("Computer first card",computer_card[0])
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to take get another card or Type 'n' to pass ").lower()
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while computer_score!=0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    print("Your final hand is ",user_cards,"And the final score is",user_score)
    print("Computer final hand is",computer_card,"And the final score is",computer_score)
    print(compare(user_score,computer_score))
while input("Do you want to play The Blackjack Game type yes to play ").lower()=="yes":
    print("\n"*25)
    play_game()



