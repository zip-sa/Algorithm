# 10~99 사이의 난수 n개 생성하기 (13이 나오면 중단)

import random

n = int(input("난수의 개수 : "))

for _ in range(n):
    r = random.randint(10,99)
    print(r, end=' ')
    if r == 13:
        print("프로그램 중단")
        break
else:
    print('난수 생성 종료')