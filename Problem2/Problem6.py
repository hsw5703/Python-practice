import random
a = random.randint(1, 100)
print('수를 결정하였습니다. 맞추어 보세요')
print('1-100')
i = 0
while True :
    i += 1
    print(i, end='')
    num = int(input('>>'))
    if num > a :
        print('더 낮게')
    elif num < a :
        print('더 높게')
    else :
        print('맞았습니다')
        print('다시 하시겠습니까?(Y/N)>>', end = '')
        i = 0
        nex = input()
        if nex == 'N' :
            break
        a = random.randint(1, 100)