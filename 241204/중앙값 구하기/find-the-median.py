a, b, c = map(int, input().split())

# 11 12 13
if a > b:
    if a < c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)

elif a > c:
    if a < b:
        print(a)
    elif b < c:
        print(b)
    else:
        print(c) 
