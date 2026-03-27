try:
    def divide(a, b):
        try:
            result = a / b
        except Exception as e:
            print(a, "/", b)
            print(f"Error: {e}")
        else:
            print(f"Result: {result}")

    divide(10, 2)
    divide2(10, "ada apa ini")

except Exception as e:
    print(f"Error: {e}")


try:
    number1 = int(input("Masukkan Angka: "))
except ValueError:
    print("Input harus berupa angka")
except Exception as e:
    print(f"Error: {e}")
else:
    if number1 % 2 == 0:
        print("Angka genap")
    else:
        print("Angka ganjil")
finally:
        print("Program selesai")
