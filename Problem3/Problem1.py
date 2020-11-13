# 문제1. 다음 세 개의 리스트가 있을 때,
#
# subs = [‘I’, ‘You’]
# verbs = [‘Play’, ‘Love’]
# objs = [‘Hockey’, ‘Football’]
#
# 3형식 문장을 모두 출력해 보세요

subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

for i in range(2) :
    for j in range(2) :
        for k in range(2) :
            print(f'{subs[i]} {verbs[j]} {objs[k]}.')