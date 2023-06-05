from abc import ABC , abstractmethod

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass
# window version
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# mac version
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        print("You have created WindowsButton.")
class WindowsCheckbox(checkbox):
    def paint(self):
        print("You have created WindowsCheckbox.")

class MacButton(Button):
    def paint(self):
        print("You have created MacButton.")

class MacCheckbox(checkbox):
    def paint(self):
        print("You have created MacCheckbox.")

def client_code(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.paint()
    checkbox.paint()

if __name__ == "__main__":
    print("App: Launched with the WindowsFactory.")
    client_code(WindowsFactory())
    print("\n")

    print("App: Launched with the MacFactory.")
    client_code(MacFactory())
    print("\n")