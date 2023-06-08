from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        print("Meow...")


class Dog(Animal):
    def talk(self):
        print("Woof...")


c = Cat("Missy")
d = Dog("jack")

c.talk()
d.talk()
