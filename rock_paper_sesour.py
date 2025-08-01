import random
emogies ={
    's': '✂️',
    'p':'📄',
    'r':'🪨'
}
choices = ("r","p","s")

while True:
    user_choise = input('Enter Rock,Paker,Sesour (r/p/s) :').lower()
    if user_choise not in choices:
        print('Invalid inpur your choise must be (r/p/s)')
        continue

    computer_choice=random.choice(choices)

    print(f'Your choise {emogies[user_choise]}')
    print(f'Computr choise {emogies[computer_choice]}')


    if user_choise == computer_choice:
        print('Its a tie')
    elif (user_choise == 'r' and computer_choice =='s') or (user_choise == 'p' and computer_choice == 's' ) or (user_choise =='p' and computer_choice=='r'):
        print('you win')
    else:
        print("computer wins ")
    on=input('Do you want to continue this game y/n :').lower()
    if on == 'n':
        print("Thank you for plaing")
        break
