# 리스트에서 임의의 원솟값을 업데이트하기

def change(lst, idx, val):
    lst [idx] = val

x = [11, 22, 33, 44, 55]
print('x = ', x)

index = int(input("업데이트할 인덱스 : "))
value = int(input("새로운 값 : "))

# print(id(value), id(x[index]))
change(x, index, value)
# print(id(value), id(x[index]))
print(f'x = {x}')