from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass

class FileDataSource(DataSource):
    def __init__(self, filename):
        self._filename = filename

    def write_data(self, data):
        print(f"Write data to file {self._filename}")

    def read_data(self):
        print(f"Read data from file {self._filename}")

class DataSourceDecorator(DataSource):
    def __init__(self, source):
        self._source = source

    def write_data(self, data):
        self._source.write_data(data)

    def read_data(self):
        self._source.read_data()

class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data):
        print("Encrypt data")
        super().write_data(data)

    def read_data(self):
        print("Decrypt data")
        super().read_data()

class CompressionDecorator(DataSourceDecorator):
    def write_data(self, data):
        print("Compress data")
        super().write_data(data)

    def read_data(self):
        print("Decompress data")
        super().read_data()

def client_code(component: DataSource):
    component.write_data("Hello world!")
    component.read_data()

if __name__ == "__main__":
    source = FileDataSource("test.txt")
    client_code(source)
    print()

    source = EncryptionDecorator(source)
    client_code(source)
    print()

    source = CompressionDecorator(source)
    client_code(source)
    print()

    source = CompressionDecorator(EncryptionDecorator(source))
    client_code(source)
    print()