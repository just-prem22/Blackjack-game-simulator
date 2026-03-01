import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(CARDS)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a Draw."

    if user_score == 0:
        return "Congratulations! You won with a Blackjack."

    if computer_score == 0:
        return "You Lose. Computer has a Blackjack."

    if user_score > 21 and computer_score > 21:
        return "Both went over. It's a Draw."

    if user_score > 21:
        return "You went over. You Lose."

    if computer_score > 21:
        return "Computer went over. You Win!"

    if user_score > computer_score:
        return "You Win!"

    return "Computer Wins."


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print("\nYour cards:", user_cards, "| Current score:", user_score)
        print("Computer's first card:", computer_cards[0])

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n----- Final Result -----")
    print("Your final hand:", user_cards, "| Final score:", user_score)
    print("Computer final hand:", computer_cards, "| Final score:", computer_score)
    print(compare(user_score, computer_score))


def main():
    while input("\nDo you want to play Blackjack? Type 'yes' to play: ").lower() == "yes":
        print("\n" * 30)
        play_game()


if __name__ == "__main__":
    main()
