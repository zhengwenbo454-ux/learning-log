class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"Book Title: 《{self.title}》, Price: {self.price}"
    
    def __repr__(self):
        return f"Book({self.title}, {self.price})"

book1 = Book("Python Programming", 29.99)
print(book1)
print(repr(book1))


class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
    def __eq__(self, other):
        if isinstance(other, Bag):
            return self.items == other.items
        return True
    def __lt__(self, other):
        if isinstance(other, Bag):
            return len(self.items) < len(other.items)
        return NotImplemented
    def __add__(self, other):
        if isinstance(other, Bag):
            return Bag(self.items + other.items)
        return NotImplemented
    def __getitem__(self, index):
        return self.items[index]

    def __iter__(self):
        return iter(self.items)
    def __call__(self):
        return f"Bag with {len(self.items)} items: {self.items}"
b1 = Bag(["a", "b", "c"])
for i in b1:
    print(i)
b1()  # 输出: Bag with 3 items: ['a', 'b', 'c']
b2 = Bag(["b"])
b3 = b1 + b2
print(b3[0])
print(len(b1))  # 输出: 1
print(b1 == b2)  # 输出: False
print(b1 < b2)  # 输出: True


class Account:
    def __init__(self, initial_balance):
        self._balance = initial_balance
        self.secret = "my_secret_code"

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value


if __name__ == "__main__":
    acc = Account(100)
    print("current balance", acc.balance)
    acc.balance = 200
    print(acc.balance)


    





