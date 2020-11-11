# 다음과 같은 출력이 되도록 이중 for~in 문을 사용한 코드를 작성하세요.

count = int(input('몇 줄 짜리로 출력하시겠습니까? : '))
for i in range(count) :
    for j in range(i+1) :
        print('*', end='')
    if i != count-1 :
        print('\n', end='')
