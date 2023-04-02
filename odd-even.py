import os

def clear_screen():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays the main menu options"""
    clear_screen()
    print("Algorithmic Adventure")
    print("1. Start Game")
    print("2. How to Play")
    print("3. Exit")
    print("Choices: [1/2/3]")

def how_to_play():
    """Displays the description of the game and how the level/rank/health system works"""
    clear_screen()
    print("Welcome to Algorithmic Adventure!")
    print("Your goal is to find the hidden treasure by completing various levels of challenges.")
    print("There are 8 levels in total, and as you complete each level, you will attain a new rank.")
    print("You start at Rank 1 and can progress up to Rank 8.")
    print("You have 3 lives to start with. If you fail a level without any remaining lives, it's game over.")
    print("Good luck!")

def display_level1():
    """Displays Level 1: Odd-Even Jump"""
    clear_screen()
    print("Level 1: Odd-Even Jump")
    print("Proceed? Y/N")
    choice = input().lower()
    if choice == "n":
        print("You are too scared to proceed. You failed in your quest to find the hidden treasure. Ashamed, you return to your hometown.")
        input("Press Enter to continue...")
        display_menu()
    elif choice == "y":
        print("You encounter a maze with floor tiles. Some of the tiles are safe but some of them are traps. Tread carefully!")
        print("The floor tiles are numbered with values like so:")
        # generate the table here
        table = [[2, 10, 3], [4, 8, 14], [5, 7, 17]]
        for row in table:
            print(*row)
        print("As an array, this looks like: [5,7,17,4,8,14,2,10,3]")
        print("You need to enter the correct starting tile that will allow you to safely reach the end of the maze.")
        correct_tile = 2
        user_input = input("Enter the correct tile number: ")
        if user_input == "":
            print("You proceed to jump around the tiles until you reach the door. You notice that the door is unlocked. You enter through the door.")
            input("Press Enter to continue...")
            clear_screen()
            print("Good job. You cleared Level 1. You earned the Newbie Hero title.")
            input("Press Enter to continue...")
            display_menu()
        elif int(user_input) == correct_tile:
            clear_screen()
            print("Good job. You cleared Level 1. You earned the Newbie Hero title.")
            input("Press Enter to continue...")
            display_menu()
        else:
            clear_screen()
            print("Game Over")
            input("Press Enter to continue...")
            display_menu()

# main loop
while True:
    display_menu()
    choice = input().lower()
    if choice == "1":
        display_level1()
    elif choice == "2":
        how_to_play()
        input("Press Enter to continue...")
        display_menu()
    elif choice == "3":
        print("Program Exit")
        break
    else:
        print("Invalid choice. Please choose again.")
