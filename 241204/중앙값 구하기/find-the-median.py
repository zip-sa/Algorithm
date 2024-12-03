a, b, c = map(int, input().split())

# 3 2 1
if a > b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    print(b)