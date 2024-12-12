n = int(input())
numbers = []
results = 0

for _ in range(n):
    number = int(input())
    numbers.append(number)
 
for num in numbers:
    if num % 2 != 0 and num % 3 == 0: results += num

print(results)