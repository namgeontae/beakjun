S = input()
s = [-1 for i in range(ord('z')-96)]
for j in range(len(S)):
    if s[ord(S[j]) - 97] != -1:
        continue
    s[ord(S[j]) - 97] = j
print(*s)