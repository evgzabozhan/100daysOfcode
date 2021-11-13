import random

people_dict = {"Antonio": 100, "Irzhi": 300, "Leopold": 150, "Uriah": 200, "Uzul": 250}
score = [0]


def check_answer(answer, value1, value2):
    is_active = True
    if answer == 'A' and value1 > value2 or answer == 'B' and value2 > value1:
        score.append(1)
    else:
        is_active = False
    return is_active


def get_random_values(dictionary):
    values = []
    value1 = random.choice(list(dictionary))
    value2 = random.choice(list(dictionary))
    while value1 == value2:
        value2 = random.choice(list(dictionary))
    values.append(value1)
    values.append(value2)
    return values


while True:
    peoples = get_random_values(people_dict)
    print(f"Compare {peoples[0]}")
    print(f"VS")
    print(f"Compare {peoples[1]}")
    human_answer = input("Type 'A' or 'B' : ").upper()

    if check_answer(human_answer, people_dict.get(peoples[0]), people_dict.get(peoples[1])):
        print(f"You're right! Current score : {sum(score)}")
    else:
        print(f"Sorry, that's wrong. Final score: {sum(score)}")
        break
