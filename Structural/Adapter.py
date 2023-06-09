# using object
class RoundHole:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def fits(self, peg):
        return self.get_radius() >= peg.get_radius()
class RoundPeg:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
# adaptee
class SquarePeg:
    def __init__(self, width):
        self.__width = width

    def get_width(self):
        return self.__width

# adpater using object
class SquarePegAdapter(RoundPeg):
    def __init__(self, peg):
        self.__peg = peg

    def get_radius(self):
        return self.__peg.get_width() * 2 ** 0.5 / 2

# using inheritance
class SquarePegAdapter2(RoundPeg, SquarePeg):
    def __init__(self, width):
        SquarePeg.__init__(self, width)

    def get_radius(self):
        return self.get_width() * 2 ** 0.5 / 2

def client_code(hole, peg):
    if hole.fits(peg):
        print('Round peg fits round hole')
    else:
        print('Round peg does not fit round hole')

round_hole = RoundHole(5)
small_square_peg = SquarePeg(5)
large_square_peg = SquarePeg(10)
# not compatible
# client_code(round_hole, small_square_peg)
# compatible
client_code(round_hole, SquarePegAdapter(small_square_peg))
client_code(round_hole, SquarePegAdapter(large_square_peg))

# using inheritance
client_code(round_hole, SquarePegAdapter2(5))
client_code(round_hole, SquarePegAdapter2(10))


