from room import Room
from player import Player
from item import Item
# Main

# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#  Prints the current room name
#  Prints the current description (the textwrap module might be useful here).
#  Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.

#items for rooms
found_items = {
    'outside': [Item('knife', 'Rusty knife sticking out of the ground')],
    'foyer': [Item('sheild', 'wooden sheild for protection')],
    'overlook': [Item('rope', 'rope that you may need at some point')],
    'narrow': [Item('coin', 'Possible treasure form the treasure room')],
    'treasure': [Item('box', 'empty treasure box')],
}


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.,"""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
print(room['outside'])

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Link rooms with items
room['outside'].items = found_items['outside']
room['foyer'].items = found_items['foyer']
room['overlook'].items = found_items['overlook']
room['narrow'].items = found_items['narrow']
room['treasure'].items = room['treasure']


#Items in room 
# outsideItems = room['outside'].items.append(Item('knife', 'A dull knife sticking out of the dirt'))
# print(room['outside'].items[0])

#Start of game here
print('Press q to quit')# gives player option to quit game

playerOne = Player('Logan', room['outside']) #new player
print(playerOne)

direction = ('n', 'e', 's', 'w') #possible directions

start = True
while start:
    choice = input('What direction would you like to go? ')

    if choice == 'q':
        start = False
        print('Thank you for playing')
    else:
        if choice in direction:
            p_direction = getattr(playerOne.current_room, f'{choice}_to')#checks to see if attribute is present in current room player is in
            if p_direction is not None:
                playerOne.move(p_direction) #moves my player to a different room 
                print(playerOne)
            elif p_direction == None:
                print('Sorry you can not go that way')
                print(playerOne.current_room)


