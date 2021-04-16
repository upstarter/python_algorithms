def get_change(m):
    denominations = [1, 3, 4]
    minCoins = [0] + [math.inf]*m

    for i in range(1, m+1):
        for j in denominations:
            if i>=j:
                coins = minCoins[i-j]+1
                if coins < minCoins[i]:
                    minCoins[i] = coins
    return minCoins[m]
