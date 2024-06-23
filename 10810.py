N, M = map(int, input().split())
listn = [0 for l in range(N)]

for o in range(M):
    i, j, k = map(int, input().split())
    for b in range(i-1, j):
        listn[b] = k

print(*listn)