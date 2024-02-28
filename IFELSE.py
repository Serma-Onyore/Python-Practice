# age = int(input ("How old are you??"))
# if age >=65:
#     print("You're old enough to retire.")
# elif age <65 and age >= 50:
#     print("You are almost going to retire")
# elif age <50 and age >= 40:
#     print("You are still active")
# elif age <40 and age >= 30:
#     print("You are considered youthful")
# else:
#     print("You are still young.")


# marks  = float(input("Enter your marks"))
# if marks >= 80 and marks <=100:
#     print("You have an A")
# elif marks >= 60 and marks <=100:
#     print("You have a B")
# elif marks >= 50 and marks <=100:
#     print("You have a C")
# elif marks >= 40 and marks <=100:
#     print("You have a D")
# elif marks >= 0 and marks <=100:
#     print("You have an E")
# else:
#     print("Enter valid marks 0 - 100")

temp = float(input("Read temperature"))
if temp >= 30:
    print("Have a vest on")
elif temp >=20 and temp <30:
    print("Put on a sweater")
else:
    print("Put on a jacket")