n = int(input("Ile liczb w ciągu Fibonacciego chcesz wyświetlić? "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Proszę wprowadzić liczbę większą niż 0.")
elif n== 1:
    print("Ciąg Fibonacciego do", n, ":")
    print(a)
else:
    print("Ciąg Fibonacciego:")
    while count < n:
        print(a)
        nth = a + b
        a = b
        b = nth
        count += 112        