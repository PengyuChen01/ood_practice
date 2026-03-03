"""Decorator Pattern Demo"""
from .pizza import BasePizza
from .size_decorator import SmallSize, MediumSize, LargeSize
from .topping_decorator import BananaTopping, MushroomTopping, CheeseTopping
from .type_decorator import TexasType, CaliforniaType, NewYorkType


def main():
    # Small Texas pizza with banana and cheese toppings
    pizza1 = BasePizza()
    pizza1 = SmallSize(pizza1)
    pizza1 = BananaTopping(pizza1)
    pizza1 = CheeseTopping(pizza1)
    pizza1 = TexasType(pizza1)
    # Price: (0 + 8 + 1.5 + 2.5) * 1.2 = 14.4
    print(f"{pizza1.get_description()}: ${pizza1.get_price():.2f}")

    # Large California pizza with mushroom (fluent style)
    pizza2 = NewYorkType(
        MushroomTopping(
            LargeSize(
                BasePizza()
            )
        )
    )
    # Price: (0 + 12 + 2) * 1.0 = 14.0
    print(f"{pizza2.get_description()}: ${pizza2.get_price():.2f}")

    # Medium California pizza (plain)
    pizza3 = CaliforniaType(MediumSize(BasePizza()))
    # Price: (0 + 10) * 1.1 = 11.0
    print(f"{pizza3.get_description()}: ${pizza3.get_price():.2f}")


if __name__ == "__main__":
    main()
