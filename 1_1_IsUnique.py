#Determine if a string has all unique characters 
import sys
def remove_with_dict(string):
    #128 unique characters in ASCII, so if string is longer than that, it can't be unique
    if len(string) > 128:
        return False 
    string_dict = {}
    for letter in string:
        if letter not in string_dict:
            string_dict[letter] = True
        else:
             print("False")
             sys.exit()
    print(string_dict.keys())

