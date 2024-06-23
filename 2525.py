a, b = map(int,input().split())
c = int(input())

mit = b + c

while(mit >= 60):
    a += 1
    mit -= 60

if (a > 23):
    a -= 24

print(a, mit)