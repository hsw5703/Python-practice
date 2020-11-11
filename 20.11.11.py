s = 'I Like Python. I Like Java Also'
print('1번 결과 : ', s.count('Like'))  # 'Like' 단어가 몇 개인지 count

print('2번 결과 : ', s.find('Like'))  # 'Like' 단어의 위치
print('3번 결과 : ', s.find('Like', 5))  # index=5부터 'Like' 단어 위치를 찾는다.
print('4번 결과 : ', s.find('JS'))  # 'JS'라는 단어는 없기 때문에 -1을 반환
print('5번 결과 : ', s.rfind('Like'))  # 'Like' 단어를 뒤에서부터 찾고 그 위치를 반환.

print('6번 결과 : ', s.index('Like'))  # 'Like'의 위치를 반환
# print(s.index('JS')) find와는 다르게 Error가 발생한다.

try:  # 예외 처리 과정
    print('7번 결과 : ', s.index('JS'))
except ValueError as e:
    print('8번 결과 : ', 'Error')
    print('9번 결과 : ', e)  # Error 발생 이유 출력

print('10번 결과 : ', s.rindex('Like'))  # 뒤에서부터 위치를 찾는다.
print('11번 결과 : ', s.startswith('I Like'))  # s라는 문자열이 I Like 로 시작하는지 True / False
print('12번 결과 : ', s.endswith('Also'))  # s라는 문자열이 Also로 끝나는지 True / False
print('13번 결과 : ', s.endswith('Python', 0, 13))  # s의 0~13위치에서 Python으로 끝나는지 여부.

print('----------------------------------------------')

s = '   spam and ham   '
print('1번 결과 : ', '----' + s.strip() + '----')  # 앞 뒤 공백을 없앤다. 단어 사이 공백은 놔둠.
print('2번 결과 : ', '----' + s.rstrip() + '----')  # 오른쪽 공백만 없앤다.
print('3번 결과 : ', '----' + s.lstrip() + '----')  # 왼쪽 공백만 없앤다.

s = '<><>><abc><><def>><><>'
print('4번 결과 : ', '----' + s.strip('<>') + '----')
# '<', '>'를 앞 뒤로 다 없애준다. '<>'를 하나로 보는 게 아니다.

s = 'Hello Java Java'
print('5번 결과 : ', s.replace('Java', 'Python'))  # 문자열 내 Java를 Python으로 치환

s = 'one:two:three'
change = s.split(':')  # ':'을 기준으로 나눠준다.
print('6번 결과 : ', change, type(change))  # list 형식으로 저장된다.

s = 'one:two:three:four:five'
change = s.split(":", 2)  # ':'를 기준으로 나누되, 앞에서부터 2개까지만 나눈다.
print('7번 결과 : ', change)
change = s.split(":", maxsplit=3)  # maxsplit=3는 ':' 기준으로 앞에서부터 3번 나눈다.
print('8번 결과 : ', change)

s = 'one:two:three:four'
change = s.rsplit(":", 2)  # 오른쪽에서부터 ':'를 기준으로 나누되, 뒤에서부터 2개까지만 나눈다.
print('9번 결과 : ', change)

print('----------------------------------------------')

lines = """1st line
2nd line
3rd line
4th line
"""
change = lines.split('\n')  # """ """은 줄간격을 포함한 문자열인데 이 줄간격을 기준으로 나눠준다.
print('1번 결과 : ', change)

change = lines.splitlines()  # split('\n')과 같다.
print('2번 결과 : ',change)

line = '&'.join(change)  # list의 data 사이에 &를 넣어 한 문자열로 만든다.
print('3번 결과 : ', line)

print('4번 결과 : ', '1234'.isdigit())  # 문자열이 숫자인지 판별
print('5번 결과 : ', '1b3d'.isdigit())
print('6번 결과 : ', '1234'.isalpha())  # 문자열이 알파벳인지 판별
print('7번 결과 : ', 'abcd'.isalpha())
print('8번 결과 : ', 'abcd'.islower())  # 문자열이 소문자인지 판별
print('9번 결과 : ', 'ABCD'.isupper())  # 문자열이 대문자인지 판별
print('10번 결과 : ', 'AbCd'.isupper())

print('----------------------------------------------')

# 포멧팅
name = '홍길동'
age = 40

f = 'name : {}, age : {}'
print('1번 결과 : ', f.format(name, age))

f = 'name : {0}, age : {1}'  # index를 주는 방법
print('2번 결과 : ', f.format(name, age))

g = f'name : {name}, age : {age}'  # f는 format을 의미
print('3번 결과 : ', g)

f = 'name : ' + format(name, 's') + ", age : " + format(age, 'd')  # s : string, d : digit
print('4번 결과 : ', f)  # 이 방법은 귀찮고 복잡해서 나머지 방법을 선호한다.

