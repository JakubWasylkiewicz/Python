
print("Podaj 10 liczb. Obliczymy sumę dodatnich liczb całkowitych.")


i = 0
total_sum = 0


while i < 10:
    try:
        number = int(input(f"Podaj liczbę {i + 1}: "))  
        if number > 0:
            total_sum += number 
        i += 1
    except ValueError:
        print("To nie jest liczba całkowita. Spróbuj ponownie.")

'''
print(f"Suma dodatnich liczb wynosi: {total_sum}")

def suma_for():
    total_sum = 0
    for i in range(1, 11):
        try:
            num = int(input(f"Podaj liczbę {i}: "))
            if num > 0:
                total_sum += num
        except ValueError:
            print("Niepoprawna wartość. Spróbuj ponownie.")
    print(f"Suma liczb dodatnich wynosi: {total_sum}")

'''