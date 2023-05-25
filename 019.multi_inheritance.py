# class A:
#     def show(self):
#         return "show methode..."
#
#
# class B:
#     def say(self):
#         return "say methode..."
#
#
# class C(A, B):
#     pass
#
#
# c1 = C()
# print(c1.show())
# print(c1.say())

# ===================================   1   =====================================================

# class Vehicle:
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#     def show(self):
#         return f"{self.name} top speed is {self.speed}"
#
#
# class Car:
#     def joy(self):
#         return f"Driving {self.name} is Awesome..."
#
#
# class Motor:
#     def joy(self):
#         return f"Riding {self.name} is Awesome..."
#
#
# class Sedan(Car, Vehicle):
#     pass
#
#
# class Retro(Motor, Vehicle):
#     pass
#
#
# s1 = Sedan("pride", 180)
# print(s1.show())
# print(s1.joy())

# ==============================    2     ================================================

# class A:
#     a_calls = 0
#
#     def call(self):
#         print("calling A class...")
#         A.a_calls += 1
#
#
# class B(A):
#     b_calls = 0
#
#     def call(self):
#         print("calling B class...")
#         B.b_calls += 1
#         A.call(self)
#
#
# class C(A):
#     c_calls = 0
#
#     def call(self):
#         print("calling C class...")
#         C.c_calls += 1
#         A.call(self)
#
#
# class D(B, C):
#     d_calls = 0
#
#     def call(self):
#         print("calling D class...")
#         D.d_calls += 1
#         B.call(self)
#         C.call(self)
#
#
# d1 = D()
# d1.call()
# print(f"d_calls = {d1.d_calls}")
# print(f"c_calls = {d1.c_calls}")
# print(f"b_calls = {d1.b_calls}")
# print(f"a_calls = {d1.a_calls}")

# =====================     3     ==============================

# class A:
#     a_calls = 0
#
#     def call(self):
#         print("calling A class...")
#         A.a_calls += 1
#
#
# class B(A):
#     b_calls = 0
#
#     def call(self):
#         print("calling B class...")
#         B.b_calls += 1
#         super().call()
#
#
# class C(A):
#     c_calls = 0
#
#     def call(self):
#         print("calling C class...")
#         C.c_calls += 1
#         super().call()
#
#
# class D(B, C):
#     d_calls = 0
#
#     def call(self):
#         print("calling D class...")
#         D.d_calls += 1
#         super().call()
#
#
# d1 = D()
# d1.call()
# print(f"d_calls = {d1.d_calls}")
# print(f"c_calls = {d1.c_calls}")
# print(f"b_calls = {d1.b_calls}")
# print(f"a_calls = {d1.a_calls}")
#
# help(D)

# ====================     4      =====================================

# class A:
#     def call(self, a=''):
#         print(f"A class => {a}")
#
#
# class B:
#     def call(self, b='', **kwargs):
#         print(f"B class => {b}")
#         super().call(**kwargs)
#
#
# class C(B, A):
#     def call(self, c='', **kwargs):
#         print(f"C class => {c}")
#         super().call(**kwargs)
#
#
# c1 = C()
# c1.call(c="ccc", b="bbb", a="aaa")

# =================     5     =======================

class A:
    def call(self, a=''):
        print(f"A class => {a}")


class B:
    def call(self, b='', a='', **kwargs):
        print(f"B class => {b}")
        print(f"a in B class => {a}")
        kwargs['a'] = a
        super().call(**kwargs)


class C(B, A):
    def call(self, c='', **kwargs):
        print(f"C class => {c}")
        super().call(**kwargs)


c1 = C()
c1.call(c="ccc", b="bbb", a="aaa")
