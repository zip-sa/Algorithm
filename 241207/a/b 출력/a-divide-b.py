def divide_to_21_decimal_places(a, b):
    # 정수 부분 출력
    print(a // b, end="")  # 몫 출력
    print(".", end="")     # 소수점 출력

    # 나머지 계산
    remainder = a % b

    # 소수점 아래 21자리 계산
    for _ in range(20):
        remainder *= 10
        digit = remainder // b  # 현재 자리수 몫
        print(digit, end="")    # 자리수 출력
        remainder %= b          # 나머지 갱신

# 입력
a, b = map(int, input().split())
divide_to_21_decimal_places(a, b)


# def divide_to_21_decimal_places(a, b):
#     result = []
#     remainder = a % b
# 
#     # 몫 계산
#     result.append(a // b)
# 
#     # 소수점 아래 계산
#     result.append('.')  # 소수점 추가
# 
#     for _ in range(20):
#         remainder *= 10
#         digit = remainder // b
#         result.append(digit)
#         remainder %= b
# 
#     # 문자열로 변환하여 출력
#     truncated_result = ''.join(map(str, result))
#     print(truncated_result)
# 
