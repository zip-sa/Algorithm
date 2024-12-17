numbers = list(map(int, input().split()))
val_sum = 0

for num in numbers:
    val_sum += num**2

print(val_sum%10)
