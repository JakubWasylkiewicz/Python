def suma_dodatnich(ilosc):
    total_sum = 0
    for i in range(ilosc):
        try:
            num = int(input(f"Podaj liczbę {i + 1}: "))
            if num > 0:
                total_sum += num
        except ValueError:
            print("Niepoprawna wartość. Spróbuj ponownie.")
    return total_sum


wynik = suma_dodatnich(10)
print(f"Suma liczb dodatnich: {wynik}")
