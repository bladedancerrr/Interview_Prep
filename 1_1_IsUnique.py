#Determine if a string has all unique characters 
import sys
def remove_with_dict(string):
    string_dict = {}
    for letter in string:
        if letter not in string_dict:
            string_dict[letter] = True
        else:
             print("False")
             sys.exit()
    print(string_dict.keys())

