for n in range(4, 200):
    s = '3' + '5'*n
    while '25' in s or '355' in s or '555' in s:                                             
        if '25' in s:
            s = s.replace('25', '3', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '23', 1)
    summ = 0
    for d in s:
        summ += int(d)

    if summ == 27:
        print(summ, n)

