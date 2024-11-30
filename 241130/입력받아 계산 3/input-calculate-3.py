#a = int(input())
#b = int(input())
#
#print(a*b)

import sys
a, b = map(int, sys.stdin.read().split("\n"))
print(a * b)