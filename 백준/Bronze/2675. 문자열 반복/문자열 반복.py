T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    r, S = map(str, input().split())  # 반복 횟수 r과 문자열 S 입력
    R = int(r)  # 반복 횟수 R을 정수로 변환
    
    for char in S:  # 문자열 S의 각 문자에 대해
        print(char * R, end='')  # 문자를 R번 반복해서 출력
    print()  # 줄 바꿈
