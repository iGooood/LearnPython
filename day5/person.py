# person.py

# !user/bin/env python3


class Person:
    """ Class to represent a person
    """
    def __init__(self):
        self.name = ''
        self.age = 0

    def display(self):
        print(self)

    def __str__(self):
        return "Person('%s', %d)" % (self.name, self.age)

    def __repr__(self):
        return str(self)


p = Person()
print(p)
p.name = 'Bob'
p.age = 27
# p.display()
str(p)

print(p)
