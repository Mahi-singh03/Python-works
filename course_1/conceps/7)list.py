# CONTENT :

# Indexing
# Accesing the element 
# Take list as input from the user  { using th .split() method }
# Adding the items to the list  {add(), insert(), extend([])}
# Removing the item in list  { remove(), pop()}





#                                     LIST:
# list is the mutable datatype in python:
# list can store hetrogenious data.


# Example :

# list_1 = ["mahi", "singh", 78 ,78, True, [578, 589, "mari"]]

# print(list_1)











# Accesing the element of list at any index :

# print("element at index 3 IS :", list_1[3])
# print("element at the 2nd index of list inside the list_1 is :", list_1[4][2])














# Indexing :
# indexing helps to locate the item in list 

# [1] Positive indexing 
# [2] Negetive indexing

# for negetive indexing the index starts from -1
# for positive indexing the index strats from 0


# Example of +ve inidexing :
#list1 = [10, 20, 30, 40]
#print("the item at the index 1 Is : ",list1[1])

# Example of -ve indexing :
#list2 = [10, 20, 30, 40]
#print("the item at the index -2 Is : ",list1[-2])   # return the 2nd last item of the list 














# List operatons :
# [1] length of list (len(list))   





#Example:

# list_1 = [10, 20, 30, 40]
# print("length of the list id : ",len(list_1))    # return length of list















# Take list as input from the user:

# you cannot take direct list input from the use
# it can be achieve using the split function
# the string is converted into the list by spacing 

# step 1 ) taking the input as strinig :
# string = input("Enter elements (Space-Separated): ")   # take the input as a string first      

# step 2) converting the string into list :
# list = string.split()

# step 3) print the list:
# print("the entered list is : ",list)












# Adding the element to the list:
# the list are mutable data type in py there for we can add element yo the list.

# Method 1 ) using append method  { only add one item at a time / add item only at he end }
# Method 2 ) using insert method   { add element at any postion }
# method 3 ) using the extend method. { [] reqired, add multiple elements at the end of the list.}


# list = [10, 20, 30, 40, 50]

# Example of Append() method :
# list.append(60)
# list.append("mahi")
# list.append([70, 80])

# print(" list after adding the iten using the .append method : ",list)




# Exapmle of insert() method :
#  SYNTEX - .add(position, item)

# list.insert(3,"mahi")
# list.insert(3,[56,77])

# print(" list after adding element using the insert() method : ",list)




# Exapmle of extend() method :

# list.extend(["mahi",768,865])
# print(" list after adding element using the extend() method : ",list)











# Removing Elements from the List
