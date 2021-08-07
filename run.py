print('Welcome to Battleships!')
print('''                __/___            
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
# Add input choosing level difficulty
# print('Please select difficulty level (easy, medium, hard)')
# print('easy = 1 ship and 6 guesses')
# print('medium = 2 ships 9 guesses')
# print('hard = 3 ships 10 guesses')
# Create variable for selecting level

# Add input for user guess
def guess(guesses):
    # Create while loop so guess will run until input is valid
    loop = 'no'
    while loop == 'no':
        shot = input("Please enter your guess between 0 and 99: \n")
        # Change shot to int as user input will be number
        shot = int(shot)
        # Create if statement checking that guess input is valid.
        # (between 0 and 99)
        if shot < 0 or shot > 99:
            print("Sorry, that number is not on the board. Please try again")
        elif shot in guesses:
            print("Sorry, you've used that number before. Try another")
        else:
            shot = 'yes'
            break

    return shot


# Create function to show board
def show_board(hit, miss, sink):
    print('   0 1 2 3 4 5 6 7 8 9')
    # Create loop for board
    place = 0
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


hit = []
miss = []
sink = []
guesses = hit + miss + sink
shot = guess(guesses)
show_board(hit, miss, sink)
