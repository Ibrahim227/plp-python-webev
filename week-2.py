"""Python Week 2 Assignment"""

my_list = []


my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(40)
my_list.append(40)
my_list.append(40)

my_list.insert(0, 15)

extended_list = [50, 60, 70]
my_list.extend(extended_list)
#my_list.pop()
sorted(my_list)
print(my_list.count(40))
print(my_list)
