mid, final = map(int,input().split())

if mid >= 90:
    if final >= 95:
        print(10)
    elif final >= 90:
        print(5)
else:
    print(0)
