
# Lista na znaki wprowadzone przez użytkownika
unique_chars = []

print("Podaj 10 znaków (mogą się powtarzać):")

# Pętla, która działa 10 razy
for _ in range(10):
    char = input("Wprowadź znak: ")  # Wprowadzenie znaku
    if char not in unique_chars:  # Sprawdzanie, czy znak jest unikalny
        unique_chars.append(char)

# Tworzenie łańcucha z unikalnych znaków
result = ''.join(unique_chars)
print("Łańcuch wynikowy z unikalnych znaków:", result)
