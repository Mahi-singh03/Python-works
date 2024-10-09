#      NUMBERS




# Mathematical operators

# Examples :

# print("10 + 2 =", 10+2)
# print("10 - 2 =", 10-2)
# print("10 * 2 =", 10*2)
# print("10 / 2 =", 10/2)
# print("10 % 2 =", 10%2)
# print("10 ** 2 =", 10**2)








# Relational operators

# returns only true or false only (Boolean values only)
# Examples 

# print("10==20",100 == 200 )
# print("10!=20",100 != 200 )
# print("10>20",100 > 200 )
# print("10<20",100 < 200 )
# print("10>=20",100 >= 200 )
# print("10<=20",100 <= 200 )







# Logical operators

# Returns only  true and False (Boolean values only)

# Examples:
# example of not
# print("not (10 == 10) :", not(10==10)) 


# example of and
# print("(10 == 10) and (10 > 9) = ",(10==10)and(10>9))    #return true as all condition true
# print("(10 == 10) and (10 < 9) = ",(10==10)and(10<9))    #return true as all condition false


# example of or
# print("(10 == 10) or (10 < 9) = ",(10==10)or(10<9))    #return true as one condition true
# print("(10 == 10) or (10 < 9) = ",(10==10)or(10>9))    #return true as both are condition true
# print("(10 == 100) or (10 < 9) = ",(10==100)or(10<9))    #return false as both are condition false









# complwx numbers:

# x = (5 + 45j)*4
# print(x)



# number with different bases:

# print(oct(576))
# print(hex(65))
# print(bin(56))

# to convert any number to any base number

# print( int("111000" ,2)) 







# Math module

# import math

# print(math.pi)
# print(math.floor(3.54))         
# print(math.trunc(654.12))








# random module

# import random

# choice = ["mahi" , "singh", "navi", ' ravi']
# print(random.random())
# print(random.randint(1,10))
# print(random.choice(choice))
# random.shuffle(choice)
# print(choice)








# Deciaml module

# print(0.1 + 0.1 + 0.1 - 0.3 )

# from decimal import Decimal

# print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3"))

















#        SETS


s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}



# Use the add() method to add a single element to a set. this method add only one iten at the end od the set

s1.add(1000)
print(s1)  



# Use the update() method to add multiple elements to a set.


s1.update(3000, 4000, 5000)
print(s1) 



#You can remove elements using remove() or discard(). The difference is that remove() raises a KeyError if the element is not found, while discard() does not.

my_set = {1, 2, 3}
my_set.remove(3) 
print(my_set) 

my_set.discard(10) 
print(my_set) 



# union and intersection :

print("union is :")
print(s1 | s2)  

print("inersection is :")
print(s1 & s2)  