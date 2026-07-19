def maximum_value(maximum_weight, items):
    
    dp = [0] * (maximum_weight + 1)
    result = []
    
    for item in items:
        for w in range(maximum_weight, item["weight"] - 1, -1):
            dp[w] = max(dp[w], dp[w - item["weight"]] + item["value"])
    return dp[maximum_weight]

        
    
