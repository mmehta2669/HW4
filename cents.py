def round_up_cost(group_sum):#simple rounding function
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
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # No items, no cost

    #Fill DP table
    for i in range(1, n + 1):  # Dividers + 1 parts (since k dividers make k+1 groups)
        for dividers in range(0, k + 1):  # number f dividers used. End of the current group
            group_sum = 0  # Reset the group sum
            for p in range(i,0,-1):  # Start of the current group and work backwards.
                group_sum += items[p - 1]  # Accumulate the group sum
                rounded_cost = round_up_cost(group_sum)
                # Only update dp[i][dividers] if dividers are available

                if dividers == 0:
                    dp[i][dividers] = dp[p - 1][dividers] + rounded_cost

                else:
                    dp[i][dividers] = min(dp[i][dividers], dp[p-1][dividers - 1] + rounded_cost)

    #Extract minimum cost from the last row of dp for all possible dividers
    min_cost = float('inf')
    for dividers in range(k + 1):
        min_cost = min(min_cost, dp[n][dividers])
    
    return round_up_cost(min_cost)  # Return the minimum rounded cost

# Example usage
def main():
    import sys
    
    input = sys.stdin.read
    data = input().splitlines()
    
    # n = num of items, k = num of dividers
    n, k = map(int, data[0].split()) #Read n and k 
    items = list(map(int, data[1].split())) #Read the item prices
    
    result = minimize_cost(items, k, n)
    print(result)
    
if __name__ == "__main__":
    main()