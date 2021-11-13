
roti = {
        "Menu_roti": ["Croissant", "Donat", "SwissRoll", "Muffin", "Brownie", "Cake", "Garlic Bread", "Roti Tawar"],
        "Harga_roti" : [14000, 12000, 18000, 13000, 15000, 50000, 17000, 10000]
        }

Data_hari = {
        "Hari" : ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"],
        "Bulan" : ["Januari","Febuari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"],
        "tanggal" : list(range(1,32)),
        "datahari" : []
            }

Keuntungan = {
        "Total_keuntungan" : []
            }

Userlogin = {
        "username" : "Yoshua",
        "Password_Normal" : 210,
        "Password_Admin" : 6093
            }

def user_login():
    print("=============")
    print("Selamat datang")
    print("=============")
    user =str(input("Masukan username :"))
    try:
        Pass =int(input("Masukan password :"))
    except ValueError:
        print("Password berbentuk angka silakan isi ulang")
        user_login()
    if user == Userlogin["username"] and Pass == Userlogin["Password_Admin"]:
        print("Login Berhasil")
        main_admin()

    elif user == Userlogin["username"] and Pass == Userlogin["Password_Normal"]:
        print("Login Berhasil")
        datahari1()
        
    else:
        print("Username atau password anda salah, silakan isi kembali")
        user_login()

def main_admin():
    
    print("Menu Admin")
    print("======================================")
    print("1. Lihat list menu roti")
    print("2. Tambahkan menu roti")
    print("3. Edit menu roti")
    print("4. Hapus menu roti ")
    print("5. Masuk ke mode kasir")
    print("6. Hapus jumlah keuntungan hari ini")
    print("7. Keluar dari program ini")
    print("0. Keluar dari menu Admin")
    print ("======================================")
    Jumlahuntung = sum(Keuntungan["Total_keuntungan"])
    print ("==================================================================")
    print("Jumlah keuntungan yang diraih pada hari ini adalah Rp.", Jumlahuntung)
    print ("==================================================================")

    pilihan_menu = input("pilih menu :")
    
    if pilihan_menu == ("1"):
        List_menuroti()
    elif pilihan_menu == ("2"):
        Tambah_menuroti()
    elif pilihan_menu == ("3"):
        Edit_menuroti()
    elif pilihan_menu == ("4"):
        Hapus_menuroti()
    elif pilihan_menu == ("5"):
        masukkasir()
    elif pilihan_menu == ("6"):
        Hapus_Keuntungan()
    elif pilihan_menu == ("7"):
        Keluar()
    elif pilihan_menu == ("0"):
        kembalilogin()        
    else:
        print("Anda salah input silakan coba kembali")
        kembali_menu()

def List_menuroti():
    print("List Menu roti Skadi Bakery Shop")
    print ("==========================================")
    try:
        print ("A.", roti["Menu_roti"][0], "Rp.", roti["Harga_roti"][0])
    except IndexError:
        print()
    try:
        print ("B.", roti["Menu_roti"][1], "Rp.", roti["Harga_roti"][1])
    except IndexError:
        print()
    try:
        print ("C.", roti["Menu_roti"][2], "Rp.", roti["Harga_roti"][2])
    except IndexError:
        print()
    try:
        print ("D.", roti["Menu_roti"][3], "Rp.", roti["Harga_roti"][3])
    except IndexError:
        print()
    try:
        print ("E.", roti["Menu_roti"][4], "Rp.", roti["Harga_roti"][4])
    except IndexError:
        print()
    try:
        print ("F.", roti["Menu_roti"][5], "Rp.", roti["Harga_roti"][5])
    except IndexError:
        print()
    try:
        print ("G.", roti["Menu_roti"][6], "Rp.", roti["Harga_roti"][6])
    except IndexError:
        print()
    try:
        print ("H.", roti["Menu_roti"][7], "Rp.", roti["Harga_roti"][7])
    except IndexError:
        print()
    try:
        print ("I.", roti["Menu_roti"][8], "Rp.", roti["Harga_roti"][8])
    except IndexError:
        print()
    try:
        print ("J.", roti["Menu_roti"][9], "Rp.", roti["Harga_roti"][9])
    except IndexError:
        print()
    print ("==========================================")
    kembali_menu()

