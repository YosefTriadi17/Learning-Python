siswa = {
    "nama": "Andi",
    "umur": 12,
    "alamat": "Jl. Merdeka No. 10"
}
print(siswa)

print(siswa["nama"])
print(siswa["umur"])
print(siswa["alamat"])

del siswa["alamat"]
print(siswa)

for key, value in siswa.items():
        print(key, "=", value)