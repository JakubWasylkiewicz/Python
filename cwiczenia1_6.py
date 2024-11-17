def common_characters(text1, text2):
    result = ""  

   
    for char in text1: #in reversed(text1): żeby poszło od końca
        if char in text2 and char not in result:  
            result += char

    return result


input1 = input("Podaj pierwszy łańcuch znaków: ")
input2 = input("Podaj drugi łańcuch znaków: ")
print("Wspólne znaki:", common_characters(input1, input2))
