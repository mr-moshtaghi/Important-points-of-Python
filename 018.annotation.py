import typing as tp


# def show(n, a):
#     return f"{n} is {a} years old"


def show(n: str, a: int) -> str:
    return f"{n} is {a} years old"


print(show("sajjad", 26))


# def shows(names: list[str]):
#     for name in names:
#         print(name)


def shows(names: tp.List[str]):
    for name in names:
        print(name)


shows(["ahmad", "ali", "sajjad"])
