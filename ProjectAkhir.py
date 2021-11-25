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
        "Iphone X" : 100000000,
    }
}

Stokhp = {

    "Samsung" : {
        "Samsung J2" : 3,
        "Samsung J1 Prime" : 2,
    },

    "Oppo" : {
        "Oppo A3s" : 4,
        "Oppo X reno" : 1,
    },
    
    "Iphone" : {
        "Iphone 123" : 3,
        "Iphone X" : 0,
    }



}

Spechp = {
    "Samsung" : {
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
    },

    "Oppo" : { 
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
    },

    "Iphone" : {
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

   
}



Merkhp = ["Oppo", "Iphone", "Samsung"]
Datahp = []

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
    print("8. Database spec hp")
    print("9. Stok hp")
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
    elif pilihan_menu == ("8"):
        Editspechp()
    elif pilihan_menu == ("9"):
        stokhp()
    elif pilihan_menu == ("0"):
        kembalilogin()        
    else:
        print("Anda salah input silakan coba kembali")
        kembali_menu()

def List_menuhp():
    print("List HP")
    print ("==========================================")
    for key, val in Daftarhp.items():
        for key2, val2 in val.items():
            print("%s : %s" % (key2,val2))
    print ("==========================================")
    kembali_menu()

def Tambah_hp():
    print                ("=============================")  
    for merk in Merkhp:
        print(merk)      
    Merk_hp = str(input("Masukan merk HP : "))
    print                ("=============================")

    if Merk_hp == "Samsung":
        Tambahhp_Samsung()
    elif Merk_hp == "Oppo":
        Tambahhp_Oppo()
    elif Merk_hp == "Iphone":
        Tambahhp_Iphone()
    else:
        print("Inputan anda salah")
        Tambah_hp()

def Tambahhp_Samsung():
    Hp_Baru = str(input("Masukan nama hp baru : "))
    if Hp_Baru == "":
        print("Harap masukan inputan dengan benar")
        Tambahhp_Samsung()
    Datahp.append(Hp_Baru)
    Tambahhp_Samsung1()

def Tambahhp_Samsung1():
    try:
        Harga_hp = int(input("Masukan harga hp baru"))
    except ValueError:
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Samsung1()
    if Harga_hp > 0:

        Daftarhp["Samsung"].update({Datahp[0] : Harga_hp})
        Datahp.clear()
        print("Hp berhasil ditambahkan")
        main_admin()

    else:
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Samsung1()

def Tambahhp_Oppo():
    Hp_Baru = str(input("Masukan nama hp baru : "))
    if Hp_Baru == "":
        print("Harap masukan inputan dengan benar")
        Tambahhp_Oppo()
    Datahp.append(Hp_Baru)
    Tambahhp_Oppo1()

def Tambahhp_Oppo1():
    try:
        Harga_hp = int(input("Masukan harga hp baru"))
    except ValueError:
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Oppo1()
    
    if Harga_hp > 0:

        Daftarhp["Oppo"].update({Datahp[0] : Harga_hp})
        Datahp.clear()
        print("Hp berhasil ditambahkan")
        main_admin()
    
    else:
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Oppo1()

def Tambahhp_Iphone():
    Hp_Baru = str(input("Masukan nama hp baru : "))
    if Hp_Baru == "":
        print("Harap masukan inputan dengan benar")
        Tambahhp_Iphone()
    Datahp.append(Hp_Baru)
    Tambahhp_Iphone1()

def Tambahhp_Iphone1():
    try:
        Harga_hp = int(input("Masukan harga hp baru"))
    except ValueError:
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Iphone1()
    
    if Harga_hp > 0:
        Daftarhp["Iphone"].update({Datahp[0] : Harga_hp})
        Datahp.clear()
        print("Hp berhasil ditambahkan")
        main_admin()
    
    else:
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Iphone1()


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
        Datahp.append(ubah)
        Edithp_Samsung1()
    else:
        print("Masukan inputan yang benar")
        Edithp_Samsung()


def Edithp_Samsung1():
    print(Datahp[0])
    print(Daftarhp["Samsung"][Datahp[0]])
    print("Menu edit")
    print("""
        1. Nama Hp
        2. Harga Hp
        3. Edit Nama dan Harga hp
        4. Kembali ke pilih merk hp
        5. Kembali ke menu
        """)
    try:
        masukan = int(input(":"))
    except ValueError:
        print("Masukan salah")
        Edithp_Samsung1()
    
    if masukan > 0:
        if masukan == 1:
            Editnama_Samsung()
        elif masukan == 2:
            Editharga_Samsung()
        elif masukan == 3:
            Editnamaharga_Samsung()
        elif masukan == 4:
            Datahp.clear()
            Edit_hp()
        elif masukan == 5:
            Datahp.clear()
            main_admin()
        else:
            print("Inputan kamu salah, silakan coba kembali")
            Edithp_Samsung1()
    else:
        print("Inputan kamu negatif, silakan coba kembali")
        Edithp_Samsung1()

def Editnama_Samsung():
    print(Datahp[0])
    print("Masukan Nama hp baru")
    namahp = str(input(":"))
    if namahp == "":
        print("Mohon isi dengan benar")
        Editnama_Samsung()
    print(namahp)
    i = 0
    while i == 0:
        print("Apakah nama sudah benar? (Y/N)")
        nama = str(input(":"))
        if nama == "Y":
            break
        elif nama == "N":
            Editnama_Samsung()
        else:
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit nama
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnama_Samsung()
                elif masukan == "D":
                    Edithp_Samsung1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    
    Daftarhp["Samsung"][namahp] = Daftarhp["Samsung"].pop(Datahp[0])
    i = 0
    while i == 0:
        print("Nama hp berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")


def Editharga_Samsung():
    print(Daftarhp["Samsung"][Datahp[0]])
    print("Masukan Harga hp baru")
    try:
        hargahp = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Editharga_Samsung()
    
    if hargahp > 0:
        print(hargahp)
        i = 0
        while i == 0:
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str(input(":"))
            if nama == "Y":
                break
            elif nama == "N":
                Editharga_Samsung()
            else:
                print("Harap input jawaban yang benar")
    else:
        print("masukan berbentuk negatif")
        Editharga_Samsung()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit harga
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editharga_Samsung()
                elif masukan == "D":
                    Edithp_Samsung1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    
    Daftarhp["Samsung"].update({Datahp[0] : hargahp})
    i = 0
    while i == 0:
        print("Harga hp berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")

def Editnamaharga_Samsung():
    print(Datahp[0])
    print("Masukan Nama hp baru")
    namahp = str(input(":"))
    if namahp == "":
        print("Mohon isi dengan benar")
        Editnamaharga_Samsung()
    print(namahp)
    i = 0
    while i == 0:
        print("Apakah nama sudah benar? (Y/N)")
        nama = str(input(":"))
        if nama == "Y":
            break
        elif nama == "N":
            Editnamaharga_Samsung()
        else:
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit nama
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnamaharga_Samsung()
                elif masukan == "D":
                    Edithp_Samsung1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    Datahp.append(namahp)
    Editnamaharga_Samsung1()
            
def Editnamaharga_Samsung1():
    print(Daftarhp["Samsung"][Datahp[0]])
    print("Masukan Harga hp baru")
    try:
        hargahp = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Editnamaharga_Samsung1()
    
    if hargahp > 0:
        print(hargahp)
        i = 0
        while i == 0:
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str(input(":"))
            if nama == "Y":
                break
            elif nama == "N":
                Editnamaharga_Samsung1()
            else:
                print("Harap input jawaban yang benar")
    else:
        print("masukan berbentuk negatif")
        Editnamaharga_Samsung1()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit harga
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnamaharga_Samsung1()
                elif masukan == "D":
                    del Datahp[1]
                    Edithp_Samsung1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    Daftarhp["Samsung"][Datahp[1]] = Daftarhp["Samsung"].pop(Datahp[0])
    Daftarhp["Samsung"].update({Datahp[1] : hargahp})
    i = 0
    while i == 0:
        print("Nama dan harga hp berhasil di ubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")








def Edithp_Oppo():
    for key, val in Daftarhp["Oppo"].items():
        print("%s = %s" % (key,val))

    print("Masukan nama hp yang akan diedit ")
    ubah = str(input(":"))
    if ubah in Daftarhp["Oppo"].keys():
        Datahp.append(ubah)
        Edithp_Oppo1()
    else:
        print("Masukan inputan yang benar")
        Edithp_Oppo()


def Edithp_Oppo1():
    print(Datahp[0])
    print(Daftarhp["Oppo"][Datahp[0]])
    print("Menu edit")
    print("""
        1. Nama Hp
        2. Harga Hp
        3. Edit Nama dan Harga hp
        4. Kembali ke pilih merk hp
        5. Kembali ke menu
        """)
    try:
        masukan = int(input(":"))
    except ValueError:
        print("Masukan salah")
        Edithp_Samsung1()
    
    if masukan > 0:
        if masukan == 1:
            Editnama_Oppo()
        elif masukan == 2:
            Editharga_Oppo()
        elif masukan == 3:
            Editnamaharga_Oppo()
        elif masukan == 4:
            Datahp.clear()
            Edit_hp()
        elif masukan == 5:
            Datahp.clear()
            main_admin()
        else:
            print("Inputan kamu salah")
            Edithp_Oppo1()
    else:
        print("Inputan kamu negatif")
        Edithp_Oppo1()

def Editnama_Oppo():
    print(Datahp[0])
    print("Masukan Nama hp baru")
    namahp = str(input(":"))
    if namahp == "":
        print("Mohon isi dengan benar")
        Editnama_Oppo()
    print(namahp)
    i = 0
    while i == 0:
        print("Apakah nama sudah benar? (Y/N)")
        nama = str(input(":"))
        if nama == "Y":
            break
        elif nama == "N":
            Editnama_Oppo()
        else:
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit nama
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnama_Oppo()
                elif masukan == "D":
                    Edithp_Oppo1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    
    Daftarhp["Oppo"][namahp] = Daftarhp["Oppo"].pop(Datahp[0])
    i = 0
    while i == 0:
        print("Nama hp berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")


def Editharga_Oppo():
    print(Daftarhp["Oppo"][Datahp[0]])
    print("Masukan Harga hp baru")
    try:
        hargahp = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Editharga_Oppo()
    
    if hargahp > 0:
        print(hargahp)
        i = 0
        while i == 0:
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str(input(":"))
            if nama == "Y":
                break
            elif nama == "N":
                Editharga_Oppo()
            else:
                print("Harap input jawaban yang benar")
    else:
        print("masukan berbentuk negatif")
        Editharga_Oppo()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit harga
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editharga_Oppo()
                elif masukan == "D":
                    Edithp_Oppo1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    
    Daftarhp["Oppo"].update({Datahp[0] : hargahp})
    i = 0
    while i == 0:
        print("Harga hp berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")

def Editnamaharga_Oppo():
    print(Datahp[0])
    print("Masukan Nama hp baru")
    namahp = str(input(":"))
    if namahp == "":
        print("Mohon isi dengan benar")
        Editnamaharga_Oppo()
    print(namahp)
    i = 0
    while i == 0:
        print("Apakah nama sudah benar? (Y/N)")
        nama = str(input(":"))
        if nama == "Y":
            break
        elif nama == "N":
            Editnamaharga_Oppo()
        else:
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit nama
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnamaharga_Oppo()
                elif masukan == "D":
                    Edithp_Oppo1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    Datahp.append(namahp)
    Editnamaharga_Oppo1()
            
def Editnamaharga_Oppo1():
    print(Daftarhp["Oppo"][Datahp[0]])
    print("Masukan Harga hp baru")
    try:
        hargahp = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Editnamaharga_Oppo1()
    
    if hargahp > 0:
        print(hargahp)
        i = 0
        while i == 0:
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str(input(":"))
            if nama == "Y":
                break
            elif nama == "N":
                Editnamaharga_Oppo1()
            else:
                print("Harap input jawaban yang benar")
    else:
        print("masukan berbentuk negatif")
        Editnamaharga_Oppo1()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit harga
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnamaharga_Oppo1()
                elif masukan == "D":
                    del Datahp[1]
                    Edithp_Oppo1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    Daftarhp["Oppo"][Datahp[1]] = Daftarhp["Oppo"].pop(Datahp[0])
    Daftarhp["Oppo"].update({Datahp[1] : hargahp})
    i = 0
    while i == 0:
        print("Nama dan harga hp berhasil di ubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")







def Edithp_Iphone():
    for key, val in Daftarhp["Iphone"].items():
        print("%s = %s" % (key,val))

    print("Masukan nama hp yang akan diedit ")
    ubah = str(input(":"))
    if ubah in Daftarhp["Iphone"].keys():
        Datahp.append(ubah)
        Edithp_Iphone1()
    else:
        print("Masukan inputan yang benar")
        Edithp_Iphone()


def Edithp_Iphone1():
    print(Datahp[0])
    print(Daftarhp["Iphone"][Datahp[0]])
    print("Menu edit")
    print("""
        1. Nama Hp
        2. Harga Hp
        3. Edit Nama dan Harga hp
        4. Kembali ke pilih merk hp
        5. Kembali ke menu
        """)
    try:
        masukan = int(input(":"))
    except ValueError:
        print("Masukan salah")
        Edithp_Iphone1()
    
    if masukan > 0:
        if masukan == 1:
            Editnama_Iphone()
        elif masukan == 2:
            Editharga_Iphone()
        elif masukan == 3:
            Editnamaharga_Iphone()
        elif masukan == 4:
            Datahp.clear()
            Edit_hp()
        elif masukan == 5:
            Datahp.clear()
            main_admin()
        else:
            print("Inputan kamu salah")
            Edithp_Iphone1()
    else:
        print("Inputan kamu negatif")
        Edithp_Iphone1()

def Editnama_Iphone():
    print(Datahp[0])
    print("Masukan Nama hp baru")
    namahp = str(input(":"))
    if namahp == "":
        print("Mohon isi dengan benar")
        Editnama_Iphone()
    print(namahp)
    i = 0
    while i == 0:
        print("Apakah nama sudah benar? (Y/N)")
        nama = str(input(":"))
        if nama == "Y":
            break
        elif nama == "N":
            Editnama_Iphone()
        else:
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit nama
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnama_Iphone()
                elif masukan == "D":
                    Edithp_Iphone1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    
    Daftarhp["Iphone"][namahp] = Daftarhp["Iphone"].pop(Datahp[0])
    i = 0
    while i == 0:
        print("Nama hp berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")


def Editharga_Iphone():
    print(Daftarhp["Iphone"][Datahp[0]])
    print("Masukan Harga hp baru")
    try:
        hargahp = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Editharga_Iphone()
    
    if hargahp > 0:
        print(hargahp)
        i = 0
        while i == 0:
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str(input(":"))
            if nama == "Y":
                break
            elif nama == "N":
                Editharga_Iphone()
            else:
                print("Harap input jawaban yang benar")
    else:
        print("masukan berbentuk negatif")
        Editharga_Iphone()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit harga
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editharga_Iphone()
                elif masukan == "D":
                    Edithp_Iphone1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    
    Daftarhp["Iphone"].update({Datahp[0] : hargahp})
    i = 0
    while i == 0:
        print("Harga hp berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")

def Editnamaharga_Iphone():
    print(Datahp[0])
    print("Masukan Nama hp baru")
    namahp = str(input(":"))
    if namahp == "":
        print("Mohon isi dengan benar")
        Editnamaharga_Iphone()
    print(namahp)
    i = 0
    while i == 0:
        print("Apakah nama sudah benar? (Y/N)")
        nama = str(input(":"))
        if nama == "Y":
            break
        elif nama == "N":
            Editnamaharga_Iphone()
        else:
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit nama
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnamaharga_Iphone()
                elif masukan == "D":
                    Edithp_Iphone1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    Datahp.append(namahp)
    Editnamaharga_Iphone1()
            
def Editnamaharga_Iphone1():
    print(Daftarhp["Iphone"][Datahp[0]])
    print("Masukan Harga hp baru")
    try:
        hargahp = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Editnamaharga_Iphone1()
    
    if hargahp > 0:
        print(hargahp)
        i = 0
        while i == 0:
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str(input(":"))
            if nama == "Y":
                break
            elif nama == "N":
                Editnamaharga_Iphone1()
            else:
                print("Harap input jawaban yang benar")
    else:
        print("masukan berbentuk negatif")
        Editnamaharga_Iphone1()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit harga
                D. Kembali ke menu edit
                """)
                masukan = str(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnamaharga_Iphone1()
                elif masukan == "D":
                    del Datahp[1]
                    Edithp_Iphone1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    Daftarhp["Iphone"][Datahp[1]] = Daftarhp["Iphone"].pop(Datahp[0])
    Daftarhp["Iphone"].update({Datahp[1] : hargahp})
    i = 0
    while i == 0:
        print("Nama dan harga hp berhasil di ubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")


def Edithp_Semuahp():
    for key, val in Daftarhp.items():
        for key2, val2 in val.items():
            print("%s : %s" % (key2,val2))

    print("Masukan nama hp yang akan diedit ")
    ubah = str(input(":"))
    if ubah in Daftarhp["Samsung"].keys():
        Datahp.append(ubah)
        Edithp_Samsung1()
    elif ubah in Daftarhp["Oppo"].keys():
        Datahp.append(ubah)
        Edithp_Oppo1()
    elif ubah in Daftarhp["Iphone"].keys():
        Datahp.append(ubah)
        Edithp_Iphone1()
    else:
        print("Masukan inputan yang benar")
        Edithp_Semuahp()

   

def Hapus_hp():
    print("=================================================================")
    for key, val in Daftarhp.items():
        for key2, val2 in val.items():
            print("%s : %s" % (key2,val2))
    print("=================================================================")
    print("Pilih Hp yang akan dihapus :")
    print("=================================================================")

    masukan = str(input(":"))

    if masukan in Daftarhp["Samsung"].keys():
        print(masukan)
        print(Daftarhp["Samsung"][masukan])
        i = 0
        while i == 0:
            print("Apakah anda ingin menghapus ini? ini tidak bisa dikembalikan! (Y/N)")
            konfirmasi = str(input(":"))
            if konfirmasi == "Y":
                del Daftarhp["Samsung"][masukan]
                print("Data berhasil dihapus!")
                main_admin()
            elif konfirmasi == "N":
                i = 0
                while i == 0:
                    print("Operasi dibatalkan, apakah anda ingin kembali ke menu hapus hp atau kembali ke menu admin?")
                    print("A. menu hapus hp")
                    print("B. menu admin")
                    konfirm = str(input(":"))
                    if konfirm == "A":
                        Hapus_hp()
                    elif konfirm == "B":
                        main_admin()
                    else:
                        print("Inputan salah")
            else:
                print("Inputan salah")

    elif masukan in Daftarhp["Oppo"].keys():
        print(masukan)
        print(Daftarhp["Oppo"][masukan])
        i = 0
        while i == 0:
            print("Apakah anda ingin menghapus ini? ini tidak bisa dikembalikan! (Y/N)")
            konfirmasi = str(input(":"))
            if konfirmasi == "Y":
                del Daftarhp["Oppo"][masukan]
                print("Data berhasil dihapus!")
                main_admin()
            elif konfirmasi == "N":
                i = 0
                while i == 0:
                    print("Operasi dibatalkan, apakah anda ingin kembali ke menu hapus hp atau kembali ke menu admin?")
                    print("A. menu hapus hp")
                    print("B. menu admin")
                    konfirm = str(input(":"))
                    if konfirm == "A":
                        Hapus_hp()
                    elif konfirm == "B":
                        main_admin()
                    else:
                        print("Inputan salah")
            else:
                print("Inputan salah")
    
    elif masukan in Daftarhp["Iphone"].keys():
        print(masukan)
        print(Daftarhp["Iphone"][masukan])
        i = 0
        while i == 0:
            print("Apakah anda ingin menghapus ini? ini tidak bisa dikembalikan! (Y/N)")
            konfirmasi = str(input(":"))
            if konfirmasi == "Y":
                del Daftarhp["Iphone"][masukan]
                print("Data berhasil dihapus!")
                main_admin()
            elif konfirmasi == "N":
                i = 0
                while i == 0:
                    print("Operasi dibatalkan, apakah anda ingin kembali ke menu hapus hp atau kembali ke menu admin?")
                    print("A. menu hapus hp")
                    print("B. menu admin")
                    konfirm = str(input(":"))
                    if konfirm == "A":
                        Hapus_hp()
                    elif konfirm == "B":
                        main_admin()
                    else:
                        print("Inputan salah")
            else:
                print("Inputan salah")
    
    else:
        print("Inputan salah")
        Hapus_hp()



def Editspechp():
    print("List Data spec hp")
    for key in Spechp:
        print(key)

    print("menu utama")
    print("A. Tampilkan seluruh database spec hp yang tersimpan")
    print("B. Tambah spec hp baru")
    print("C. Edit spechp pada database")
    print("D. Kembali ke menu admin")
    print("Masukan input")
    masukan = str(input(":"))

    if masukan == "A":
        Tampilspechp()
    elif masukan == "B":
        Tambahspechp()
    elif masukan == "C":
        Editspechpada()
    elif masukan == "D":
        main_admin()
    elif masukan == "":
        print("Mohon masukan inputan yang benar")
        Editspechp()
    else:
        print("Masukan inputan yang benar")
        Editspechp()


def Tampilspechp():
    for key, val in Spechp["Samsung"].items():
        print(key, val)
    
    for key, val in Spechp["Oppo"].items():
        print(key, val)

    for key, val in Spechp["Iphone"].items():
        print(key, val)

    Editspechp()


def Tambahspechp():
    for key in Spechp.keys():
        print(key)

    print("pilih merk hp")
    masukan = str(input(":"))

    if masukan == "Samsung":
        Tambahspechp_Samsung()
    elif masukan == "Oppo":
        Tambahspechp_Oppo()
    elif masukan == "Iphone":
        Tambahspechp_Iphone()
    else:
        print("Masukan salah")

def Tambahspechp_Samsung():
    print("Nama hp?")
    Nama = str(input(":"))
    if Nama == "":
        print("harap masukan input")
        Tambahspechp_Samsung()

    i = 0
    while i == 0:   
        print(Nama)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Nama)
            Tambahspechp_Samsung1()
        elif Masukan == "N":
            Tambahspechp_Samsung()
        else:
            print("Masukan salah")
            
def Tambahspechp_Samsung1():   
    print("Tahun keluar?")
    try:
        Tahun_Keluar = int(input(":"))
    except ValueError:
        print("Masukan harus berbentuk angka")
        Tambahspechp_Samsung1()
    if Tahun_Keluar > 0:
        i = 0
        while i == 0:   
            print(Tahun_Keluar)
            print("Apakah Tahun Keluar sudah benar? (Y/N)")
            Masukan = str(input(":"))
            if Masukan == "Y":
                Datahp.append(Tahun_Keluar)
                Tambahspechp_Samsung2()
            elif Masukan == "N":
                Tambahspechp_Samsung1()
            else:
                print("Masukan salah")

def Tambahspechp_Samsung2():
    print("Versi OS?")
    Os = str(input(":"))
    if Os == "":
        print("harap masukan input")
        Tambahspechp_Samsung2()

    i = 0
    while i == 0:   
        print(Os)
        print("Apakah Versi OS sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Os)
            Tambahspechp_Samsung3()
        elif Masukan == "N":
            Tambahspechp_Samsung2()
        else:
            print("Masukan salah")


    
def Tambahspechp_Samsung3():
    print("Chipset?")
    Chipset = str(input(":"))
    if Chipset == "":
        print("harap masukan input")
        Tambahspechp_Samsung3()

    i = 0
    while i == 0:   
        print(Chipset)
        print("Apakah nama Chipset sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Chipset)
            Tambahspechp_Samsung4()
        elif Masukan == "N":
            Tambahspechp_Samsung3()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung4():
    print("CPU?")
    Cpu = str(input(":"))
    if Cpu == "":
        print("harap masukan input")
        Tambahspechp_Samsung4()

    i = 0
    while i == 0:   
        print(Cpu)
        print("Apakah nama CPU sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Cpu)
            Tambahspechp_Samsung5()
        elif Masukan == "N":
            Tambahspechp_Samsung4()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung5():
    print("GPU?")
    Gpu = str(input(":"))
    if Gpu == "":
        print("harap masukan input")
        Tambahspechp_Samsung5()

    i = 0
    while i == 0:   
        print(Gpu)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Gpu)
            Tambahspechp_Samsung6()
        elif Masukan == "N":
            Tambahspechp_Samsung5()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung6():
    print("Display?")
    Display = str(input(":"))
    if Display == "":
        print("harap masukan input")
        Tambahspechp_Samsung6()

    i = 0
    while i == 0:   
        print(Display)
        print("Apakah nama Display sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Display)
            Tambahspechp_Samsung7()
        elif Masukan == "N":
            Tambahspechp_Samsung6()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung7():
    print("Total Memori Internal?")
    Memori = str(input(":"))
    if Memori == "":
        print("harap masukan input")
        Tambahspechp_Samsung7()

    i = 0
    while i == 0:   
        print(Memori)
        print("Apakah Total memori sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Memori)
            Tambahspechp_Samsung8()
        elif Masukan == "N":
            Tambahspechp_Samsung7()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung8():
    print("Total Ram?")
    Ram = str(input(":"))
    if Ram == "":
        print("harap masukan input")
        Tambahspechp_Samsung8()

    i = 0
    while i == 0:   
        print(Ram)
        print("Apakah Total Ram sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Ram)
            Tambahspechp_Samsung9()
        elif Masukan == "N":
            Tambahspechp_Samsung8()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung9():
    print("Kamera?")
    Kamera = str(input(":"))
    if Kamera == "":
        print("harap masukan input")
        Tambahspechp_Samsung9()

    i = 0
    while i == 0:   
        print(Kamera)
        print("Apakah Kamera sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Kamera)
            Tambahspechp_Samsung10()
        elif Masukan == "N":
            Tambahspechp_Samsung9()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung10():
    print("Jaringan?")
    Jaringan = str(input(":"))
    if Jaringan == "":
        print("harap masukan input")
        Tambahspechp_Samsung10()

    i = 0
    while i == 0:   
        print(Jaringan)
        print("Apakah nama Jaringan sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Jaringan)
            Tambahspechp_Samsung11()
        elif Masukan == "N":
            Tambahspechp_Samsung10()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung11():
    print("Kapasitas Baterai?")
    Baterai = str(input(":"))
    if Baterai == "":
        print("harap masukan input")
        Tambahspechp_Samsung11()

    i = 0
    while i == 0:   
        print(Baterai)
        print("Apakah Kapasitas Baterai sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Baterai)
            Tambahspechp_Samsung12()
        elif Masukan == "N":
            Tambahspechp_Samsung11()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung12():
    Spechp["Samsung"][Datahp[0]] = {"Nama" : Datahp[0], "Tahun Keluar" : Datahp[1], "OS" : Datahp[2], "Chipset" : Datahp[3], "CPU" : Datahp[4], "GPU" : Datahp[5], "Display" : Datahp[6], "Memori Internal" : Datahp[7], "RAM" : Datahp[8], "Kamera" : Datahp[9], "Jaringan" : Datahp[10], "Kapasitas Baterai" : Datahp[11]}
    print("Data hp berhasil ditambah")
    Editspechp()

def Tambahspechp_Oppo():
    print("Nama hp?")
    Nama = str(input(":"))
    if Nama == "":
        print("harap masukan input")
        Tambahspechp_Oppo()

    i = 0
    while i == 0:   
        print(Nama)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Nama)
            Tambahspechp_Oppo1()
        elif Masukan == "N":
            Tambahspechp_Oppo()
        else:
            print("Masukan salah")
            
def Tambahspechp_Oppo1():   
    print("Tahun keluar?")
    try:
        Tahun_Keluar = int(input(":"))
    except ValueError:
        print("Masukan harus berbentuk angka")
        Tambahspechp_Oppo1()
    if Tahun_Keluar > 0:
        i = 0
        while i == 0:   
            print(Tahun_Keluar)
            print("Apakah Tahun Keluar sudah benar? (Y/N)")
            Masukan = str(input(":"))
            if Masukan == "Y":
                Datahp.append(Tahun_Keluar)
                Tambahspechp_Oppo2()
            elif Masukan == "N":
                Tambahspechp_Oppo1()
            else:
                print("Masukan salah")

def Tambahspechp_Oppo2():
    print("Versi OS?")
    Os = str(input(":"))
    if Os == "":
        print("harap masukan input")
        Tambahspechp_Oppo2()

    i = 0
    while i == 0:   
        print(Os)
        print("Apakah Versi OS sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Os)
            Tambahspechp_Oppo3()
        elif Masukan == "N":
            Tambahspechp_Oppo2()
        else:
            print("Masukan salah")


    
def Tambahspechp_Oppo3():
    print("Chipset?")
    Chipset = str(input(":"))
    if Chipset == "":
        print("harap masukan input")
        Tambahspechp_Oppo3()

    i = 0
    while i == 0:   
        print(Chipset)
        print("Apakah nama Chipset sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Chipset)
            Tambahspechp_Oppo4()
        elif Masukan == "N":
            Tambahspechp_Oppo3()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo4():
    print("CPU?")
    Cpu = str(input(":"))
    if Cpu == "":
        print("harap masukan input")
        Tambahspechp_Oppo4()

    i = 0
    while i == 0:   
        print(Cpu)
        print("Apakah nama CPU sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Cpu)
            Tambahspechp_Oppo5()
        elif Masukan == "N":
            Tambahspechp_Oppo4()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo5():
    print("GPU?")
    Gpu = str(input(":"))
    if Gpu == "":
        print("harap masukan input")
        Tambahspechp_Oppo5()

    i = 0
    while i == 0:   
        print(Gpu)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Gpu)
            Tambahspechp_Oppo6()
        elif Masukan == "N":
            Tambahspechp_Oppo5()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo6():
    print("Display?")
    Display = str(input(":"))
    if Display == "":
        print("harap masukan input")
        Tambahspechp_Oppo6()

    i = 0
    while i == 0:   
        print(Display)
        print("Apakah nama Display sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Display)
            Tambahspechp_Oppo7()
        elif Masukan == "N":
            Tambahspechp_Oppo6()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo7():
    print("Total Memori Internal?")
    Memori = str(input(":"))
    if Memori == "":
        print("harap masukan input")
        Tambahspechp_Oppo7()

    i = 0
    while i == 0:   
        print(Memori)
        print("Apakah Total memori sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Memori)
            Tambahspechp_Oppo8()
        elif Masukan == "N":
            Tambahspechp_Oppo7()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo8():
    print("Total Ram?")
    Ram = str(input(":"))
    if Ram == "":
        print("harap masukan input")
        Tambahspechp_Oppo8()

    i = 0
    while i == 0:   
        print(Ram)
        print("Apakah Total Ram sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Ram)
            Tambahspechp_Oppo9()
        elif Masukan == "N":
            Tambahspechp_Oppo8()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo9():
    print("Kamera?")
    Kamera = str(input(":"))
    if Kamera == "":
        print("harap masukan input")
        Tambahspechp_Oppo9()

    i = 0
    while i == 0:   
        print(Kamera)
        print("Apakah Kamera sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Kamera)
            Tambahspechp_Oppo10()
        elif Masukan == "N":
            Tambahspechp_Oppo9()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo10():
    print("Jaringan?")
    Jaringan = str(input(":"))
    if Jaringan == "":
        print("harap masukan input")
        Tambahspechp_Oppo10()

    i = 0
    while i == 0:   
        print(Jaringan)
        print("Apakah nama Jaringan sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Jaringan)
            Tambahspechp_Oppo11()
        elif Masukan == "N":
            Tambahspechp_Oppo10()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo11():
    print("Kapasitas Baterai?")
    Baterai = str(input(":"))
    if Baterai == "":
        print("harap masukan input")
        Tambahspechp_Oppo11()

    i = 0
    while i == 0:   
        print(Baterai)
        print("Apakah Kapasitas Baterai sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Baterai)
            Tambahspechp_Oppo12()
        elif Masukan == "N":
            Tambahspechp_Oppo11()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo12():
    Spechp["Oppo"][Datahp[0]] = {"Nama" : Datahp[0], "Tahun Keluar" : Datahp[1], "OS" : Datahp[2], "Chipset" : Datahp[3], "CPU" : Datahp[4], "GPU" : Datahp[5], "Display" : Datahp[6], "Memori Internal" : Datahp[7], "RAM" : Datahp[8], "Kamera" : Datahp[9], "Jaringan" : Datahp[10], "Kapasitas Baterai" : Datahp[11]}
    print("Data hp berhasil ditambah")
    Editspechp()



def Tambahspechp_Iphone():
    print("Nama hp?")
    Nama = str(input(":"))
    if Nama == "":
        print("harap masukan input")
        Tambahspechp_Iphone()

    i = 0
    while i == 0:   
        print(Nama)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Nama)
            Tambahspechp_Iphone1()
        elif Masukan == "N":
            Tambahspechp_Iphone()
        else:
            print("Masukan salah")
            
def Tambahspechp_Iphone1():   
    print("Tahun keluar?")
    try:
        Tahun_Keluar = int(input(":"))
    except ValueError:
        print("Masukan harus berbentuk angka")
        Tambahspechp_Iphone1()
    if Tahun_Keluar > 0:
        i = 0
        while i == 0:   
            print(Tahun_Keluar)
            print("Apakah Tahun Keluar sudah benar? (Y/N)")
            Masukan = str(input(":"))
            if Masukan == "Y":
                Datahp.append(Tahun_Keluar)
                Tambahspechp_Iphone2()
            elif Masukan == "N":
                Tambahspechp_Iphone1()
            else:
                print("Masukan salah")

def Tambahspechp_Iphone2():
    print("Versi OS?")
    Os = str(input(":"))
    if Os == "":
        print("harap masukan input")
        Tambahspechp_Iphone2()

    i = 0
    while i == 0:   
        print(Os)
        print("Apakah Versi OS sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Os)
            Tambahspechp_Iphone3()
        elif Masukan == "N":
            Tambahspechp_Iphone2()
        else:
            print("Masukan salah")


    
def Tambahspechp_Iphone3():
    print("Chipset?")
    Chipset = str(input(":"))
    if Chipset == "":
        print("harap masukan input")
        Tambahspechp_Iphone3()

    i = 0
    while i == 0:   
        print(Chipset)
        print("Apakah nama Chipset sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Chipset)
            Tambahspechp_Iphone4()
        elif Masukan == "N":
            Tambahspechp_Iphone3()
        else:
            print("Masukan salah")

def Tambahspechp_Iphone4():
    print("CPU?")
    Cpu = str(input(":"))
    if Cpu == "":
        print("harap masukan input")
        Tambahspechp_Iphone4()

    i = 0
    while i == 0:   
        print(Cpu)
        print("Apakah nama CPU sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Cpu)
            Tambahspechp_Iphone5()
        elif Masukan == "N":
            Tambahspechp_Iphone4()
        else:
            print("Masukan salah")

def Tambahspechp_Iphone5():
    print("GPU?")
    Gpu = str(input(":"))
    if Gpu == "":
        print("harap masukan input")
        Tambahspechp_Iphone5()

    i = 0
    while i == 0:   
        print(Gpu)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Gpu)
            Tambahspechp_Iphone6()
        elif Masukan == "N":
            Tambahspechp_Iphone5()
        else:
            print("Masukan salah")

def Tambahspechp_Iphone6():
    print("Display?")
    Display = str(input(":"))
    if Display == "":
        print("harap masukan input")
        Tambahspechp_Iphone6()

    i = 0
    while i == 0:   
        print(Display)
        print("Apakah nama Display sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Display)
            Tambahspechp_Iphone7()
        elif Masukan == "N":
            Tambahspechp_Iphone6()
        else:
            print("Masukan salah")

def Tambahspechp_Iphone7():
    print("Total Memori Internal?")
    Memori = str(input(":"))
    if Memori == "":
        print("harap masukan input")
        Tambahspechp_Iphone7()

    i = 0
    while i == 0:   
        print(Memori)
        print("Apakah Total memori sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Memori)
            Tambahspechp_Iphone8()
        elif Masukan == "N":
            Tambahspechp_Iphone7()
        else:
            print("Masukan salah")

def Tambahspechp_Iphone8():
    print("Total Ram?")
    Ram = str(input(":"))
    if Ram == "":
        print("harap masukan input")
        Tambahspechp_Iphone8()

    i = 0
    while i == 0:   
        print(Ram)
        print("Apakah Total Ram sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Ram)
            Tambahspechp_Iphone9()
        elif Masukan == "N":
            Tambahspechp_Iphone8()
        else:
            print("Masukan salah")

def Tambahspechp_Iphone9():
    print("Kamera?")
    Kamera = str(input(":"))
    if Kamera == "":
        print("harap masukan input")
        Tambahspechp_Iphone9()

    i = 0
    while i == 0:   
        print(Kamera)
        print("Apakah Kamera sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Kamera)
            Tambahspechp_Iphone10()
        elif Masukan == "N":
            Tambahspechp_Iphone9()
        else:
            print("Masukan salah")

def Tambahspechp_Iphone10():
    print("Jaringan?")
    Jaringan = str(input(":"))
    if Jaringan == "":
        print("harap masukan input")
        Tambahspechp_Iphone10()

    i = 0
    while i == 0:   
        print(Jaringan)
        print("Apakah nama Jaringan sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Jaringan)
            Tambahspechp_Iphone11()
        elif Masukan == "N":
            Tambahspechp_Iphone10()
        else:
            print("Masukan salah")

def Tambahspechp_Iphone11():
    print("Kapasitas Baterai?")
    Baterai = str(input(":"))
    if Baterai == "":
        print("harap masukan input")
        Tambahspechp_Iphone11()

    i = 0
    while i == 0:   
        print(Baterai)
        print("Apakah Kapasitas Baterai sudah benar? (Y/N)")
        Masukan = str(input(":"))
        if Masukan == "Y":
            Datahp.append(Baterai)
            Tambahspechp_Iphone12()
        elif Masukan == "N":
            Tambahspechp_Iphone11()
        else:
            print("Masukan salah")

def Tambahspechp_Iphone12():
    Spechp["Iphone"][Datahp[0]] = {"Nama" : Datahp[0], "Tahun Keluar" : Datahp[1], "OS" : Datahp[2], "Chipset" : Datahp[3], "CPU" : Datahp[4], "GPU" : Datahp[5], "Display" : Datahp[6], "Memori Internal" : Datahp[7], "RAM" : Datahp[8], "Kamera" : Datahp[9], "Jaringan" : Datahp[10], "Kapasitas Baterai" : Datahp[11]}
    print("Data hp berhasil ditambah")
    Editspechp()



def Editspechpada():
    for key in Spechp.keys():
        print(key)
        print("Pilih merk hp")
        masukan = str(input(":"))

        if masukan == "Samsung":
            for key in Spechp["Samsung"].keys():
                print(key)
                print("Pilih hp yang akan di edit")
                i = 0
                while i == 0:
                    masukan1 = str(input(":"))
                    if masukan1 in Spechp["Samsung"]:
                        Datahp.append(masukan1)
                        Editspechpsamsung()
                    else:
                        print("Masukan salah")
        
        elif masukan == "Oppo":
            for key in Spechp["Oppo"].keys():
                print(key)
                print("Pilih hp yang akan di edit")
                i = 0
                while i == 0:
                    masukan1 = str(input(":"))
                    if masukan1 in Spechp["Oppo"]:
                        Datahp.append(masukan1)
                        Editspechpoppo()
                    else:
                        print("Masukan salah")

        elif masukan == "Iphone":
            for key in Spechp["Iphone"].keys():
                print(key)
                print("Pilih hp yang akan di edit")
                i = 0
                while i == 0:
                    masukan1 = str(input(":"))
                    if masukan1 in Spechp["Iphone"]:
                        Datahp.append(masukan1)
                        Editspechpiphone()
                    else:
                        print("Masukan salah")

        else:
            print("Inputan salah")
            Editspechpada()


def Editspechpsamsung():

    print("Menu Edit spec hp")
    print("A. Edit spec hp ")
    print("B. Kembali ke menu edit")
    print("C. Kembali ke menu admin")
    masukan = str(input(":"))

    if masukan == "A":
        for key, val in Spechp["Samsung"][Datahp[0]].items():
            print("%s = %s" % (key,val))
        print(""" 
        Edit spec hp
        A. Nama
        B. Tahun Keluar
        C. OS
        D. Chipset
        E. CPU
        F. GPU
        G. Display
        H. Memori Internal
        I. RAM
        J. Kamera
        K. Jaringan
        L. Kapasitas Baterai
        M. Nama hp
        N. Kembali ke menu edit
        """)
        print("pilih huruf yang mau di edit ")
        i = 0
        while i == 0:
            ubah = str(input(":"))

            if ubah == "A":
                Namaspecsamsung()
            elif ubah == "B":
                Tahunspecsamsung()
            elif ubah == "C":
                Osspecsamsung()
            elif ubah == "D":
                Chipsetspecsamsung()
            elif ubah == "E":
                Cpuspecsamsung()
            elif ubah == "F":
                Gpuspecsamsung()
            elif ubah == "G":
                Displayspecsamsung()
            elif ubah == "H":
                Memorispecsamsung()
            elif ubah == "I":
                Ramspecsamsung()
            elif ubah == "J":
                Jaringanspecsamsung()
            elif ubah == "K":
                Kameraspecsamsung()
            elif ubah == "L":
                Bateraispecsamsung()
            elif ubah == "M":
                Namahpspecsamsung()
            elif ubah == "N":
                Editspechpsamsung()
            else:
                print("Mohon masukan input dengan benar")

    elif masukan == "B":
        Editspechp()
    
    elif masukan == "C":
        main_admin()
    
    else:
        print("Masukan salah")
            
               
def Namaspecsamsung():
    print("Masukan nama baru")
    nama = str(input(":"))
    if nama == "":
        print("masukan nama yang benar")
        Namaspecsamsung()
    print(nama)

    i = 0
    while i == 0:

        print("Apakah sudah benar namanya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Namaspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Namaspecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"Nama" : nama})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
    
        print("""
        Apakah anda ingin kembali ke:
        A. Edit spec
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Editspechpsamsung()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")




def Tahunspecsamsung():
    print("Masukan nama baru")
    try:
        Tahun = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Tahunspecsamsung()
    if Tahun > 0:
        i = 0
        while i == 0:
            print(Tahun)
            print("Apakah sudah benar tahunnya? (Y/N)")
            Konfirmasi = str(input(":"))
            if Konfirmasi == "Y":
                break
            elif Konfirmasi == "N":
                Tahunspecsamsung()
            else:
                print("Inputan salah")

        i = 0
        while i == 0:

            print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
            finalisasi = str(input(":"))
            if finalisasi == "Y":
                break
            elif finalisasi == "N":
                print("""
                A. Kembali ke awal edit
                B. Kembali ke menu edit
                C. Kembali ke menu admin
                """)
                masukan = str(input(":"))
                if masukan == "A":
                    Tahunspecsamsung()
                elif masukan == "B":
                    Editspechpsamsung()
                elif masukan == "C":
                    Datahp.clear()
                    main_admin()
                else:
                    print("Masukan salah")
                
            else:
                print("Inputan salah")

        Spechp["Samsung"][Datahp[0]].update({"Tahun Keluar" : Tahun})
        print("item berhasil di ubah!")
        i = 0
        while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Osspecsamsung():
    print("Masukan nama OS baru")
    Os = str(input(":"))
    if Os == "":
        print("masukan nama yang benar")
        Osspecsamsung()
    print(Os)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama Os nya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Osspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Osspecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"OS" : Os})
    print("item berhasil di ubah!")
    
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Chipsetspecsamsung():
    print("Masukan nama chipset baru")
    chipset = str(input(":"))
    if chipset == "":
        print("masukan nama yang benar")
        Chipsetspecsamsung()
    print(chipset)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama chipsetnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Chipsetspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Chipsetspecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"Chipset" : chipset})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Cpuspecsamsung():
    print("Masukan nama CPU baru")
    Cpu = str(input(":"))
    if Cpu == "":
        print("masukan nama yang benar")
        Cpuspecsamsung()
    print(Cpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama CPUnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Cpuspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Cpuspecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"CPU" : Cpu})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Gpuspecsamsung():
    print("Masukan nama Gpu baru")
    Gpu = str(input(":"))
    if Gpu == "":
        print("masukan nama yang benar")
        Gpuspecsamsung()
    print(Gpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama GPUnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Gpuspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Gpuspecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"GPU" : Gpu})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Displayspecsamsung():
    print("Masukan nama tipe Display baru")
    Display = str(input(":"))
    if Display == "":
        print("masukan nama yang benar")
        Displayspecsamsung()
    print(Display)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama Displaynya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Displayspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Displayspecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"Display" : Display})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")



