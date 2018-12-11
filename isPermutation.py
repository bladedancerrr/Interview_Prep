def isPermutation(s, t):
    if len(s) != len(t):
        return False 
    dict_s = {}
    dict_t = {}
    for letter in s: 
        if letter not in dict_s:
            dict_s[letter] = 1;
        else:
            dict_s[letter] += 1;
    
    for letter in t: 
        if letter not in dict_t:
            dict_t[letter] = 1;
        else: 
            dict_t[letter] += 1;
            
    print(dict_t == dict_s)
    print(dict_t, dict_s)
    
isPermutation("aahsey", "ayesha")
