# # declaring the string

# x = "mahi"
# y = 'singh'
# z ='''ji  Greate'''


# print(x)
# print(y)
# print(z)








# # indexing

# str = "mahi singh ji"

# # Exapmles of Positive indexing :
# print("character a index 2 is :",str[2])

# # Example of Negetive indexing :
# print("character at negetive index 2 is :",str[-2])







# # Slicing in string :


# # Example :

# string = "mahi singh hii"

# #To slice the string from index 2 to 7
# print("string after slicing from index 2 to 7 is :",string[2:7])  #7TH character excluded

# #to slice the string from index 2 to second last index
# print("String after slicing from index 2 to 2nd last index :", string[2:-2])

# print("String after string[::1]  :",string[::1])   #return complete strinig

# print("String after string[::-1] :",string[::-1])   #return complete strinig but in reverse

# print("String after string[::2] :",string[::2])  
#     #return string with 0th index and trim odd index  { retrn : mh ig i} 

# print("String after string[::3] :",string[::3])
#     #return string with 0th index and trim 2 index return 3rd index { return: miihi }

# print("String after string[1::3] :",string[1::3])
#     #return string with 1th index and trim 2 index return 3rd index { return: a n i }








# # methods in string

# #Example of concationation :

# str_1 = "mahi"
# str_2 = " singh"
# print("afer concatination :", str_1+str_2)


# #Example of length of str

# str_1 = "mahi"
# str_2 = "mahi singh"

# print("length of str_1 :",len(str_1))
# print("length os atr_2 :",len(str_2))


# #Example of list str

# str ="mahi singh"
# print(list(str))


# #Example of join to str

# str = "mahi singh"
# print("&".join(str))



# # Example of endswith("somthing") 
# str5 = "mahi singh"
# print(str5.endswith("gh"))



# #  Example of the string capatilizer 

# str5 = "mahi singh"
# print( str5.capitalize())



# # example of replace()
# str5 = "mahi singh"
# print(str5.replace("singh", "ji"))



# # Example of find()      # return the index
# str5 = "mahi singh"
# print(str5.find("i"))


# # Exmaple of count()
# str5 = "mahi singh ji"
# print(str.count("i"))



# # Example of Strip()
# str5 ="     mahi singh"
# print(str5)
# print(str.strip())








# # Formatinig the str :

# x = "{0} is a student of {2} class and has roll no. {1} ".format("mahi sing","504","BSc")

# print(x)















