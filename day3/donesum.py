# donesum.py

total = 0
s = input('Enter a number (or "done"): ')
i = 0
while s != "done":
    num = int(s)
    total = total + num
    i = i + 1
    s = input('Enter a number (or "done"): ')
if i == 1:
    print('You\'ve input one number.')
    print('The sum is ' + str(total) + '.')
elif i == 0:
    print('You didn\'t input any number.')
else:
    print('You\'ve input %s numbers.' % i)
    print('The sum is ' + str(total) + '.')
