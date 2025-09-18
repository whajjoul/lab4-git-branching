def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows your hesitation...")

def left_path():
    print("You walk left and find a cursed blade glowing with a sinister aura.")
    print("The moment you touch it, whispers fill your mind... urging you to seize power.")
    print("Your heart blackens, and you become the villain of this story.")

def right_path():
    print("You walk right and encounter a talking squirrel... but its eyes glow red.")
    print("It tempts you with promises of dominion over the forest.")
    print("You accept, and the forest bends to your will in fear.")

if __name__ == "__main__":
    intro()