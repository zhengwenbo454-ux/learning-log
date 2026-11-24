from dataclasses import dataclass
class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} 是 {self.price}"

class Fruit(Goods):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
    def __str__(self):
        return f"水果{self.name} 重量{self.weight}kg 价格{self.price}"

class Cart:
    def __init__(self):
        self.goods_list = []
    def __len__(self):
        return len(self.goods_list)
    def __add__(self, other):
        if isinstance(other, Goods):
            self.goods_list.append(other)
        return self
    def __iter__(self):
        return iter(self.goods_list)

    @property
    def total(self):
        return sum(g.price for g in self.goods_list)

@dataclass
class Coupon:
    discount: float

def settle(g: Goods):
    print(f"结算{g}")

apple = Fruit("apple", 5, 2)
pen = Goods ("pen", 2)
cart = Cart()
cart + apple
cart + pen
print(cart.total)
settle(apple)
settle(pen)
print(isinstance(apple, Goods))
print(issubclass(Fruit, Goods))


        
    
        
    


        