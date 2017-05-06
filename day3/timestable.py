#timestable.py

for row in range(1, 10):
    for col in range(1, 10):
        prod = row * col
        if prod < 10:
            print(' ', end='')
        #print(' ', end=' ')
        print('%s' % row, '*', '%s' % col, '=', '%s' % prod, ' ', end='')
    print()
