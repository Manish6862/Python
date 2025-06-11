#String------------------------------


# str ="My name is manish rajput.\nI am a python developer."
# print(str)

# str ="My name is manish rajput.\tI am a python developer."
# print(str)

#Concatination of String

# str1 = "Manish"
# str2 = "Rajput"
# print(str1+str2)

# str1 = "Manish"
# str2 = "Rajput"
# print(str1+" "+str2)


# #lenth of string---

# str1 = "Manish"
# len1 = len(str1)
# print("Length of string is: ", len1)

# str2 = "Rajput"
# len2 = len(str2)
# print("Length of string is: ", len2)
# print(str1+" "+str2)
# final_length = len(str1 + " " + str2)
# print("Final Length of string is: ", final_length)



#indexing of string

# str = "Manish Rajput"
# ch = str[0]
# print("Character at index 0 is: ", ch)
# print(str[5])

#Scilicing of string
# str = "Manish Rajput"
# slice1 = str[2:5]  # nis(2,3,4)
# print("Slice from index 2 to 5 is: ", slice1)
# print(str[2:8])  # nis R    (2,3,4,5,6,7)
# print(str[7:len(str)])  #[7:12] last index (7,8,9,10,11)
# print(str[7:])  # last index (7,8,9,10,11)
# print(str[:7]) #[0:7] first index (0,1,2,3,4,5,6)


# Negative indexing of string
# str = "Manish"
# #######654321
# print(str[-4]) #n
# print(str[-4:-1]) #nis



# STRING FUNCTION-----------------------------------------------------
str = "i am manish rajput And i am student"

# 1. Return true iif string ends with sbstr
# print(str.endswith("ut")) #True
# print(str.endswith("re")) #False


#2. Capitalize 1st char
# print(str.capitalize())

#3. Replace
# print(str.replace("m" , "p"))
# print(str.replace("manish" , "tushar"))

#4. find)return 1st index
# print(str.find("m"))
# print(str.find("manish"))

#5 count
# print(str.count("i"))
# print(str.count("am"))




# 1.Question -- WAP to input user's first name & print its length
# name = input("Enter Your First Name: ")
# print(len(name))

# 2. Question -- WAP to find the occurrence of '$' in a string
# str = "$ this is a string $ and i count the dooler $ sign in string$"
# print(str.count("$"))