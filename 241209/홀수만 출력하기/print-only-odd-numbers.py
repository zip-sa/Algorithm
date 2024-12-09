n = int(input())
arr = []
k = 0

for _ in range(n):
    num = int(input())
    arr.append(num)

for _ in range(n):
    if arr[k] % 2 != 0 and arr[k] % 3 == 0:
        print(int(arr[k]))
    k += 1