def Tambah_menuroti():
    print                ("=============================")        
    Menu_baru = str(input("Masukan nama menu roti baru : "))
    print                ("=============================")

    roti["Menu_roti"].append(Menu_baru)
    Tambah_menuroti1()
   
def Tambah_menuroti1():
    print                     ("==============================")

    try:
        Harga_baru = int(input("Masukan harga menu roti baru : "))
    except ValueError:
        print("Masukan harga dengan betul bukan dengan huruf")
        print(" ============================================")
        Tambah_menuroti1()
    
    print                     ("===============================") 

    roti["Harga_roti"].append(Harga_baru)
    print("======================")
    print("Menu berhasil dimasukan!")
    print("======================")
    kembali_menu()

def Edit_menuroti():

    print("===============================================================")
    print(roti["Menu_roti"])
    print("===============================================================")
    print("Pilih menu roti yang akan di edit (angka 0 sebagai menu pertama)")
    print("===============================================================")

   

    try:
        Menu_edit = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Edit_menuroti()
    
    try:
        print(roti["Menu_roti"][Menu_edit])
    except IndexError:
        print("Masukan angka yang ada (dimulai dari 0)")
        Edit_menuroti()
    
    print                ("===============")
    Nama_edit = str(input("Edit nama menu: "))
    print                ("===============")
    roti["Menu_roti"][Menu_edit] = Nama_edit
    Edit_menuroti1()

def Edit_menuroti1():

    print("==============================================================================")
    print(roti["Harga_roti"])
    print("==============================================================================")
    print("Pilih harga roti yang akan di edit (masukan angka yang sama seperti sebelumnya)")
    print("==============================================================================")

    try:
        Harga_edit = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Edit_menuroti1()

    try:
        print(roti["Harga_roti"][Harga_edit])
    except IndexError:
        print("Masukan angka yang ada (dimulai dari 0)")
        Edit_menuroti1()

    try:
        harga_edit = int(input("Edit harga menu: "))
    except ValueError:
        print("Masukan angka bukan huruf")
        Edit_menuroti1()
            
        
        
    roti["Harga_roti"][Harga_edit] = harga_edit
    print("====================")
    print("Menu berhasil diubah!")
    print("====================")
    kembali_menu()

def Hapus_menuroti():
    print("=================================================================")
    print(roti["Menu_roti"])
    print("=================================================================")
    print("Pilih menu roti yang akan dihapus (angka 0 sebagai menu pertama) :")
    print("=================================================================")

    try:
        Hapus_menu = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Hapus_menuroti()

    try:
        del roti["Menu_roti"][Hapus_menu]
    except IndexError:
        print("Masukan angka yang ada (dimulai dari 0)")
        Hapus_menuroti()

    del roti["Harga_roti"][Hapus_menu]

    print("======================")
    print("Menu berhasil di hapus!")
    print("======================")
    kembali_menu()

def masukkasir():
    print("====================================")
    print("Apakah anda ingin masuk mode kasir? ")
    print("====================================")
    konfirmasi = str(input("Ya/Tidak :"))
    if konfirmasi == "Ya":
            datahari1()
    elif konfirmasi == "Tidak":
            print ("Aksi dihentikan")
            kembali_menu()
    else:
            print("Inputan salah, silakan konfirmasi kembali")
            masukkasir()


def Keluar():
    print("======================================")
    print("Apakah anda ingin matikan program ini?")
    print("======================================")
    konfirmasi = str(input("Ya/Tidak :"))
    if konfirmasi == "Ya":
        print ("==========================================")
        print ("Terima kasih telah menggunakan program ini")
        print ("==========================================")
        exit()
    elif konfirmasi == "Tidak":
        kembali_menu()
    else:
        print("Inputan salah, silakan isi konfimasi kembali")
        Keluar()

