"""
    shallow copy vs deep copy
        only for mutable object(list, dictionary, set)
"""

a1 = [1, 2, 3, 4]
b1 = a1

print("id of a1 =", id(a1))
print("id of b1 =", id(b1))

b1[0] = 11

print("list a1 = ", a1)
print("list b1 = ", b1)

# ===================================================

print("======================================================")

a2 = [1, 2, 3, 4]
b2 = list(a2)

print("id of a2 =", id(a2))
print("id of b2 =", id(b2))

b2[0] = 11

print("list a2 = ", a2)
print("list b2 = ", b2)


# ===================================================

print("======================================================")

a3 = [1, 2, 3, 4, [5, 6]]
b3 = list(a3)

print("id of a3 =", id(a3))
print("id of b3 =", id(b3))

b3[4][0] = 55

print("list a3 = ", a3)
print("list b3 = ", b3)




