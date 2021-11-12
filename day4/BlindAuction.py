import os

print("Welcome to the secret auction program.")

bidders = {}


def add_bidders():
    name = input("What is your name? : ")
    bid = int(input("What's your bid? : "))
    bidders[name] = bid


def find_max_key(dictionary):
    max_key = max(dictionary, key=dictionary.get)
    return max_key


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


add_bidders()

while input("Are there any other bidders?").lower() == "yes":
    clear()
    add_bidders()

winner = find_max_key(bidders)

print(f"The winner is {winner} with a bid of ${bidders[winner]}")
