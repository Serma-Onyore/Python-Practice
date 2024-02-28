def my_function():
    print("This is my first function")
    print("This is my first function")
    print("This is my first function")
my_function()
my_function()

def mine(name):
    print(name)
    print(name)
    print(name)
mine("Serma")
mine("Becky")
mine("Onyore")

def salute(fname):
    print("Heyyyy " +fname + "Good morning")
salute("Esther, ")
salute("Anne, ")

def miaka(age):
    print("Hello, you are " + str(age) + " years of age")
miaka(18)


def majina(first_name, last_name,):
    print(first_name+ '' + last_name + "is my full name ")
majina("serma"," Onyore",)

def employees(fname, age):
    if age>=20:
        print(fname + " you are " + str(age), "years of age hence you are old enough")
    elif age <20 and age>=15:
        print(fname + " you are " ,str(age), "years old hence you are a youth")
    else:
        print(fname + " you are ", str(age), "years of age hence you are young")
employees("Tonny",38)
employees("Anita",19)
employees("Serma",10)

def age_calc(age):
    new = age + 10
    return new
print(age_calc(35))

def marks_calc(*subjects):
    total = sum(subjects)
    return (total)
print(marks_calc(83,87,81,99,78))
print(marks_calc(86,43,23,98,56))

def test(name,*marks):
    total = sum(marks)
    return total
print(test("sarah",98, 60))

def bored(age):
    if age > 60:
        print("Because you are " + str(age) + " you are posted to Kisumu")
    elif age>50 and age <=60:
        print("Because you are " + str(age) + " you are posted to Nakuru")
    elif age>30 and age <=50:
        print("Because you are " + str(age) + " you are posted to Mombasa")
    else:
        print("Because you are " + str(age) + " you are too young for the job")
bored(87)

def country(nchi ="kenya"):
    return nchi
print(country("Tnzania"))
print(country("Uganda"))
print(country("Tanzania"))