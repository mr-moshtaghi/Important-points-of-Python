def show1(name, age, height):
    print(name, age, height)


print("======show1.....======")
show1('sajjad', 26, 180)

# =======================================

l = ['sajjad', 25, 175]


def show2(name, age, height):
    print(name, age, height)


print("======show2.....======")
show2(l[0], l[1], l[2])

# =======================================

l = ['sajjad', 24, 170]


def show3(name, age, height):
    print(name, age, height)


print("======show3.....======")
show3(*l)

# =======================================

dic = {'name': 'sajjad', 'age': 24, 'height': 170}
dic2 = {'age': 23, 'name': 'sajjad', 'height': 165}
dic3 = {'age': 23, 'name': 'sajjad', 'fhehssdkh': 165}


def show4(name, age, height):
    print(name, age, height)


print("======show4.....======")
show4(*dic)
show4(**dic)
show4(**dic2)
show4(**dic3)
