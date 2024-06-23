N = int(input())
listn=list(map(int,input().split()))
k = 0
v = int(input())

for j in range(len(listn)):
    if v == listn[j]:
        k += 1
print(k)