print('''
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
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
player = input("What's your gamertag?")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
way = input(f"Which way would you like to go {player}? Left or Right?")
new_way = way.lower()
if new_way == "right":
  print(f"You made a bad choice {player}, cause you fell into a hole. GAME OVER!!!")
else:
  print(f"Good Choice {player}! you chose the right way")
  swim = input("Now you have 2 options: There is a river in front of you, would you like to go across by swimming or wait here? Swim or Wait?")
  new_swim = swim.lower()
  if new_swim == "swim":
    print(f"Ahhhhhhhh! Hard luck {player}, you made a bad decision. You are now a crocodile's lunch!! HAHAHAHA!")
  else:
    print(f"Well done {player}! you made the right choice")
    door = input("Suddenly there was a lightning and 3 doors magically appeared in front of you! RED BLUE and Yellow. One door leads to victory rest to somewhere I don't want to talk about!! So which color door you choosing? Red, Blue or Yellow?")
    new_door = door.lower()
    if new_door == "yellow":
      print(f"Congratulations!!!! {player}, you have made all the right choices and won the game")
    elif new_door == "red":
      print(f"HAHA!! {player} You fell into hell becuase of your lust for treasure!")
    elif new_door == "blue":
      print(f"HAHA!! {player} You were taken as a specimen by the alien race!!!")
    else:
      print(f"HAHA!! {player} you made a choice that is not in the game, GAME OVER!!!!!")
    
    
  

