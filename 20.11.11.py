s = 'I Like Python. I Like Java Also'
print(s.count('Like'))  # 'Like' 단어가 몇 개인지 count

print(s.find('Like'))  # 'Like' 단어의 위치
print(s.find('Like', 5))  # index=5부터 'Like' 단어 위치를 찾는다.
print(s.find('JS'))  # 'JS'라는 단어는 없기 때문에 -1을 반환
print(s.rfind('Like'))  # 'Like' 단어를 뒤에서부터 찾고 그 위치를 반환.

print(s.index('Like'))  # 'Like'의 위치를 반환
# print(s.index('JS')) find와는 다르게 Error가 발생한다.

try:  # 예외 처리 과정
    print(s.index('JS'))
except ValueError as e:
    print('Error')
    print(e)  # Error 발생 이유 출력

print(s.rindex('Like'))  # 뒤에서부터 위치를 찾는다.
print(s.startswith('I Like'))  # s라는 문자열이 I Like 로 시작하는지 True / False
print(s.endswith('Also'))  # s라는 문자열이 Also로 끝나는지 True / False
print(s.endswith('Python', 0, 13))  # s의 0~13위치에서 Python으로 끝나는지 여부.

s = '   spam and ham   '
print(s.strip())  # 앞 뒤 공백을 없앤다. 단어 사이 공백은 놔둠.
print(s.rstrip() + '----')  # 오른쪽 공백만 없앤다.
print('----' + s.lstrip() + '----')  # 왼쪽 공백만 없앤다.

s = '<><>><abc><><def>><><>'
print('----' + s.strip('<>') + '----')
# '<', '>'를 앞 뒤로 다 없애준다. '<>'를 하나로 보는 게 아니다.

s = 'Hello Java Java'
print(s.replace('Java', 'Python'))  # 문자열 내 Java를 Python으로 치환

s = 'one:two:three'
change = s.split(':')  # ':'을 기준으로 나눠준다.
print(change, type(change))  # list 형식으로 저장된다.

s = 'one:two:three:four:five'
change = s.split(":", 2)  # ':'를 기준으로 나누되, 앞에서부터 2개까지만 나눈다.
print(change)
change = s.split(":", maxsplit=2)  # maxsplit=2는 ':' 기준으로 앞에서부터 3개의 묶음으로 만든다.
print(change)

s = 'one:two:three:four'
change = s.rsplit(":", 2)  # 오른쪽에서부터 ':'를 기준으로 나누되, 앞에서부터 2개까지만 나눈다.
print(change)

lines = """1st line
2nd line
3rd line
4th line
"""
change = lines.split('\n')  # """ """은 줄간격을 포함한 문자열인데 이 줄간격을 기준으로 나눠준다.
print(change)

change = lines.splitlines()  # split('\n')과 같다.
print(change)

line = '&'.join(change)  # list의 data 사이에 &를 넣어 한 문자열로 만든다.
print(line)

print('1234'.isdigit())  # 문자열이 숫자인지 판별
print('1b3d'.isdigit())
print('1234'.isalpha())  # 문자열이 알파벳인지 판별
print('abcd'.isalpha())
print('abcd'.islower())  # 문자열이 소문자인지 판별
print('ABCD'.isupper())  # 문자열이 대문자인지 판별
print('AbCd'.isupper())

# 포멧팅
name = '홍길동'
age = 40

f = 'name : {}, age : {}'
print(f.format(name, age))

f = 'name : {0}, age : {1}'  # index를 주는 방법
print(f.format(name, age))

g = f'name : {name}, age : {age}'  # f는 format을 의미
print(g)

f = 'name : ' + format(name, 's') + ", age : " + format(age, 'd')  # s : string, d : digit
print(f)  # 이 방법은 귀찮고 복잡해서 나머지 방법을 선호한다.

l = [1, 2, 3, 4, 5, 6]
print(l[::-1])  # 역 방향으로 읽는다. a :: b b는 간격으로 한칸씩 뒤에서부터의 의미이다. a는 시작 지점이다.
print(l[5:2:-1])  # index=5부터 2 초과까지 1 간격으로 역순으로 출력한다.

del l[1]  # list의 data를 삭제한다.
print(l)

l = [1, 12, 123, 1234]

l[0:2] = [10, 20]  # index=0~1을 10과 20으로 바꾼다.
print(l)

l[0:2] = [100]  # index=0~1([10, 20])을 [100]으로 바꾼다.
print(l)  # data가 3개로 줄어든다.

l[0:2] = []  # slicing을 이용해 del.
print(l)

l[0:] = []  # slicing을 이용해 전체 data del.
print(l)

l = [1, 12, 123, 1234]
l[1:1] = [456]  # 중간에 삽입.
print(l)

l[5:] = [456]
print(l)

l[:0] = ['처음']  # 첫 자리에 data 추가.
print(l)

l[2:2] = ['새로운', '추가']  # 여러 개의 data를 삽입.
print(l)

a = [1, 2, 3, 4, 5, 6]
a.insert(2, ['a', 'b', 'c']) # slicing과 다르게 리스트로도 넣을 수 있다.
print(a)
a.append('이름') # 마지막에 추가.
print(a)
a.reverse() # 역순 정렬
print(a)

try :
    a.remove('d')
except ValueError as e :
    print('Error') # remove는 값이 없을 때 Error가 발생한다.

a.remove(['a', 'b', 'c'])
a.remove('이름')
print(a)