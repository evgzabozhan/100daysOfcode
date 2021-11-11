alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type tour message:\n").lower()
shift_number = int(input("Type the shift number:\n"))


def get_index(character):
    return int(alphabet.index(character))


def encryption(text, number):
    for num in range(0, int(len(text))):
        text[num] = alphabet[(get_index(text[num]) + number) % len(alphabet)]
    return "".join(text)


def decryption(text, number):
    for num in range(0, int(len(text))):
        text[num] = alphabet[(get_index(text[num]) - number) % len(alphabet)]
    return "".join(text)


if action == "encode":
    print("The encoded text is : " + encryption(list(message), shift_number))
elif action == "decode":
    print("The encoded text is : " + decryption(list(message), shift_number))
else:
    print("Wrong action!!!")
