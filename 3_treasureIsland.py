welcome = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

Welcome to Treasure Island.
Your mission is to find the treasure.
'''
prize = '''
You opened the door and you see a treasure chest. Congrats you found the treasure!\n
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
'''
print(welcome)
opt1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if opt1 == 'left':
    opt2 = input('You arrived at a lake. There\'s an island in the middle of the lake. Type "wait" to wait for a boat or type "swim" to swim across.\n').lower()
    if opt2 == 'wait':
        opt3 = input('You get a boat and arrived at the island. There\'s a house with 3 doors: one red, one yellow and one blue. Type "red", "yellow" or "blue" to choose one of the doors.\n').lower()
        if opt3 == 'yellow':
            print(prize)
        elif opt3 == 'blue':
            print('You are eaten by Beasts.\nGAME OVER!!!\n')
        elif opt3 == 'red':
            print('You are burned by fire.\nGAME OVER!!!\n')
        else:
            print('The door you have selected doesn\'t exist.\nGAME OVER!!!\n')
    elif opt2 == 'swim':
        print('You are attacked by trout.\nGAME OVER!!!\n')
    else:
        print('You have entered an invalid choice.\nGAME OVER!!!\n')
elif opt1 == 'right':
    print('You fall into a hole.\nGAME OVER!!!\n')
else:
    print('You have entered an invalid choice.\nGAME OVER!!!\n')

        