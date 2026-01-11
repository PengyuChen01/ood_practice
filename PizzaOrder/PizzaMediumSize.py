from PizzaOrder.Pizza import Pizza

class PizzaMediumSize(Pizza):
    def __init__(self,mediumSize):
        self.mediumSize = mediumSize

    def getPrice(self,original):
        assert original >=0
        return original + self.mediumSize


