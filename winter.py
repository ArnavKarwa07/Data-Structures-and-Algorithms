# Winter is Coming
# Chef feels comfortable depending on the temperature and whether he is wearing a jacket.
# - Comfortable without jacket: temperature >= A
# - Comfortable with jacket: temperature <= B
# - Guaranteed: A <= B
# - Chef starts without a jacket
# 
# Each time Chef puts on a jacket counts as one action (removing doesn't count).
# Find the minimum number of times Chef needs to put on a jacket to be comfortable on all N days.

# Input Format
# - First line: T (number of test cases)
# - For each test case:
#   - Line 1: N, A, B (number of days, comfort thresholds)
#   - Line 2: N space-separated integers (temperatures for each day)

# Output Format
# For each test case, output the minimum number of times Chef needs to put on a jacket.

# Constraints: 1 ≤ T ≤ 10^4, 1 ≤ N ≤ 100, 1 ≤ T_i ≤ 50, 1 ≤ A ≤ B ≤ 50

# Solution
def solve():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        temps = list(map(int, input().split()))
        
        jacket_count = 0
        has_jacket = False  # Chef starts without a jacket
        
        for temp in temps:
            if temp < a:
                # Needs jacket (cold)
                if not has_jacket:
                    jacket_count += 1
                    has_jacket = True
            elif temp > b:
                # Doesn't need jacket (hot)
                has_jacket = False
            # else: a <= temp <= b, jacket state doesn't matter
        
        print(jacket_count)

solve()