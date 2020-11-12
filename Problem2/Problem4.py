for i in range(1, 100) :
    a = str(i)
    num = len(a)
    b = 0
    count = 0
    for j in range(num) :
        if a[j] == '3' or a[j] == '6' or a[j] == '9' :
            count += 1
            b = 1
    if b == 1 :
        print(i, '짝'*count)