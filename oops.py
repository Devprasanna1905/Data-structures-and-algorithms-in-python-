"""
PYTHON OBJECT-ORIENTED PROGRAMMING (OOP) CHEATSHEET
====================================================
A comprehensive guide with all major OOP concepts and implementations
"""

# ============================================================================
# 1. BASIC CLASS AND OBJECT
# ============================================================================

class BasicClass:
    """A simple class example"""
    
    def __init__(self, name, age):
        """Constructor/Initializer"""
        self.name = name  # Instance variable
        self.age = age
    
    def greet(self):
        """Instance method"""
        return f"Hello, I'm {self.name} and I'm {self.age} years old"


# Creating objects
person1 = BasicClass("Alice", 25)
person2 = BasicClass("Bob", 30)
print(person1.greet())
print(person2.greet())


# ============================================================================
# 2. CLASS VARIABLES vs INSTANCE VARIABLES
# ============================================================================

class Employee:
    # Class variable (shared by all instances)
    company = "TechCorp"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Instance variables (unique to each instance)
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def display_info(self):
        return f"{self.name} works at {self.company} with salary ${self.salary}"


emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)
print(f"Total employees: {Employee.employee_count}")
print(emp1.display_info())


# ============================================================================
# 3. INSTANCE METHODS, CLASS METHODS, STATIC METHODS
# ============================================================================

class MethodTypes:
    class_variable = "I'm a class variable"
    
    def __init__(self, value):
        self.instance_variable = value
    
    # Instance method (has access to instance via self)
    def instance_method(self):
        return f"Instance method accessing: {self.instance_variable},{MethodTypes.class_variable}"
    
    # Class method (has access to class via cls)
    @classmethod
    def class_method(cls):
        return f"Class method accessing: {cls.class_variable}"
    
    # Static method (no access to class or instance)
    @staticmethod
    def static_method(x, y):
        return f"Static method calculating: {x + y}"


obj = MethodTypes("instance value")
print(obj.instance_method())
print(MethodTypes.class_method())
print(MethodTypes.static_method(5, 10))


# ============================================================================
# 4. INHERITANCE (Single, Multiple, Multilevel)
# ============================================================================

# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())


# Multiple Inheritance
  


# Multilevel Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} vehicle starting"


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def drive(self):
        return f"Driving {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        return f"Charging {self.battery_capacity}kWh battery"


tesla = ElectricCar("Tesla", "Model 3", 75)
print(tesla.start())
print(tesla.drive())
print(tesla.charge())


# ============================================================================
# 5. METHOD RESOLUTION ORDER (MRO)
# ============================================================================

class A:
    def method(self):
        return "A's method"


class B(A):
    def method(self):
        return "B's method"


class C(A):
    def method(self):
        return "C's method"


class D(B, C):
    pass


d = D()
print(d.method())  # Which method gets called?
print(D.__mro__)   # Method Resolution Order
print(D.mro())     # Alternative way to see MRO


# ============================================================================
# 6. ENCAPSULATION (Public, Protected, Private)
# ============================================================================

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number      # Public
        self._balance = balance                   # Protected (convention)
        self.__pin = "1234"                       # Private (name mangling)
    
    # Public method
    def deposit(self, amount):
        self._balance += amount
        return f"Deposited ${amount}. New balance: ${self._balance}"
    
    # Protected method
    def _calculate_interest(self):
        return self._balance * 0.05
    
    # Private method
    def __verify_pin(self, pin):
        return pin == self.__pin
    
    # Public method accessing private method
    def withdraw(self, amount, pin):
        if self.__verify_pin(pin):
            if amount <= self._balance:
                self._balance -= amount
                return f"Withdrawn ${amount}. Remaining: ${self._balance}"
            return "Insufficient funds"
        return "Invalid PIN"


account = BankAccount("123456", 1000)
print(account.deposit(500))
print(account.withdraw(200, "1234"))
# print(account.__pin)  # This will raise AttributeError
# Access private attribute (not recommended): account._BankAccount__pin


# ============================================================================
# 7. POLYMORPHISM (Method Overriding)
# ============================================================================

