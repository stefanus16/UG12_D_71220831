print("~~~~~ Table Matematika Nich ~~~~~")
print("pilihan model matematika")
print("1. Perkalian")
print("2. Pembagian")
input("Masukan model matematika yang diinginkan 1/2: ")
angka = int(input("menampilkan tabel matematika dari angka: "))
for i in range(1,11):
    print(angka, 'x', i, '=', angka*i)

angka = int(input("menampilkan table matematika dengan angka: "))
for x in range(50,66):
    print(angka, ":", x, "=", angka/x)