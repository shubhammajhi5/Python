# Computer Guess
from random import randint
comp = randint(0,9)

# User Valid Guess
while True:
    player = int(input('Enter a Random number between 0 - 9 : '))
    if player in range(10):
        break

# User guess if not equal to comp and counting the number of guesses of user
n = 1
while comp != player :
    if comp > player:
        player = int(input('Too small, Enter a higher Number : '))
    elif comp < player:
        player = int(input('Too large, Enter a smaller Number : '))

    n += 1

# printing the results
print(f'\nComputer chose : {comp}')
print(f'You chose : {player}')
print(f'\nYou Guessed the correct number in {n} guesses')

# checking for highscore
with open('hiscore.txt', 'r') as f:
    hiscore = int(f.read())

if n < hiscore:
    print('Congratulations !!! You have achieved a highscore')
    with open('hiscore.txt', 'w') as f:
        f.write(str(n))