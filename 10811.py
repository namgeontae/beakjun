def reverse(list, i, j):
    l = i
    temp = list[i:j+1]
    temp.reverse()
    for o in range(len(temp)):
        if l <= j:
            list[l] = temp[o]
        l += 1
    return list


N, M = map(int, input().split())
listn = list(range(1, N+1))

for k in range(M):
    i, j = map(int, input().split())
    reverse(listn, i-1, j-1)
print(*listn)