def ask_for_player_name() -> str:
    print("Enter player name: ", end="")
    name = input()
    return name
    
def will_add_another_player() -> bool:
    while True:
        print("Would you like to add another player? (Y/N): ", end="")
        response = input()
        if response in ["Y", "y", "Yes", "yes"]:
            return True
        elif response in ["N", "n", "No", "no"]:
            return False
        else:
            print("Invalid Input.")
            
def read_square_input_file(input_file_path: str) -> list[str]:
    square_info = []
    try:
        with open(input_file_path, "r") as file:
            for line in file:
                square_info.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' was not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
    return square_info

def return_input_file_path() -> str:
    pass