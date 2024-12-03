a, b, c = map(int, input().split())

# 11 12 13
if a > b:
    if a < c:
        print(a)
    else:
        print(c)

elif a < b:
    if a > c:
        print(a)
    else:
        print(b) 
