a, b = map(int, input().split())
val_sum = 0
cnt = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        val_sum += i
        cnt += 1

print(f"{val_sum} {val_sum/cnt:.1f}")