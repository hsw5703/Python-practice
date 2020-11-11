# 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요

try :
    number = int(input('수를 입력하세요 : '))
    if type(number) is int :
        if number % 3 == 0 :
            print(f'{number}은 3의 배수입니다.')
        else :
            print(f'{number}은 3의 배수가 아닙니다.')
except ValueError as e :
    print('정수가 아닙니다')