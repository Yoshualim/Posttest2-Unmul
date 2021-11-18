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
Datahp = []

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
    print("List HP")
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
    print("Mau edit apa?")
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
            print("Inputan kamu salah")
            Edithp_Samsung1()
    else:
        print("Inputan kamu negatif")
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
        print("Nama berhasil diubah")
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
    print("Masukan Harga baru")
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
        print("Harga berhasil diubah")
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
    print("Masukan Harga baru")
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
        print("Nama dan harga berhasil di ubah")
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
    print("Mau edit apa?")
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
        print("Nama berhasil diubah")
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
    print("Masukan Harga baru")
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
        print("Harga berhasil diubah")
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
    print("Masukan Harga baru")
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
        print("Nama dan harga berhasil di ubah")
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
    print("Mau edit apa?")
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
        print("Nama berhasil diubah")
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
    print("Masukan Harga baru")
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
        print("Harga berhasil diubah")
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
    print("Masukan Harga baru")
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
        print("Nama dan harga berhasil di ubah")
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