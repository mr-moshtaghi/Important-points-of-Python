class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def __repr__(self):
        # return f'Person({self.name} , {self.age})'
        return f'{self.__class__.__name__}({self.name} , {self.age})'


P = Person('amir', 21)

print(P)

print(str(P))

print(repr(P))
