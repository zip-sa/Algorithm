A_math, A_eng = map(int,input().split())
B_math, B_eng = map(int,input().split())

if A_math > B_math:
    print("A")
    
if A_math == B_math:
    print("A" if A_eng > B_eng else "B")

if A_math < B_math:
    print("B")

# if a_math > b_math or (a_math == b_math and a_eng > b_eng):
#     print("A")
# else:
#     print("B")