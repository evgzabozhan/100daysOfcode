import random


def generate_cards(player, count):
    for i in range(count):
        player.append(cards[random.randint(0, len(cards) - 1)])
    return player


def print_sum(human, comp):
    print(f"Your cards : {human}, current score {sum(man_cards)}")
    print(f"Computer first card : {comp[0]}")


def decision(human, comp):
    print(f"Your final hand : {human} , score : {sum(human)}")
    print(f"Computer's final hand : {comp} , score : {sum(comp)}")
    human_sum = sum(human)
    comp_sum = sum(comp)
    if human_sum == comp_sum:
        print("Draw\n")
    elif human_sum < comp_sum or human_sum > 21:
        print("You lose\n")
    elif comp_sum < human_sum < 21:
        print("You win\n")


while input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n") == "y":

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    man_cards = []
    comp_cards = []
    print_sum(generate_cards(man_cards, 2), generate_cards(comp_cards, 2))

    while input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        generate_cards(man_cards, 1)
        print_sum(man_cards, comp_cards)
        if sum(man_cards) > 21:
            print("Brute force!!!")
            break

    decision(man_cards, comp_cards)

print("Good bye!")