def Hapus_Keuntungan():
    print ("===================================================================================================================")
    print("Apakah anda yakin untuk menghapus jumlah keuntungan hari ini? pastikan anda sudah mencatat jumlah keuntungan hari ini")
    print ("===================================================================================================================")
    konfirmasi = str(input("Ya/Tidak :"))
    if konfirmasi == "Ya":
        Keuntungan["Total_keuntungan"].clear()
        print ("====================")
        print ("Data berhasil di hapus")
        print ("====================")
        kembali_menu()
    elif konfirmasi == "Tidak":
        print ("Aksi dihentikan")
        kembali_menu()
    else:
        print("Inputan salah, silakan isi konfimasi kembali")
        Hapus_Keuntungan()

def kembalilogin():
    print("=======================================")
    print("Apakah anda ingin kembali ke menu login? ")
    print("=======================================")
    konfirmasi = str(input("Ya/Tidak :"))
    if konfirmasi == "Ya":
            user_login()
    elif konfirmasi == "Tidak":
            print ("Aksi dihentikan")
            kembali_menu()
    else:
            print("Inputan salah, silakan konfirmasi kembali")
            kembalilogin()


def kembali_menu():
    input("Tekan enter untuk kembali")
    main_admin()

    
def datahari1():
        print("====================")
        print("hari?")
        print("====================")
        print(Data_hari["Hari"])
        print("====================")
        hari1 = str(input(":"))
        if hari1 in Data_hari["Hari"]:
            Data_hari["datahari"].append(hari1)
            datahari2()
        else:
            print("Anda salah masukan hari")
            datahari1()
        
def datahari2():
        print("====================")
        print("Tanggal?")
        print("====================")
        print(Data_hari["tanggal"])
        print("====================")
        try:
            tanggal1 = int(input(":"))
        except ValueError:
            print("Anda salah masukan tanggal")
            datahari2()
        if tanggal1 in range(1,32):
            Data_hari["datahari"].append(tanggal1)
            datahari3()
        else:
            print("Anda salah masukan tanggal")
            datahari2()

        

def datahari3():
        print("====================")
        print("Bulan?")
        print("====================")
        print(Data_hari["Bulan"])
        print("====================")
        bulan1 = str(input(":"))
        if bulan1 in Data_hari["Bulan"]:
            Data_hari["datahari"].append(bulan1)
            datahari4()
        else:
            print("Anda salah masukan bulan")
            datahari3()
        

def datahari4():
        Tahun1 = 2021
        Data_hari["datahari"].append(Tahun1)
        menu()

def menu():

        print("====================================================================================")
        print("Selamat datang di program ini")
        print("Untuk hari biasa silakan ketik Nondiskon dan untuk hari spesial silakan ketik Diskon")
        print("====================================================================================")
        masukan = str(input(":"))

        if masukan == ("Nondiskon"):
            nondiskon()
        elif masukan == ("Diskon"):
            diskon()
        else:
            print("ISI YANG BENAR!!!")
            menu()
        
