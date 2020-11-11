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
