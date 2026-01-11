from PizzaOrder.Pizza import Pizza
class PizzaCaliforniaType(Pizza):
    def __init__(self, type):
        self.type = type

    def getPrice(self,original):
        return original * self.type
        