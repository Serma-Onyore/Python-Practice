my_set = {122,423,645,567,354}
print(my_set)
my_set.add(879)
print(my_set)
my_set.update([978,454,465,121])
print(my_set)
my_set2 = my_set.copy()
print(my_set)
print(len(my_set))
my_set.discard(354)
print(my_set)
my_set.clear()
print(my_set)
del my_set
print(max(my_set2))
print(min(my_set2))
print(sum(my_set2))
print(sum(my_set2)/len(my_set2))
names = {"John", "James", "Peter", "Grace", "Mary", "Jane"}
if "Peter" in names:
    print("Peter is present in the school system.")
else:
    print("Peter is not present in the school system")
parents = {"Serma, Grandy, Daniel, Becky"}
value = "Serma"
if value in parents:
    output = value
    print(output)
test = {45, 73, 78.89, 25.94, 98, 89.58, 100}
print(test)
if 45 in test:
    display = 45
    print(display)
if 25.94 in test:
    display = 25.94
    print(display)
if 100 in test:
    print("YOU PASSED")
else:
    print("YOU FAILED")
if 60 in test:
    print("YOU PASSED")
else:
    print("YOU FAILED")