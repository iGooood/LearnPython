# person.py

# !user/bin/env python3


class Person:
    """ Class to represent a person
    """
    def __init__(self, name = '', age = 0):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 0 < age <= 150:
            self._age = age

    def display(self):
        print(self)

    def __str__(self):
        return "Person('%s', %d)" % (self._name, self._age)

    def __repr__(self):
        return str(self)

p = Person('Lisa', -6)
print(p)
