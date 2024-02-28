class Person:
    name = "Peter"
    age = 19
    gender = "male"
    marital_status  = "complicated"
print(Person.name)
print(Person.age)
print(Person.gender)
print(Person.marital_status)
Person.age = 30
print(Person.age)
class Employees:
    name = "Lucia Awuor"
    gender = "Female"
    age = 30
    Salary = 45000
    location = "Siaya"
    Telephone = 106792433
print(f"{Employees.name} who is a {Employees.gender} aged {Employees.age} from {Employees.location}, earns a salary of {Employees.Salary} annualy can be accessed through {Employees.Telephone}")
print(f"{Employees.name} is a {Employees.gender} of age {Employees.age}")
class Parent:
    first_name = "Martha"
    last_name = "Awino"
Parent1 = Parent()
print(Parent1.first_name)

class Parent:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
Parent1 = Parent("John","Ochieng", 43)
Parent2 = Parent("Angel","Njora",29)
Parent3 = Parent("Becky","Serma",89)
print(Parent1.first_name)
print(Parent2.first_name)
print(Parent3.first_name)
print(Parent1.last_name)
print(Parent2.last_name)
print(Parent3.last_name)

class Cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
Car1 = Cars("Ford","Ranger",2010)
Car2 = Cars("Toyota", "Axis", 2018)
Car3 = Cars("Nissan", "Sunny", 2014)
print(Car1.make)
print(Car2.make)
print(Car3.make)
print(f"My car is a {Car1.make} {Car1.model} manufactured in the year {Car1.year}")

class Students:
    def __init__(self, name ,age, gender):
        self.name = name
        self.age = age
        self.gender = gender
Student1 = Students("Sweeney", 18, "Female")
Student2 = Students("Sharon", 20, "Female")
Student3 = Students("Lenox", 30, "male")
print(f"{Student1.name},{Student2.name} and {Student3.name} are students of gender {Student1.age}, {Student2.age} and {Student3.age} years respectively , however the first two are of {Student1.gender} gender and the last is of {Student3.gender} gender.")

class Magari:
    def __init__(self, make, model, price, year):
        self.make = make
        self.model = model
        self.price = price
        self.year = year
    def describe(self):
        print(
            f"My favourite car is {self.make} and it is a model of {self.model} , it was manufactured in the year {self.year}")
Obj1 = Magari("nissan","toyota", 1000000, 2010)
Obj2 = Magari("tesla", "ranger", 1220000, 2001)
Obj3 = Magari("g-wagon", "axis", 3000000, 2018)
print(Obj1.describe())
print(Obj2.describe())
Obj3.describe()

class person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def fullname(self):
        print(f"{self.name}")
    def realage(self):
        print(f"{self.age}")
    def rgender(self):
        print(f"{self.gender}")
    def increment_age(self):
        self.age +=10
Obj1 = person("becky serma", "female", 30)
print(Obj1.fullname())
print(Obj1.rgender())
print(Obj1.increment_age())
