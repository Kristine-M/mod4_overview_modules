def reverse_string(s):
    # function to reverse a string
     
    backward = ""
    for i in range(len(s) - 1, -1, -1):
        backward += s[i]
        
    return backward


def capitalize_string(s):
    # function to capitalize a string
    
    cap = ""
    
    for i in range(len(s)):
        cap += s[i].upper()
        
    return cap