n = int(input())
sum_val = 0

for i in range(1, n+1):
    if i % n == 0: sum_val += i

if sum_val % i == 0:
    print('P')

else: print('N')