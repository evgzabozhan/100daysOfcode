import random

man_choose  = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock,paper,scissors]
comp_choose = random.randint(0,len(rock_paper_scissors)-1)
print(f"You \n {rock_paper_scissors[man_choose]}")
print(f"comp choose {rock_paper_scissors[comp_choose]}")

if (man_choose == comp_choose) :
    print("draw")
elif (man_choose == 0) :
    if (comp_choose == 1) :
        print("you lose")
    else:
        print("you win")
elif (man_choose == 1) :
    if (comp_choose == 0) :
        print("you win")
    else:
        print("you lose")
elif (man_choose == 2) :
    if (comp_choose == 0) :
        print("you lose")
    else:
        print("you win")
else:
    print("Write number from 0 to 2")

