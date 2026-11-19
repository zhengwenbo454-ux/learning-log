"""practice class"""
class Student: 
    category = "University of Auckland"  # 类属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Category: {Student.category}")
    
p1 = Student("Alice", 20)
p1.show_info()  # 输出: Name: Alice, Age: 20, Category

"""practice 2"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")
p1 = Student("Bob", 22, "S12345")
p1.show_info()  # 输出: Name: Bob, Age: 22, Student ID: S12345