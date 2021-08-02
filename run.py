print('Welcome to Battleships!')
print('_______________________')
# Add input choosing level difficulty
print('Please select difficulty level (easy, medium, hard)')
print('easy = 1 ship and 6 guesses')
print('medium = 2 ships 9 guesses')
print('hard = 3 ships 10 guesses')
# Show board after difficulty selected
print('   0 1 2 3 4 5 6 7 8 9')
# Create vairables for hit, miss and sink
hit = []
miss = []
sink = []
place = 0
# Create loop for board
for x in range(10):
    row = ""
    for y in range(10):
        character = " _"
        if place in miss:
            character = " x"
        elif place in hit:
            character = " o"
        elif place in sink:
            character = " O"
        row = row + character
        place = place + 1
    print(x, row)
