def StringCompression(s):
    curr_letter = s[0]
    count = 1
    string = ""
    for i in range(1, len(s)):
        if s[i] == curr_letter:
            count += 1;
            curr_letter = s[i]
        else:
            string = string + curr_letter + str(count)
            curr_letter = s[i]
            count = 1
    string = string + curr_letter + str(count)
        
    print(string)
  
        
StringCompression("aabbcccccccccccccc")
StringCompression("a")

