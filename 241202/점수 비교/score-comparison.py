A_eng, A_math = map(int, input().split())
B_eng, B_math = map(int, input().split())

print(int(A_eng > B_eng and A_math > B_math))