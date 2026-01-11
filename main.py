from PizzaOrder.Pizza import Pizza
from PizzaOrder.PizzaBananaTopping import PizzaBananaTopping
from PizzaOrder.PizzaMongoTopping import PizzaMongoTopping
from PizzaOrder.PizzaSmallSize import PizzaSmallSize
from PizzaOrder.PizzaMediumSize import PizzaMediumSize
from PizzaOrder.PizzaBigSize import PizzaBigSize
from PizzaOrder.PizzaCaliforniaType import PizzaCaliforniaType
# 测试基础价格
base_price = 10

# 测试 Topping
banana_topping = PizzaBananaTopping(2)  # 香蕉 topping 加 $2
print(f"Base price: {base_price}")
print(f"With banana topping: {banana_topping.getPrice(base_price)}")

mongo_topping = PizzaMongoTopping(3)  # Mongo topping 加 $3
print(f"With mongo topping: {mongo_topping.getPrice(base_price)}")

# 测试 Size
small_size = PizzaSmallSize(0)  # 小号不加价
medium_size = PizzaMediumSize(2)  # 中号加 $2
big_size = PizzaBigSize(5)  # 大号加 $5

print(f"Small size price: {small_size.getPrice(base_price)}")
print(f"Medium size price: {medium_size.getPrice(base_price)}")
print(f"Big size price: {big_size.getPrice(base_price)}")

california = PizzaCaliforniaType(2)
print(f"California Type price: {california.getPrice(base_price)}")