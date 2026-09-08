w = 3
n = 3

weights = [2,3,5]
values = [12,34,56]

dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,w+1):
        if weights[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weights[i-1]]+values[i-1])
print(dp)
print(dp[n][w])