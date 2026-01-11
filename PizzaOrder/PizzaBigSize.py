from PizzaOrder.Pizza import Pizza

class PizzaBigSize(Pizza):
    def __init__(self,bigSize):
        self.bigSize = bigSize

    def getPrice(self,original):
        assert original >=0
        return original + self.bigSize


