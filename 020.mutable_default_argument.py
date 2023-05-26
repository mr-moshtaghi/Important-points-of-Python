# def show(name, person=[]):
#     person.append(name)
#     return person


def show(name, person=None):
    if person is None:
        person = []
    person.append(name)
    return person


s1 = show('ahmad')
print(s1)

s2 = show("ali")
print(s2)

s3 = show("sajjad")
print(s3)
