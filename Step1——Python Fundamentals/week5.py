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
        
b1 = Bag(["a"])
b2 = Bag(["b"])
b3 = b1 + b2
print(b3[0])
print(len(b1))  # 输出: 1
print(b1 == b2)  # 输出: False
print(b1 < b2)  # 输出: True



