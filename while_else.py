true_pwd="12345"
max_attempt=3
attempt=0

while attempt<max_attempt:
    pwd = input("Masukkan password: ")
    if pwd==true_pwd:
        print("Password benar")
        break
    else:
        print("Password salah")
        attempt+=1
else:
    print("Anda telah mencoba sebanyak", max_attempt, "kali. Password salah.")
