import random

word_list = ["Hello", "Share", "Testing"]
hidden_word = list(random.choice(word_list))
death = 0
att = 10


def hidden_word_spaces(word):
    word_spaces = []
    for i in word:
        word_spaces.append("_")

    return word_spaces

def char_number_in_word (word, user_char):
    if word.count(char):
        return word.index(user_char)


word_spaces = hidden_word_spaces(hidden_word)
while death != 10 and word_spaces.count("_"):
    char = input("Write your char :\n")
    if hidden_word.count(char):
        word_spaces[int(hidden_word.index(char))] = char
        print("".join(word_spaces))
    else:
        death += 1
        att -= 1
        print(f"Noup, attempts : {att}")

if word_spaces.count("_"):
    print("You death, lol")
else:
    print(f"You win!!! Word {hidden_word}")