from PizzaOrder.Pizza import Pizza

class PizzaSmallSize(Pizza):
    # intialize with small price
    def __init__(self,smallSize):
        self.smallSize = smallSize
    # adding price of original to the different size
    def getPrice(self,original):
        assert original >=0
        return original + self.smallSize


