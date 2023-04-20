"""

    general structure =====> lambda arguments : manipulate

"""


def add1(x, y):
    return x + y


add2 = lambda x, y: x + y

print("add1 :", add1(2, 5))

print("add2 :", add2(6, 8))

# __________________________________________________________________________


x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def tavan(i):
    return i * i


print("tavan :", list(map(tavan, x1)))
print("tavan-lambda :", list(map(lambda i: i * i, x1)))


def even(i):
    if i % 2 == 0:
        return True
    return False


print("even :", list(filter(even, x1)))
print("even-lambda :", list(filter(lambda i: i % 2 == 0, x1)))

# _____________________________________________________________________________


x2 = [(4, 'b'), (2, 'a'), (5, 'c'), (1, 'e'), (3, 'd'), (7, 'f')]

print("sorted without lambda (based on the numbers) :", sorted(x2))
print("sorted with lambda (based on the letters)", sorted(x2, key=lambda i: i[1]))

# _______________________________________________________________________________
