def calculate_bracket_value(brackets):
    stack = []
    result = 0
    temp = 1  # 중간 계산을 위한 임시 변수
    
    for i, ch in enumerate(brackets):
        if ch == '(':
            stack.append(ch)
            temp *= 2  # '('를 만난 경우 2를 곱해줍니다.
        elif ch == '[':
            stack.append(ch)
            temp *= 3  # '['를 만난 경우 3을 곱해줍니다.
        elif ch == ')':
            # 스택이 비어있거나 최상단에 '('가 없으면 잘못된 괄호열
            if not stack or stack[-1] != '(':
                return 0
            # 바로 이전 문자가 '('인 경우 temp 값을 누적
            if brackets[i-1] == '(':
                result += temp
            stack.pop()
            temp //= 2  # '('에 대한 연산이 끝났으므로 다시 나눠줍니다.
        elif ch == ']':
            # 스택이 비어있거나 최상단에 '['가 없으면 잘못된 괄호열
            if not stack or stack[-1] != '[':
                return 0
            # 바로 이전 문자가 '['인 경우 temp 값을 누적
            if brackets[i-1] == '[':
                result += temp
            stack.pop()
            temp //= 3  # '['에 대한 연산이 끝났으므로 다시 나눠줍니다.
        else:
            # 올바르지 않은 문자 입력 처리
            return 0
    
    # 스택이 비어있어야 올바른 괄호열
    if stack:
        return 0
    return result

# 입력
brackets = input().strip()
print(calculate_bracket_value(brackets))
