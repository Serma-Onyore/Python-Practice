#TEST ONE A(2-28)
def students(name):
    print(name)
students("Becky")
students("Lydia")
students("Betty")
students("Tani")
students("Lydia")

#TEST ONE B
def students(fname, sname):
    print("My full names are " + fname +" " + sname )
students("Becky", "Serma")
students("Natasha", "Atieno")

#TEST ONE C
class Students:
    def __init__(self, fname ,sname):
        self.fname = fname
        self.sname = sname
Obj1 = Students("Natalia", "Achieng")
Obj2 = Students("Gift", "Mugo")
Obj3 = Students("Sheila", "Bakhita")
print(f"{Obj1.fname} {Obj1.sname} is one of my students.")
print(f"{Obj2.fname} {Obj2.sname} is one of my students.")
print(f"{Obj3.fname} {Obj3.sname} is one of my students.")
print(f"My students are {Obj1.fname} {Obj1.sname}, {Obj2.fname} {Obj2.sname} and {Obj3.fname} {Obj3.sname}.")

#TEST TWO(29-37 )
class Student:
    name = "Serma"
    marks = 84
print(f"My name is {Student.name} and I got {Student.marks} in my exams.")
Student.name = "Onyore"
Student.marks = 80
print(f"My name is {Student.name} and I got {Student.marks} in my exams.")

#TEST THREE A
class Rectangles:
    length = 38
    width = 30
    area = (length * width)
    print(area)
    # print(f"The area of the triangle whose length is {Rectangle.length} and width is {Rectangle.width} is ")

#TEST THREE B
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.area = width * length
Result1 = Rectangle (37,49)
print(f"The area is {Result1.area}")

#TEST FOUR A
class Circles:
    pi = 3.142
    radius = 14
    area = (pi * radius *radius)
    perimeter = (2 * pi * radius)
    print(area)
    print(perimeter)

#TEST FOUR B
class Circle:
    def __init__(self, pi, radius):
        self.pi = pi
        self.radius = radius
        self.area = pi * radius * radius
        self.perimeter = pi * 2 * radius
Total1 = Circle(3.142, 14)
print(f"The area of a cicle of radius {Total1.radius} is {Total1.area}")
print(f"The perimeter of a cicle of radius {Total1.radius} is {Total1.perimeter}")

#TEST FIVE
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def deposit(self):
        deposit = int(input("Enter amount you would like to deposit:"))
        balance = self.balance + deposit
        print(f"Dear {self.customer_name} your new balance is {balance}")
    def withdraw(self):
        withdraw = int(input("Enter amount you would like to withdraw: "))
        balance = self.balance - withdraw
        print(f"Dear {self.customer_name} your new balance is {balance}")
Obj4 = BankAccount(54789, 680000, "12th december", "John")
Obj4.deposit()
Obj4.withdraw()
