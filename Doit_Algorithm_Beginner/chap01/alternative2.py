# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('how many? : '))

for _ in range(n // 2):
    print('+-', end='')

if n % 2:
    print('+', end='')
    
print()