def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest surrounds you, but hope shines within...")

def left_path():
    print("You walk left and discover a legendary sword of light.")
    print("The blade fills you with courage and strength.")
    print("With it, you defeat the lurking shadows in the forest.")
    print("The kingdom hails you as a true hero who brought peace!")
    print("Your bravery will be remembered for generations...")


def right_path():
    print("You walk right and encounter a wise owl perched on a branch.")
    print("The owl shares its ancient wisdom and grants you guidance.")
    print("With its help, you unite the forest creatures in harmony.")
    print("Together, you bring lasting peace to the land!")

if __name__ == "__main__":
    intro()
