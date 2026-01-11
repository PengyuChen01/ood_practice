from PizzaOrder.Pizza import Pizza

class PizzaBananaTopping(Pizza):
    def __init__(self, topping):
        self.topping = topping
    
    def getPrice(self,original):
        return original + self.topping
    