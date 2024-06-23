listn = [0 for i in range(30)]

for i in range(28):
    k = int(input())
    listn[k -1] = 1

for j in range(len(listn)):
    if listn[j] == 0:
        print(j+1)