# a부터 b까지 정수의 합 구하기 (for 문)

print('sum a to b')
a = int(input('a : '))
b = int(input('b : '))

if a > b:
    a, b = b, a

sum = 0

for i in range(a, b+1):
    sum += i

print(f'{a}부터 {b}까지 정수의 합 : {sum}')