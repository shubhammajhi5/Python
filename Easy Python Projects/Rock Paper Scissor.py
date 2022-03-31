# Rock, Paper, Scissor Game

print ('\t*** Welcome ***\nLets play Rock, Paper, Scissor\n')


# Game function

def game(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False    
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False    
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False    
    

# Computer Choice 

import random
a = random.randint(1,3)
if a == 1:
    comp = 'r'
elif a == 2:
    comp = 'p'
elif a == 3:
    comp = 's'


# Player Choice

while True:
    you = input("Enter valid choice : Rock(r) Paper(p) Scissor(s)\n") 
    if you in ['r', 'p', 's']:
        break


# Displaying Choices

print(f'You chose {you}')
print(f'Computer chose {comp}')


# Displaying Results

result = game(comp, you)

if result == None:
    print('Its a Tie !!!')
elif result == True:
    print('Congratulations !!! You won...')
else:
    print('Sorry !!! You Lose...')

