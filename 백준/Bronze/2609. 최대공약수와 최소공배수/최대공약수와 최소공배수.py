def solution(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_result = gcd(a, b)
    lcm_result = a * b // gcd_result
    print(gcd_result)
    print(lcm_result)

# Input
a, b = map(int, input().split())
solution(a, b)
