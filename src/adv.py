from room import Room
from player import Player
from textwrap import fill
from item import Item
from item import LightSource
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),

    'dungeon': Room("Filthy Dungeon", """The stench of death overwhelms you as you enter the room.  Ancient bones and more freshly rotten corpses litter the floor, walls, and cells of this dungeon.  It looks like no one fed the prisoners and they died agonizing deaths. A grimy passage leads to the west.""", False)
}

item = {
	'flashlight': LightSource("flashlight", "a flashlight. That could be handy!"),

	'sword': Item("sword", "a large broadsword"),

	'shield': Item("shield", "a protective shield"),

	'nothing': Item("nothing", "nothing. Keep looking"),

	'pokeball': Item("pokeball", "a pokeball. Huh? Are there pokemon around here?"),

	'tunic': Item("tunic", "a warm tunic"),

	'hookshot': Item("hookshot", "a hookshot. You can escape by pressing q!")
	
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['dungeon']
room['dungeon'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#

# Add items to rooms
room['outside'].items =[item['flashlight']]
room['foyer'].items = [item['sword'], item['shield']]
room['overlook'].items = [item['nothing']]
room['narrow'].items = [item['pokeball']]
room['treasure'].items = [item['tunic']]
room['dungeon'].items = [item['hookshot']]
# Main
#
def location(player, prev_room = ''):
	if player.current_room.name!= prev_room:
		print(f"\n{player.name} is in room: {player.current_room.name}\n{fill(player.current_room.description, 50)}\n")
	if player.current_room.is_light==True:
		print("\nIn this room you see: \n ")
		for item in player.current_room.items:
			print(item.name)
		print('\nYou are carrying:\n')
		for item in player.inventory:
			print(item.name)
	else:
		print("\nIn this room you see:\nNothing, it's dark!\n")
# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name? "), room['outside'], [])

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

def intro():
	print('\nWelcome to the game!\n')

intro()
directions = {'n':'n_to', 'e':'e_to', 's':'s_to', 'w':'w_to'}
inv = ['i', 'inventory']
grab = ['take', 'get']

location(player)
while True:
    cmd = input('Welcome.  What is your first move? -->')
    words = cmd.split(' ')
    
    if directions.get(cmd):
	        prev_room = player.current_room.name
	        player.current_room = player.current_room.move(directions[cmd])
	        location(player, prev_room)
    
    elif words[0] in grab:
            player.take(item.get(words[1]))

    elif words[0] == 'drop':
	        player.drop(item.get(words[1]))
    
    elif cmd in inv:
	        player.holding()
    
    elif cmd == 'q':
		    print('\nAll done. Play any time you would like\n')
		    break
    
    else:
		    print('\n "Does not compute. Try again?" \n')