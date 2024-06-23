X = int(input())
N = int(input())
allx = 0
for i in range(N):
    x, n = map(int, input().split())
    allx += x * n

if allx == X:
    print("Yes")
else:
    print("No")