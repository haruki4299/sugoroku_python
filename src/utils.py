def ask_for_player_name() -> str:
    print("Enter player name: ", end="")
    name = input()
    return name
    
def ask_if_add_another_player() -> bool:
    while True:
        print("Would you like to add another player? (Y/N): ", end="")
        response = input()
        if response in ["Y", "y", "Yes", "yes"]:
            return True
        elif response in ["N", "n", "No", "no"]:
            return False
        else:
            print("Invalid Input.")