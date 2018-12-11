def OneAway(s, t):
    if len(s) - 1 == len(t):
        for letter in t: 
            if letter not in s: 
                print("False")
        print("True")
            
    if len(t) - 1 == len(s):
        for letter in s:
            if letter not in t:
                print("False")
        print("True")
        
    if s == t:
        print("True")
    count = 0
    if(len(s) == len(t)):
        for letter in s:
            if letter not in t:
                count+=1
            if count > 1:
                print("False")
        print("True")
        
        
            
OneAway("play", "blay")
