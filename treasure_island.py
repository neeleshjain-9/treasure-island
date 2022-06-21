print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ". |
|___________________ | _._"  ,. .` ` `` ,  `"-._"-._   ". '__ | ___________________
          |           | o`"=._` , "` `; .". ,  "-._"-._;;              |
 _________|___________ | ; `-.o`"=._; ." ` '`."\` . "-._ / _______________|_______
| | | o;    `"-.o`"=._``  '` ", __.--o; |
|___________________|_ |;     (  # ) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___ | o; ._    "      `".o | o_.--"; o; ____/______/______/____
/ ______/______/______/_"=._o--._; |;        ; ; / ______/______/______/_
____/______/______/______/__"=._o--._; o | o;     _._; o; ____/______/______/____
/ ______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/ ______/______/______/______/______/______/______/______/______/______/_______ /
*******************************************************************************
''')

print("Choose your Own Adventure")

r1 = "It's a room full of fire. Game Over."
r2 = "You found the treasure! You Win!"
r3 = "You enter a room of beasts. Game Over!"
r4 = "You chose a door that doesn't exist. Game Over!"
r5 = "You get attacked by an angry trout. Game Over!"
r6 = "You fell into a hole. Game Over."

q1 = input(
    "You're at a crossroads. Where do you want to go? Type \"left\" or \"right\"\n")
if q1 == "right":
    print(r6)
elif q1 == "left":
    q2 = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for the boat. Type \"swim\" to swim across.\n")
    if q2 == "swim":
        print(r5)
    elif q2 == "wait":
        q3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose.\n")
        if q3 == "blue":
            print(r3)
        elif q3 == "red":
            print(r1)
        elif q3 == "yellow":
            print(r2)
        else:
            print("Game Over!!!")
    else:
        print("Game Over!!!")
else:
    print("Game Over!!!")