class Shape:
    def area(self):
        return 0
    
    def perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


# Polymorphism in action
shapes = [Rectangle(5, 3), Circle(4), Rectangle(2, 8)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")


# ============================================================================
# 8. ABSTRACTION (Abstract Base Classes)
# ============================================================================

from abc import ABC, abstractmethod


class Database(ABC):
    """Abstract base class"""
    
    @abstractmethod
    def connect(self):
        """Must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Must be implemented by subclasses"""
        pass
    
    def log(self, message):
        """Concrete method (optional to override)"""
        print(f"LOG: {message}")


class MySQLDatabase(Database):
    def connect(self):
        return "Connected to MySQL"
    
    def execute_query(self, query):
        return f"Executing MySQL query: {query}"


class PostgreSQLDatabase(Database):
    def connect(self):
        return "Connected to PostgreSQL"
    
    def execute_query(self, query):
        return f"Executing PostgreSQL query: {query}"


# db = Database()  # This will raise TypeError
mysql_db = MySQLDatabase()
print(mysql_db.connect())
print(mysql_db.execute_query("SELECT * FROM users"))
mysql_db.log("Query executed successfully")


# ============================================================================
# 9. SPECIAL/MAGIC METHODS (DUNDER METHODS)
# ============================================================================

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # String representation (for developers)
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # String representation (for users)
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    # Length
    def __len__(self):
        return self.pages
    
    # Comparison operators
    def __eq__(self, other):
        return self.pages == other.pages
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    # Addition
    def __add__(self, other):
        return self.pages + other.pages
    
    # Indexing/Subscripting
    def __getitem__(self, index):
        return f"Page {index} of {self.title}"
    
    # Deletion
    def __del__(self):
        print(f"Book '{self.title}' is being deleted")


book1 = Book("1984", "George Orwell", 328)
book2 = Book("Animal Farm", "George Orwell", 112)

print(str(book1))           # Calls __str__
print(repr(book1))          # Calls __repr__
print(len(book1))           # Calls __len__
print(book1 == book2)       # Calls __eq__
print(book1 > book2)        # Calls __gt__
print(book1 + book2)        # Calls __add__
print(book1[5])             # Calls __getitem__


# ============================================================================
# 10. OPERATOR OVERLOADING
# ============================================================================

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2)
print(v1 - v2)
print(v1 * 3)
print(abs(v1))


# ============================================================================
# 11. PROPERTY DECORATORS (Getters, Setters, Deleters)
# ============================================================================

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    # Getter
    @property
    def celsius(self):
        return self._celsius
    
    # Setter
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    # Deleter
    @celsius.deleter
    def celsius(self):
        print("Deleting temperature")
        del self._celsius
    
    # Computed property
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9


temp = Temperature(25)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")
temp.fahrenheit = 86
print(f"New Celsius: {temp.celsius}")


# ============================================================================
# 12. COMPOSITION
# ============================================================================

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return f"Engine with {self.horsepower}HP started"


class Wheel:
    def __init__(self, size):
        self.size = size


class CarComposition:
    def __init__(self, brand, engine, wheels):
        self.brand = brand
        self.engine = engine        # Has-a relationship
        self.wheels = wheels        # Has-a relationship
    
    def start(self):
        return f"{self.brand} car: {self.engine.start()}"
    
    def info(self):
        return f"{self.brand} with {len(self.wheels)} wheels of size {self.wheels[0].size}"


engine = Engine(200)
wheels = [Wheel(18) for _ in range(4)]
car = CarComposition("Toyota", engine, wheels)
print(car.start())
print(car.info())


# ============================================================================
# 13. AGGREGATION
# ============================================================================

class Department:
    def __init__(self, name):
        self.name = name


class Professor:
    def __init__(self, name, department):
        self.name = name
        self.department = department  # Aggregation (professor uses department)
    
    def info(self):
        return f"{self.name} teaches in {self.department.name}"


dept = Department("Computer Science")
prof1 = Professor("Dr. Smith", dept)
prof2 = Professor("Dr. Jones", dept)
print(prof1.info())
print(prof2.info())


