from room import Room
from rooms import rooms
from items import items

#
# Main
#

from player import Player


def load():
    while True:
        name = input("What is your Name? ")
        player = Player(name, rooms['outside'])
        print(f"Welcome, {player.name}, lets get started")
        return player


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# If the user enters 'back' go back one room.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player = load()
print(f"You are at {player.location.name}, {player.location.description}")


while True:
    player_input = input(
        "What will you do next? Enter 'help' to see some options: ")
    player_input = player_input.lower().split(' ')

    if (player_input[0] == 'north') or (player_input[0] == 'n') or (player_input[0] == 'south') or (player_input[0] == 's') or (player_input[0] == 'west') or (player_input[0] == 'w') or (player_input[0] == 'east') or (player_input[0] == 'e') or (player_input[0] == 'back'):
        player.move(player_input[0])
        print(
            f"***{player.location.name}*** \n ***{player.location.description}***")

    elif ((player_input[0] == 'move') or (player_input[0] == 'go') or (player_input[0] == 'walk')) and ((player_input[1] == 'north') or (player_input[1] == 'n') or (player_input[1] == 'south') or (player_input[1] == 's') or (player_input[1] == 'west') or (player_input[1] == 'w') or (player_input[1] == 'east') or (player_input[1] == 'e') or (player_input[1] == 'back')):
        player.move(player_input[1])
        print(f"***{player.location.name}***\n ***{player.location.description}***")

    elif (player_input[0] == 'look') or (player_input[0] == 'room') or (player_input[0] == 'location') or (player_input[0] == 'where') or (player_input[0] == 'explore'):
        print(f"***{player.location.name}*** \n***{player.location.description}***")
    elif (player_input[0] == 'inventory'):
        player.inventory()
    elif (player_input[0] == 'search'):
        player.location.search()
    elif (player_input[0] == 'get') or (player_input[0] == 'take'):
        if player_input[1]:
            item = player.location.takeitem(player_input[1])
            if item:
                player.recieveitem(item)
            else:
                print("That item isn't here.")
        else:
            print("What would you like to take?")
    elif (player_input[0] == 'drop') or (player_input[0] == 'leave'):
        if player_input[1]:
            item = player.dropitem(player_input[1])
            if item:
                player.location.recieveitem(item)
            else:
                print("You don't have that item.")
        else:
            print("What would you like to drop?")
    elif (player_input[0] == 'q') or (player_input[0] == 'quit'):
        print("See you next time!")
        break

    elif (player_input[0] == 'help') or (player_input[0] == 'commands') or (player_input[0] == 'h'):
        print("You can 'go north' or any other cardinal direction.")
        print("You can 'look' to see the description of the room you are in.")
        print("You can 'search' to try to find any items.")
        print(
            "You can 'take [item]' to put an item you find in your inventory, or 'drop [item]'.")
        print("Type 'quit' to save and quit.")
    else:
        print("Didn't recognize that input, try again. Type 'help' to view the list of commands.")
