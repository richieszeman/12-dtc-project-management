##
# Japanese phrase game/quiz

MENUS = ["1) Play", "2) Reward", "3) Score", "Q) quit"]
user_choice = input("Welcome to the Japanese phrases game!")
for menu in MENUS:
    print(menu)
if user_choice == 1:
    print("playing game")
elif user_choice == 2:
    print("Rewards earned so far")
elif user_choice == 3:
    print("here is your score")
elif user_choice == "Q":
    print("Thank you for playing")
else:
    print("please select a valid choice")
