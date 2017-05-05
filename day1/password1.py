#! /usr/bin/env python3
# password1.py
pwd = input('What is the password? ')
if pwd == 'apple':   # note use of ==
    # instead of =
    print('Logining on ...')
else:
    print('Incorrect password.')
print('All done!')