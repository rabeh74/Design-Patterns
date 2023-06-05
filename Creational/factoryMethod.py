from abc import ABC , abstractmethod

class Creator(ABC):
    @abstractmethod
    def factoryMethod(self):
        pass

    def some_operation(self):
        product = self.factoryMethod()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    def factoryMethod(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factoryMethod(self):
        return ConcreteProduct2()

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self):
        return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self):
        return "{Result of the ConcreteProduct2}"

def client_code(creator):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
    print("\n")