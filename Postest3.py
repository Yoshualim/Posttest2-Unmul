from typing import ValuesView


Menu_roti = ["Croissant", "Donat", "SwissRoll", "Muffin", "Brownie"]
Harga_roti = [14000, 12000, 18000, 13000, 15000]
Total_keuntungan = []
Hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
Bulan = ["Januari","Febuari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
tanggal = list(range(32))
datahari = []

def main_admin():
    
    print("Menu Admin")
    print (" ======================================")
    print("1. Lihat list menu roti")
    print("2. Tambahkan menu roti")
    print("3. Edit menu roti")
    print("4. Hapus menu roti ")
    print("5. Masuk ke mode kasir")
    print("6. Hapus jumlah keuntungan hari ini")
    print("0. Keluar dari menu Admin")
    print (" ======================================")
    Jumlahuntung = sum(Total_keuntungan)
    print (" ==================================================================")
    print("Jumlah keuntungan yang diraih pada hari ini adalah Rp.", Jumlahuntung)
    print (" ==================================================================")

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
        datahari1()
    elif pilihan_menu == ("6"):
        Hapus_Keuntungan()
    elif pilihan_menu == ("0"):
        user_login()        
    else:
        print("Anda salah input silakan coba kembali")
        kembali_menu()

def Hapus_Keuntungan():
    print (" ===================================================================================================================")
    print("Apakah anda yakin untuk menghapus jumlah keuntungan hari ini? pastikan anda sudah mencatat jumlah keuntungan hari ini")
    print (" ===================================================================================================================")
    konfirmasi = str(input("Ya/Tidak :"))
    if konfirmasi == "Ya":
        Total_keuntungan.clear()
        print (" ====================")
        print ("Data berhasil di hapus")
        print (" ====================")
        kembali_menu()
    elif konfirmasi == "Tidak":
        kembali_menu()
    else:
        print("Inputan salah, silakan isi konfimasi kembali")
        Hapus_Keuntungan()

def List_menuroti():
    print("List Menu roti Skadi Bakery Shop")
    print (" ==========================================")
    try:
        print ("A.", Menu_roti[0], "Rp.", Harga_roti[0] )
    except IndexError:
        print()
    try:
        print ("B.", Menu_roti[1], "Rp.", Harga_roti[1] )
    except IndexError:
        print()
    try:
        print ("C.", Menu_roti[2], "Rp.", Harga_roti[2] )
    except IndexError:
        print()
    try:
        print ("D.", Menu_roti[3], "Rp.", Harga_roti[3] )
    except IndexError:
        print()
    try:
        print ("E.", Menu_roti[4], "Rp.", Harga_roti[4] )
    except IndexError:
        print()
    try:
        print ("F.", Menu_roti[5], "Rp.", Harga_roti[5] )
    except IndexError:
        print()
    try:
        print ("G.", Menu_roti[6], "Rp.", Harga_roti[6] )
    except IndexError:
        print()
    try:
        print ("H.", Menu_roti[7], "Rp.", Harga_roti[7] )
    except IndexError:
        print()
    try:
        print ("I.", Menu_roti[8], "Rp.", Harga_roti[8] )
    except IndexError:
        print()
    try:
        print ("J.", Menu_roti[9], "Rp.", Harga_roti[9] )
    except IndexError:
        print()
    print (" ==========================================")
    kembali_menu()

def Tambah_menuroti():
    print                (" =============================")        
    Menu_baru = str(input("Masukan nama menu roti baru : "))
    print                (" =============================")
    Menu_roti.append(Menu_baru)
    Tambah_menuroti1()
   
def Tambah_menuroti1():
    print                     (" ==============================")

    try:
        Harga_baru = int(input("Masukan harga menu roti baru : "))
    except ValueError:
        print("Masukan harga dengan betul bukan dengan huruf")
        print(" ============================================")
        Tambah_menuroti1()
    
    print                     (" ===============================") 

    Harga_roti.append(Harga_baru)
    print(" ======================")
    print("Menu berhasil dimasukan!")
    print(" ======================")
    kembali_menu()

def Edit_menuroti():

    print(" ===============================================================")
    print(Menu_roti)
    print(" ===============================================================")
    print("Pilih menu roti yang akan di edit (angka 0 sebagai menu pertama)")
    print(" ===============================================================")

   

    try:
        Menu_edit = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Edit_menuroti()
    
    try:
        print(Menu_roti[Menu_edit])
    except IndexError:
        print("Masukan angka yang ada (dimulai dari 0)")
        Edit_menuroti()
    
    print                (" ===============")
    Nama_edit = str(input("Edit nama menu: "))
    print                (" ===============")
    Menu_roti[Menu_edit] = Nama_edit
    Edit_menuroti1()

def Edit_menuroti1():

    print(" ==============================================================================")
    print(Harga_roti)
    print(" ==============================================================================")
    print("Pilih harga roti yang akan di edit (masukan angka yang sama seperti sebelumnya)")
    print(" ==============================================================================")

    try:
        Harga_edit = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Edit_menuroti1()

    try:
        print(Harga_roti[Harga_edit])
    except IndexError:
        print("Masukan angka yang ada (dimulai dari 0)")
        Edit_menuroti1()

    try:
        harga_edit = int(input("Edit harga menu: "))
    except ValueError:
        print("Masukan angka bukan huruf")
        Edit_menuroti1()
            
        
        
    Harga_roti[Harga_edit] = harga_edit
    print(" ====================")
    print("Menu berhasil diubah!")
    print(" ====================")
    kembali_menu()

def Hapus_menuroti():
    print(" =================================================================")
    print(Menu_roti)
    print(" =================================================================")
    print("Pilih menu roti yang akan dihapus (angka 0 sebagai menu pertama) :")
    print(" =================================================================")

    try:
        Hapus_menu = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Hapus_menuroti()

    try:
        del Menu_roti[Hapus_menu]
    except IndexError:
        print("Masukan angka yang ada (dimulai dari 0)")
        Hapus_menuroti()

    del Harga_roti[Hapus_menu]

    print(" ======================")
    print("Menu berhasil di hapus!")
    print(" ======================")
    kembali_menu()


def kembali_menu():
    input("Tekan enter untuk kembali")
    main_admin()

def user_login():
    print(" =============")
    print("Selamat datang")
    print(" =============")
    user =str(input("Masukan username :"))
    try:
        Pass =int(input("Masukan password :"))
    except ValueError:
        print("Password berbentuk angka silakan isi ulang")
        user_login()
    if user == "Yoshua" and Pass == 6093:
        print("Login Berhasil")
        main_admin()

    elif user == "Yoshua" and Pass == 210:
        print("Login Berhasil")
        datahari1()
        
    else:
        print("Username atau password anda salah, silakan isi kembali")
        user_login()
    
def datahari1():
        print(" ====================")
        print("hari?")
        print(" ====================")
        print(Hari)
        print(" ====================")
        hari1 = str(input(":"))
        if hari1 in Hari:
            datahari.append(hari1)
            datahari2()
        else:
            print("Anda salah masukan hari")
            datahari1()
        
def datahari2():
        print(" ====================")
        print("Tanggal?")
        print(" ====================")
        print(tanggal)
        print(" ====================")
        try:
            tanggal1 = int(input(":"))
        except ValueError:
            print("Anda salah masukan tanggal")
            datahari2()
        
        datahari.append(tanggal1)
        datahari3()
        

def datahari3():
        print(" ====================")
        print("Bulan?")
        print(" ====================")
        print(Bulan)
        print(" ====================")
        bulan1 = str(input(":"))
        if bulan1 in Bulan:
            datahari.append(bulan1)
            datahari4()
        else:
            print("Anda salah masukan bulan")
            datahari3()
        

def datahari4():
        print(" ====================")
        print("Tahun?")
        print(" ====================")
        try:
            Tahun1 = int(input(":"))
        except ValueError:
            print("Harap masukan angka bukan huruf")
            datahari4()

        datahari.append(Tahun1)
        menu()
        
def nondiskon():

    print (datahari)
    print (" ==========================================")
    print (" ==========================================")
    print ("Skadi Bakery Shop")
    print (" ==========================================")
    print ("Nama dan Harga Roti")
    print (" ==========================================")

    try:
        print ("A.", Menu_roti[0], "Rp.", Harga_roti[0] )
    except IndexError:
        print()
    try:
        print ("B.", Menu_roti[1], "Rp.", Harga_roti[1] )
    except IndexError:
        print()
    try:
        print ("C.", Menu_roti[2], "Rp.", Harga_roti[2] )
    except IndexError:
        print()
    try:
        print ("D.", Menu_roti[3], "Rp.", Harga_roti[3] )
    except IndexError:
        print()
    try:
        print ("E.", Menu_roti[4], "Rp.", Harga_roti[4] )
    except IndexError:
        print()
    try:
        print ("F.", Menu_roti[5], "Rp.", Harga_roti[5] )
    except IndexError:
        print()
    try:
        print ("G.", Menu_roti[6], "Rp.", Harga_roti[6] )
    except IndexError:
        print()
    try:
        print ("H.", Menu_roti[7], "Rp.", Harga_roti[7] )
    except IndexError:
        print()
    try:
        print ("I.", Menu_roti[8], "Rp.", Harga_roti[8] )
    except IndexError:
        print()
    try:
        print ("J.", Menu_roti[9], "Rp.", Harga_roti[9] )
    except IndexError:
        print()
    print (" ==========================================")
    print (" ==========================================")

    pesanan1 = str(input("Masukan Abjad dari menu roti :"))
    print (" ============================================")
    try:
        jumlahpesanan1 = int(input("masukan jumlah pesanan :"))
    except ValueError:
        print("Mohon input jumlah pesanan dengan benar")
        nondiskon()
    print (" =========================================")

    if pesanan1 == ("A"):
        try:
            namapesanan1 = Menu_roti [0]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (Harga_roti [0] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0

    elif pesanan1 == ("B"):
        try:
            namapesanan1 = Menu_roti [1]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (Harga_roti [1] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("C"):
        try:
            namapesanan1 = Menu_roti [2]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (Harga_roti [2] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("D"):
        try:
            namapesanan1 = Menu_roti [3]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (Harga_roti [3] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
        
    elif pesanan1 == ("E"):
        try:
            namapesanan1 = Menu_roti [4]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (Harga_roti [4] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0

    elif pesanan1 == ("F"):
        try:
            namapesanan1 = Menu_roti [5]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (Harga_roti [5] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("G"):
        try:
            namapesanan1 = Menu_roti [6]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (Harga_roti [6] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("H"):
        try:
            namapesanan1 = Menu_roti [7]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (Harga_roti [7] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0
    
    elif pesanan1 == ("I"):
        try:
            namapesanan1 = Menu_roti [8]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (Harga_roti [8] * jumlahpesanan1)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        totalharga1 = int(harga1)
        diskon1 = 0

    elif pesanan1 == ("J"):
        try:
            namapesanan1 = Menu_roti [9]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            nondiskon()
        try:
            harga1 = (Harga_roti [9] * jumlahpesanan1)
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
    print(datahari)
    print("menu :", namapesanan1)
    print("jumlah pesanan :", jumlahpesanan1)
    print("harga :", harga1)
    print("diskon :", diskon1)
    print("jumlah bayar :", totalharga1)
    print("===============================================")
    print("Terima kasih telah belanja di Skadi Bakery Shop")
    Total_keuntungan.append(totalharga1)

    print(" ===========================================")
    opsi = input("apakah anda ingin order lagi? (Y/N) :")
    print(" ===========================================")
    if opsi == "Y":
        nondiskon()
    else:
        print(" ===========================================================")
        masukan_1 = input("apakah anda ingin kembali ke menu login? (Y/N) :")
        print(" ===========================================================")
        if masukan_1 == "Y":
            datahari.clear()
            user_login()
        else:
            nondiskon()



def diskon():
 
    print (datahari)
    print (" ==========================================")
    print (" ==========================================")
    print ("Skadi Bakery Shop")
    print (" ==========================================")
    print ("Nama dan Harga Roti")
    print (" ==========================================")

    try:
        print ("A.", Menu_roti[0], "Rp.", Harga_roti[0] )
    except IndexError:
        print()
    try:
        print ("B.", Menu_roti[1], "Rp.", Harga_roti[1] )
    except IndexError:
        print()
    try:
        print ("C.", Menu_roti[2], "Rp.", Harga_roti[2] )
    except IndexError:
        print()
    try:
        print ("D.", Menu_roti[3], "Rp.", Harga_roti[3] )
    except IndexError:
        print()
    try:
        print ("E.", Menu_roti[4], "Rp.", Harga_roti[4] )
    except IndexError:
        print()
    try:
        print ("F.", Menu_roti[5], "Rp.", Harga_roti[5] )
    except IndexError:
        print()
    try:
        print ("G.", Menu_roti[6], "Rp.", Harga_roti[6] )
    except IndexError:
        print()
    try:
        print ("H.", Menu_roti[7], "Rp.", Harga_roti[7] )
    except IndexError:
        print()
    try:
        print ("I.", Menu_roti[8], "Rp.", Harga_roti[8] )
    except IndexError:
        print()
    try:
        print ("J.", Menu_roti[9], "Rp.", Harga_roti[9] )
    except IndexError:
        print()
    print (" ==========================================")
    print (" ==========================================")

    pesanan2 = str(input("Masukan Abjad dari menu roti :"))
    print (" ============================================")
    try:
        jumlahpesanan2 = int(input("masukan jumlah pesanan :"))
    except ValueError:
        print("Mohon input jumlah pesanan dengan benar")
        diskon()
    print (" ================================================")

    if pesanan2 == ("A"):
        try:
            namapesanan2 = Menu_roti [0]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        try:
            harga2 = (Harga_roti [0] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        
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
            namapesanan2 = Menu_roti [1]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        try:
            harga2 = (Harga_roti [1] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        
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
            namapesanan2 = Menu_roti [2]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        try:
            harga2 = (Harga_roti [2] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        
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
            namapesanan2 = Menu_roti [3]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        try:
            harga2 = (Harga_roti [3] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        
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
            namapesanan2 = Menu_roti [4]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        try:
            harga2 = (Harga_roti [4] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        
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
            namapesanan2 = Menu_roti [5]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        try:
            harga2 = (Harga_roti [5] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        
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
            namapesanan2 = Menu_roti [6]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        try:
            harga2 = (Harga_roti [6] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        
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
            namapesanan2 = Menu_roti [7]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        try:
            harga2 = (Harga_roti [7] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        
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
            namapesanan2 = Menu_roti [8]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        try:
            harga2 = (Harga_roti [8] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        
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
            namapesanan2 = Menu_roti [9]
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        try:
            harga2 = (Harga_roti [9] * jumlahpesanan2)
        except IndexError:
            print("Data tidak dapat ditemukan, silakan hubungi admin untuk memperbaikii masalah ini ")
            diskon()
        
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
    print(datahari)
    print("menu :", namapesanan2)
    print("jumlah pesanan :", jumlahpesanan2)
    print("harga :", harga2)
    print("diskon :", diskon2)
    print("jumlah bayar :", totalharga2)
    print("===============================================")
    print("Terima kasih telah belanja di Skadi Bakery Shop")
    Total_keuntungan.append(totalharga2)
    
    print(" ===========================================")
    opsi = input("apakah anda ingin order lagi? (Y/N) :")
    print(" ===========================================")
    if opsi == "Y":
        diskon()
    else:
        print(" ===========================================================")
        masukan_1 = input("apakah anda ingin kembali ke menu login? (Y/N) :")
        print(" ===========================================================")
        if masukan_1 == "Y":
            datahari.clear()
            user_login()
        else:
            diskon()

def menu():

    i=0
    while i == 0:

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

user_login()