# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

def sum(number) :
    a = 0
    for i in number :
        a = a + i
    return a

a = int(input('몇 개 입력할건가요? : '))
b = [int(input()) for i in range(a)]
result = sum(b)
print(result)