#
# class Person:
#     def __init__(self, age):
#         self.__age = age
#
#     def getter_age(self):
#         return self.__age
#
#     def setter_age(self, age):
#         self.__age = age
#
#     def deleter_age(self):
#         del self.__age
#
#
# p1 = Person(26)
#
# print(p1.getter_age())
#
# p1.setter_age(30)
#
# print(p1.getter_age())
#
# p1.deleter_age()
#
# print(p1.getter_age())


class Person:
    def __init__(self):
        self.__age = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


p = Person()

print(p.age)

p.age = 32

print(p.age)

del p.age

print(p.age)
