n = int(input())
sum_val = 0

for i in range(1, n):
    if n % i == 0: sum_val += i

if sum_val % i == 0:
    print('P')

else: print('N')