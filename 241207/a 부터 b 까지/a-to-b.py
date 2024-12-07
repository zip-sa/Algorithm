a, b = map(int, input().split())
print(a, end=' ')

while a < b and (a*2 < b or a+2 < b):
    if a % 2 != 0:
        a *= 2
        print(a, end=' ')

    elif a % 3 != 0:
        a += 3
        print(a, end=' ')
    