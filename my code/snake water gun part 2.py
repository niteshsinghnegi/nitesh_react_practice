import random

computer=random.choice(["snake","water","gun"])
plyername=input("enter your name")
plyerchoice=input("choice:,snake,water,gun").lower()

print(f"\n{plyername},choice:{plyername}")
print(f"computer choice {computer}\n")

if (computer==plyerchoice):
    print("game is tie and match over")
elif (computer=="snake"and plyerchoice=="gun") or\
(computer=='water'and plyerchoice=='snake')or\
(computer=="gun"and plyerchoice=='water'):
 print(f"plyer{plyername}is win")
else:
 print("compuer is win")
