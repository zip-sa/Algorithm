arr = list(map(int, input().split()))

n = len(arr)
arr_sorted = sorted(arr)

print((arr_sorted[n//2] + arr_sorted[n//2-1])/2 if n%2==0 else arr_sorted[n//2])
