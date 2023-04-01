#Pierre Victor T. Zurbito
#Object Oriented Programming
#BSCPE 1-4
#Polytechnic University of the Philippines
#PROBLEM 2

#Allows the user to input a certain string
input_string=input("Please input a string to decrypt:")

#String undergoes decryption
if "*" in input_string:
    string_a_decrypt=input_string.replace("*", "a")
if "&" in string_a_decrypt:
    string_e_decrypt=string_a_decrypt.replace("&", "e")
if "#" in string_e_decrypt:
    string_i_decrypt=string_e_decrypt.replace("#","i")
if "+" in string_i_decrypt:
    string_o_decrypt=string_i_decrypt.replace("+","o")
if "!" in string_o_decrypt:
    output_string=string_o_decrypt.replace("!","u")

#Prints the decrypted string
print(output_string)