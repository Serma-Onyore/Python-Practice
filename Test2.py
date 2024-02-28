weight = float(input("Input your weight in kg"))
height = float(input("Input your height in metres"))
new_height = height * height
bmi = weight / new_height
print(bmi)
if bmi < 18:
    print("you are underweight")
elif bmi >=18 and bmi <=25:
    print("You are normal")
elif bmi >25 and bmi <=30:
    print("You are overweight")
else:
    print("You are obese")