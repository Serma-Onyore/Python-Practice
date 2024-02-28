class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Receptionist(Employees):
    def __init__(self, name, salary, gender):
        super().__init__(name, salary)
        self.gender = gender
class Frontend_developer:

Receptionist1 = Receptionist("Susan Otieno", 39990, "female")
Employees1 = Employees("Serma", 290000)
print(Receptionist1.name)
print(Employees1.name)
 
