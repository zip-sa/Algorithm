# 0일을 기점으로 -> 2일마다 교실, 3일마다 복도, 12일마다 화장실 청소
n = int(input())

cnt_2, cnt_3, cnt_12 = 0, 0, 0

for k in range(1, n+1):
    if k % 12 == 0:
        cnt_12 += 1
    elif k % 3 == 0:
        cnt_3 += 1
    elif k % 2 == 0:
        cnt_2 += 1

print(cnt_2, cnt_3, cnt_12)
