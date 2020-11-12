# Packing
t = 10, 20, 30, 'Python'
print(t, type(t))

# UnPacking
a, b, c, d = t
print(a, b, c, d, type(a))

# a, b, c = t 갯수를 맞추지 않으면 Error

a, *b = [1, 2, 3, 4] # tuple과 마찬가지로 list도 unpacking 가능.
print(a, '\n', *b)

# UnPacking 확장
t = (1, 2, 3, 4, 5)
a, *b = t
print(a, b, type(b))

# dictionary 생성
a = dict(one = 1, two = 2) # one과 two는 keys, 1과 2는 values.
print(a)

keys = ['one', 'two', 'three']
values = [1, 2, 3]
dic = dict(zip(keys, values)) # zip으로 서로 다른 list나 tuple을 dictionary로 바꿀 수 있다.
print(dic)

dic = {'one' : 1, 'two' : 2, 'three' : 3}
dic_list = list(dic.items()) # items로 나누고 list화 할 수도 있고, 역으로 tuple list를 dict()를 이용해 dictionary로 바꿀 수도 있다.
print(dic_list)
dic_list = dict(dic_list)
print(dic_list)

# dictionary의 특징 copy와 = 의 차이
dict_al = {'a': 1, 'b': 2, 'c': 3}
p = dict_al
print(p)
print(dict_al)

dict_al['d'] = 4
print(p)
print(dict_al)

p = dict_al.copy()
print(p)
print(dict_al)

dict_al['e'] = 5
print(p)
print(dict_al)

# 객체함수 get()
print(dict_al.get('f'))  # dict_al에 key : 'f'가 없으나 Error가 발생하지 않고 None을 반환.
# print(dict_al['f']) dict_al에 'f'는 없으므로 Error 발생

# setDefault()
print(dict_al.setdefault('e', '----'))  # 기존에 있던 key인 'e'의 경우 'e'의 value를 반환하고 아무것도 변하지 않는다.
print(dict_al)
print(dict_al.setdefault('f', '----'))  # 기존의 key에 없는 'f'인 경우 새롭게 데이터가 추가된다.
print(dict_al)

print(dict_al.pop('a'))  # 'a'의 value를 출력하고 key 'a' 값을 제거한다.
print(dict_al)

k = dict_al.popitem() # 마지막 데이터를 지운다. 지울 데이터가 없으면 Error.
print(k, type(k))
print(dict_al)

dict_al.update({'한글' : 'good', '영어' : 'difficult'}) # 여러 데이터를 한번에 추가한다.
print(dict_al)

dict_al.clear()  # 빈 dictionary로 만든다.
print(dict_al)

# zip

s1 = {'foo', 'far', 'baz'}
s2 = {'one', 'two', 'three'}

z = zip(s1, s2)
print(z, type(z))

for t in z:  # s1과 s2가 set(집합) data type이라서 순서가 섞여나온다.
    print(t, type(t))

z = zip(s1, s2)
for a, b in z:
    print(a, b)

print(list(zip(s1, s2)))

for idx, (a, b) in enumerate(z) : # (a, b)의 괄호는 있어도 되고 없어도 된다.
    print('%d : %s %s' %(idex, a, b))

z = [('foo', 'one'), ('far', 'two'), ['baz', 'three']]
s3, s4 = zip(*z) # tuple list를 나눠줄 수도 있다.
print(s3)
print(s4)

# 복합 자료형의 출력 방법
l = [('둘리', 10), ('또치', 20), ('도우너', 30)]
for t in l:
    print('이름 : %s, 나이 : %d' % t)
for a, b in l:
    print(f'이름 : {a}, 나이 : {b}')

# enumerate
# 색인과 데이터를 둘 다 사용하고 싶을 때 쓴다.

# 방법 1
count = 0
for i in ['red', 'blue', 'green', 'yellow'] :
    print(f'{count+1} : {i}')
    count += 1

# 방법 2
for i, value in enumerate(['red', 'blue', 'green', 'yellow']) :
    print(f'{i+1} : {value}')

# enumerate의 형태
print(list(enumerate(['red', 'blue', 'green', 'yellow'])))

for i in range(5) :
    print('1234')
else : # 위 for문이 끝까지 동작하면 마지막에 else문을 실행시킨다.
    print('over')

for i in range(5):
    if i < 4 :
        print('1234')
        break
else:  # 단 break가 있다면 for문과 else문 둘 다 탈출.
    print('over')