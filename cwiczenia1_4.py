def count_chars_occuring_twice(text):
    char_counts = {}  

    
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1

    
    result = 0
    for count in char_counts.values():
        if count == 2:
            result += 1

    return result


input_text = input("Podaj łańcuch znaków: ")
print("Liczba znaków występujących dokładnie dwa razy:", count_chars_occuring_twice(input_text))

"""
def count_chars_occuring_twice_reverse(text):
    char_counts = {}  # Słownik na liczbę wystąpień znaków

    
    for char in reversed(text):
        char_counts[char] = char_counts.get(char, 0) + 1

    
    result = 0
    for count in char_counts.values():
        if count == 2:
            result += 1

    return result


input_text = input("Podaj łańcuch znaków: ")
print("Liczba znaków występujących dokładnie dwa razy:", count_chars_occuring_twice_reverse(input_text))
"""