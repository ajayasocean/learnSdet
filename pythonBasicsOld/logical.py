#logical operators

if 1 < 4 and 4 > 3:
    a = True
    print('and result',a)
elif 1 > 4 or 4 > 3:
    a = True
    print('or result',a)
elif not(1 < 5):
    a = True
    print('not result', a)
else:
    a = True
    print('else',a)
