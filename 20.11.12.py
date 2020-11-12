# Packing
t = 10, 20, 30, 'Python'  # ( ) 없어도 된다.
print(t, type(t))

# UnPacking
a, b, c, d = t
print(a, b, c, d, type(a))

# a, b, c = t 갯수를 맞추지 않으면 Error

a, *b = [1, 2, 3, 4]  # tuple과 마찬가지로 list도 unpacking 가능.
print(a, '\n', *b)

# UnPacking 확장
t = (1, 2, 3, 4, 5)
a, *b = t
print(a, b, type(b))

print('--------------------------------------------------')

# dictionary 생성
a = dict(one=1, two=2)  # one과 two는 keys, 1과 2는 values. 하지만 거의 안 씀.
print('1번 결과 : ', a)

keys = ['one', 'two', 'three']
values = [1, 2, 3]
dic = dict(zip(keys, values))  # zip으로 서로 다른 list나 tuple을 dictionary로 바꿀 수 있다.
print('2번 결과 : ', dic)

dic = {'one': 1, 'two': 2, 'three': 3}
dic_list = list(dic.items())
# items로 나누고 list화 할 수도 있고, 역으로 tuple list를 dict()를 이용해 dictionary로 바꿀 수도 있다.
print('3번 결과 : ', dic_list)
dic_list = dict(dic_list)
print('4번 결과 : ', dic_list)

# dictionary의 특징 copy와 = 의 차이
dict_al = {'a': 1, 'b': 2, 'c': 3}
p = dict_al
print('5번 결과 : ', p)
print('6번 결과 : ', dict_al)

dict_al['d'] = 4  # p = dict_al로 같은 객체에 묶여있다. 그래서 dict_al에 추가하면 p도 따라 변한다.
print('7번 결과 : ', p)
print('8번 결과 : ', dict_al)

p = dict_al.copy()  # copy는 새로운 객체를 만들어주기 때문에 위와 같이 따라 변하지 않는다.
print('9번 결과 : ', p)
print('10번 결과 : ', dict_al)

dict_al['e'] = 5
print('11번 결과 : ', p)
print('12번 결과 : ', dict_al)

print('--------------------------------------------------')

dict_al = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 객체함수 get()
print('1번 결과 : ', dict_al.get('f'))  # dict_al에 key : 'f'가 없으나 Error가 발생하지 않고 None을 반환.
# print(dict_al['f']) dict_al에 'f'는 없으므로 Error 발생

# setDefault()
print('2번 결과 : ', dict_al.setdefault('e', '----'))
# 기존에 있던 key인 'e'의 경우 'e'의 value를 반환하고 아무것도 변하지 않는다.
print('3번 결과 : ', dict_al)
print('4번 결과 : ', dict_al.setdefault('f', '----'))  # 기존의 key에 없는 'f'인 경우 새롭게 데이터가 추가된다.
print('5번 결과 : ', dict_al)

print('6번 결과 : ', dict_al.pop('a'))  # 'a'의 value를 출력하고 key 'a' 값을 제거한다.
print('7번 결과 : ', dict_al)

k = dict_al.popitem()  # 마지막 데이터를 지운다. 지울 데이터가 없으면 Error. pop()과 동일.
print('8번 결과 : ', k, type(k))
print('9번 결과 : ', dict_al)

dict_al.update({'한글': 'good', '영어': 'difficult'})  # 여러 데이터를 한번에 추가한다.
print('10번 결과 : ', dict_al)

dict_al.clear()  # 빈 dictionary로 만든다.
print('11번 결과 : ', dict_al)

print('--------------------------------------------------')

# zip

s1 = {'foo', 'far', 'baz'}
s2 = {'one', 'two', 'three'}

z = zip(s1, s2)
print('1번 결과 : ', z, type(z))

for t in z:  # s1과 s2가 set(집합) data type이라서 순서가 섞여나온다.
    print(t, type(t))

z = zip(s1, s2)
for a, b in z:
    print(a, b)

print('2번 결과 : ', list(zip(s1, s2)))

for idx, (a, b) in enumerate(z):  # (a, b)의 괄호는 있어도 되고 없어도 된다.
    print('%d : %s %s' % (idex, a, b))  # enumerate : 색인과 데이터를 둘 다 사용하고 싶을 때 쓴다.

z = [('foo', 'one'), ('far', 'two'), ['baz', 'three']]
s3, s4 = zip(*z)  # tuple list를 나눠줄 수도 있다.
print('3번 결과 : ', s3)
print('4번 결과 : ', s4)

print('-----------------------------------------')

# 복합 자료형의 출력 방법
l = [('둘리', 10), ('또치', 20), ('도우너', 30)]
for t in l:
    print('이름 : %s, 나이 : %d' % t)
for a, b in l:
    print(f'이름 : {a}, 나이 : {b}')

# 방법 1
count = 0
for i in ['red', 'blue', 'green', 'yellow']:
    print(f'{count + 1} : {i}')
    count += 1

# 방법 2
for i, value in enumerate(['red', 'blue', 'green', 'yellow']):
    print(f'{i + 1} : {value}')

# enumerate의 형태
print('결과 :', list(enumerate(['red', 'blue', 'green', 'yellow'])))

for i in range(5):
    print('1234')
else:  # 위 for문이 끝까지 동작하면 마지막에 else문을 실행시킨다.
    # 단, for문이나 while문 내에서 break로 탈출 시 실행하지 않는다. (잘 안씀)
    print('over')