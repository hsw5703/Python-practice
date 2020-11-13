# 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.

num = int(input('몇 개 데이터를 입력하시겠습니까? : '))
print('데이터를 입력해주세요.')

a = [int(input()) for k in range(num)]

for i in range(num) :
    for j in range(1+i, num) :
        if a[i] < a[j] :
            temp = a[j]
            a[j] = a[i]
            a[i] = temp

print(a)