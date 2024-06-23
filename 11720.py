N = int(input())
s = [0 for i in range(N)]
S = input()
sn = 0
for j in range(len(S)):
    s[j] = int(S[j])

for k in range(len(s)):
    sn += s[k]

print(sn)