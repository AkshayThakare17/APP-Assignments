def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    dp = {}

    def solve(i, w):
        if i == 0 or w == 0:
            return 0

        if (i, w) in dp:
            return dp[(i, w)]

        if weights[i - 1] <= w:
            dp[(i, w)] = max(
                values[i - 1] + solve(i - 1, w - weights[i - 1]),
                solve(i - 1, w)
            )
        else:
            dp[(i, w)] = solve(i - 1, w)

        return dp[(i, w)]

    return solve(n, capacity)


n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter capacity: "))

print("Maximum value using Bottom-Up:", knapsack_bottom_up(weights, values, capacity))
print("Maximum value using Top-Down:", knapsack_top_down(weights, values, capacity))
