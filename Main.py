import turtle
import random

# The countGoodStrings function provided
def countGoodStrings(n: int, s1: str, s2: str, evil: str) -> int:
    dp = [[[-1] * 2 for _ in range(26)] for _ in range(n + 1)]

    def count(prefix_len, last_char, is_s1, is_s2):
        if evil in chr(last_char + ord('a')) * prefix_len:
            return 0
        if prefix_len == n:
            return 1
        if dp[prefix_len][last_char][is_s1] != -1 and not is_s2:
            return dp[prefix_len][last_char][is_s1]
        ans = 0
        for i in range(last_char, 26):
            if not is_s1 and chr(i + ord('a')) < s1[prefix_len]:
                continue
            if chr(i + ord('a')) > s2[prefix_len]:
                break
            ans = (ans + count(prefix_len + 1, i, is_s1 and chr(i + ord('a')) == s1[prefix_len], is_s2 and chr(i + ord('a')) == s2[prefix_len])) % MOD
        if not is_s2:
            dp[prefix_len][last_char][is_s1] = ans
        return ans

    return count(0, 0, True, True)

# Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")

# Create Pen (for drawing walls)
pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.speed(0)
pen.penup()

# Create Player
player = turtle.Turtle()
player.shape("circle")
player.color("blue")
player.speed(0)
player.penup()

# Draw the maze
# Add the rest of the code to draw the maze and move the player using arrow keys

# Check if move is valid
def check_collision(x, y):
    # Check for collision with walls
    # Add the rest of the code to check for collision with walls

    # Check for collision with door
    if is_door(x, y):
        s1 = "abcdefghijklm"  # Example input string 1
        s2 = "nopqrstuvwxyz"  # Example input string 2
        evil = "evil"         # The substring to avoid
        n = len(s1)
        good_strings_count = countGoodStrings(n, s1, s2, evil)
        try:
            user_input = wn.textinput("Enter the combination", f"Enter the correct combination of letters (total: {good_strings_count}):")
            if user_input == "your_correct_combination":  # Replace this with the actual correct combination
                print("Congratulations! You've unlocked the door.")
                return True
            else:
                print("Incorrect combination. Try again.")
                return False
        except TypeError:
            print("You've closed the input box. Try again.")
            return False
    return True

# Set up keyboard bindings
wn.listen()
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")

# Main game loop
while True:
    wn.update()

    # Get the player's current position
    x = player.xcor()
    y = player.ycor()

    # Check if the player is at the door
    if is_door(x, y):
        s1 = "abcdefghijklm"  # Example input string 1
        s2 = "nopqrstuvwxyz"  # Example input string 2
        evil = "evil"         # The substring to avoid
        n = len(s1)
        good_strings_count = countGoodStrings(n, s1, s2, evil)
        try:
            user_input = wn.textinput("Enter the combination", f"Enter the correct combination of letters (total: {good_strings_count}):")
            if user_input == "your_correct_combination":  # Replace this with the actual correct combination
                print("Congratulations! You've unlocked the door.")
                # Add code here to move the player to the next level or display a victory message
                break
            else:
                print("Incorrect combination. Try again.")
        except TypeError:
            print("You've closed the input box. Try again.")

# Close the window after finishing the game
turtle.done()

