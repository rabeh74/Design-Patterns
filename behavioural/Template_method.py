from abc import ABC, abstractmethod
class GameAI(ABC):
    def _turn(self):
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()
    @abstractmethod
    def collect_resources(self):
        pass
    @abstractmethod
    def build_structures(self):
        pass
    @abstractmethod
    def build_units(self):
        pass
    @abstractmethod
    def attack(self):
        pass
class OrcsAI(GameAI):
    def collect_resources(self):
        print('Orcs AI collect resources')
    def build_structures(self):
        print('Orcs AI build structures')
    def build_units(self):
        print('Orcs AI build units')
    def attack(self):
        print('Orcs AI attack')
class MonstersAI(GameAI):
    def collect_resources(self):
        print('Monsters AI collect resources')
    def build_structures(self):
        print('Monsters AI build structures')
    def build_units(self):
        print('Monsters AI build units')
    def attack(self):
        print('Monsters AI attack')
def client_code(ai):
    ai._turn()
client_code(OrcsAI())
client_code(MonstersAI())


