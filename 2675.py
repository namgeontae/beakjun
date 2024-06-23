T = int(input())
s = [0 for j in range(T)]
for i in range(T):
    R, S = input().split()
    si = ''
    for k in range(len(S)):
        for l in range(int(R)):
            si += S[k]
    s[i] = si

for j in range(len(s)):
    print(s[j])
