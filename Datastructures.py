my_list = [123, 456, 789, 102, 394, 586]
print(my_list)
print(my_list[4])
print(my_list[0])
my_list[0] = 132
print(my_list[0])
my_list[5] = 875
print(my_list)
print(len(my_list))
my_list.append(587)
print(my_list)
my_list.append(894)
my_list.append(904)
my_list.append(943)
my_list.insert(1, 254)
my_list.insert(5, 878)
my_list.extend([789,908,980])
print(my_list)
print(len(my_list))
my_list.remove(456)
print(my_list)
print(len(my_list))
del my_list[2]
print(my_list)
print(len(my_list))
my_list.clear()
print(my_list)
print(len(my_list))
del my_list
b_list = [978, 890, 209, 349, 849]
print(b_list)
print(len(b_list))
print(max(b_list))
print(min(b_list))
print(sum(b_list))
print(sum(b_list)/len(b_list))
print(b_list.index(209))