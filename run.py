from random import randrange


print('Welcome to Battleships!')
print('''                __/___            
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

# Add rules description
# Add Build Board function


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
        # Check if user has used number before
        elif shot in guesses:
            print("Sorry, you've used that number before. Try another")
        else:
            loop = 'yes'
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


# Create function for computer to place its ships at random
# Create function to check boat range stays on board
def check_board(b):
    for i in range(len(b)):
        num = b[i]
        if num < 0 or num > 99:
            b = [-1]
            break

    return b


def check_boat(boat, start, direct):
    b = []
    # up
    if direct == 1:
        for i in range(boat):
            b.append(start - i * 10)
            b = check_board(b)
    # right
    elif direct == 2:
        for i in range(boat):
            b.append(start + i)
            b = check_board(b)
    # down
    elif direct == 3:
        for i in range(boat):
            b.append(start + i * 10)
            b = check_board(b)
    # left
    elif direct == 4:
        for i in range(boat):
            b.append(start - i)
            b = check_board(b)
    print(b)


boats = [5]#, 4, 3, 3, 2, 2]
for boat in boats:
    boat_start = randrange(99)
# boat_direct - 1 = up, 2 = right, 3 = down, 4 = left
    boat_direct = randrange(1, 4)
    print(boat, boat_start, boat_direct)
    check_boat(boat, boat_start, boat_direct)


# Create function to check if shot in guess hits ship
def check_shot(shot, ship1, hit, miss, sink):
    if shot in ship1:
        ship1.remove(shot)
        # Check if length of ship is greater than 0
        if len(ship1) > 0:
            hit.append(shot)
        else:
            sink.append(shot)
    else:
        miss.append(shot)

    return ship1, hit, miss, sink


ship1 = [45, 46, 47]
hit = []
miss = []
sink = []

# Create loop so user has number of guesses
for i in range(6):
    guesses = hit + miss + sink
    shot = guess(guesses)
    ship1, hit, miss, sink = check_shot(shot, ship1, hit, miss, sink)
    show_board(hit, miss, sink)

    if len(ship1) < 1:
        print("Congratulations! You sunk all the ships")
        break
print("Game Finished")
