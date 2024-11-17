def reorganize_string(text):
    uppercase = ""  # Duże 
    lowercase = ""  # Małe 
    digits = ""     # Cyfry
    others = ""     # Inne 

    
    for char in text:
        if char.isupper():
            uppercase += char
        elif char.islower():
            lowercase += char
        elif char.isdigit():
            digits += char
        else:
            others += char

   
    return uppercase + lowercase + digits + others


input_text = input("Podaj łańcuch znaków: ")
print("Przekształcony łańcuch:", reorganize_string(input_text))


'''
def reorganize_string_reverse(text):
    uppercase = ""  
    lowercase = ""  
    digits = ""
    others = "" 

   
    for char in reversed(text):
        if char.isupper():
            uppercase += char
        elif char.islower():
            lowercase += char
        elif char.isdigit():
            digits += char
        else:
            others += char

    
    return uppercase + lowercase + digits + others


input_text = input("Podaj łańcuch znaków: ")
print("Przekształcony łańcuch:", reorganize_string_reverse(input_text))

'''