"""Strategy Pattern Demo"""
from .pizza import Pizza
from .size_strategy import SmallSize, MediumSize, LargeSize
from .topping_strategy import BananaTopping, MushroomTopping, CheeseTopping
from .type_strategy import TexasType, CaliforniaType, NewYorkType


def main():
    # Small Texas pizza with banana and cheese toppings
    pizza1 = Pizza(
        size=SmallSize(),
        pizza_type=TexasType(),
        toppings=[BananaTopping(), CheeseTopping()]
    )
    # Price: (8 + 1.5 + 2.5) * 1.2 = 14.4
    print(f"Pizza 1 price: ${pizza1.get_price():.2f}")

    # Large California pizza with mushroom
    pizza2 = Pizza(
        size=LargeSize(),
        pizza_type=CaliforniaType()
    )
    pizza2.add_topping(MushroomTopping())
    # Price: (12 + 2) * 1.1 = 15.4
    print(f"Pizza 2 price: ${pizza2.get_price():.2f}")

    # Medium New York pizza (plain)
    pizza3 = Pizza(
        size=MediumSize(),
        pizza_type=NewYorkType()
    )
    # Price: 10 * 1.0 = 10.0
    print(f"Pizza 3 price: ${pizza3.get_price():.2f}")


if __name__ == "__main__":
    main()
