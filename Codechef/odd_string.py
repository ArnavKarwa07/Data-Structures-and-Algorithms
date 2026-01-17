# Odd String
# You are given a string S of length N with lowercase English letters.
# 
# An "odd string" requires: for every pair of equal characters at indices i < j,
# the distance (j - i) must be odd.
# 
# You can rearrange S in any order.
# Determine if it's possible to rearrange S into an odd string.

# Key Insight:
# - If two identical characters are both at even positions (0, 2, 4, ...) or both at odd positions (1, 3, 5, ...),
#   their distance is even, which violates the constraint.
# - So each character can appear at most once at even positions and at most once at odd positions.
# - Maximum frequency for any character is 2.

# Input Format
# - First line: T (number of test cases)
# - For each test case:
#   - Line 1: N (length of string)
#   - Line 2: S (string of lowercase English letters)

# Output Format
# For each test case, output YES if rearrangement is possible, otherwise NO.

# Constraints: 1 ≤ T ≤ 10, 1 ≤ N ≤ 100

# Solution
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        
        # Count frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Check if any character appears more than 2 times
        possible = all(count <= 2 for count in freq.values())
        
        print("YES" if possible else "NO")

solve()