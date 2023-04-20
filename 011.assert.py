# x = 4
# assert x == 5
# print("x is equals to 5")

# ========================================
#
# x = 4
# assert x == 4
# print("x is equals to 4")

# ========================================

# shoe = {'name': 'nike', 'price': 400}
#
#
# def apply_discount(product, discount):
#     price = product['price'] - discount
#     return price
#
#
# print(apply_discount(shoe, 30))
# print(apply_discount(shoe, 700))


# ========================================

# shoe = {'name': 'nike', 'price': 400}
#
#
# def apply_discount(product, discount):
#     price = product['price'] - discount
#     assert 0 <= price <= product['price']
#     return price
#
#
# print(apply_discount(shoe, 30))
# print(apply_discount(shoe, 700))


# =========================================
#
# shoe = {'name': 'nike', 'price': 400}
#
#
# def apply_discount(product, discount):
#     price = product['price'] - discount
#     assert 0 <= price <= product['price'], "sorry"  # show message
#     return price
#
#
# print(apply_discount(shoe, 30))
# print(apply_discount(shoe, 700))


# ==============================================

x = 4
assert (x == 5,)
print("x is equals to 5")
