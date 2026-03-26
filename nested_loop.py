number1 = int(input("Masukkan bilangan pertama: "))
number2 = int(input("Masukkan bilangan kedua: "))

for i in range(number1, number2+1):
    for j in range(number1, number2):
        print(i, "*", j, " = ", i*j)
    print("======")
    