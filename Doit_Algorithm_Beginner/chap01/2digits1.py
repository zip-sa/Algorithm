# 2자리 양수 (10~99) 입력받기

print('2자리 양수를 입력하세요.')

while True:
    no = int(input('값을 입력하세요 : '))
    if no >= 10 and no <= 90: # if 10 <= no <= 99: 로 작성해도 동일
        break

print(f'입력받은 양수는 {no}입니다.')