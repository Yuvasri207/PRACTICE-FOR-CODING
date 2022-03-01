import random
print("WELCOME ROCK,PAPER,SCISSORS GAME")
print('its your turn')
print('Enter choice \n 1 for Rock\n 2 for Paper\n 3 for Scissors')
user=int(input('enter the choice please'))
if user==1:
    choice='Rock'
elif user==2:
    choice='Paper'
else:
    choice='Scissors'
print('your choice is:',choice)
print('now its a computer choice')
computer=(input(random.randint(1,3)))
if computer==1:
    choice='Rock'
elif computer==2:
    choice='Paper'
else:
    choice='Scissors'
print('computer choice is:',choice)
print('the winner is')
if user==1 and computer==2 or user==2 and computer==1:
    print('Paper wins')
    result='Paper'
elif user==1 and computer==3 or user==3 and computer==1:
    print('Rock wins')
    result='Rock'
else:
    print('Scissor wins')
    result='Scissor'
if result==choice:
    print('user wins')
else:
    print('computer wins')
print('THANKS FOR PLAYING')



