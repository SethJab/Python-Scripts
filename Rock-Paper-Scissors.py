import random

t = ['rock','paper','scissors']
computer = t[random.randint(0,2)]
player = False

while player == False:
    player = input('Rock, Paper, Scissors? >')
    if player == computer:
        print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('You Lose!',computer,'Covers',player)
        else:
            print("You win!",player,'Smashes', computer)
    elif player == 'paper':
        if computer == 'scissors':
            print('You Lose!',computer,'Cut',player)
        else:
            print("You win!",player,'Covers', computer)
    elif player == 'scissors':
        if computer == 'rock':
            print('You Lose!',computer,'Smashes',player)
        else:
            print("You win!",player,'Cut', computer)
    else:
        print('That is not a valid play.(check spelling)')
    player = False
    computer = t[random.randint(0,2)]
