Project Title: ESCAPE THE WOODS

VIDEO URL: https://youtu.be/1DzpvIEvDp4

DESCRIPTION:

This is a video game based on the idea of escaping a dark wood. It is verry simple the player is in the woods with a radar gadget that tells them their longitude and latitude. In order to escape the player needs some keys and a gas can to escape.

The player starts out knowing that the keys are somewhere in the ruins of the old farm which is to their east while the gas can they need to escape is to their west.

Straight down the road is the car that they need the supplies mentioned earlier to escape. The player can type out remember in order to recal the exact longitude of one item and the latitude of the other.

The game uses a grid system to detect the players location. Using the x and y axis.Should the player's x or y axis be at certain a value then the game will give out hints regarding where the object is.

However be fast though the game has a turn timer counting down from 75. Upon reaching 0 a monster has found your location and will end you before you can think of trying to escape.

The reason for this game being created is that I love video games and creating my own text based adventure for my project for cs50 seemed like a fun thing to do.

To explain the code

The main function is the starting hub of the code.

The start function is meant to describe that it is a text based product and emulate a start screen of video games. It will wait for the user to type yes to start.

The tutorial function is to print the data and teach the user what they can do in the game. It will take the user input on whether they are ready or not.

The gameplay function is the final function in the main and meant to be where all gameplay will be simulated. First it will keep track of the user inventory. Which they will start with radar. As they get the 2 items they need it will be appended to the inventory list. A timer is there which the player will have 75 turns to finish their little scavenger hunt and get to the vehicle. player_x and player_y which gets its values from the location() function.

The location function will return the value of player_x and player_y which is 0.

The gameplay function will then move into a while loop to keep looping until the game ends and then pass the data into the player_movement(). This function will use match and case to detect if the player moves forward, backward, left, right along with movement; It also tries to detect if the player wants to try and remember the location of the items or look at their inventory. It initializes a while True loop to keep asking player input if they put something wrong.

The gameplay function will then pass the movement and inventory into the position() function. Now this function detects player locaiton based on player_x and player_y coordinates and then prints out data based on their current location. It also detects when the player enters one of the two zones if the player has the item they need. If not it will tell the player the item should be in area. If they do however. Then the function will not tell the player anything regarding the item. If the player tries to go beyond the boundary the function will also bounce the player back into the zone through resetting the specific coordinate. For example if the player is at player_x = 20 which is at the edge. If they move one more to the left then it will issue a text prompt before promptly resetting them back to player_x = 20. Now this code also detects when the player is at the escape vehicle. If they have the 2 items needed to escape then the program will issue a text promt and exit. If not it will print the escape vehicle is there and then subsequently act like this is a space the player can walk on. All this data is returned back into gameplay() function.

gameplay() function will then print the players coordinates as their longitude and latitude locations. Followed by parsing their coordinates and inventory into the hint() function. Now this function will detect the players coordinates and if they have the item. If they do not it will give hints as to where they have to go to find the item. If the player has the item already then there it will not give a hint.

last function is the timer function. It takes the timer which starts at 75 and deducts it by 1 every player move and then return that data. It will issue text prompts every now and then warning the player as it counts down. However it will not tell the player exactly how much time left. The mystery is part of the fun. Once it reaches 0 however, It is game over and the program ends.