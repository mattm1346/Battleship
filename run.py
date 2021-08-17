from random import randrange
import random
from constants import INTRO_TEXT
from constants import RULES

print(INTRO_TEXT)
print('Welcome to Battleships!')
print(RULES)
# Final message with added whitespace for clearer separation for rules and game
print('''
Good luck and enjoy

''')


# Create a function that checks for duplicates when placing ships
def check_board(b, taken):
    b.sort()
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
        if i != 0:
            if b[i] != b[i-1]+1 and b[i] != b[i-1]+10:
                b = [-1]
                break

    return b


# Create function for user to build ships
def get_ship(ship_length, taken):
    check_ship_length = True
    while check_ship_length:
        try:
            ship = []
            # user input numbers
            print('Place your Ships!')
            print('Enter ship of length', ship_length, 'between 0 and 99')
            for i in range(ship_length):
                boat_num = input('Please enter a number  \n')
                ship.append(int(boat_num))
            # check ship is in board and not in taken
            ship = check_board(ship, taken)
            if ship[0] != -1:
                taken = taken + ship
                break
            else:
                print('Error, Ship not finished')
        except ValueError:
            print('Error, Please enter a number')
    return ship


# Creates lists of ships
def create_ships_player(taken):
    ships = []
    boats = [5, 4, 3, 3, 2, 2]

    for boat in boats:
        ship = get_ship(boat, taken)
        ships.append(ship)
    return ships, taken


# Function checks that boat position is valid (connected and not scattered)
def check_boat(boat, start, ship_direction, taken):
    b = []
    # up = 1
    if ship_direction == 1:
        for i in range(boat):
            b.append(start - i * 10)
    # right = 2
    elif ship_direction == 2:
        for i in range(boat):
            b.append(start + i)
    # down = 3
    elif ship_direction == 3:
        for i in range(boat):
            b.append(start + i * 10)
    # left = 4
    elif ship_direction == 4:
        for i in range(boat):
            b.append(start - i)
    b = check_board(b, taken)
    return(b)


# Computer create ships
def create_ships(taken):
    ships = []
    boats = [5, 4, 3, 3, 2, 2]
    for boat in boats:
        b = [-1]
        while b[0] == -1:
            boat_start = randrange(99)
            # boat_direction - 1 = up, 2 = right, 3 = down, 4 = left
            boat_direction = randrange(1, 4)
            b = check_boat(boat, boat_start, boat_direction, taken)
        ships.append(b)
        taken = taken + b
    return ships, taken


# Create function to show computer board
def show_board_c(taken):
    print('   0 1 2 3 4 5 6 7 8 9')
    # Create loop for board
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            character = " _"
            if place in taken:
                character = " o"
            row = row + character
            place = place + 1
        print(x, row)


# Function for computer to guess
def guess_comp(guesses, tactics):
    # Create while loop so guess will run until input is valid
    is_guess_not_valid = True
    while is_guess_not_valid:
        if len(tactics) > 0:
            shot = tactics[0]
        else:
            shot = randrange(99)
        if shot not in guesses:
            is_guess_not_valid = False
            guesses.append(shot)
            break
    return shot, guesses


# Show player board
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


# Function checks if shot hits, misses or sinks ship
def check_shot(shot, boats, hit, miss, sink):
    missed = 0
    for i in range(len(boats)):
        if shot in boats[i]:
            boats[i].remove(shot)
            if len(boats[i]) > 0:
                hit.append(shot)
                missed = 1
            else:
                sink.append(shot)
                missed = 2
    # If shot misses, place in list
    if missed == 0:
        miss.append(shot)

    return boats, hit, miss, sink, missed


# Function so computer use logic after hits player ship
def calc_tactics(shot, tactics, guesses, hit):
    # tact is a temporary list that shots will append to
    tact = []
    if len(tactics) < 1:
        tact = [shot-1, shot+1, shot-10, shot+10]
    else:
        if shot - 1 in hit:
            if shot - 2 in hit:
                tact = [shot-3, shot+1]
            else:
                tact = [shot-2, shot+1]
        elif shot + 1 in hit:
            if shot - 2 in hit:
                tact = [shot+3, shot-1]
            else:
                tact = [shot+2, shot-1]
        elif shot - 10 in hit:
            if shot - 2 in hit:
                tact = [shot-30, shot+10]
            else:
                tact = [shot-20, shot+10]
        elif shot + 10 in hit:
            if shot - 2 in hit:
                tact = [shot+30, shot-10]
            else:
                tact = [shot+20, shot-10]
    # Out of tact, if the values are valid, append to tact_list
    tact_list = []
    for i in range(len(tact)):
        if tact[i] not in guesses and tact[i] < 100 and tact[i] > -1:
            tact_list.append(tact[i])
    random.shuffle(tact_list)
    return tact_list


# Add input for user guess
def guess(guesses):
    # Create while loop so guess will run until input is valid
    is_guess_not_valid = True
    while is_guess_not_valid:
        try:
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
                is_guess_not_valid = False
                break
        except ValueError:
            print('Error, Please enter a number')
    return shot


# Function checks if list is empty, used to check if no boats remaining
# so game will end
# Code taken from https://thispointer.com/
def check_if_empty(list_of_lists):
    return all([not elem for elem in list_of_lists])


# Create order for functions to be called
# Define lists and variables for actions
# Board 1 - Computer
comp_hit = []
comp_miss = []
comp_sink = []
comp_guess = []
comp_missed = 0
comp_tactics = []
comp_taken = []
# Board 2 - Player
player_hit = []
player_miss = []
player_sink = []
player_guesses = []
player_missed = 0
player_taken = []

# Computer creates board
boats, comp_taken = create_ships(comp_taken)
# User creates board
ships, player_taken = create_ships_player(player_taken)
show_board_c(player_taken)
# Create loop for game until player or computer sinks ships
for i in range(99):
    # Player shoots
    player_guesses = player_hit + player_miss + player_sink
    shot2 = guess(player_guesses)
    boats, player_hit, player_miss, player_sink, player_missed = check_shot(
        shot2, boats, player_hit, player_miss, player_sink)
    show_board(player_hit, player_miss, player_sink)
    # Check player shot

    # Repeat loop until ships empty
    if check_if_empty(boats):
        print('Game Finished - You Win in', i, 'moves')
        break
    # Computer shoots
    shot1, comp_guess = guess_comp(comp_guess, comp_tactics)
    ships, comp_hit, comp_miss, comp_sink, comp_missed = check_shot(
        shot1, ships, comp_hit, comp_miss, comp_sink)
    show_board(comp_hit, comp_miss, comp_sink)
    # Check computer shot
    if comp_missed == 1:
        comp_tactics = calc_tactics(
            shot1, comp_tactics, comp_guess, comp_hit)
    elif comp_missed == 2:
        comp_tactics = []
    elif len(comp_tactics) > 0:
        comp_tactics.pop(0)
    # Repeat loop until ships empty
    if check_if_empty(ships):
        print('Game Finished - Computer Wins in', i, 'moves')
        break
