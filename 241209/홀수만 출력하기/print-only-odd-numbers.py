n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    arr.append(num)

for num in arr:
    if num % 2 != 0 and num % 3 == 0:  # 홀수이면서 3의 배수인 경우
        print(num)

# n = int(input())
# arr = []
# k = 0
# 
# for _ in range(n):
#     num = int(input())
#     arr.append(num)
# 
# for _ in range(n):
#     if arr[k] % 2 != 0 and arr[k] % 3 == 0:
#         print(int(arr[k]))
#     k += 1
