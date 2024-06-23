N ,K = map(int, input().split())

list = []
for i in range(N):
    W, V = map(int, input().split())
    list[i] = [W, V]

for j in range(N):
    max_k = list[j][0]
    for k in range(j+1, N):
