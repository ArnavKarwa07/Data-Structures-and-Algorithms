# Protein Diet
# You consume X grams of protein daily. A balanced diet requires at least Y grams of protein per day.
# Determine whether your daily protein intake fulfills the recommended requirement.
# The daily protein intake is considered fulfilled if and only if X is greater than or equal to Y.

# Input Format
# The first line of input contains two space-separated integers X and Y
# X: grams of protein consumed daily
# Y: minimum grams of protein recommended

# Output Format
# Print YES if the daily protein intake meets or exceeds the recommended amount.
# Otherwise, print NO.
# Each letter of the output may be printed in either uppercase or lowercase.

# Constraints: 1 ≤ X, Y ≤ 100

# Solution
X, Y = map(int, input().split())

if X >= Y:
    print("YES")
else:
    print("NO")