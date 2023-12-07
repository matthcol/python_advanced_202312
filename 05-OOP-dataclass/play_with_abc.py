from abc import ABC, abstractmethod

class MyAbtractClass(ABC):

    @abstractmethod
    def f(self):
        pass


# TypeError: Can't instantiate abstract class MyAbtractClass without an implementation for abstract method 'f'
# o = MyAbtractClass()