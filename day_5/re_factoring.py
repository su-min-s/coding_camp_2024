def ask_player_for_input():
    """
    it should take the player name, it should request an input forom that player
    and it should return that input
    """
    pass
    while player1 not in ['rock', 'paper', 'scissors']:
        player1 = input('Player 1, enter rock, paper, or scissors: ')
    player2 = ''
    while player2 not in ['rock', 'paper', 'scissors']:
        player2 = input('Player 2, enter rock, paper, or scissors: ')


def get_round_outcome(player1, player2, name1='player1', name2='player2'):
    """
    Given two players (one for the first player and one for the second one)
    it returns what is the outcome of the round (player who won or 'tie').

    Parameters
    ----------
    player1 : type
        descripton
    player2 : type
        descripton
    """
    pass

    
def they_want_to_continue():
    answer =''
    while answer not in ['yes', 'no']:
        answer = input('Do you want to play again? Enter yes or no: ')
    return answer

winner_message = ''
if player1 == player2:
    winner_message = 'It\'s a tie!'
elif player1 == 'rock' and player2 == 'scissors':
    winner_message = 'Player 1 wins!'
elif player1 == 'paper' and player2 == 'rock':
    winner_message = 'Player 1 wins!'
elif player1 == 'scissors' and player2 == 'paper':
    winner_message = 'Player 1 wins!'
else:
    winner_message = 'Player 2 wins!'

name1 = 'player1'
name2 = 'player2'

continue_game = 'yes'

while continue_game == 'yes':
    player1 = ask_player_for_input(name=name1)
    player2 = ask_player_for_input(name=name2)
    player1 = ''
    
    outcome = get_round_outcome(player1, player2, anme1=name1, name2=name2)
    if outcome == 'tie':
        winner_message = 'It\'s a tie!'
    else:
        winner_message = f'{outcome} wins!'
    
    print(winner_message)

    continue_game = they_want_to_continue()

print('game is ended')
    