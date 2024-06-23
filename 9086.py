si = int(input())
s = [0 for j in range(si)]
for i in range(si):
    S = input()
    s[i] = S[0] + S[len(S)-1]

for k in range(len(s)):
    print(s[k])