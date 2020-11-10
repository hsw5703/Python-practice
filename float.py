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

print("hello 'world'")
print('hello \'world\'')
print("hello \"world\"")
print('hello "world"')

print("name" " ad " "name")  # 문자열끼리는 + 사용하지 않아도 된다.

name = '길동'
# name[0] = 'a' 문자열은 변경 불가
age = 40

# print(name + age) 문자열과 숫자는 + 사용할 수 없다.
print(name + str(age))
print(name + format(age, 'd'))
print(format(name, 's') + str(age))  # 굳이 문자열에는 format 안해줘도 되긴 함.

a = """i like Python
Do you AGREE me?"""
print(a.swapcase()) # 대문자는 소문자로 소문자는 대문자로
print(a.capitalize()) # 첫문자만 대문자로, 나머지는 소문자로
print(a.title()) # 단어마다 첫 글자는 대문자로 나머지는 소문자로

a = 1
b = a == 1
print(b, b + 10) # True 값은 1이다.
print(True + True)

e = 2 ** 1024 # Python에서는 long type이 없어져 int형으로 엄청 긴 자료형도 나타낼 수 있다.

number = 2 + 3j
print(number, type(number), number.real, number.imag)
# 복소수의 데이터 타입은 complex이다. .real은 실수부를, .imag는 허수부를 출력한다.

print(2 ** 3 ** 4) # ** 제곱의 연산방향은 뒤에서부터 온다. <-
print((2 ** 3) ** 4)

print(bool(10), bool(0))
print(bool(''), bool(0.), bool([]))

print(abs(-5), abs(5), int(3.9))