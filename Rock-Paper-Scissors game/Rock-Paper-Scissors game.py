#Basic version

# print('Enter Player-1 choice')
# player1 = input('Rock, Paper or Scissors => ').lower()
# print('Enter Player-2 choice')
# player2 = input('Rock, Paper or Scissors => ').lower()

# if player1 == player2:
#     print('Draw! Try Again')
# elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 =='rock') or (player1 == 'scissor' and player2 =='paper'):
#     print('Player 1 WINS')
# elif (player2 == 'rock' and player1 == 'scissors') or (player2 == 'paper' and player1 =='rock') or (player2 == 'scissor' and player1 =='paper'):
#     print('Player 2 WINS')
# else:
#     print('Enter a valid choice!')


#Advanced version

from random import choice

print('...rock...')
print('...paper...')
print('...scissors...')

player_wins = 0
computer_wins = 0
winning_score = int(input('How many wins you want to play to? '))
while player_wins < winning_score and computer_wins < winning_score:
    print(f'Player score: {player_wins} : {computer_wins} Computer score')
    print('''Please type your choice (rock, paper, scissors):
(Type 'qiut' to stop the game.)''')
    player_move = input().lower()
    if player_move == 'quit':
        break
    computer_move = choice(['rock', 'paper', 'scissors'])
    print(f'Computer plays {computer_move}')

    if player_move in ['rock', 'paper', 'scissors']:
        if player_move == computer_move:
            print('It\`s a tie!')
        elif (player_move == 'rock' and computer_move == 'scissors') or (player_move == 'paper' and computer_move == 'rock'):
            print('Player win!')
            player_wins += 1
        else:
            print('Computer win!')
            computer_wins += 1
    else:
        print('Check your spelling')
print('******************')
if player_wins == winning_score:
    print('Congratulation! You WIN!')
else: print('Sorry. You lost..')
print('Final score: ')
print(f'Player score: {player_wins} : {computer_wins} Computer score')