# ============================================================================
# 14. ITERATOR PROTOCOL
# ============================================================================

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


counter = Counter(1, 5)
for num in counter:
    print(num, end=" ")
print()


# ============================================================================
# 15. GENERATOR (using yield)
# ============================================================================

class FibonacciGenerator:
    def __init__(self, n):
        self.n = n
    
    def generate(self):
        a, b = 0, 1
        count = 0
        while count < self.n:
            yield a
            a, b = b, a + b
            count += 1


fib = FibonacciGenerator(10)
for num in fib.generate():
    print(num, end=" ")
print()


# ============================================================================
# 16. CONTEXT MANAGERS (with statement)
# ============================================================================

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()
        return False  # Don't suppress exceptions


# Using context manager
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")


# ============================================================================
# 17. DESCRIPTORS
# ============================================================================

class ValidatedAttribute:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"{self.name} must be between {self.min_value} and {self.max_value}")
        instance.__dict__[self.name] = value


class Student:
    age = ValidatedAttribute(5, 100)
    grade = ValidatedAttribute(0, 100)
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student = Student("Alice", 20, 85)
print(f"{student.name}, Age: {student.age}, Grade: {student.grade}")
# student.age = 150  # This will raise ValueError


# ============================================================================
# 18. METACLASSES
# ============================================================================

class SingletonMeta(type):
    """Metaclass for Singleton pattern"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating database connection")
        self.connection = "Connected"


db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True - same instance


# ============================================================================
# 19. DATACLASSES (Python 3.7+)
# ============================================================================

from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: list = field(default_factory=list)
    
    def total_value(self):
        return self.price * self.quantity
    
    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")


product = Product("Laptop", 999.99, 5, ["electronics", "computers"])
print(product)
print(f"Total value: ${product.total_value()}")


# ============================================================================
# 20. SLOTS (Memory Optimization)
# ============================================================================

class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class WithSlots:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj1 = WithoutSlots(1, 2)
obj2 = WithSlots(1, 2)
# obj1.z = 3  # Works fine
# obj2.z = 3  # Raises AttributeError


# ============================================================================
# 21. MIXIN CLASSES
# ============================================================================

class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)


class LogMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")


class User(JSONMixin, LogMixin):
    def __init__(self, username, email):
        self.username = username
        self.email = email


user = User("john_doe", "john@example.com")
print(user.to_json())
user.log("User created successfully")


# ============================================================================
# 22. CALLABLE OBJECTS
# ============================================================================

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor


double = Multiplier(2)
triple = Multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15


# ============================================================================
# 23. CLASS INHERITANCE WITH super()
# ============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"I'm {self.name}, {self.age} years old"


class StudentInheritance(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def introduce(self):
        return f"{super().introduce()}, Student ID: {self.student_id}"


student = StudentInheritance("Emma", 19, "S12345")
print(student.introduce())


# ============================================================================
# 24. DESIGN PATTERNS
# ============================================================================

# Factory Pattern
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog("Factory Dog")
        elif animal_type == "cat":
            return Cat("Factory Cat")
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


animal = AnimalFactory.create_animal("dog")
print(animal.speak())


# Observer Pattern
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name} received: {message}")


subject = Subject()
observer1 = Observer("Observer 1")
observer2 = Observer("Observer 2")
subject.attach(observer1)
subject.attach(observer2)
subject.notify("Hello Observers!")


# ============================================================================
# 25. COPY (Shallow vs Deep)
# ============================================================================

import copy


class Address:
    def __init__(self, street, city):
        self.street = street
        self.city = city


class PersonCopy:
    def __init__(self, name, address):
        self.name = name
        self.address = address


original = PersonCopy("John", Address("123 Main St", "NYC"))
shallow = copy.copy(original)
deep = copy.deepcopy(original)

# Modify address
original.address.city = "Boston"

print(f"Original city: {original.address.city}")
print(f"Shallow copy city: {shallow.address.city}")  # Changed
print(f"Deep copy city: {deep.address.city}")        # Unchanged


print("\n" + "="*60)
print("PYTHON OOP CHEATSHEET COMPLETED!")
print("="*60)