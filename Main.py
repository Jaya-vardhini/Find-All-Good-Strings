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
            display_level2()
        else:
            clear_screen()
            print("Game Over")
            input("Press Enter to continue...")
            display_menu()

def display_level2():
    """Displays Level 2: Good Strings"""
    clear_screen()
    print("Level 2: Good Strings")
    print("Proceed? Y/N")
    choice = input().lower()
    if choice == "n":
        print("You are too scared to proceed. You failed in your quest to find the hidden treasure. Ashamed, you return to your hometown.")
        input("Press Enter to continue...")
        display_menu()
    elif choice == "y":
        get_good_strings()
        input("Press Enter to continue...")
        clear_screen()
        print("Good job. You cleared Level 2. You earned the Master of Strings title.")
        input("Press Enter to continue...")

def countGoodStrings(n: int, s1: str, s2: str, evil: str) -> int:
    mod = 10**9 + 7

    m = len(evil)
    dp = [[[[-1] * (m + 1) for _ in range(2)] for _ in range(n + 1)] for _ in range(27)]

    def dfs(pos: int, prefix_match: int, lower_bound: bool, upper_bound: bool) -> int:
        if prefix_match == m:
            return 0
        if pos == n:
            return 1
        if dp[prefix_match][pos][prefix_match][int(lower_bound)] != -1 and not upper_bound:
            return dp[prefix_match][pos][prefix_match][int(lower_bound)]

        lb = ord(s1[pos]) if lower_bound else ord('a')
        ub = ord(s2[pos]) if upper_bound else ord('z')

        ans = 0
        for ch in range(lb, ub + 1):
            new_prefix_match = prefix_match
            while new_prefix_match >= 0 and evil[new_prefix_match] != chr(ch):
                new_prefix_match = new_prefix_match - 1
            new_prefix_match += 1

            ans += dfs(pos + 1, new_prefix_match, lower_bound and ch == lb, upper_bound and ch == ub)
            ans %= mod

        if not upper_bound:
            dp[prefix_match][pos][prefix_match][int(lower_bound)] = ans

        return ans

    return dfs(0, 0, True, True)


def get_good_strings():
    n = int(input("Enter the length of the string (n): "))
    s1 = input("Enter the lower bound of the good string (s1): ")
    s2 = input("Enter the upper bound of the good string (s2): ")
    evil = input("Enter the forbidden substring (evil): ")
    
    good_strings = countGoodStrings(n, s1, s2, evil)
    print(f"The number of good strings is {good_strings}")


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
