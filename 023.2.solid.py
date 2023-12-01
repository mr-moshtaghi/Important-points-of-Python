"""
    2. Open/Closed Principle: software entities should be open for extension but close for modification
"""


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def sound(self):
#         if self.name == 'cat':
#             print('meow')
#         elif self.name == 'dog':
#             print('woof')
#         elif self.name == 'snake':
#             print('hiss')
#
#
# missy = Animal('cat')
# jack = Animal('dog')
# mark = Animal('snake')
#
# missy.sound()
# jack.sound()
# mark.sound()


# ====================================================================================

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def sound(self):
#         pass
#
#
# class Cat(Animal):
#     def sound(self):
#         print('meow')
#
#
# class Dog(Animal):
#     def sound(self):
#         print('woof')
#
#
# class Snake(Animal):
#     def sound(self):
#         print('hiss')
