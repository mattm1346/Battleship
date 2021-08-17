from random import randrange
import random

print(
    '''  ____       _______ _______ _      ______  _____ _    _ _____ _____   _____ 
|  _ \   /\|__   __|__   __| |    |  ____|/ ____| |  | |_   _|  __ \ / ____|
| |_) | /  \  | |     | |  | |    | |__  | (___ | |__| | | | | |__) | (___  
|  _ < / /\ \ | |     | |  | |    |  __|  \___ \|  __  | | | |  ___/ \___ \ 
| |_) / ____ \| |     | |  | |____| |____ ____) | |  | |_| |_| |     ____) |
|____/_/    \_\_|     |_|  |______|______|_____/|_|  |_|_____|_|    |_____/ 
''')

print('Welcome to Battleships!')
# Add a rules print message at start of game
print('How to Play')
print('''
First place your ships, a total of 6 ships are needed to start.
1st ship of length 5 spaces, 2nd length 4, 3rd and 4th length 3, and 5th
& 6th of length 2.
''')
print('''
Next take a shot at the computer's board.
Enter a number between 0 and 99 to guess. After you make your shot, the board 
will update with either a hit or miss.

Hit = o
Miss = x

If a ship has been sunk, "O" will display to show that that ship is sunk.

Sink = O
''')
# Final message with added whitespace for clearer separation for rules and game
print('''
Good luck and enjoy :)


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


def get_ship(long, taken):
    loop = True
    while loop:
        ship = []
        # user input numbers
        print('Place your Ships!')
        print('Enter ship of length', long, 'between 0 and 99')
        for i in range(long):
            boat_num = input('Please enter a number  \n')
            ship.append(int(boat_num))
        # check ship
        ship = check_board(ship, taken)
        if ship[0] != -1:
            taken = taken + ship
            break
        else:
            print('Error, Ship not finished')
    return ship


def create_ships_player(taken):
    ships = []
    boats = [5, 4, 3, 3, 2, 2]

    for boat in boats:
        ship = get_ship(boat, taken)
        ships.append(ship)
    return ships, taken


def check_boat(boat, start, direct, taken):
    b = []
    # up
    if direct == 1:
        for i in range(boat):
            b.append(start - i * 10)
    # right
    elif direct == 2:
        for i in range(boat):
            b.append(start + i)
    # down
    elif direct == 3:
        for i in range(boat):
            b.append(start + i * 10)
    # left
    elif direct == 4:
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
            # boat_direct - 1 = up, 2 = right, 3 = down, 4 = left
            boat_direct = randrange(1, 4)
            b = check_boat(boat, boat_start, boat_direct, taken)
        ships.append(b)
        taken = taken + b
    return ships, taken


# Create function to show board
def show_board_c(taken):
    print('      Computer Board  ')
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


def guess_comp(guesses, tactics):
    # Create while loop so guess will run until input is valid
    loop = 'no'
    while loop == 'no':
        if len(tactics) > 0:
            shot = tactics[0]
        else:
            shot = randrange(99)
        if shot not in guesses:
            loop = 'yes'
            guesses.append(shot)
            break
    return shot, guesses


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


def calc_tactics(shot, tactics, guesses, hit):
    temp = []
    if len(tactics) < 1:
        temp = [shot-1, shot+1, shot-10, shot+10]
    else:
        if shot - 1 in hit:
            if shot - 2 in hit:
                temp = [shot-3, shot+1]
            else:
                temp = [shot-2, shot+1]
        elif shot + 1 in hit:
            if shot - 2 in hit:
                temp = [shot+3, shot-1]
            else:
                temp = [shot+2, shot-1]
        elif shot - 10 in hit:
            if shot - 2 in hit:
                temp = [shot-30, shot+10]
            else:
                temp = [shot-20, shot+10]
        elif shot + 10 in hit:
            if shot - 2 in hit:
                temp = [shot+30, shot-10]
            else:
                temp = [shot+20, shot-10]
    # For longer ships
    cand = []
    for i in range(len(temp)):
        if temp[i] not in guesses and temp[i] < 100 and temp[i] > -1:
            cand.append(temp[i])
    random.shuffle(cand)
    return cand


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


def check_if_empty(list_of_lists):
    return all([not elem for elem in list_of_lists])


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

# Computer creates board
boats, taken1 = create_ships(taken1)
# User creates board
ships, taken2 = create_ships_player(taken2)
show_board_c(taken2)
# Create loop for game
for i in range(80):
    # Player shoots
    guesses2 = hit2 + miss2 + sink2
    shot2 = guess(guesses2)
    ships, hit2, miss2, sink2, missed2 = check_shot(shot2, ships, hit2, miss2, sink2)
    show_board(hit2, miss2, sink2)
    # Check player shot

    # Repeat loop until ships empty
    if check_if_empty(boats):
        print('Game Finished - You Win', i)
        break
    # Computer shoots
    shot1, guesses1 = guess_comp(guesses1, tactics1)
    boats, hit1, miss1, sink1, missed1 = check_shot(shot1, boats, hit1, miss1, sink1)
    show_board(hit1, miss1, sink1)
    # Check computer shot
    if missed1 == 1:
        tactics1 = calc_tactics(shot1, tactics1, guesses1, hit1)
    elif missed1 == 2:
        tactics1 = []
    elif len(tactics1) > 0:
        tactics1.pop(0)
    # Repeat loop until ships empty
    if check_if_empty(boats):
        print('Game Finished - Computer Wins', i)
        break
