class Student: 
    category = "University of Auckland"  # 类属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Category: {Student.category}")
    
p1 = Student("Alice", 20)
p1.show_info()  # 输出: Name: Alice, Age: 20, Category
