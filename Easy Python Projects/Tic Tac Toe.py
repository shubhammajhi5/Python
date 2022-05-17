# function to display the board
def displayBoard(board):
    print(board.get('TL', ' '), '|', board.get('TM', ' '), '|', board.get('TR', ' '))
    print('--+---+--')
    print(board.get('ML', ' '), '|', board.get('MM', ' '), '|', board.get('MR', ' '))
    print('--+---+--')
    print(board.get('BL', ' '), '|', board.get('BM', ' '), '|', board.get('BR', ' '))

# initialising the board data
board = {'TL':' ', 'TM':' ', 'TR':' ',
         'ML':' ', 'MM':' ', 'MR':' ',
         'BL':' ', 'BM':' ', 'BR':' '}


print('********* WELCOME TO MY TIC-TAC-TOE GAME *********')
displayBoard(board)
print('Lets begin the Game !!!')

turn = 'X'

for i in range(9):
    print(f"\n{turn}'s turn. Enter the position where you want to place your move ?")
    move = input().upper()

    # to check valid move
    while move not in board:
        displayBoard(board)
        print(f'Player {turn}...! Kindly enter valid move only !!!')
        print('Valid moves -> ', list(board.keys()))
        move = input().upper()

    # to check moves are not getting over written
    while board[move] != ' ':
        displayBoard(board)
        print(f'Player {turn}...! Over writing the moves not allowed, Please enter valid move only !!!')
        move = input().upper()

    # implementing the move
    board[move] = turn
    displayBoard(board)

    # condition for X winning the game
    if board['TL'] == board['TM'] == board['TR'] == 'X' or \
       board['ML'] == board['MM'] == board['MR'] == 'X' or \
       board['BL'] == board['BM'] == board['BR'] == 'X' or \
       board['TL'] == board['ML'] == board['BL'] == 'X' or \
       board['TM'] == board['MM'] == board['BM'] == 'X' or \
       board['TR'] == board['MR'] == board['BR'] == 'X' or \
       board['TL'] == board['MM'] == board['BR'] == 'X' or \
       board['TR'] == board['MM'] == board['BL'] == 'X':

       print('\nX Won the Game !!!\n')
       break

    # condition for O winning the game
    elif board['TL'] == board['TM'] == board['TR'] == 'O' or \
         board['ML'] == board['MM'] == board['MR'] == 'O' or \
         board['BL'] == board['BM'] == board['BR'] == 'O' or \
         board['TL'] == board['ML'] == board['BL'] == 'O' or \
         board['TM'] == board['MM'] == board['BM'] == 'O' or \
         board['TR'] == board['MR'] == board['BR'] == 'O' or \
         board['TL'] == board['MM'] == board['BR'] == 'O' or \
         board['TR'] == board['MM'] == board['BL'] == 'O':

         print('\nO Won the Game !!!\n')
         break

    # condition when nobody wins
    elif i == 8:
        print('\nGame Drawn !!!\n')
       
    # changing the turn         
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'



# final see off
print('Thank you for Playing Tic Tac Toe, \nHope to see you playing again soon... !!!')