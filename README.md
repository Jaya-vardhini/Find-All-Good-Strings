# Find-All-Good-Strings
In this level, the hero must find the correct combination of letters to unlock a door to the next room. The hero is given a string of letters and must determine which letters to use to form a good string that meets the alphabetical constraints and avoids the substring evil.
# Algorithmic Adventure

Algorithmic Adventure is a text-based adventure game where the player must solve a series of algorithmic challenges to progress through the levels and ultimately find the hidden treasure.

## Level 1: Odd-Even Jump

In this level, the player encounters a maze with floor tiles. Some tiles are safe, while others are traps. The player must enter the correct starting tile number to safely reach the end of the maze.

### Logic

The player is given a 3x3 grid of integers, which is represented as a 1D array. The player must find the correct starting tile that allows them to safely reach the end of the maze.

The correct starting tile is the tile with the smallest value in the array. This is based on the assumption that the player must start at the lowest value to minimize the risk of stepping on a trap. The player must enter the correct tile number to proceed to the next level.

## Level 2: Good Strings

In this level, the player is challenged to find the number of "good strings" between a given lower bound (s1) and upper bound (s2) that do not contain a forbidden substring (evil).

### Logic

A "good string" is defined as a string between the lower bound (s1) and upper bound (s2) that does not contain the forbidden substring (evil). To find the number of good strings, we use a depth-first search (DFS) algorithm.

The DFS algorithm starts at position 0, with a prefix_match of 0, lower_bound=True, and upper_bound=True. The DFS function recursively explores all possible characters from the lower bound to the upper bound, updating the prefix_match and lower_bound/upper_bound flags as needed.

The prefix_match tracks how many characters of the evil substring we have matched so far. If we reach the end of the evil substring (prefix_match == m), we return 0, as we have found a forbidden substring. If we reach the end of the string (pos == n), we return 1, as we have found a good string.

We also use memoization to store intermediate results in a 4D array called `dp`. This helps to avoid redundant calculations and speed up the algorithm.

The final result is the number of good strings between the lower bound (s1) and upper bound (s2) that do not contain the forbidden substring (evil).