def Memorispecsamsung():
    print("Masukan jumlah memori hp baru")
    Memori = str(input(":"))
    if Memori == "":
        print("masukan nama yang benar")
        Memorispecsamsung()
    print(Memori)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas memorinya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Memorispecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Memorispecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"Memori Internal" : Memori})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Ramspecsamsung():
    print("Masukan jumlah RAM baru")
    Ram = str(input(":"))
    if Ram == "":
        print("masukan nama yang benar")
        Ramspecsamsung()
    print(Ram)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas RAMnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Ramspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Ramspecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"RAM" : Ram})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Kameraspecsamsung():
    print("Masukan total MP Kamera baru")
    Kamera = str(input(":"))
    if Kamera == "":
        print("masukan nama yang benar")
        Kameraspecsamsung()
    print(Kamera)

    i = 0
    while i == 0:

        print("Apakah sudah benar MP kameranya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Kameraspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Kameraspecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"Kamera" : Kamera})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Jaringanspecsamsung():
    print("Masukan Support Jaringan baru")
    Jaringan = str(input(":"))
    if Jaringan == "":
        print("masukan nama yang benar")
        Jaringanspecsamsung()
    print(Jaringan)

    i = 0
    while i == 0:

        print("Apakah sudah benar Jaringannya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Jaringanspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Jaringanspecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"Jaringan" : Jaringan})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Bateraispecsamsung():
    print("Masukan jumlah kapasitas baterai baru")
    Baterai = str(input(":"))
    if Baterai == "":
        print("masukan nama yang benar")
        Bateraispecsamsung()
    print(Baterai)

    i = 0
    while i == 0:

        print("Apakah sudah benar jumlah Kapasitas Baterainya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Bateraispecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Bateraispecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Datahp[0]].update({"Kapasitas Baterai" : Baterai})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Namahpspecsamsung():
    print("Masukan Nama hp baru")
    Nama = str(input(":"))
    if Nama == "":
        print("masukan nama yang benar")
        Namahpspecsamsung()
    print(Nama)

    i = 0
    while i == 0:

        print("Apakah sudah benar jumlah Kapasitas Baterainya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Namahpspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Namahpspecsamsung()
            elif masukan == "B":
                Editspechpsamsung()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Samsung"][Nama] = Daftarhp["Samsung"].pop(Datahp[0])
    Datahp.clear()
    Datahp.append(Nama)
    i = 0
    while i == 0:
        print("Item berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit spec
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Editspechpsamsung()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")



def Editspechpoppo():

    print("Menu Edit spec hp")
    print("A. Edit spec hp ")
    print("B. Kembali ke menu edit")
    print("C. Kembali ke menu admin")
    masukan = str(input(":"))

    if masukan == "A":
        for key, val in Spechp["Oppo"][Datahp[0]].items():
            print("%s = %s" % (key,val))
        print(""" 
        Edit spec hp
        A. Nama
        B. Tahun Keluar
        C. OS
        D. Chipset
        E. CPU
        F. GPU
        G. Display
        H. Memori Internal
        I. RAM
        J. Kamera
        K. Jaringan
        L. Kapasitas Baterai
        M. Nama hp
        N. Kembali ke menu edit
        """)
        print("pilih huruf yang mau di edit ")
        i = 0
        while i == 0:
            ubah = str(input(":"))

            if ubah == "A":
                Namaspecoppo()
            elif ubah == "B":
                Tahunspecoppo()
            elif ubah == "C":
                Osspecoppo()
            elif ubah == "D":
                Chipsetspecoppo()
            elif ubah == "E":
                Cpuspecoppo()
            elif ubah == "F":
                Gpuspecoppo()
            elif ubah == "G":
                Displayspecoppo()
            elif ubah == "H":
                Memorispecoppo()
            elif ubah == "I":
                Ramspecoppo()
            elif ubah == "J":
                Jaringanspecoppo()
            elif ubah == "K":
                Kameraspecoppo()
            elif ubah == "L":
                Bateraispecoppo()
            elif ubah == "M":
                Namahpspecoppo()
            elif ubah == "N":
                Editspechpoppo()
            else:
                print("Mohon masukan input dengan benar")

    elif masukan == "B":
        Editspechp()
    
    elif masukan == "C":
        Datahp.clear()
        main_admin()
    
    else:
        print("Masukan salah")
            
               
def Namaspecoppo():
    print("Masukan nama baru")
    nama = str(input(":"))
    if nama == "":
        print("masukan nama yang benar")
        Namaspecoppo()
    print(nama)

    i = 0
    while i == 0:

        print("Apakah sudah benar namanya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Namaspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Namaspecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"Nama" : nama})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
    
        print("""
        Apakah anda ingin kembali ke:
        A. Edit spec
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Editspechpoppo()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")




def Tahunspecoppo():
    print("Masukan nama baru")
    try:
        Tahun = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Tahunspecoppo()
    if Tahun > 0:
        i = 0
        while i == 0:
            print(Tahun)
            print("Apakah sudah benar tahunnya? (Y/N)")
            Konfirmasi = str(input(":"))
            if Konfirmasi == "Y":
                break
            elif Konfirmasi == "N":
                Tahunspecoppo()
            else:
                print("Inputan salah")

        i = 0
        while i == 0:

            print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
            finalisasi = str(input(":"))
            if finalisasi == "Y":
                break
            elif finalisasi == "N":
                print("""
                A. Kembali ke awal edit
                B. Kembali ke menu edit
                C. Kembali ke menu admin
                """)
                masukan = str(input(":"))
                if masukan == "A":
                    Tahunspecoppo()
                elif masukan == "B":
                    Editspechpoppo()
                elif masukan == "C":
                    Datahp.clear()
                    main_admin()
                else:
                    print("Masukan salah")
                
            else:
                print("Inputan salah")

        Spechp["Oppo"][Datahp[0]].update({"Tahun Keluar" : Tahun})
        print("item berhasil di ubah!")
        i = 0
        while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Osspecoppo():
    print("Masukan nama OS baru")
    Os = str(input(":"))
    if Os == "":
        print("masukan nama yang benar")
        Osspecoppo()
    print(Os)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama Os nya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Osspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Osspecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"OS" : Os})
    print("item berhasil di ubah!")
    
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Chipsetspecoppo():
    print("Masukan nama chipset baru")
    chipset = str(input(":"))
    if chipset == "":
        print("masukan nama yang benar")
        Chipsetspecoppo()
    print(chipset)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama chipsetnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Chipsetspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Chipsetspecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"Chipset" : chipset})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Cpuspecoppo():
    print("Masukan nama CPU baru")
    Cpu = str(input(":"))
    if Cpu == "":
        print("masukan nama yang benar")
        Cpuspecoppo()
    print(Cpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama CPUnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Cpuspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Cpuspecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"CPU" : Cpu})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Gpuspecoppo():
    print("Masukan nama Gpu baru")
    Gpu = str(input(":"))
    if Gpu == "":
        print("masukan nama yang benar")
        Gpuspecoppo()
    print(Gpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama GPUnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Gpuspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Gpuspecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"GPU" : Gpu})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Displayspecoppo():
    print("Masukan nama tipe Display baru")
    Display = str(input(":"))
    if Display == "":
        print("masukan nama yang benar")
        Displayspecoppo()
    print(Display)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama Displaynya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Displayspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Displayspecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"Display" : Display})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")



def Memorispecoppo():
    print("Masukan jumlah memori hp baru")
    Memori = str(input(":"))
    if Memori == "":
        print("masukan nama yang benar")
        Memorispecoppo()
    print(Memori)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas memorinya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Memorispecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Memorispecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"Memori Internal" : Memori})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Ramspecoppo():
    print("Masukan jumlah RAM baru")
    Ram = str(input(":"))
    if Ram == "":
        print("masukan nama yang benar")
        Ramspecoppo()
    print(Ram)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas RAMnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Ramspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Ramspecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"RAM" : Ram})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Kameraspecoppo():
    print("Masukan total MP Kamera baru")
    Kamera = str(input(":"))
    if Kamera == "":
        print("masukan nama yang benar")
        Kameraspecoppo()
    print(Kamera)

    i = 0
    while i == 0:

        print("Apakah sudah benar MP kameranya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Kameraspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Kameraspecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"Kamera" : Kamera})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Jaringanspecoppo():
    print("Masukan Support Jaringan baru")
    Jaringan = str(input(":"))
    if Jaringan == "":
        print("masukan nama yang benar")
        Jaringanspecoppo()
    print(Jaringan)

    i = 0
    while i == 0:

        print("Apakah sudah benar Jaringannya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Jaringanspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Jaringanspecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"Jaringan" : Jaringan})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Bateraispecoppo():
    print("Masukan jumlah kapasitas baterai baru")
    Baterai = str(input(":"))
    if Baterai == "":
        print("masukan nama yang benar")
        Bateraispecoppo()
    print(Baterai)

    i = 0
    while i == 0:

        print("Apakah sudah benar jumlah Kapasitas Baterainya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Bateraispecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Bateraispecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Datahp[0]].update({"Kapasitas Baterai" : Baterai})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Namahpspecoppo():
    print("Masukan Nama hp baru")
    Nama = str(input(":"))
    if Nama == "":
        print("masukan nama yang benar")
        Namahpspecoppo()
    print(Nama)

    i = 0
    while i == 0:

        print("Apakah sudah benar jumlah Kapasitas Baterainya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Namahpspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Namahpspecoppo()
            elif masukan == "B":
                Editspechpoppo()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Oppo"][Nama] = Daftarhp["Oppo"].pop(Datahp[0])
    Datahp.clear()
    Datahp.append(Nama)
    i = 0
    while i == 0:
        print("Item berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit spec
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Editspechpoppo()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")







def Editspechpiphone():

    print("Menu Edit spec hp")
    print("A. Edit spec hp ")
    print("B. Kembali ke menu edit")
    print("C. Kembali ke menu admin")
    masukan = str(input(":"))

    if masukan == "A":
        for key, val in Spechp["Iphone"][Datahp[0]].items():
            print("%s = %s" % (key,val))
        print(""" 
        Edit spec hp
        A. Nama
        B. Tahun Keluar
        C. OS
        D. Chipset
        E. CPU
        F. GPU
        G. Display
        H. Memori Internal
        I. RAM
        J. Kamera
        K. Jaringan
        L. Kapasitas Baterai
        M. Nama hp
        N. Kembali ke menu edit
        """)
        print("pilih huruf yang mau di edit ")
        i = 0
        while i == 0:
            ubah = str(input(":"))

            if ubah == "A":
                Namaspeciphone()
            elif ubah == "B":
                Tahunspeciphone()
            elif ubah == "C":
                Osspeciphone()
            elif ubah == "D":
                Chipsetspeciphone()
            elif ubah == "E":
                Cpuspeciphone()
            elif ubah == "F":
                Gpuspeciphone()
            elif ubah == "G":
                Displayspeciphone()
            elif ubah == "H":
                Memorispeciphone()
            elif ubah == "I":
                Ramspeciphone()
            elif ubah == "J":
                Jaringanspeciphone()
            elif ubah == "K":
                Kameraspeciphone()
            elif ubah == "L":
                Bateraispeciphone()
            elif ubah == "M":
                Namahpspeciphone()
            elif ubah == "N":
                Editspechpiphone()
            else:
                print("Mohon masukan input dengan benar")

    elif masukan == "B":
        Editspechp()
    
    elif masukan == "C":
        Datahp.clear()
        main_admin()
    
    else:
        print("Masukan salah")
            
               
def Namaspeciphone():
    print("Masukan nama baru")
    nama = str(input(":"))
    if nama == "":
        print("masukan nama yang benar")
        Namaspeciphone()
    print(nama)

    i = 0
    while i == 0:

        print("Apakah sudah benar namanya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Namaspeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Namaspeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"Nama" : nama})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
    
        print("""
        Apakah anda ingin kembali ke:
        A. Edit spec
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Editspechpiphone()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")




def Tahunspeciphone():
    print("Masukan nama baru")
    try:
        Tahun = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Tahunspeciphone()
    if Tahun > 0:
        i = 0
        while i == 0:
            print(Tahun)
            print("Apakah sudah benar tahunnya? (Y/N)")
            Konfirmasi = str(input(":"))
            if Konfirmasi == "Y":
                break
            elif Konfirmasi == "N":
                Tahunspeciphone()
            else:
                print("Inputan salah")

        i = 0
        while i == 0:

            print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
            finalisasi = str(input(":"))
            if finalisasi == "Y":
                break
            elif finalisasi == "N":
                print("""
                A. Kembali ke awal edit
                B. Kembali ke menu edit
                C. Kembali ke menu admin
                """)
                masukan = str(input(":"))
                if masukan == "A":
                    Tahunspeciphone()
                elif masukan == "B":
                    Editspechpiphone()
                elif masukan == "C":
                    Datahp.clear()
                    main_admin()
                else:
                    print("Masukan salah")
                
            else:
                print("Inputan salah")

        Spechp["Iphone"][Datahp[0]].update({"Tahun Keluar" : Tahun})
        print("item berhasil di ubah!")
        i = 0
        while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Osspeciphone():
    print("Masukan nama OS baru")
    Os = str(input(":"))
    if Os == "":
        print("masukan nama yang benar")
        Osspeciphone()
    print(Os)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama Os nya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Osspeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Osspeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"OS" : Os})
    print("item berhasil di ubah!")
    
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Chipsetspeciphone():
    print("Masukan nama chipset baru")
    chipset = str(input(":"))
    if chipset == "":
        print("masukan nama yang benar")
        Chipsetspeciphone()
    print(chipset)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama chipsetnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Chipsetspeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Chipsetspeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"Chipset" : chipset})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Cpuspeciphone():
    print("Masukan nama CPU baru")
    Cpu = str(input(":"))
    if Cpu == "":
        print("masukan nama yang benar")
        Cpuspeciphone()
    print(Cpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama CPUnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Cpuspeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Cpuspeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"CPU" : Cpu})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Gpuspeciphone():
    print("Masukan nama Gpu baru")
    Gpu = str(input(":"))
    if Gpu == "":
        print("masukan nama yang benar")
        Gpuspeciphone()
    print(Gpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama GPUnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Gpuspeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Gpuspeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"GPU" : Gpu})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Displayspeciphone():
    print("Masukan nama tipe Display baru")
    Display = str(input(":"))
    if Display == "":
        print("masukan nama yang benar")
        Displayspeciphone()
    print(Display)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama Displaynya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Displayspeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Displayspeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"Display" : Display})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")



