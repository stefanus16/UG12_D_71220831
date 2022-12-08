susu = 20000
permen = 500
roti = 15000
indomie = 3000
vitamin = 50000

uangSemula = int(input('Masukkan jumlah uang: RP'))
start = input('ketik START untuk memulai: ')
if start.lower() == 'start':
    while True:
        buy = input('Apa barang yang akan Anda buy? ')
        if buy.lower() =='susu':
            if uangSemula >= susu:
                uangSemula -= susu
                print('Sisa uang Anda',uangSemula)
            else:
                print('Uang tidak cukup')
        elif buy.lower() =='permen':
            if uangSemula >= permen:
                uangSemula -= permen
                print('Sisa uang Anda',uangSemula)
            else:
                print('Uang anda tidak cukup')
        elif buy.lower() =='roti':
            if uangSemula >= roti:
                uangSemula -= roti
                print('Sisa uang Anda',uangSemula)
            else:
                print('Uang anda tidak cukup')
        elif buy.lower() =='indomie':
            if uangSemula >= indomie:
                uangSemula -= indomie
                print('Sisa uang Anda',uangSemula)
            else:
                print('Uang anda tidak cukup')
        elif buy.lower() =='vitamin':
            if uangSemula >= vitamin:
                uangSemula -= vitamin
                print('Sisa uang Anda',uangSemula)
            else:
                print('Uang anda tidak cukup')
        elif buy.lower() == 'sudah':
            break
        else :
            print('Barang tidak tersedia')