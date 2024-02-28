number = [234, 475, 566, 875, 784]
for i in number:
    print(i)

set = {"John", "Mary", "Jane", "Smith"}
for name in set:
    print(name)

my_string = "Hello world, welcome to my channel"
for letter in my_string:
    print(letter)

char = ("a", "b", "c", "d")
for letter in char:
    if letter =="b":
        continue
    print(letter)
else:
    print("finished")