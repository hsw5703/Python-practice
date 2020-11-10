b = 20
print(b, isinstance(b, bool))  # b가 bool타입인지 아닌지 True/False 반환
c = 0b1011  # 2진수로 인식
print(c)  # 10진수로 표시
print(bin(c))  # 2진수로 표현

d = 0o23  # 8진수로 인식
print(d)  # 10진수로 표시
print(oct(d))  # 8진수로 표현

e = 0x34  # 16진수로 인식
print(e)  # 10진수로 표시
print(hex(e))  # 16진수로 표현
