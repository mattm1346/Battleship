print('Welcome to Battleships')
print('______________________')
# Add input choosing level difficulty
print('Please select difficulty level (easy, medium, hard)')
print('easy = 1 ship and 6 guesses')
print('medium = 2 ships 9 guesses')
print('hard = 3 ships 10 guesses')
# Show board after difficulty selected
print('   0 1 2 3 4 5 6 7 8 9')
# Create loop for board
for x in range(10):
    print(x, " _"*10)
# Add input for guess
