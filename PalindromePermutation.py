def PalindromePermutation(p):
    letter_dict = {}
    p = p.lower()
    for letter in p:
        if letter not in letter_dict and letter != ' ':
            letter_dict[letter] = 1
        elif letter != ' ':
            letter_dict[letter] += 1

    twos = 0
    for key in letter_dict:
        if letter_dict.get(key) == 2:
            twos += 1;

    if twos < len(letter_dict) - 1:
        print("False")
    else:
        print("True")
        
    print(letter_dict)
    
PalindromePermutation("Taco Cat")

    
