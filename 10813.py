N, M = map(int, input().split())
listn = list(range(1,N+1))

for l in range(M):
    i, j = map(int, input().split())
    listn[i-1], listn[j-1] = listn[j-1], listn[i-1]

print(*listn)