def nondiskon():

    print (Data_hari["datahari"])
    print ("==========================================")
    print ("==========================================")
    print ("Skadi Bakery Shop")
    print ("==========================================")
    print ("Nama dan Harga Roti")
    print ("==========================================")

    try:
        print ("A.", roti["Menu_roti"][0], "Rp.", roti["Harga_roti"][0])
    except IndexError:
        print()
    try:
        print ("B.", roti["Menu_roti"][1], "Rp.", roti["Harga_roti"][1])
    except IndexError:
        print()
    try:
        print ("C.", roti["Menu_roti"][2], "Rp.", roti["Harga_roti"][2])
    except IndexError:
        print()
    try:
        print ("D.", roti["Menu_roti"][3], "Rp.", roti["Harga_roti"][3])
    except IndexError:
        print()
    try:
        print ("E.", roti["Menu_roti"][4], "Rp.", roti["Harga_roti"][4])
    except IndexError:
        print()
    try:
        print ("F.", roti["Menu_roti"][5], "Rp.", roti["Harga_roti"][5])
    except IndexError:
        print()
    try:
        print ("G.", roti["Menu_roti"][6], "Rp.", roti["Harga_roti"][6])
    except IndexError:
        print()
    try:
        print ("H.", roti["Menu_roti"][7], "Rp.", roti["Harga_roti"][7])
    except IndexError:
        print()
    try:
        print ("I.", roti["Menu_roti"][8], "Rp.", roti["Harga_roti"][8])
    except IndexError:
        print()
    try:
        print ("J.", roti["Menu_roti"][9], "Rp.", roti["Harga_roti"][9])
    except IndexError:
        print()
    print ("==========================================")
    print ("==========================================")

    pesanan1 = str(input("Masukan Abjad dari menu roti :"))
    print ("============================================")
    try:
        jumlahpesanan1 = int(input("masukan jumlah pesanan :"))
    except ValueError:
        print("Mohon input jumlah pesanan dengan benar")
        nondiskon()
    print ("=========================================")

    if pesanan1 == ("A"):
        try:
            namapesanan1 = roti["Menu_roti"][0]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (roti["Harga_roti"][0] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0

    elif pesanan1 == ("B"):
        try:
            namapesanan1 = roti["Menu_roti"][1]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (roti["Harga_roti"][1] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("C"):
        try:
            namapesanan1 = roti["Menu_roti"][2]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (roti["Harga_roti"][2] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("D"):
        try:
            namapesanan1 = roti["Menu_roti"][3]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (roti["Harga_roti"][3] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
        
    elif pesanan1 == ("E"):
        try:
            namapesanan1 = roti["Menu_roti"][4]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (roti["Harga_roti"][4] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0

    elif pesanan1 == ("F"):
        try:
            namapesanan1 = roti["Menu_roti"][5]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (roti["Harga_roti"][5] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("G"):
        try:
            namapesanan1 = roti["Menu_roti"][6]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (roti["Harga_roti"][6] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("H"):
        try:
            namapesanan1 = roti["Menu_roti"][7]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (roti["Harga_roti"][7] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("I"):
        try:
            namapesanan1 = roti["Menu_roti"][8]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (roti["Harga_roti"][8] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0

    elif pesanan1 == ("J"):
        try:
            namapesanan1 = roti["Menu_roti"][9]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (roti["Harga_roti"][9] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0

    else:
        print("index list huruf yang dicari tidak ada, silakan coba lagi.")
        nondiskon()

    
    print("===============================================")
    print("Skadi Bakery Shop")
    print("===============================================")
    print(Data_hari["datahari"])
    print("menu :", namapesanan1)
    print("jumlah pesanan :", jumlahpesanan1)
    print("harga :", harga1)
    print("diskon :", diskon1)
    print("jumlah bayar :", totalharga1)
    print("===============================================")
    print("Terima kasih telah belanja di Skadi Bakery Shop")
    Keuntungan["Total_keuntungan"].append(totalharga1)

    print("===========================================")
    opsi = input("apakah anda ingin order lagi? (Y/N) :")
    print("===========================================")
    if opsi == "Y":
        nondiskon()
    else:
        print("===========================================================")
        masukan_1 = input("apakah anda ingin kembali ke menu login? (Y/N) :")
        print("===========================================================")
        if masukan_1 == "Y":
            Data_hari["datahari"].clear()
            user_login()
        else:
            nondiskon()



def diskon():
 
    print (Data_hari["datahari"])
    print ("==========================================")
    print ("==========================================")
    print ("Skadi Bakery Shop")
    print ("==========================================")
    print ("Nama dan Harga Roti")
    print ("==========================================")

    try:
        print ("A.", roti["Menu_roti"][0], "Rp.", roti["Harga_roti"][0])
    except IndexError:
        print()
    try:
        print ("B.", roti["Menu_roti"][1], "Rp.", roti["Harga_roti"][1])
    except IndexError:
        print()
    try:
        print ("C.", roti["Menu_roti"][2], "Rp.", roti["Harga_roti"][2])
    except IndexError:
        print()
    try:
        print ("D.", roti["Menu_roti"][3], "Rp.", roti["Harga_roti"][3])
    except IndexError:
        print()
    try:
        print ("E.", roti["Menu_roti"][4], "Rp.", roti["Harga_roti"][4])
    except IndexError:
        print()
    try:
        print ("F.", roti["Menu_roti"][5], "Rp.", roti["Harga_roti"][5])
    except IndexError:
        print()
    try:
        print ("G.", roti["Menu_roti"][6], "Rp.", roti["Harga_roti"][6])
    except IndexError:
        print()
    try:
        print ("H.", roti["Menu_roti"][7], "Rp.", roti["Harga_roti"][7])
    except IndexError:
        print()
    try:
        print ("I.", roti["Menu_roti"][8], "Rp.", roti["Harga_roti"][8])
    except IndexError:
        print()
    try:
        print ("J.", roti["Menu_roti"][9], "Rp.", roti["Harga_roti"][9])
    except IndexError:
        print()
    print ("==========================================")
    print ("==========================================")

    pesanan2 = str(input("Masukan Abjad dari menu roti :"))
    print ("============================================")
    try:
        jumlahpesanan2 = int(input("masukan jumlah pesanan :"))
    except ValueError:
        print("Mohon input jumlah pesanan dengan benar")
        diskon()
    print ("================================================")

    if pesanan2 == ("A"):
        try:
            namapesanan2 = roti["Menu_roti"][0]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga2 = (roti["Harga_roti"][0] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = int(harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 == 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)

    elif pesanan2 == ("B"):
        try:
            namapesanan2 = roti["Menu_roti"][1]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga2 = (roti["Harga_roti"][1] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = int(harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 == 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    
    elif pesanan2 == ("C"):
        try:
            namapesanan2 = roti["Menu_roti"][2]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga2 = (roti["Harga_roti"][2] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = int(harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 == 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    
    elif pesanan2 == ("D"):
        try:
            namapesanan2 = roti["Menu_roti"][3]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga2 = (roti["Harga_roti"][3] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = int(harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 == 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    
    elif pesanan2 == ("E"):
        try:
            namapesanan2 = roti["Menu_roti"][4]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga2 = (roti["Harga_roti"][4] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = (harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 == 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    
    elif pesanan2 == ("F"):
        try:
            namapesanan2 = roti["Menu_roti"][5]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga2 = (roti["Harga_roti"][5] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = (harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 == 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)

    elif pesanan2 == ("G"):
        try:
            namapesanan2 = roti["Menu_roti"][6]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga2 = (roti["Harga_roti"][6] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = (harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 == 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    
    elif pesanan2 == ("H"):
        try:
            namapesanan2 = roti["Menu_roti"][7]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga2 = (roti["Harga_roti"][7] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = (harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 == 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)

    elif pesanan2 == ("I"):
        try:
            namapesanan2 = roti["Menu_roti"][8]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga2 = (roti["Harga_roti"][8] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = (harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 == 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    
    elif pesanan2 == ("J"):
        try:
            namapesanan2 = roti["Menu_roti"][9]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga2 = (roti["Harga_roti"][9] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        
        if (jumlahpesanan2 == 3):
            diskon2 = int(harga2 * 10/100)
            totalharga2 = (harga2 - diskon2)

        elif (jumlahpesanan2 == 5):
            diskon2 = int(harga2 * 25/100)
            totalharga2 = int(harga2 - diskon2)
        
        elif (jumlahpesanan2 == 10):
            diskon2 = int(harga2 * 50/100)
            totalharga2 = int(harga2 - diskon2)
        
        else:
            diskon2 = 0
            totalharga2 = int(harga2)
    else:
        print("index list huruf yang dicari tidak ada, silakan coba lagi.")

    
    print("===============================================")
    print("Skadi Bakery Shop")
    print("===============================================")
    print(Data_hari["datahari"])
    print("menu :", namapesanan2)
    print("jumlah pesanan :", jumlahpesanan2)
    print("harga :", harga2)
    print("diskon :", diskon2)
    print("jumlah bayar :", totalharga2)
    print("===============================================")
    print("Terima kasih telah belanja di Skadi Bakery Shop")
    Keuntungan["Total_keuntungan"].append(totalharga2)
    
    print("===========================================")
    opsi = input("apakah anda ingin order lagi? (Y/N) :")
    print("===========================================")
    if opsi == "Y":
        diskon()
    else:
        print("===========================================================")
        masukan_1 = input("apakah anda ingin kembali ke menu login? (Y/N) :")
        print("===========================================================")
        if masukan_1 == "Y":
            Data_hari["datahari"].clear()
            user_login()
        else:
            diskon()






user_login()