player = {
    'room': 'cell',
}

inventory = {}

rooms = {
    "cell": {
        "title": "Cell",
        "description": "You wake up in a dark cell.",
        "exit": "west",
        "directions" : {"west": "Harry's cell"}},
    "Harry's cell": {
        "title": "Harry's cell",
        "description": "You're in Harry's cell.",
        "exit": "east, north",
        "directions": {
            "east" : "cell",
            "north" : "hallway"
            },
        "items" : {"piece of parchment": "skidaddle skidoodle ur nose is now a noodle", "weird key" : "it turns into a toad",},
        },
    "Hallway": {
        "title": "Hallway",
        "description": "You see long, dark corridor",
        "exit": "north, south",
        "directions" : {
            "north" : "chamber",
            "south" : "Harry's cell"
        },

    },
    }


def movement(player, rooms):
    room = rooms[player['room']]
    print(f'There are following exits: {(room["exit"])}')
    direction = input("Where would you like to go? \n")
    available_directions = room["directions"]
 
    if direction in available_directions:
        player['room'] = room["directions"][direction]
        describe_room()
    else:
        print(f"You can't go {direction}!")

def look_around(player, rooms):
    room = rooms[player['room']]
    for key in room["items"]:
        item = key
        print(f'There is a {item} lying on the floor.')


def get_items(player, rooms):
    room = rooms[player['room']]
    new_item = input("Which item would you like to pick up?\n")
    available_items = room["items"]
    value = room["items"][new_item]
    if new_item in available_items:
        inventory[new_item] = value
    elif new_item in inventory:
        inventory[new_item] += 1
    elif new_item not in available_item:
        print("There is nothing like that in this room!")


def check_item(inventory):

    room = rooms[player['room']]
    item_to_check = input("Which item would you like to check? \n")
    available_items = room["items"]
    value = room["items"][item_to_check]
    if item_to_check in available_items:
        print(value)

def possible_actions():
    print("possible actions: look (l), quit (q), movement (m), look around (la), check (ch), pick up (p)")

def main():

    describe_room()
    movement(player, rooms)
    possible_actions()
    playing = True
    while playing:
        command = get_command()
        if command in ['look', 'l']:
            describe_room()
        elif command in ['quit', 'q']:
            print('Bye!')
            playing = False
        elif command in ['movement', 'm']:
            movement(player, rooms)
        elif command in ['look around', 'la']:
            look_around(player, rooms)
        elif command in ['check', 'ch']:
            check_item(inventory)
        elif command in ['pick up', 'p']:
            get_items(player, rooms)
        else:
            print(f'Unrecognized command: {command}')


def get_command():
    print()
    return input('> ')


def describe_room():
    room = rooms[player['room']]
    print()
    print(room['title'])
    print()
    print(room['description'])


if __name__ == '__main__':
    main()
