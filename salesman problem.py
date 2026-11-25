from sys import maxsize

def tsp(mask, pos):
    # All cities visited
    if mask == (1 << n) - 1:
        return graph[pos][0]

    ans = maxsize

    for city in range(n):
        if (mask & (1 << city)) == 0:
            new_ans = graph[pos][city] + tsp(mask | (1 << city), city)
            ans = min(ans, new_ans)

    return ans


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)

# Start from city 0
print("Minimum cost:", tsp(1, 0))
