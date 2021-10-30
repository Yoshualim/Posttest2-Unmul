def menu():

    print("====================================================================================")
    print("Selamat datang di program ini")
    print("Untuk hari biasa silakan ketik Nondiskon dan untuk hari spesial silakan ketik Diskon")
    print("====================================================================================")
    
def nondiskon():

 opsi = "Y"
 while opsi == "Y":

    Hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
    Bulan = ["Januari","Febuari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
    tanggal = list(range(32))
    datahari = []

    print("hari?")
    print(Hari)
    hari1 = str(input(":"))
    datahari.append(hari1)
    print("Tanggal?")
    print(tanggal)
    tanggal1 = int(input(":"))
    datahari.append(tanggal1)
    print("Bulan?")
    print(Bulan)
    bulan1 = str(input(":"))
    datahari.append(bulan1)
    print("Tahun?")
    Tahun1 = int(input(":"))
    datahari.append(Tahun1)

    break

 opsi = "Y"
 while opsi == "Y":
 
    print (datahari)
    print("""
    ======================================
    ======================================

    Skadi Bakery Shop
    List menu roti

    ======================================
    A. Croissant      : Rp 14.000 
    B. Donat          : Rp 12.000
    C. SwissRoll      : Rp 18.000
    D. Muffin         : Rp 13.000
    E. Brownie        : Rp 15.000
    ======================================
    ======================================
    
    """)

    pesanan1 = str(input("Masukan Abjad dari menu roti :"))
    jumlahpesanan1 = int(input("masukan jumlah pesanan :"))

    if pesanan1 == ("A"):
        namapesanan1 = ("Croissant")
        harga1 = (14000 * jumlahpesanan1)
        totalharga1 = int(harga1)
        diskon1 = 0

    elif pesanan1 == ("B"):
        namapesanan1 = ("Donat")
        harga1 = (12000 * jumlahpesanan1)
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("C"):
        namapesanan1 = ("Swiss Roll")
        harga1 = (18000 * jumlahpesanan1)
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("D"):
        namapesanan1 = ("Muffin")
        harga1 = (13000 * jumlahpesanan1)
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("E"):
        namapesanan1 = ("Brownie")
        harga1 = (15000 * jumlahpesanan1)
        totalharga1 = int(harga1)
        diskon1 = 0

    else:
        print("index list huruf yang dicari tidak ada, silakan coba lagi.")

    
    print("==============================")
    print("Skadi Bakery Shop")
    print("=======================")
    print(datahari)
    print("menu :", namapesanan1)
    print("jumlah pesanan :", jumlahpesanan1)
    print("harga :", harga1)
    print("diskon :", diskon1)
    print("jumlah bayar :", totalharga1)
    print("===========================")
    print("Terima kasih telah belanja di Skadi Bakery Shop")
    
    opsi = input("apakah anda ingin order lagi? (Y/N) :")


def diskon():

 opsi = "Y"
 while opsi == "Y":

    Hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
    Bulan = ["Januari","Febuari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
    tanggal = list(range(32))
    datahari = []

    print("hari?")
    print(Hari)
    hari1 = str(input(":"))
    datahari.append(hari1)
    print("Tanggal?")
    print(tanggal)
    tanggal1 = int(input(":"))
    datahari.append(tanggal1)
    print("Bulan?")
    print(Bulan)
    bulan1 = str(input(":"))
    datahari.append(bulan1)
    print("Tahun?")
    Tahun1 = int(input(":"))
    datahari.append(Tahun1)

    break

 opsi = "Y"
 while opsi == "Y":
 
    print (datahari)

    print("""
    ======================================
    ======================================

    Skadi Bakery Shop
    List menu roti

    ======================================
    A. Croissant      : Rp 14.000 
    B. Donat          : Rp 12.000
    C. SwissRoll      : Rp 18.000
    D. Muffin         : Rp 13.000
    E. Brownie        : Rp 15.000
    ======================================
    ======================================
    
    """)

    pesanan2 = str(input("Masukan Abjad dari menu roti :"))
    jumlahpesanan2 = int(input("masukan jumlah pesanan :"))

    if pesanan2 == ("A"):
        namapesanan2 = ("Croissant")
        harga2 = (14000 * jumlahpesanan2)
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = int(harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 >= 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)

    elif pesanan2 == ("B"):
        namapesanan2 = ("Donat")
        harga2 = (12000 * jumlahpesanan2)
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = int(harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 >= 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    
    elif pesanan2 == ("C"):
        namapesanan2 = ("Swiss Roll")
        harga2 = (18000 * jumlahpesanan2)
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = int(harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 >= 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    
    elif pesanan2 == ("D"):
        namapesanan2 = ("Muffin")
        harga2 = (13000 * jumlahpesanan2)
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = int(harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 >= 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    
    elif pesanan2 == ("E"):
        namapesanan2 = ("Brownie")
        harga2 = (15000 * jumlahpesanan2)
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = (harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 >= 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    else:
        print("index list huruf yang dicari tidak ada, silakan coba lagi.")

    
    print("==============================")
    print("Skadi Bakery Shop")
    print("==============================")
    print(datahari)
    print("menu :", namapesanan2)
    print("jumlah pesanan :", jumlahpesanan2)
    print("harga :", harga2)
    print("diskon :", diskon2)
    print("jumlah bayar :", totalharga2)
    print("==============================")
    print("Terima kasih telah belanja di Skadi Bakery Shop")
    

    opsi = input("Apakah ingin kembali keawal? (Y/N) :")

menu()

masukan = str(input(":"))


if masukan == ("Nondiskon"):
    nondiskon()
elif masukan == ("Diskon"):
    diskon()
else:
    print("ISI YANG BENAR!!!")