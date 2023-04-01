#Pierre Victor T. Zurbito
#Object Oriented Programming
#BSCPE 1-4
#Polytechnic University of the Philippines
#PROBLEM 1

#Allows the user to input a certain string
input_string=input("Please input a string to encrypt:")

#String undergoes encryption
if "a" in input_string:
    string_a_encrypt=input_string.replace("a", "*")
if "e" in string_a_encrypt:
    string_e_encrypt=string_a_encrypt.replace("e", "&")
if "i" in string_e_encrypt:
    string_i_encrypt=string_e_encrypt.replace("i","#")
if "o" in string_i_encrypt:
    string_o_encrypt=string_i_encrypt.replace("o","+")
if "u" in string_o_encrypt:
    output_string=string_o_encrypt.replace("u","!")

#Prints the encrypted string
print(output_string)
