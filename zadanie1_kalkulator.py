import math
a = float(input("Liczba pierwsza: "))
b = float(input("Liczba druga: "))

operation = input("Wybierz operację (+, -, *, /, ^, sqrt): ")

if operation == '+':
    print("Wynik: ", a + b)
elif operation == '-':
    print("Wynik: ", a - b)
elif operation == '*':
    print("Wynik: ", a * b)
elif operation == '/':
    if b != 0:
            print("Wynik: ", a / b)
    else:
         print("Pamiętaj cholero nie dziel przez zero!")
elif operation == '^':
    print("Wynik: ", a ** b)
elif operation == 'sqrt':
    if a >= 0:
        print("Pierwiastek kwadratowy z pierwszej liczby: ", math.sqrt(a))
    else:
        print("Pierwiastek z liczby ujemnej nie isnieje w zbiorze liczb rzeczywistych...")        
             