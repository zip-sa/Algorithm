# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('how many? : '))

for i in range(n):
    if i % 2:
        print('-', end='')
    else:
        print('+', end='')

print()