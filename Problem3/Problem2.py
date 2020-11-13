# 문제2. range() 함수와 유사한 frange() 함수를 작성해 보세요.
# frange() 함수는 실수 리스트를 반환합니다.

def frange(val, base=0.0, step=0.1):
    results = []
    print(type(val),type(base),type(step))
    num = int((val - base) // step)

    for i in range(1, num+1) :
        results.append(val-step*i)

    return results


print(frange(2))
print(frange(2.0, 1.0))
print(frange(3.0, 1.0, 0.5))