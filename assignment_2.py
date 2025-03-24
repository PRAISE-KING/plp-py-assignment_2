
my_list = []
# list created


my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# adding items using the '.append()' method


my_list.insert(1 ,15)
# inserting 15 - index comes before number to be inserted


my_list.extend([50, 60, 70])
# extending the list / adding a list to the list
# can also use += operator instead of .extend() method          e.g          my_list += [50, 60, 70]


my_list.pop()
# .pop() method always removes and returns the last number when called
# can also use : 
# pop with index = '.pop(-1)'
# .remove(70) - if you know the exact num
# del statement e.g 'del my_list[-1]'
# slicing 'my_list = my_list[:-1]'


my_list.sort()
# defaultly sorts in ascending order or use '.sorted(my_list)'- but this prints a new sorted list but the original remains unchanged
# descending order use boolean i.e .sort(reverse = True) or .sorted(my_list, reverse = True) - but this prints a new sorted list but the original remains unchanged


print(my_list[3])
# prints the third index 