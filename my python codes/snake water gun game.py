
import random

# computer choice
computer = random.choice(["snake", "water", "gun"])

# enter plyer name and choice
playername = input("Enter player name: ")
playerchoice = input("Choose snake / water / gun: ").lower()

print(f"\n{playername} chose: {playerchoice}")
print(f"Computer chose: {computer}\n")

# condition 
if computer == playerchoice:
    print(f"😃 Game Drawn between {playername} and Computer!")

elif (playerchoice == "snake" and computer == "water") or \
     (playerchoice == "water" and computer == "gun") or \
     (playerchoice == "gun" and computer == "snake"):
    print(f"🎉 {playername} Wins!")
else:
    print("💻 Computer Wins!")
