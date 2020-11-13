def area(width, height):
    return width * height


print(area(10, 20))
print(area(width=10, height=20))
print(area(height=20, width=10))
print(area(10, height=20))


# print(area(20, width = 10))
# print(area(height = 20, 10))

def a(num):
    print(num)


# a(10, 20, 30)
a([10, 20, 30])


def b(*num):
    print(num)


b(10, 20, 30)
b([10, 20, 30])


def c(a, *num):
    print(a, num)


c(10, 20, 30)
c([10, 20, 30])


def sum(*a):  # 입력된 모든 값을 더하는 함수
    s = 0
    for i in a:
        s += i
    return s


print(sum(10, 20, 30))

def f(t) :
    t = 20
a = 10
f(a)
print(a)

def h(t) : # 불변 객체를 인수로 전달
    t = (10, 20, 30)
a = (1, 2, 3)
h(a)
print(a)

def g(t) : # 가변 객체를 인수로 전달
    t[0] = 0

a = [1, 2, 3]
g(a)
print(a)