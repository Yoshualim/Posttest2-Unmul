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
    "Samsung J2 Prime" : {
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
Tambahhp = []

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
    print("1. Lihat list Hp")
    print("2. Tambahkan Hp")
    print("3. Edit Hp")
    print("4. Hapus Hp ")
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
        List_menuhp()
    elif pilihan_menu == ("2"):
        Tambah_hp()
    elif pilihan_menu == ("3"):
        Edit_hp()
    elif pilihan_menu == ("4"):
        Hapus_hp()
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

def List_menuhp():
    print("List Menu roti Skadi Bakery Shop")
    print ("==========================================")
    for key, val in Daftarhp.items():
        for key2, val2 in val.items():
            print("%s : %s" % (key2,val2))
    print ("==========================================")
    kembali_menu()

def Tambah_hp():
    print                ("=============================")        
    Merk_hp = str(input("Masukan merk HP : "))
    print                ("=============================")

    if Merk_hp == "Samsung":
        Tambahhp_Samsung()
    elif Merk_hp == "Oppo":
        Tambahhp_Oppo()
    elif Merk_hp == "Iphone":
        Tambahhp_Iphone()

def Tambahhp_Samsung():
    Hp_Baru = str(input("Masukan nama hp baru : "))
    if Hp_Baru == None:
        print("Harap masukan inputan dengan benar")
        Tambahhp_Samsung()
    Tambahhp.append(Hp_Baru)
    Tambahhp_Samsung1()

def Tambahhp_Samsung1():
    try:
        Harga_hp = int(input("Masukan harga hp baru"))
    except ValueError:
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Samsung1()
    Daftarhp["Samsung"].update({Tambahhp[0] : Harga_hp})
    Tambahhp.clear()
    print("Hp berhasil ditambahkan")
    main_admin()

def Tambahhp_Oppo():
    Hp_Baru = str(input("Masukan nama hp baru : "))
    if Hp_Baru == None:
        print("Harap masukan inputan dengan benar")
        Tambahhp_Oppo()
    Tambahhp.append(Hp_Baru)
    Tambahhp_Oppo1()

def Tambahhp_Oppo1():
    try:
        Harga_hp = int(input("Masukan harga hp baru"))
    except ValueError:
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Oppo1()
    Daftarhp["Oppo"].update({Tambahhp[0] : Harga_hp})
    Tambahhp.clear()
    print("Hp berhasil ditambahkan")
    main_admin()

def Tambahhp_Iphone():
    Hp_Baru = str(input("Masukan nama hp baru : "))
    if Hp_Baru == None:
        print("Harap masukan inputan dengan benar")
        Tambahhp_Iphone()
    Tambahhp.append(Hp_Baru)
    Tambahhp_Iphone1()

def Tambahhp_Iphone1():
    try:
        Harga_hp = int(input("Masukan harga hp baru"))
    except ValueError:
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Iphone1()
    Daftarhp["Iphone"].update({Tambahhp[0] : Harga_hp})
    Tambahhp.clear()
    print("Hp berhasil ditambahkan")
    main_admin()


def Edit_hp():

    print("===============================================================")
    print("===============================================================")
    for merk in Merkhp:
        print(merk)
    print("Semua hp")
    print("Pilih merk hp yang akan diedit")
    masukan = str(input(":"))
    print("===============================================================")

    if masukan == "Samsung":
        Edithp_Samsung()
    elif masukan == "Oppo":
        Edithp_Oppo()
    elif masukan == "Iphone":
        Edithp_Iphone()
    elif masukan == "Semua hp":
        Edithp_Semuahp()
    else:
        print("masukan salah")
        Edit_hp()

    
def Edithp_Samsung():
    for key, val in Daftarhp["Samsung"].items():
        print("%s = %s" % (key,val))

    print("Masukan nama hp yang akan diedit ")
    ubah = str(input(":"))
    if ubah in Daftarhp["Samsung"].keys():
        print(ubah)
        print(Daftarhp["Samsung"][ubah])
        print("Mau edit dibagian mana?")
        print("""
        1. Nama Hp
        2. Harga Hp
        3. Spec hp
        4. Edit Nama, Harga, dan Spec Hp
        4. Kembali ke pilih merk hp
        0. Kembali ke menu
        """)

        try:
            print(Spechp.get(ubah))
        except KeyError:
            print("Data spec hp tidak dapat ditemukan")





def Edithp_Oppo():


def Edithp_Iphone():


def Edithp_Semuahp():

   

   

def Hapus_hp():
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
    for key, val in Daftarhp.items():
        for key2, val2 in val.items():
            print("%s : %s" % (key2,val2))
    
    print("pilih merk")
    for i in Merkhp:
        print(i)

    X = input(":")



    if X in Daftarhp.keys():
        
        if X == "Samsung":
            for key, val in Daftarhp["Samsung"].items():
                    print("%s = %s" % (key,val))
               
            print("Pilih hp")
            Masukan = input(":")

            if Masukan in Daftarhp["Samsung"].keys():
                print(Masukan)
                print(Daftarhp["Samsung"][Masukan])
                try:
                    print(Spechp.get(Masukan))
                except KeyError:
                    print("Data spec hp tidak dapat ditemukan")

            else:
                print("asss")
            

        elif X == "Oppo":
            
            for key, val in Daftarhp.items():
                for key2, val2 in val.items():
                        print("%s = %s" % (key2,val2))
                        

        else:
            print("error")
    
    else:
        print("aslah")
        




user_login()