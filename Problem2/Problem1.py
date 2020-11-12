# 문제1. 파이썬 경로명 s = &#39;/usr/local/bin/python&#39; 에서 각각의 디렉토리 경로명을 분리하여
# 출력하세요.

s = '/usr/local/bin/python'
solve = s.strip().split('/')
del solve[0]
number = len(solve)
for i in solve :
    if i != solve[number-1] :
        print(f'\'{i}\',', end = ' ')
    else :
        print(f'\'{i}\'')

location = s.rfind('/')
file_name = s[location+1 : ]
file_location = s[ : location]

print(f'\'{file_location}\', \'{file_name}\'')