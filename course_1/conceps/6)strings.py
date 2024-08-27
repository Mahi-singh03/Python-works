# CONTENT:

# Escape Character 
# String operations( concatination, length of str, list(str), join(str))
# String Indexing
# Slicing
# formating in str



#                                      Strings

# Striing is collection of cheractors
# string is immutable data-type in python 
# you cannot update the character at any index
# yu can ony assign the new string to same variable to update the strinig
# You can declare the string using '' , "" and ''' '''


x = 'Mahi singh'
x = "Mahi sing"
x = '''Mahi singh'''
# above all ways of declaring the string are Possible.








# Escape Charactors :

# [1] \n  { used to give new line }
# [2] \t  { used to give tab space between lines }











# Striing Operations:

# [1] Concatination ( + )    { used to add two strings }
# [2] length of str ( len(str) )       { used to find the length of string }
# [3] list str (list(str))    { conver the string into array}
# [4] join str  { join the particular and eacjh index }



# Example of concationation :

# str_1 = "mahi"
# str_2 = " singh"
# print("afer concatination :", str_1+str_2)


# Example of length of str

# str_1 = "mahi"
# str_2 = "mahi singh"

# print("length of str_1 :",len(str_1))
# print("length os atr_2 :",len(str_2))


# Example of list str

# str ="mahi singh"
# print(list(str))


# Example of join to str

# str = "mahi singh"
# print("&".join(str))









#  String indexing :
# indexing helps to locate the character in string 

# [1] Positive indexing 
# [2] Negetive indexing

# for negetive indexing the index starts from -1
# for positive indexing the index strats from 0


# str = "mahi singh ji"

# Exapmles of Positive indexing :
# print("character a index 3 is :",str[0])

# Example of Negetive indexing :
# print("character at negetive index 1 is :",str[-1])











# Slicing in string :
# slicing refers to trim the string

# Example :

# string = "mahi singh hii"

# To slice the string from index 2 to 7
# print("string after slicing from index 2 to 7 is :",string[2:7])  #7TH character excluded

# to slice the string from index 2 to second last index
# print("String after slicing from index 2 to 2nd last index :", string[2:-2])

# print("String after string[::1]  :",string[::1])   #return complete strinig

# print("String after string[::-1] :",string[::-1])   #return complete strinig but in reverse

# print("String after string[::2] :",string[::2])  
    # return string with 0th index and trim odd index  { retrn : mh ig i} 

# print("String after string[::3] :",string[::3])
    # return string with 0th index and trim 2 index return 3rd index { return: miihi }

# print("String after string[1::3] :",string[1::3])
    # return string with 1th index and trim 2 index return 3rd index { return: a n i }












# String reverse
# used to reverse the string  

# Example of str reverse

# str = "mahi singh"
# print("reverse of str is :","".join(reversed(str)))








# Formatinig the str :
#used to print the string in any order


# x = "{0} is a student of {2} class and has roll no. {1} ".format("mahi sing","504","BSc")

# print(x)

