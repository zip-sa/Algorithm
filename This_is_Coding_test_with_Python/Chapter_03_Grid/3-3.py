# 숫자 카드 게임 | 3-3.py min() 함수를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)