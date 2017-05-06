# donesum_break.py

total = 0
i = 0
while True:
        s = input('Enter a number (or "done"): ')
        if s == "done":
            break
        num = int(s)
        total += num
        i += 1
if i == 1:
    print('You\'ve input one number.')
    print('The sum is ' + str(total) + '.')
elif i == 0:
    print('You didn\'t input any number.')
else:
    print('You\'ve input %s numbers.' % i)
    print('The sum is ' + str(total) + '.')
