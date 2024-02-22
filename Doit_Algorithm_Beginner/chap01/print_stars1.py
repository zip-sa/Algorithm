# *를 n개 출력하되 w개마다 줄바꿈하기 1

print('Print -> *')
n = int(input('How many stars? : '))
w = int(input('How often change line? : '))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()
    
if n % w:
    print()