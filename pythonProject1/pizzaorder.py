import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
paper = ''' _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
images = [paper, rock, scissor]

user_choice = int(input("enter your choice 0 for rock 1 for scissors and 2 for paper: "))
if 3 > user_choice >= 0:
    print(images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f'computer choose {computer_choice}')
    print(images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("you win")
    elif user_choice == 2 and computer_choice == 0:
        print("you loose")
    elif user_choice > computer_choice:
        print("you win")
    elif user_choice < computer_choice:
        print("you loose")
    elif computer_choice == user_choice:
        print("Its a draw")
else:
    print("invalid number,you loose")
