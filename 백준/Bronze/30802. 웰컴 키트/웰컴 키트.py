N = int(input())
size_list = list(map(int, input().split()))
T, P = map(int, input().split())
T_bundle= 0

for i in size_list:
    if i == 0:
            continue
    elif i <= T:
          T_bundle += 1
    elif i % T == 0:
          T_bundle += i // T
    else:
          T_bundle += i // T+1

P_bundle = N // P
Pen = N % P

print(T_bundle)
print(P_bundle, Pen)
