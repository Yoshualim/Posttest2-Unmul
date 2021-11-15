Daftarhp = {

    "Samsung" : {
        "Samsung J2" : 1000000,
        "Samsung J1 Prime" : 2000000,
    },
    "Oppo" : {
        "Oppo A3s" : 500000,
        "Oppo X reno" : 750000,
    },
    "Iphone" : {
        "Iphone 123" : 100000,
        "Iphone X " : 100000000,
    }
}

Spechp = {
    "Samsung J1 Prime" : {
            "Nama" : "Samsung J2 Prime",
            "Tahun Keluar" : "2016",
            "OS" : "Android 6.0 (Marshmallow)",
            "Chipset" : "Mediatek MT6737T (28nm)",
            "CPU" : "Quad-core 1.4 GHz Cortex A53",
            "GPU" : "Mali T720MP2",
            "Display" : "PLS IPS",
            "Memori Internal" : "8GB",
            "RAM" : "1.5GB",
            "Kamera" : "8MP",
            "Jaringan" : "GSM/HSPA/LTE",
            "Kapasitas Baterai" : "260 mAh, Baterai lepas"
            },
    
    "Samsung J1 Prime" : {
            "Nama" : "Samsung J2 Prime",
            "Tahun Keluar" : "2016",
            "OS" : "Android 6.0 (Marshmallow)",
            "Chipset" : "Mediatek MT6737T (28nm)",
            "CPU" : "Quad-core 1.4 GHz Cortex A53",
            "GPU" : "Mali T720MP2",
            "Display" : "PLS IPS",
            "Memori Internal" : "8GB",
            "RAM" : "1.5GB",
            "Kamera" : "8MP",
            "Jaringan" : "GSM/HSPA/LTE",
            "Kapasitas Baterai" : "260 mAh, Baterai lepas"
            },



}

Merkhp = ["Oppo", "Iphone", "Samsung"]

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
        kasir()
        
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
    for key, val in Daftarhp.items():
        print("%s : %s" % (key, val))
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










def kasir():



    print("toko")
    for val in Daftarhp.items():
        print("%s : %s" % ( val))
    print("pilih merk")
    for i in Merkhp:
        print(i)

    X = print((input("masukan inputan :")))

    if X in Daftarhp.items():
        for key2, val2 in Daftarhp.items():
            print("%s " % (key2, val2))
            print("pilih hp :")
        
        pilihhp = str(input(":"))

        if pilihhp == Daftarhp["Samsung"]:
            for pilihhp in Spechp.items():
                print("%s : %s" % (pilihhp))







kasir()