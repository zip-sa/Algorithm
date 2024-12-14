a, b = map(int, input().split())
val_sum = 0

if a >= b:
    for i in range(b, a+1):
        if i % 5 == 0: val_sum += i
else:
    for i in range(a, b+1):
        if i % 5 == 0: val_sum += i

print(val_sum)
