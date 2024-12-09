arr = []
cnt = 0
i = 0

for _ in range(5):
    num = int(input())
    arr.append(num)

for num in arr:
    if num % 2 == 0: cnt += 1

print(cnt)