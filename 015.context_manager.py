# f = open("test_context_manager.txt", "r")
# for i in f:
#     print(i)
#
# f.close()


# with open("test_context_manager.txt", "r") as f:
#     for i in f:
#         print(i)


# class A:
#     def __enter__(self):
#         print("starting context manger...")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("closing context manger")
#
#
# def show():
#     print("show function...")
#
#
# with A():
#     show()


class FileManager:

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print(f"Type : {exc_type}")
    #     print(f"Value : {exc_val}")
    #     print(f"Traceback : {exc_tb}")
    #
    #     self.file.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Type : {exc_type}")
        print(f"Value : {exc_val}")
        print(f"Traceback : {exc_tb}")

        self.file.close()

        return True


with FileManager("test_context_manager.txt", "r") as f:
    for i in f:
        print(i)

    f.idk()
