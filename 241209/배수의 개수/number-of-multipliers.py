arr = []

for _ in range(10):
    num = int(input())
    arr.append(num)

cnt_3 = 0
cnt_5 = 0

for num in arr:
    if num % 3 == 0: cnt_3 += 1
    if num % 5 == 0: cnt_5 += 1

print(cnt_3, cnt_5)