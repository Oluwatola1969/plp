my_list =[]
#appending values to the list
my_list =[10, 20, 30, 40]
# inserting new value
my_list[1] = 15

print(my_list) #[10, 15, 30, 40]

#Removing the last element
my_list.pop()
print(my_list) #[10, 15, 30]

#Extending the list
my_list2= [50,60,70]
my_list.extend(my_list2)
print(my_list) #[10, 15, 30, 50, 60, 70]

#removing the last element
my_list.pop()
print(my_list) #[10, 15, 30, 50, 60]

#sorting the list in ascending order
my_list.sort()
print(my_list) #[10, 15, 30, 50, 60]

#printing the index of the value 30 in my_list
print(my_list.index(30)) #2
