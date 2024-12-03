A = input().split()
A[0] = int(A[0])

B = input().split()
B[0] = int(B[0])

if (A[0] >= 19 or B[0] >= 19) and (A[1] == 'M' or B[1] == 'M'):
    print(1)
else:
    print(0)

