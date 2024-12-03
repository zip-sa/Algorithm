P1_x, P1_y = map(str, input().split())
P2_x, P2_y = map(str, input().split())
P3_x, P3_y = map(str, input().split())

count = 0

if count == 0:
    if P1_x == 'Y' and int(P1_y) >= 37: count += 1
    if P2_x == 'Y' and int(P2_y) >= 37: count += 1
    if P3_x == 'Y' and int(P3_y) >= 37: count += 1

if count >= 2:
    print("E")
else:
    print("N")

# # 변수 선언 및 입력
# inp = input().split()
# c1, t1 = inp[0], int(inp[1])
# inp = input().split()
# c2, t2 = inp[0], int(inp[1])
# inp = input().split()
# c3, t3 = inp[0], int(inp[1])
# 
# # A가 2명 이상인지 판단하기
# if c1 == 'Y' and t1 >= 37:
#     # 첫 번째 사람이 A라면, 남은 두 사람 중 한 사람이라도 A면 됩니다.
#     if (c2 == 'Y' and t2 >= 37) or (c3 == 'Y' and t3 >= 37):
#         print("E")
#     else:
#         print("N")
# else:
#     # 첫 번째 사람이 A가 아니라면, 남은 두 사람 모두 A여야만 합니다.
#     if (c2 == 'Y' and t2 >= 37) and (c3 == 'Y' and t3 >= 37):
#         print("E")
#     else:
#         print("N")