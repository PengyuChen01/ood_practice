import Pizza
class PizzaTexasType(Pizza):
    def __init__(self, type):
        self.type = type

    def getPrice(self,original):
        return original * self.type
        