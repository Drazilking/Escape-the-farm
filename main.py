import sys
#start by making the script#
def main():
    start()
    tutorial()
    gameplay()



def start():
    while True:
        print("TUTORIAL: This is a text based adventure game.")
        start = input("Are you ready to start? ").lower().strip()
        if start == "yes" or start == "yeah" or start == "affirmative" :
            return
        else:
            print("\n\n\n")
            pass

def tutorial():
    while True:
        print("\n")
        print("In order to move around you type: w, a, s, d You can also remember vaguely where the items you need are." )
        print("You are to find a key and a gas can to escape. Beware though you are on a timer and there is something else in the woods")
        print("Try")
        question = input("Are you ready to begin ").strip().lower()
        if question == "yes" or question == "yeah" or question == "affirmative":
            return
        else:
            pass

def gameplay():
    inventory = ["radar"]
    timer = 150
    player_x, player_y = location()
    while True:
        player_x, player_y = player_movement(player_x, player_y, inventory)
        player_x, player_y = position(player_x, player_y, inventory)
        print(f"longitude:{player_x} latitude:{player_y}")
        hint(player_x, player_y, inventory)
        timer = timer_countdown(timer)


def location():
    player_x = 0
    player_y = 0
    return player_x, player_y,


def player_movement(player_x, player_y, inventory):
    while True:
        move = input("w = forward, a = left, s = right, d = back, inventory, remember \n" ).lower().strip()
        match move:
            case "w":
                player_y += 1
                return player_x, player_y
            case "s":
                player_y -= 1
                return player_x, player_y
            case "a":
                player_x -= 1
                return player_x, player_y
            case "d":
                player_x += 1
                return player_x, player_y
            case "inventory":
                print(inventory)
            case "remember":
                print("hint The key is in the old farm with a latitude of 14 \n")
                print("The gas can is in the dark woods. A longitude of -19 \n")
                print("There is a car directly to the north of where you woke up \n")
            case _ :
                pass

def position(player_x, player_y, inventory):
    if player_y == -1:
        print("There is a fence in front of you lined with barbed wire. You cannot climb it. ")
        player_y = 0
        return player_x, player_y

    if player_x > 20:
        print("There is a fence in front of you lined with barbed wire. You cannot climb it. ")
        player_x -= 1
        return player_x, player_y
    if player_x < -20:
        print("There is a fence in front of you lined with barbed wire. You cannot climb it. ")
        player_x = -20
        return player_x, player_y

    if player_y > 20:
        print("A vast road deep forest. You dare not proceed.")
        player_y = 20
        return player_x, player_y

    if player_x == 0 and player_y == 20:
        print("There is a car infront of you it needs gas and keys. ")
        if "key" in inventory and "gas can" in inventory:
            print("You get into the car after refilling it with gas. Twist the keys and begin to drive off.")
            sys.exit()

    if player_x == 0 and player_y == 0:
        print("You are in the center of wherever this it" )
        return player_x, player_y
    if player_x >= 1 and player_y >= 0:
        if "key" in inventory:
            print("You are within a farm")
            return player_x, player_y
        else:
            print("You look around and find yourself within the ruins of a farm. The keys should be here")
            if player_x == 12 and player_y == 14:
                print("You have found keys within the ruins of the old farm.")
                inventory.append("key")
                return player_x, player_y
            else:
                return player_x, player_y
    if player_x <= 0 and player_y >= 0:
        if "gas tank" in inventory:
            print("You appear to be in the dark woods. ")
            return player_x, player_y
        else:
            print("You appear to be within the dark woods. You remember seeing somoene carry a jerry can here that appeared full here.")
            if player_x == -19 and player_y == 10:
                print("You have found the jerry can it appears to be half full." )
                inventory.append("gas can")
                return player_x, player_y
            else:
                return player_x, player_y

    return player_x, player_y
def timer_countdown(timer):
    if timer == 140:
        print("A beast stalks looking for you. You have gotten its attention. You need to escape. ")
    if timer == 100:
        print("You can sense something coming soon")
    elif timer == 50:
        print("it is almost here")
    elif timer == 20:
        print("you need to get out")
    elif timer == 0:
        print("it is too late. You hear the howl before something lunges at you and everything fades to black")
        sys.exit()
    timer -= 1
    return timer

def hint(player_x, player_y, inventory):
    key_hintx = [10, 3, 9]
    key_hintxplus = [14, 16, 19]
    if player_x in key_hintx and player_y == 14 and "key" not in inventory:
        print("You can hear the jingle of keys to the east of your current location.")
    if player_x in key_hintxplus and player_y == 14 and "key" not in inventory:
        print("You can hear the jingle of keys to the west of your position. ")
    gas_hinty = [3, 4, 5, 7, 8, 9]
    gas_hintyplus = [13, 15, 17, 19]
    if player_x == -19 and player_y in gas_hinty and "gas can" not in inventory:
        print("A gasoline trail, it cuts off every now and then but it goes northward.")
    if player_x == -19 and player_y in gas_hintyplus and "gas can" not in inventory :
        print("A scent of gasoline, It smells like its southward of your location")

main()