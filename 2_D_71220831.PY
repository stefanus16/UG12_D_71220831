print("~~~~~ Table Matematika Nich ~~~~~")
print("Pilihan Model Matematika")

print("1. Perkalian")
print("2. Pembagian")
model=int(input("Masukkan model matematika yang diinginkan 1/2 :"))
angka=int(input("Menampilkan table matematika dari angka:"))
if(model==1) :
    for i in range(1,11)   :
        hasil = (angka*i)
        print(angka, "x", i, "=", hasil)

elif(model==2) :
    for a in range(50,66) :
        hasil = (a/angka)
        print(a, ":", angka, "=", hasil)
else :
    print("Pilihan tidak tersedia, jangan ngasal!")