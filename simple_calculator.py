print(" ===== KALKULATOR SEDERHANA =====")

try:
    valid = True
    while valid:
        angka1 = input("Masukkan Angka Pertama: ")
        angka2 = input("Masukkan Angka Kedua: ")

        if not angka1.isdigit() or not angka2.isdigit():
            print("Input harus berupa angka")
        else:
            valid = False
            break;

    result = int(angka1) + int(angka2)
    print(f"Hasil Penjumlahan: {result}")
except Exception as e:
    print(f"Error: {e}")

print(" ===== SELESAI =====")
