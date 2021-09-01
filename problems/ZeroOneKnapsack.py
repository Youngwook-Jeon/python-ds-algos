# 아이템 들의 무게와 값어치가 들어있는 배열들과 가방의 무게한도가 주어졌을 때
# 최대한의 값어치를 얻도록 가방에 아이템 넣기
def zoKnapsackBU(profits, weights, capacity):
    # TODO
    n = len(weights)
    # dp[i][w]: the max value of j-weight considering all values from 1st to ith weight
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][w]