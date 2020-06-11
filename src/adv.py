from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
playerOne = Player(input("What is your name? "), room['outside'])
print(playerOne)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print('Press q to quit')
# print(room['outside'].n_to)


while True:
    choice = input('What direction would you like to go in? (n, e, s, w) ')
    try:
        if(choice == 'q'):
            break
        if choice == 'n':
            if playerOne.current_room.n_to:
                playerOne.current_room = playerOne.current_room.n_to
                print(playerOne)
        if(choice == 'e'):
            if playerOne.current_room.e_to:
                playerOne.current_room = playerOne.current_room.e_to
                print(playerOne)
        if(choice == 's'):
            if playerOne.current_room.s_to:
                playerOne.current_room = playerOne.current_room.s_to
                print(playerOne)
        if(choice == 'w'):
            if playerOne.current_room.w_to:
                playerOne.current_room = playerOne.current_room.w_to
                print(playerOne)


    except ValueError:
        print('Please enter a valid direction')
