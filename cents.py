import sys

#simple rounding function
def round_up_cost(group_sum):
    if (group_sum%10 < 5):
        return group_sum - (group_sum%10)
    else:
        return group_sum + (10 - group_sum%10)


def minimize_cost(items, k, n):
    
    #Compute precalc sums
    precalc = [0] * (n + 1)
    for i in range(1, n + 1):
        precalc[i] = precalc[i - 1] + items[i - 1] #adds a series of sums, so 0 = item[0], 1 = item[0]+ item[1] and so on

    #Initialize DP table
    dp = [[float('inf')] * (k + 2) for _ in range(n + 1)]
    dp[0][0] = 0  # No items, no cost

    #Fill DP table
    for dividers in range(1, k + 1):  # Dividers + 1 parts (since k dividers make k+1 groups)
        for i in range(1, n + 1):  # End of the current group
            for p in range(i):  # Start of the current group (0 <= p < i)
                group_sum = precalc[i] - precalc[p] #equation for using the percalcs, subtracks start from end val
                rounded_cost = round_up_cost(group_sum)
                dp[i][dividers] = min(dp[i][dividers], dp[p][dividers - 1] + rounded_cost)

    
    return dp[n][k + 1]

# Example usage

input = sys.stdin.readline
# n = num of val, k = num of dividers
n, k = map(int, input().split()) 
input = sys.stdin.readline
lis = input().split()
items = [eval(i) for i in lis]
    
result = minimize_cost(items, k, n)
print(result)
