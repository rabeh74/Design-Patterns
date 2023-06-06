# Purpose: Builder pattern implementation
class Builder:
    def reset(self):
        pass
    def setSeats(self, number):
        pass
    def setEngine(self, engine):
        pass
    def setTripComputer(self):
        pass
    def setGPS(self):
        pass
# Purpose: Concrete builder implementation
class CarBuilder(Builder):
    def __init__(self):
        self.reset()
    def reset(self):
        self._car = Car()
    def setSeats(self, number):
        self._car.seats = number
    def setEngine(self, engine):
        self._car.engine = engine
    def setTripComputer(self):
        self._car.tripComputer = True
    def setGPS(self):
        self._car.GPS = True
    def getProduct(self):
        return self._car


# Purpose: Concrete builder implementation
class ManualBuilder(Builder):
    def __init__(self):
        self.reset()
    def reset(self):
        self._manual = Manual()
    def setSeats(self, number):
        self._manual.seats = number
    def setEngine(self, engine):
        self._manual.engine = engine
    def setTripComputer(self):
        self._manual.tripComputer = True
    def setGPS(self):
        self._manual.GPS = True
    def getProduct(self):
        return self._manual

# Purpose: Product implementation
class Car:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.tripComputer = None
        self.GPS = None
    def __str__(self):
        return f"Car with {self.seats} seats, engine {self.engine} and {self.tripComputer} trip computer and {self.GPS} GPS"

# Purpose: Product implementation
class Manual:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.tripComputer = None
        self.GPS = None
    def __str__(self):
        return f"Manual with {self.seats} seats, engine {self.engine} and {self.tripComputer} trip computer and {self.GPS} GPS"

class Director:
    def __init__(self):
        self._builder = None
    def setBuilder(self, builder):
        self._builder = builder
    def constructSportsCar(self):
        self._builder.reset()
        self._builder.setSeats(2)
        self._builder.setEngine("SportEngine")
        self._builder.setTripComputer()
        self._builder.setGPS()
    def constructSUV(self):
        self._builder.reset()
        self._builder.setSeats(4)
        self._builder.setEngine("SUVEngine")
        self._builder.setTripComputer()
        self._builder.setGPS()
    def constructTruck(self):
        self._builder.reset()
        self._builder.setSeats(6)
        self._builder.setEngine("TruckEngine")
        self._builder.setTripComputer()
        self._builder.setGPS()

if __name__ == "__main__":
    director = Director()
    carBuilder = CarBuilder()
    manualBuilder = ManualBuilder()
    director.setBuilder(carBuilder)
    director.constructSportsCar()
    car = carBuilder.getProduct()
    print(car)
    director.setBuilder(manualBuilder)
    director.constructSportsCar()
    manual = manualBuilder.getProduct()
    print(manual)
    director.setBuilder(carBuilder)
    director.constructSUV()
    car = carBuilder.getProduct()
    print(car)


