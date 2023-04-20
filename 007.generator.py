"""
	Generator => 1.function, 2.experssion(comprehension)

	Lazy Evaluation
"""


def show1():
    return "show..."


def show2():
    yield "show..."
    yield "Hello......"


print("show1 = ", show1())
print("show2 = ", show2())

for i in show2():
    print(i)

print("#############################")


# -----------------------------------------


def show3(num):
    print("starting....")
    while num > 0:
        yield num
        num = num - 1


print(show3(5))

for i in show3(5):
    print(i)

print("##############################")


# -----------------------------------------
def show4(num):
    print("starting....")
    while num > 0:
        yield num
        num = num - 1


s = show4(5)

print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

print("##############################")

# -----------------------------------------


even_nums1 = [x for x in range(11) if x % 2 == 0]  # list comprehension

even_nums2 = (x for x in range(11) if x % 2 == 0)  # generator expression(comprehension)

print(even_nums1)
# print(list(even_nums2))
print(even_nums2)

print(next(even_nums2))
print(next(even_nums2))
print(next(even_nums2))
print(next(even_nums2))

print("##############################")

# -----------------------------------------
