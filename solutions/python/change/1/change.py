def find_fewest_coins(coins, target):
    if target == 0:
        return []
    elif target < 0:
        raise ValueError("target can't be negative")
    elif target < coins[0]:
        raise ValueError("can't make target with given coins")
    
    result = []
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    
        
        
    for amount in range(1, target + 1):
        for coin in coins:
            
            if amount >= coin and 1 + dp[amount - coin] < dp[amount]:
                dp[amount] = 1 + dp[amount - coin]
                
    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")  

        
    while target > 0:
        for coin in coins:
            if dp[target - coin] == dp[target] - 1:
                result.append(coin)
                target -= coin
                break
    return result