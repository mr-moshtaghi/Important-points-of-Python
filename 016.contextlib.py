import contextlib


# @contextlib.contextmanager
# def show():
#     print("starting function show...")  # __enter__
#
#     yield {1000}
#
#     print("ending function show...")  # __exit__
#
#
# with show() as f:
#     print(f)
#     print("hello")


# @contextlib.contextmanager
# def show(name):
#     print("starting function show...", name)  # __enter__
#
#     yield {1000}
#
#     print("ending function show...", name)  # __exit__
#
#
# with show("ahmad") as f, show("ali") as a, show("sajjad") as s:
#     print(f)
#     print("hello")


class A(contextlib.ContextDecorator):
    def __enter__(self):
        print("starting context manger...")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closing context manger")


@A()
def show():
    print("show function...")


show()
