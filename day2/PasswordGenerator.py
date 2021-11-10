import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

chars = [letters, numbers, symbols]

command = input("Нажмите g если хотите получить пароль\n")
password_list = []
password_len = random.randint(8, 12)

if command == "g":
    for char in range(1, round(password_len)):
        number = random.randint(0, len(chars) - 1)
        password_list.append(random.choice(chars[number]))

random.shuffle(password_list)

print("".join(password_list))
