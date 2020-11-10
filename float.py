"""
a, b = 1.2, 2.
print(a.is_integer())  # 객체에 저장된 값이 정수인지 실수인지 판단.
print(b.is_integer())  # 소수점을 가지곤 있으나 소수점 아래 수가 없으므로 False
print(type(a), type(b))

d = 3e3
print(d, type(d))
e = 2e-4
f = 0.2e-5  # 소수점 자리가 길어지면 e를 사용해 표시한다.
print(e, type(e), '\n', f, type(f))
"""

result = divmod(2, 3)  # 2를 3으로 나눈다. tuple 값 하나(몫, 나머지)를 반환.
a, b = divmod(2, 3)  # tuple의 내부 값을 하나씩 받는다. a는 몫, b는 나머지
print(result, type(result))
print(a, b, type(a), type(b))

c = pow(3, 4)  # 3의 4승, pow는 제곱 명령어
print(c)