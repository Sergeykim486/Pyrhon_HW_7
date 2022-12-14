def printtable(data):
    res = ''
    coint = 0
    for i in data:
        if coint != 0:
            res = res + '\n'
        for j in i:
            res = res + str(i[j]) + '  '
        coint += 1
    return res