a, b, c = map(int, input().split())
same = 0
samei = 0
if a == b:
    same += 1
    samei = a
if a == c:
    same += 1
    samei = a
if b == c:
    same += 1
    samei = b

if same == 0:
    maxi = 0
    if a > b:
        if b > c:
            maxi = a
        else:
            if a < c:
                maxi = c
            else:
                maxi = a
    else:
        if b > c:
            maxi = b
        else:
            maxi = c

    print(maxi * 100)

elif same == 1:
    print((1000 + (samei*100)))

else:
    print((10000 + (samei * 1000)))