def Memorispeciphone():
    print("Masukan jumlah memori hp baru")
    Memori = str(input(":"))
    if Memori == "":
        print("masukan nama yang benar")
        Memorispeciphone()
    print(Memori)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas memorinya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Memorispeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Memorispeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"Memori Internal" : Memori})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Ramspeciphone():
    print("Masukan jumlah RAM baru")
    Ram = str(input(":"))
    if Ram == "":
        print("masukan nama yang benar")
        Ramspeciphone()
    print(Ram)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas RAMnya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Ramspeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Ramspeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"RAM" : Ram})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Kameraspeciphone():
    print("Masukan total MP Kamera baru")
    Kamera = str(input(":"))
    if Kamera == "":
        print("masukan nama yang benar")
        Kameraspeciphone()
    print(Kamera)

    i = 0
    while i == 0:

        print("Apakah sudah benar MP kameranya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Kameraspeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Kameraspeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"Kamera" : Kamera})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Jaringanspeciphone():
    print("Masukan Support Jaringan baru")
    Jaringan = str(input(":"))
    if Jaringan == "":
        print("masukan nama yang benar")
        Jaringanspeciphone()
    print(Jaringan)

    i = 0
    while i == 0:

        print("Apakah sudah benar Jaringannya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Jaringanspeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Jaringanspeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"Jaringan" : Jaringan})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Bateraispeciphone():
    print("Masukan jumlah kapasitas baterai baru")
    Baterai = str(input(":"))
    if Baterai == "":
        print("masukan nama yang benar")
        Bateraispeciphone()
    print(Baterai)

    i = 0
    while i == 0:

        print("Apakah sudah benar jumlah Kapasitas Baterainya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Bateraispeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Bateraispeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Datahp[0]].update({"Kapasitas Baterai" : Baterai})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str(input(":"))

            if masukan1 == "A":
                Editspechpiphone()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Namahpspeciphone():
    print("Masukan Nama hp baru")
    Nama = str(input(":"))
    if Nama == "":
        print("masukan nama yang benar")
        Namahpspeciphone()
    print(Nama)

    i = 0
    while i == 0:

        print("Apakah sudah benar jumlah Kapasitas Baterainya? (Y/N)")
        Konfirmasi = str(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Namahpspeciphone()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke awal edit
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str(input(":"))
            if masukan == "A":
                Namahpspeciphone()
            elif masukan == "B":
                Editspechpiphone()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Iphone"][Nama] = Daftarhp["Iphone"].pop(Datahp[0])
    Datahp.clear()
    Datahp.append(Nama)
    i = 0
    while i == 0:
        print("Item berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit spec
        B. Menu admin
        """)
        masukan1 = str(input(":"))

        if masukan1 == "A":
            Editspechpiphone()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")


def stokhp():
    for key, val in Spechp.items():
        for key2, val2 in val.items():
            print("%s : %s" % (key2,val2))
    
    print("""
    A. Tambah stok hp
    B. Ubah stok hp
    C. Kembali ke menu admin
    
    """)







def masukkasir():
    print("====================================")
    print("Apakah anda ingin masuk mode kasir? ")
    print("====================================")
    konfirmasi = str(input("Ya/Tidak :"))
    if konfirmasi == "Ya":
            kasir()
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

    print("Menu Kasir")
    print("""
    A. Jual Hp
    B. Beli Hp
    C. Kembali ke login
    """)

    masukan = str(input(":"))

    if masukan == "A":
        jualhp()
    elif masukan == "B":
        belihp()
    elif masukan == "C":
        user_login()
    else:
        print("Masukan pilihan dengan benar")
        kasir()


def jualhp():
    print("Jual hp")
    print("toko")
    for key, val in Daftarhp.items():
        for key2, val2 in val.items():
            print("%s : %s" % (key2,val2))
    print("""
    A. Pilih hp berdasarkan merk
    B. Pilih hp berdasarkan harga
    C. Kembali ke awal 
    Ket: Masukan nama hp sesuai di tabel untuk pilih hp yang akan di beli
    """)
    masukan = str(input(":"))

    if masukan == "A":
        jualhpmerk()
    elif masukan == "B":
        jualhpharga()
    elif masukan == "C":
        kasir()
    else:
        print("masukan salah")
        jualhp()


def jualhpmerk():
    for merk in Merkhp:
        print(merk)
    print("Pilih merk yang di inginkan")
    pilihmerk = str(input(":"))        
    if pilihmerk == "Samsung":
        i = 0
        while i == 0:
            for key,val in Daftarhp["Samsung"].items():
                print("%s : %s" % (key,val))
            
            print("""
                A. Tampilkan seluruh merk hp
                B. Pilih hp berdasarkan harga
                C. Kembali ke awal

                Ket: Masukan nama hp sesuai di tabel untuk pilih hp yang akan di beli 
            """)

            masukansamsung = str(input(":"))
            if masukansamsung == "A":
                jualhp()
            elif masukansamsung == "B":
                jualhpharga()
            elif masukansamsung == "C":
                kasir()
            elif masukansamsung in Daftarhp["Samsung"].keys():
                Datahp.append(masukansamsung)
                konfirmasibeli()
            else:
                print("masukan salah")

    elif pilihmerk == "Oppo":
        i = 0
        while i == 0:
            for key,val in Daftarhp["Oppo"].items():
                print("%s : %s" % (key,val))
            
            print("""
                A. Tampilkan seluruh merk hp
                B. Pilih hp berdasarkan harga
                C. Kembali ke awal

                Ket: Masukan nama hp sesuai di tabel untuk pilih hp yang akan di beli 
            """)

            masukanoppo = str(input(":"))
            if masukanoppo == "A":
                jualhp()
            elif masukanoppo == "B":
                jualhpharga()
            elif masukanoppo == "C":
                kasir()
            elif masukanoppo in Daftarhp["Oppo"].keys():
                Datahp.append(masukanoppo)
                konfirmasibeli()
            else:
                print("masukan salah")
    elif pilihmerk == "Iphone":
        i = 0
        while i == 0:
            for key,val in Daftarhp["Iphone"].items():
                print("%s : %s" % (key,val))
            
            print("""
                A. Tampilkan seluruh merk hp
                B. Pilih hp berdasarkan harga
                C. Kembali ke awal

                Ket: Masukan nama hp sesuai di tabel untuk pilih hp yang akan di beli 
            """)

            masukaniphone = str(input(":"))
            if masukaniphone == "A":
                jualhp()
            elif masukaniphone == "B":
                jualhpharga()
            elif masukaniphone == "C":
                kasir()
            elif masukaniphone in Daftarhp["Iphone"].keys():
                Datahp.append(masukaniphone)
                konfirmasibeli()
            else:
                print("Masukan salah")
                
    else:
        print("masukan anda salah, silakan isi kembali")
        


    
def konfirmasibeli():
    if Datahp[0] in Daftarhp["Samsung"].keys():
        print("Nama Hp :", Datahp[0])
        print("Harga Hp :", Daftarhp["Samsung"][Datahp[0]])
        try:
            print("Spec hp :", Spechp["Samsung"][Datahp[0]])
        except KeyError:
            print("Spec hp tidak ada")

        print("Stok Hp :", Stokhp["Samsung"][Datahp[0]])
        print("""
        A. Jual Hp ini
        B. Pilih Hp lain
        C. Kembali ke awal
        """)
        masukan = str(input(":"))
        if masukan == "A":
            print("Apakah anda ingin menjual hp ini? (Y/N)")
            Konfirmasi = str(input(":"))
            if Konfirmasi == "Y":
                if Stokhp["Samsung"][Datahp[0]] > 0:
                    print("Toko")
                    print("Nama Hp :", Datahp[0])
                    print("Harga Hp :", Daftarhp["Samsung"][Datahp[0]])
                    print("Jumlah Bayar Total : Rp.", Daftarhp["Samsung"][Datahp[0]])
                    print("Terima kasih telah membeli di toko kami")
                    ubah = Stokhp["Samsung"][Datahp[0]] - 1
                    Stokhp["Samsung"].update({Datahp[0] : ubah})
                    Keuntungan["Total_keuntungan"].append(Daftarhp["Samsung"][Datahp[0]])
                    Datahp.clear()
                    kasir()
                else:
                    print("Mohon maaf hp ini tidak ada stoknya")
                    jualhp()
            
            elif Konfirmasi == "N":
                i = 0
                while i == 0:

                    print("""
                    A. Kembali ke daftar seluruh hp
                    B. Kembali ke kasir
                    """)
                    kembali = str(input(":"))

                    if kembali == "A":
                        jualhp()
                    elif kembali == "B":
                        kasir()
                    else:
                        print("Masukan salah silakan coba kembali")


        elif masukan == "B":
            Datahp.clear()
            jualhpmerk()
        elif masukan == "C":
            Datahp.clear()
            jualhp()
    
    elif Datahp[0] in Daftarhp["Oppo"].keys():
        print("Nama Hp :", Datahp[0])
        print("Harga Hp :", Daftarhp["Oppo"][Datahp[0]])
        try:
            print("Spec hp :", Spechp["Oppo"][Datahp[0]])
        except KeyError:
            print("Spec hp tidak ada")

        print("Stok Hp :", Stokhp["Oppo"][Datahp[0]])
        print("""
        A. Jual Hp ini
        B. Pilih Hp lain
        C. Kembali ke awal
        """)
        masukan = str(input(":"))
        if masukan == "A":
            print("Apakah anda ingin menjual hp ini? (Y/N)")
            Konfirmasi = str(input(":"))
            if Konfirmasi == "Y":
                if Stokhp["Oppo"][Datahp[0]] > 0:
                    print("Toko")
                    print("Nama Hp :", Datahp[0])
                    print("Harga Hp :", Daftarhp["Oppo"][Datahp[0]])
                    print("Jumlah Bayar Total : Rp.", Daftarhp["Oppo"][Datahp[0]])
                    print("Terima kasih telah membeli di toko kami")
                    ubah = Stokhp["Oppo"][Datahp[0]] - 1
                    Stokhp["Oppo"].update({Datahp[0] : ubah})
                    Keuntungan["Total_keuntungan"].append(Daftarhp["Oppo"][Datahp[0]])
                    Datahp.clear()
                    kasir()
                else:
                    print("Mohon maaf hp ini tidak ada stoknya")
                    jualhp()
            
            elif Konfirmasi == "N":
                i = 0
                while i == 0:

                    print("""
                    A. Kembali ke daftar seluruh hp
                    B. Kembali ke kasir
                    """)
                    kembali = str(input(":"))

                    if kembali == "A":
                        jualhp()
                    elif kembali == "B":
                        kasir()
                    else:
                        print("Masukan salah silakan coba kembali")

        elif masukan == "B":
            Datahp.clear()
            jualhpmerk()
        elif masukan == "C":
            Datahp.clear()
            jualhp()

    elif Datahp[0] in Daftarhp["Iphone"].keys():
        print("Nama Hp :", Datahp[0])
        print("Harga Hp :", Daftarhp["Iphone"][Datahp[0]])
        try:
            print("Spec hp :", Spechp["Iphone"][Datahp[0]])
        except KeyError:
            print("Spec hp tidak ada")

        print("Stok Hp :", Stokhp["Iphone"][Datahp[0]])
        print("""
        A. Jual Hp ini
        B. Pilih Hp lain
        C. Kembali ke awal
        """)
        masukan = str(input(":"))
        if masukan == "A":
            print("Apakah anda ingin menjual hp ini? (Y/N)")
            Konfirmasi = str(input(":"))
            if Konfirmasi == "Y":
                if Stokhp["Iphone"][Datahp[0]] > 0:
                    print("Toko")
                    print("Nama Hp :", Datahp[0])
                    print("Harga Hp :", Daftarhp["Iphone"][Datahp[0]])
                    print("Jumlah Bayar Total : Rp.", Daftarhp["Iphone"][Datahp[0]])
                    print("Terima kasih telah membeli di toko kami")
                    ubah = Stokhp["Iphone"][Datahp[0]] - 1
                    Stokhp["Iphone"].update({Datahp[0] : ubah})
                    Keuntungan["Total_keuntungan"].append(Daftarhp["Iphone"][Datahp[0]])
                    Datahp.clear()
                    kasir()
                else:
                    print("Mohon maaf hp ini tidak ada stoknya")
                    jualhp()
            
            elif Konfirmasi == "N":
                i = 0
                while i == 0:

                    print("""
                    A. Kembali ke daftar seluruh hp
                    B. Kembali ke kasir
                    """)
                    kembali = str(input(":"))

                    if kembali == "A":
                        jualhp()
                    elif kembali == "B":
                        kasir()
                    else:
                        print("Masukan salah silakan coba kembali")

        elif masukan == "B":
            Datahp.clear()
            jualhpmerk()
        elif masukan == "C":
            Datahp.clear()
            jualhp()

    else:
        print("data tidak ada")
                

def jualhpharga():
    Samsung = sorted(Daftarhp["Samsung"].items(), key=lambda x: x[1])
    Oppo = sorted(Daftarhp["Oppo"].items(), key=lambda x: x[1])
    Iphone = sorted(Daftarhp["Iphone"].items(), key=lambda x: x[1])
    for s in Samsung:
        print(s[0], s[1])
    for o in Oppo:
        print(o[0], o[1])
    for i in Iphone:
        print(i[0], i[1])

    print("""
                A. Tampilkan seluruh merk hp
                B. Pilih hp berdasarkan merk
                C. Kembali ke awal

                Ket: Masukan nama hp sesuai di tabel untuk pilih hp yang akan di beli 
    """)

    masukan = str(input(":"))
    if masukan == "A":
        jualhp()
    elif masukan == "B":
        jualhpmerk()
    elif masukan == "C":
        kasir()
    elif masukan in Daftarhp["Samsung"].keys():
        Datahp.append(masukan)
        konfirmasibeli()
    elif masukan in Daftarhp["Oppo"].keys():
        Datahp.append(masukan)
        konfirmasibeli()
    elif masukan in Daftarhp["Iphone"].keys():
        Datahp.append(masukan)
        konfirmasibeli()
    else:
        print("Masukan salah")
        jualhpharga()

    
    
def belihp():
    for i in Merkhp:
        print(i)
    print("Pilih merk hp yang akan dibeli")
    masukan = str(input(":"))
    if masukan == "Samsung":
        belihpsamsung()
    elif masukan == "Oppo":
        belihpoppo()
    elif masukan == "Iphone":
        belihpiphone()
    else:
        print("masukan salah")
        belihp()

def belihpsamsung():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        nama = str(input(":"))
        if nama == "":
            print("mohon masukan input dengan benar")
        else:
            Datahp.append(nama)
            belihpsamsung1()

def belihpsamsung1():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        try:
            harga = int(input(":"))
        except ValueError:
            print("harap masukan angka bukan huruf")
        if harga > 0:
            Datahp.append(harga)
            belihpsamsung2()
        else:
            print("masukan anda negatif atau bukan angka")
        
def belihpsamsung2():
    print("Nama Hp", Datahp[0])
    print("Harga hp", Datahp[1])
    print("Apakah nama dan harga sudah sesuai? (konfirmasi kepada penjual) (Y/N)")
    finalisasi = str(input(":"))
    if finalisasi == "Y":
        print("toko hp")
        print("Nama Hp", Datahp[0])
        print("Harga hp", Datahp[1])
        print("terima kasih telah menjual di sini")
        kasir()

    elif finalisasi == "N":
        i = 0
        while i == 0:
            print("""
            A. Ubah nama
            B. Ubah harga
            C. Batalkan penbelian
            """)
            masukan = str(input(":"))
            if masukan == "A":
                belihpsamsung()
            elif masukan == "B":
                belihpsamsung1()
            elif masukan == "C":
                i = 0
                while i == 0:
                    print("Apakah anda yakin untuk membatalkan (Y/N)")
                    batal = str(input(":"))
                    if batal == "Y":
                        Datahp.clear()
                        print("pembelian dibatalkan")
                        kasir()
                    elif batal == "N":
                        belihpsamsung2()
                    else:
                        print("masukan salah")
            else:
                print("Masukan salah")
    else:
        print("masukan salah")


def belihpoppo():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        nama = str(input(":"))
        if nama == "":
            print("mohon masukan input dengan benar")
        else:
            Datahp.append(nama)
            belihpoppo1()

def belihpoppo1():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        try:
            harga = int(input(":"))
        except ValueError:
            print("harap masukan angka bukan huruf")
        if harga > 0:
            Datahp.append(harga)
            belihpoppo2()
        else:
            print("masukan anda negatif atau bukan angka")
        
def belihpoppo2():
    print("Nama Hp", Datahp[0])
    print("Harga hp", Datahp[1])
    print("Apakah nama dan harga sudah sesuai? (konfirmasi kepada penjual) (Y/N)")
    finalisasi = str(input(":"))
    if finalisasi == "Y":
        print("toko hp")
        print("Nama Hp", Datahp[0])
        print("Harga hp", Datahp[1])
        print("terima kasih telah menjual di sini")
        kasir()

    elif finalisasi == "N":
        i = 0
        while i == 0:
            print("""
            A. Ubah nama
            B. Ubah harga
            C. Batalkan penbelian
            """)
            masukan = str(input(":"))
            if masukan == "A":
                belihpoppo()
            elif masukan == "B":
                belihpoppo1()
            elif masukan == "C":
                i = 0
                while i == 0:
                    print("Apakah anda yakin untuk membatalkan (Y/N)")
                    batal = str(input(":"))
                    if batal == "Y":
                        Datahp.clear()
                        print("pembelian dibatalkan")
                        kasir()
                    elif batal == "N":
                        belihpoppo2()
                    else:
                        print("masukan salah")
            else:
                print("Masukan salah")
    else:
        print("masukan salah")
                

def belihpiphone():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        nama = str(input(":"))
        if nama == "":
            print("mohon masukan input dengan benar")
        else:
            Datahp.append(nama)
            belihpiphone1()

def belihpiphone1():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        try:
            harga = int(input(":"))
        except ValueError:
            print("harap masukan angka bukan huruf")
        if harga > 0:
            Datahp.append(harga)
            belihpiphone2()
        else:
            print("masukan anda negatif atau bukan angka")
        
def belihpiphone2():
    print("Nama Hp", Datahp[0])
    print("Harga hp", Datahp[1])
    print("Apakah nama dan harga sudah sesuai? (konfirmasi kepada penjual) (Y/N)")
    finalisasi = str(input(":"))
    if finalisasi == "Y":
        print("toko hp")
        print("Nama Hp", Datahp[0])
        print("Harga hp", Datahp[1])
        print("terima kasih telah menjual di sini")
        kasir()

    elif finalisasi == "N":
        i = 0
        while i == 0:
            print("""
            A. Ubah nama
            B. Ubah harga
            C. Batalkan penbelian
            """)
            masukan = str(input(":"))
            if masukan == "A":
                belihpiphone()
            elif masukan == "B":
                belihpiphone1()
            elif masukan == "C":
                i = 0
                while i == 0:
                    print("Apakah anda yakin untuk membatalkan (Y/N)")
                    batal = str(input(":"))
                    if batal == "Y":
                        Datahp.clear()
                        print("pembelian dibatalkan")
                        kasir()
                    elif batal == "N":
                        belihpiphone2()
                    else:
                        print("masukan salah")
            else:
                print("Masukan salah")
    else:
        print("masukan salah")
    
   


user_login()