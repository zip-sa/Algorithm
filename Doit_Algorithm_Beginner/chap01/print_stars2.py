# *를 n개 출력하되 w개마다 줄바꿈하기 2

print('Print -> *')
n = int(input('How many stars? : '))
w = int(input('How often change line? : '))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)