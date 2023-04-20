def show1(value):
    if value:
        return value
    else:
        return None


def show2(value):
    if value:
        return value
    else:
        return


def show3(value):
    if value:
        return value


print(type(show1(1)))
print(type(show2(1)))
print(type(show3(1)))

print(type(show1(0)))
print(type(show2(0)))
print(type(show3(0)))
