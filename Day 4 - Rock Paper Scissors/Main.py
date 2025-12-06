import random

symbol: dict[str, str] = {'rock': '🪨',
                          'paper': '📄',
                          'scissors': '✂️'}

player_choice: str = input('Chose rock (🪨), paper (📄), or scissors (✂️): '). strip().lower()
computer_choice: str = random.choice(tuple(symbol))

print('\nResults')
print('---------------------')
print(f'You:      {symbol[player_choice]} {player_choice}')
print(f'Computer: {symbol[computer_choice]} {computer_choice}')
print('---------------------')

if player_choice == computer_choice:
    print('It\'s a tie!')
elif player_choice == 'rock' and computer_choice == 'scissors':
    print('You won with rock! 🪨')
elif player_choice == 'paper' and computer_choice == 'rock':
    print('You won with paper! 📄')
elif player_choice == 'scissors' and computer_choice == 'paper':
    print('You won with scissors! ✂️')
else:
    print('Computer wins! 🤖')