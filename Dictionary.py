my_dictionary = {
    "Model" : "G-Wagon",
    "Company" : "Toyota",
    "Age" : "19 years",
    "Marital status" : "Complicated",
}
print(my_dictionary)
print(my_dictionary["Marital status"])
print(my_dictionary["Name"])
print(my_dictionary.get("Marital status"))
my_dictionary["Marital status"] = "Unmarried"
my_dictionary["Location"] = "Homa-Bay"
my_dictionary["Salary"] = 900200
print(my_dictionary)
my_dictionary2 = my_dictionary.copy()
print(my_dictionary2)
print(len(my_dictionary2))
my_dictionary2.pop("Marital status")
print(my_dictionary2)
my_dictionary2.clear()
print(my_dictionary2)
del my_dictionary2