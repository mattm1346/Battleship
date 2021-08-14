from random import randrange


print(
    '''  ____       _______ _______ _      ______  _____ _    _ _____ _____   _____ 
|  _ \   /\|__   __|__   __| |    |  ____|/ ____| |  | |_   _|  __ \ / ____|
| |_) | /  \  | |     | |  | |    | |__  | (___ | |__| | | | | |__) | (___  
|  _ < / /\ \ | |     | |  | |    |  __|  \___ \|  __  | | | |  ___/ \___ \ 
| |_) / ____ \| |     | |  | |____| |____ ____) | |  | |_| |_| |     ____) |
|____/_/    \_\_|     |_|  |______|______|_____/|_|  |_|_____|_|    |_____/ 
''')


# Add rules description
# Add Build Board function

# Define lists and variables for actions
# Board 1 - Computer
hit1 = []
miss1 = []
sink1 = []
guesses1 = []
missed1 = 0
tactics1 = []
taken1 = []
# Board 2 - Player
hit2 = []
miss2 = []
sink2 = []
guesses2 = []
missed2 = 0
tactics2 = []
taken2 = []
# Set amount of ships
# Computer creates board as player 1
boats, taken1 = create_ships(taken1)
# Player creates board as player 2
ships, taken2 = create_ships_player(taken2)
# Create loop for game
for i in range(80):

    # Player shoots
    guesses = hit + miss + sink
    shot = guess(guesses)
    ships, hit, miss, sink = check_shot(shot, ships, hit, miss, sink)
    show_board(hit, miss, sink)
    # Check Player shot
    # Computer shoots
    # Check Computer shot
    shot, guesses = guess_comp(guesses, tactics)
    boats, hit, miss, sink, missed = check_shot(shot, boats, hit, miss, sink)
    if missed == 1:
        tactics = calc_tactics(shot, tactics, guesses, hit)
    elif missed == 2:
        tactics = []
    elif len(tactics) > 0:
        tactics.pop(0)

    if check_if_empty(boats):
        print('Game Finished', i)
        break


# Repeat until ships are empty

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
def check_board(b, taken):
    for i in range(len(b)):
        num = b[i]
        # Check for duplicates so ships do not overlap
        if num in taken:
            b = [-1]
            break
        elif num < 0 or num > 99:
            b = [-1]
            break
        # Add statement if number ends in 9 then continues
        # If ends in 0 then not valid
        elif b[i] % 10 == 9 and i < len(b) - 1:
            if b[i+1] % 10 == 0:
                b = [-1]
                break

    return b


def check_boat(boat, start, direct, taken):
    b = []
    # up
    if direct == 1:
        for i in range(boat):
            b.append(start - i * 10)
            b = check_board(b, taken)
    # right
    elif direct == 2:
        for i in range(boat):
            b.append(start + i)
            b = check_board(b, taken)
    # down
    elif direct == 3:
        for i in range(boat):
            b.append(start + i * 10)
            b = check_board(b, taken)
    # left
    elif direct == 4:
        for i in range(boat):
            b.append(start - i)
            b = check_board(b, taken)
    return(b)


def create_ships(taken):
    ships = []
    boats = [5, 4, 3, 3, 2, 2]
    for boat in boats:
        b = [-1]
        while b[0] == -1:
            boat_start = randrange(99)
            # boat_direct - 1 = up, 2 = right, 3 = down, 4 = left
            boat_direct = randrange(1, 4)
            print(boat, boat_start, boat_direct)
            b = check_boat(boat, boat_start, boat_direct, taken)
        ships.append(b)
        taken = taken + b
        print(ships)
    return ships, taken


boats, taken = create_ships()


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


    if len(ship1) < 1:
        print("Congratulations! You sunk all the ships")
        break
print("Game Finished")
print('''                __/___            
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')