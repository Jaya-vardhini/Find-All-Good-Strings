MOD = 10**9 + 7
def countGoodStrings(n: int, s1: str, s2: str, evil: str) -> int:
# Initialize a DP table to store the number of good strings for a given prefix length and last
character
dp = [[[-1] * 2 for _ in range(26)] for _ in range(n + 1)]
# Define a recursive function to count the number of good strings for a given prefix length and last character
def count(prefix_len, last_char, is_s1, is_s2):
# Base case: if evil is a substring of the current prefix, then there are no good strings if evil in chr(last_char + ord('a')) * prefix_len:
return 0
# Base case: if we've reached the desired prefix length, then there is exactly one good string
if prefix_len == n: return 1
# Memoization
if dp[prefix_len][last_char][is_s1] != -1 and not is_s2:
return dp[prefix_len][last_char][is_s1]
# Count the number of good strings for the next prefix length and last character ans = 0 for i in range(last_char, 26):
if not is_s1 and chr(i + ord('a')) < s1[prefix_len]: Continue
if chr(i + ord('a')) > s2[prefix_len]: Break
ans = (ans + count(prefix_len + 1, i, is_s1 and chr(i + ord('a')) == s1[prefix_len], is_s2 and chr(i + ord('a')) == s2[prefix_len])) % MOD
# Memoization if not is_s2: dp[prefix_len][last_char][is_s1] = ans return ans
# Call the recursive function with initial parameters return count(0, 0, True, True)