l = [1, 2, 3, 4, 5, 6]
print('5번 결과 : ', l[::-1])  # 역 방향으로 읽는다. a :: b b는 간격으로 한칸씩 뒤에서부터의 의미이다. a는 시작 지점이다.
print('6번 결과 : ', l[5:2:-1])  # index=5부터 2 초과까지 1 간격으로 역순으로 출력한다.

del l[1]  # list의 data를 삭제한다.
print('7번 결과 : ', l)

print('----------------------------------------------')

l = [1, 12, 123, 1234]

l[0:2] = [10, 20]  # index=0~1을 10과 20으로 바꾼다.
print('1번 결과 : ', l)

l[0:2] = [100]  # index=0~1([10, 20])을 [100]으로 바꾼다.
print('2번 결과 : ', l)  # data가 3개로 줄어든다.

l[0:2] = []  # slicing을 이용해 del.
print('3번 결과 : ', l)

l[0:] = []  # slicing을 이용해 전체 data del.
print('4번 결과 : ', l)

l = [1, 12, 123, 1234]
l[1:1] = [456]  # 중간에 삽입.
print('5번 결과 : ', l)

l[5:] = [456]
print('6번 결과 : ', l)

l[:0] = ['처음']  # 첫 자리에 data 추가.
print('7번 결과 : ', l)

l[2:2] = ['새로운', '추가']  # 여러 개의 data를 삽입.
print('8번 결과 : ', l)

print('----------------------------------------------')

s = 'king and queen'

print('1번 결과 : ', s.center(60))  # 60(공백 하나당 1)만큼의 공간에서 가운데 정렬.
print('2번 결과 : ', s.center(60, '-'))  # 공백 대신 '-'를 추가한다.
print('3번 결과 : ', s.ljust(60, '-'))  # 왼쪽 정렬
print('4번 결과 : ', s.rjust(60, '-'))  # 오른쪽 정렬

print('5번 결과 : ', '\n\n'.isspace())  # 줄바꿈과 공백은 공간으로 처리되어 True 출력.
print('6번 결과 : ', '  '.isspace())
print('7번 결과 : ', ''.isspace())  # ''은 빈공간으로 공백 X

print('8번 결과 : ', '20'.zfill(5))  # 총 5칸의 공간에 '20'을 제외한 앞부분을 0으로 채운다.
print('9번 결과 : ', '1234'.zfill(5))
print('10번 결과 : ', '안녕'.zfill(5))

I = [1, 5, 3, 9, 8, 4, 2]
I.sort()  # 오름차순 정렬
print('11번 결과 : ', I)

I.sort(reverse=True)  # 내림차순 정렬
print('12번 결과 : ', I)

I = [10, 2, 22, 9, 8, 33, 4, 11]
I.sort(key=str)  # 문자열을 기준으로 정렬하여 1로 시작하는 숫자를 먼저 정렬 후 2를 정렬.
print('13번 결과 : ', I)

I.sort(key=int)  # 숫자로 보고 오름차순 정렬.
print('14번 결과 : ', I)

print('----------------------------------------------')

a = {1, 2, 3}
print('1번 결과 : ', 2 in a)
print('2번 결과 : ', 3 not in a)

a.add(4)  # 4는 중복이 아니므로 추가된다.
print('3번 결과 : ', a)

a.add(1)  # 중복되는 값은 입력해도 그대로이다.
print('4번 결과 : ', a)

a.discard(2)
print('5번 결과 : ', a)
# 값을 제거한다. set 내부에 없는 값을 입력해도 Error가 발생하지 않는다.

a.remove(4)
print('6번 결과 : ', a)
# 값을 제거한다. set 내부에 없는 값을 입력하면 Error가 발생한다.

a.update({3, 8})  # 여러 데이터를 한번에 추가한다. 단 {} 필요.
print('7번 결과 : ', a)

a.clear()  # set 내부 데이터를 모두 지운다.
print('8번 결과 : ', a)

a.add(1)
print('9번 결과 : ', a)

print('----------------------------------------------')

s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

s3 = s1.union(s2)  # 합집합
print('1번 결과 : ', s3)

s4 = s1.intersection(s2)  # 교집합
print('2번 결과 : ', s4)

s5 = s1.difference(s2)  # 차집합
print('3번 결과 : ', s5)

s6 = s1.symmetric_difference(s2)  # 합집합 - 교집합
print('4번 결과 : ', s6)

print('5번 결과 : ', s1.issuperset(s5))  # s5가 s1의 부분집합인지 여부
print('6번 결과 : ', s6.issuperset(s1))
print('7번 결과 : ', s2.issubset(s3))  # s2가 s3의 부분집합인지 여부

print('----------------------------------------------')

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