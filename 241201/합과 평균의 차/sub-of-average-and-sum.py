arr = list(map(int,input().split()))
s = sum(arr)
m = int(s/3)

print(s, m, s-m, sep="\n")