numbers = []
cnt = 0

for _ in range(10):
    number = int(input())
    numbers.append(number)

for odd in numbers:
    if odd % 2 != 0:
        cnt += 1

print(cnt)
