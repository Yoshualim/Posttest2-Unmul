import time
import os

Daftarhp = {

    "Samsung" : {
        "SAMSUNG J2" : 1000000,
        "SAMSUNG J1 PRIME" : 2000000,
    },

    "Oppo" : {
        "OPPO A3S" : 500000,
        "OPPO X RENO" : 750000,
    },
    
    "Merk lain" : {
        "ADVAN C10" : 100000,
        "IPHONE X" : 100000000,
    }
}

Stokhp = {

    "Samsung" : {
        "SAMSUNG J2" : 3,
        "SAMSUNG J1 PRIME" : 2,
    },

    "Oppo" : {
        "OPPO A3S" : 4,
        "OPPO X RENO" : 1,
    },
    
    "Merk lain" : {
        "ADVAN C10" : 3,
        "IPHONE X" : 0,
    }

}

Spechp = {
    "Samsung" : {
         "SAMSUNG J1 PRIME" : {
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
        "OPPO A3S" : {
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

    "Merk lain" : {
        "IPHONE X" : {
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




Merkhp = ["Samsung", "Oppo", "Merk lain"]
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
        os.system('cls')
        print("Login Berhasil")
        main_admin()

    elif user == Userlogin["username"] and Pass == Userlogin["Password_Normal"]:
        os.system('cls')
        print("Login Berhasil")
        kasir()
        
    else:
        print("Username atau password anda salah, silakan isi kembali")
        os.system('cls')
        user_login()

def main_admin():
    
    print("Menu Admin")
    waktu = time.ctime()
    print(waktu)
    print("======================================")
    print("1. Lihat list Hp")
    print("2. Tambahkan Hp")
    print("3. Edit Hp")
    print("4. Hapus Hp ")
    print("5. Hapus jumlah keuntungan hari ini")
    print("6. Database spec hp")
    print("7. Stok hp")
    print("0. Keluar dari menu Admin")
    print ("======================================")
    Jumlahuntung = sum(Keuntungan["Total_keuntungan"])
    print ("==================================================================")
    print("Jumlah keuntungan yang diraih pada hari ini adalah Rp.", Jumlahuntung)
    print ("==================================================================")

    pilihan_menu = input("pilih menu :")
    
    if pilihan_menu == ("1"):
        os.system('cls')
        List_menuhp()
    elif pilihan_menu == ("2"):
        os.system('cls')
        Tambah_hp()
    elif pilihan_menu == ("3"):
        os.system('cls')
        Edit_hp()
    elif pilihan_menu == ("4"):
        os.system('cls')
        Hapus_hp()
    elif pilihan_menu == ("5"):
        os.system('cls')
        Hapus_Keuntungan()
    elif pilihan_menu == ("6"):
        os.system('cls')
        Editspechp()
    elif pilihan_menu == ("7"):
        os.system('cls')
        stokhp()
    elif pilihan_menu == ("0"):
        os.system('cls')
        kembalilogin()        
    else:
        os.system('cls')
        print("Anda salah input silakan coba kembali")
        kembali_menu()







def List_menuhp():
    print("List HP")
    print ("==========================================")
    for key, val in Daftarhp.items():
        for key2, val2 in val.items():
            print("%s : ""Rp."" %s" % (key2,val2))
    print ("==========================================")
    kembali_menu()

def Tambah_hp():
    print                ("=============================")  
    for merk in Merkhp:
        print(merk)      
    print("Kembali")
    Merk_hp = str.lower(input("Masukan merk HP (Ketik kembali untuk kembali kemenu admin) : "))
    print                ("=============================")

    if Merk_hp == "samsung":
        os.system('cls')
        Tambahhp_Samsung()
    elif Merk_hp == "oppo":
        os.system('cls')
        Tambahhp_Oppo()
    elif Merk_hp == "merk lain":
        os.system('cls')
        Tambahhp_merklain()
    elif Merk_hp == "kembali":
        os.system('cls')
        main_admin()
    else:
        os.system('cls')
        print("Inputan anda salah")
        Tambah_hp()

def Tambahhp_Samsung():
    Hp_Baru = str.upper(input("Masukan nama hp baru : "))
    if Hp_Baru == "":
        os.system('cls')
        print("Harap masukan inputan dengan benar")
        Tambahhp_Samsung()
    
    os.system('cls')
    i = 0
    while i == 0:
        print("Nama hp : ", Hp_Baru)
        print("Apakah nama sudah benar? (Y/N)")
        masukan = str.upper(input(":"))
        if masukan == "Y":
            Datahp.append(Hp_Baru)
            os.system('cls')
            Tambahhp_Samsung1() 
        elif masukan == "N":
            os.system('cls')
            Tambahhp_Samsung()
        else:
            os.system('cls')
            print("masukan salah")
    

def Tambahhp_Samsung1():
    try:
        Harga_hp = int(input("Masukan harga hp baru : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Samsung1()
    os.system('cls')
    if Harga_hp > 0:
        i = 0
        while i == 0:
            print("Harga hp : ", Harga_hp)
            print("Apakah harga sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp.append(Harga_hp)
                os.system('cls')
                Tambahhp_Samsung2() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_Samsung1()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Samsung1()

def Tambahhp_Samsung2():
    try:
        stok = int(input("Stok hp ada berapa? : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Samsung2() 
    os.system('cls')
    if stok > 0:
        i = 0
        while i == 0:
            print("Stok hp : ", stok)
            print("Apakah stok sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp.append(stok)
                os.system('cls')
                Tambahhp_Samsung3() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_Samsung2()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        os.system('cls')
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Samsung2()
    


def Tambahhp_Samsung3():
    i = 0
    while i == 0:
        
        print("Nama hp : ", Datahp[0]) 
        print("Harga hp : Rp. ", Datahp[1])
        print("Stok : ", Datahp[2])
        print("Apakah anda ingin menambahkan hp ini? (Y/N)")
        masukan = str.upper(input(":"))

        if masukan == "Y":
            os.system('cls')
            break
        elif masukan == "N":
            os.system('cls')
            i = 0
            while i == 0:

                print("""
                A. Ubah nama hp
                B. Ubah harga hp
                C. Ubah stok hp
                D. Batalkan isi hp baru
                """)
                opsi = str.upper(input(":"))

                if opsi == "A":
                    os.system('cls')
                    Tambahhp_Samsung4()
                elif opsi == "B":
                    os.system('cls')
                    Tambahhp_Samsung5()
                elif opsi == "C":
                    os.system('cls')
                    Tambahhp_Samsung6()
                elif opsi == "D":
                    os.system('cls')
                    Tambahhp_Samsung7()
                else:
                    os.system('cls')
                    print("masukan salah")
        else:
            os.system('cls')
            print("masukan salah")
        
    Daftarhp["Samsung"].update({Datahp[0] : Datahp[1]})
    Stokhp["Samsung"].update({Datahp[0] : Datahp[2]})
    Datahp.clear()
    print("Hp berhasil ditambahkan")
    input("Tekan enter untuk kembali ke menu admin")
    os.system('cls')
    main_admin()



def Tambahhp_Samsung4():
    Hp_Baru = str.upper(input("Masukan nama hp baru : "))
    if Hp_Baru == "":
        os.system('cls')
        print("Harap masukan inputan dengan benar")
        Tambahhp_Samsung4()
    os.system('cls')
    i = 0
    while i == 0:
        print("Nama hp : ", Hp_Baru)
        print("Apakah nama sudah benar? (Y/N)")
        masukan = str.upper(input(":"))
        if masukan == "Y":
            Datahp[0] = Hp_Baru
            os.system('cls')
            Tambahhp_Samsung3() 
        elif masukan == "N":
            os.system('cls')
            Tambahhp_Samsung4()
        else:
            os.system('cls')
            print("masukan salah")
    

def Tambahhp_Samsung5():
    try:
        Harga_hp = int(input("Masukan harga hp baru : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Samsung5()
    os.system('cls')
    if Harga_hp > 0:
        i = 0
        while i == 0:
            print("Harga hp : ", Harga_hp)
            print("Apakah harga sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp[1] = Harga_hp
                os.system('cls')
                Tambahhp_Samsung3() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_Samsung5()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        os.system('cls')
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Samsung5()

def Tambahhp_Samsung6():
    try:
        stok = int(input("Stok hp ada berapa? : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Samsung6() 
    if stok > 0:
        i = 0
        while i == 0:
            print("Stok hp : ", stok)
            print("Apakah stok sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp[2] = stok
                os.system('cls')
                Tambahhp_Samsung3() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_Samsung6()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        os.system('cls')
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Samsung6()


def Tambahhp_Samsung7():
    print("Apakah anda ingin batal isi hp ini? (Y/N)")
    masukan = str.upper(input(":"))
    if masukan == "Y":
        os.system('cls')
        Datahp.clear()

        i = 0
        while i == 0:
            
            print("Operasi berhasil dibatalkan")
            print("A. Kembali ke menu admin")
            print("B. Kembali ke menu tambah hp")
            opsi = str.upper(input(":"))
            if opsi == "A":
                os.system('cls')
                main_admin()
            elif opsi == "B":
                os.system('cls')
                Tambah_hp()
            else:
                os.system('cls')
                print("masukan salah")
    
    elif masukan == "N":
        os.system('cls')
        Tambahhp_Samsung3()

    else:
        os.system('cls')
        print("masukan salah")
        Tambahhp_Samsung7()


def Tambahhp_Oppo():
    Hp_Baru = str.upper(input("Masukan nama hp baru : "))
    if Hp_Baru == "":
        os.system('cls')
        print("Harap masukan inputan dengan benar")
        Tambahhp_Oppo()
    
    os.system('cls')
    i = 0
    while i == 0:
        print("Nama hp : ", Hp_Baru)
        print("Apakah nama sudah benar? (Y/N)")
        masukan = str.upper(input(":"))
        if masukan == "Y":
            Datahp.append(Hp_Baru)
            os.system('cls')
            Tambahhp_Oppo1() 
        elif masukan == "N":
            os.system('cls')
            Tambahhp_Oppo()
        else:
            os.system('cls')
            print("masukan salah")
    

def Tambahhp_Oppo1():
    try:
        Harga_hp = int(input("Masukan harga hp baru : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Oppo1()
    os.system('cls')
    if Harga_hp > 0:
        i = 0
        while i == 0:
            print("Harga hp : ", Harga_hp)
            print("Apakah harga sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp.append(Harga_hp)
                os.system('cls')
                Tambahhp_Oppo2() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_Oppo1()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Oppo1()

def Tambahhp_Oppo2():
    try:
        stok = int(input("Stok hp ada berapa? : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Oppo2() 
    os.system('cls')
    if stok > 0:
        i = 0
        while i == 0:
            print("Stok hp : ", stok)
            print("Apakah stok sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp.append(stok)
                os.system('cls')
                Tambahhp_Oppo3() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_Oppo2()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        os.system('cls')
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Oppo2()
    


def Tambahhp_Oppo3():
    i = 0
    while i == 0:
        
        print("Nama hp : ", Datahp[0]) 
        print("Harga hp : Rp. ", Datahp[1])
        print("Stok : ", Datahp[2])
        print("Apakah anda ingin menambahkan hp ini? (Y/N)")
        masukan = str.upper(input(":"))

        if masukan == "Y":
            os.system('cls')
            break
        elif masukan == "N":
            os.system('cls')
            i = 0
            while i == 0:

                print("""
                A. Ubah nama hp
                B. Ubah harga hp
                C. Ubah stok hp
                D. Batalkan isi hp baru
                """)
                opsi = str.upper(input(":"))

                if opsi == "A":
                    os.system('cls')
                    Tambahhp_Oppo4()
                elif opsi == "B":
                    os.system('cls')
                    Tambahhp_Oppo5()
                elif opsi == "C":
                    os.system('cls')
                    Tambahhp_Oppo6()
                elif opsi == "D":
                    os.system('cls')
                    Tambahhp_Oppo7()
                else:
                    os.system('cls')
                    print("masukan salah")
        else:
            os.system('cls')
            print("masukan salah")
        
    Daftarhp["Oppo"].update({Datahp[0] : Datahp[1]})
    Stokhp["Oppo"].update({Datahp[0] : Datahp[2]})
    Datahp.clear()
    print("Hp berhasil ditambahkan")
    input("Tekan enter untuk kembali ke menu admin")
    os.system('cls')
    main_admin()



def Tambahhp_Oppo4():
    Hp_Baru = str.upper(input("Masukan nama hp baru : "))
    if Hp_Baru == "":
        os.system('cls')
        print("Harap masukan inputan dengan benar")
        Tambahhp_Oppo4()
    os.system('cls')
    i = 0
    while i == 0:
        print("Nama hp : ", Hp_Baru)
        print("Apakah nama sudah benar? (Y/N)")
        masukan = str.upper(input(":"))
        if masukan == "Y":
            Datahp[0] = Hp_Baru
            os.system('cls')
            Tambahhp_Oppo3() 
        elif masukan == "N":
            os.system('cls')
            Tambahhp_Oppo4()
        else:
            os.system('cls')
            print("masukan salah")
    

def Tambahhp_Oppo5():
    try:
        Harga_hp = int(input("Masukan harga hp baru : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Oppo5()
    os.system('cls')
    if Harga_hp > 0:
        i = 0
        while i == 0:
            print("Harga hp : ", Harga_hp)
            print("Apakah harga sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp[1] = Harga_hp
                os.system('cls')
                Tambahhp_Oppo3() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_Oppo5()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        os.system('cls')
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Oppo5()

def Tambahhp_Oppo6():
    try:
        stok = int(input("Stok hp ada berapa? : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_Oppo6() 
    if stok > 0:
        i = 0
        while i == 0:
            print("Stok hp : ", stok)
            print("Apakah stok sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp[2] = stok
                os.system('cls')
                Tambahhp_Oppo3() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_Oppo6()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        os.system('cls')
        print("Inputan negatif silakan isi kembali")
        Tambahhp_Oppo6()


def Tambahhp_Oppo7():
    print("Apakah anda ingin batal isi hp ini? (Y/N)")
    masukan = str.upper(input(":"))
    if masukan == "Y":
        os.system('cls')
        Datahp.clear()

        i = 0
        while i == 0:
            
            print("Operasi berhasil dibatalkan")
            print("A. Kembali ke menu admin")
            print("B. Kembali ke menu tambah hp")
            opsi = str.upper(input(":"))
            if opsi == "A":
                os.system('cls')
                main_admin()
            elif opsi == "B":
                os.system('cls')
                Tambah_hp()
            else:
                os.system('cls')
                print("masukan salah")
    
    elif masukan == "N":
        os.system('cls')
        Tambahhp_Oppo3()

    else:
        os.system('cls')
        print("masukan salah")
        Tambahhp_Oppo7()

def Tambahhp_merklain():
    Hp_Baru = str.upper(input("Masukan nama hp baru : "))
    if Hp_Baru == "":
        os.system('cls')
        print("Harap masukan inputan dengan benar")
        Tambahhp_merklain()
    
    os.system('cls')
    i = 0
    while i == 0:
        print("Nama hp : ", Hp_Baru)
        print("Apakah nama sudah benar? (Y/N)")
        masukan = str.upper(input(":"))
        if masukan == "Y":
            Datahp.append(Hp_Baru)
            os.system('cls')
            Tambahhp_merklain1() 
        elif masukan == "N":
            os.system('cls')
            Tambahhp_merklain()
        else:
            os.system('cls')
            print("masukan salah")
    

def Tambahhp_merklain1():
    try:
        Harga_hp = int(input("Masukan harga hp baru : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_merklain1()
    os.system('cls')
    if Harga_hp > 0:
        i = 0
        while i == 0:
            print("Harga hp : ", Harga_hp)
            print("Apakah harga sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp.append(Harga_hp)
                os.system('cls')
                Tambahhp_merklain2() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_merklain1()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        print("Inputan negatif silakan isi kembali")
        Tambahhp_merklain1()

def Tambahhp_merklain2():
    try:
        stok = int(input("Stok hp ada berapa? : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_merklain2() 
    os.system('cls')
    if stok > 0:
        i = 0
        while i == 0:
            print("Stok hp : ", stok)
            print("Apakah stok sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp.append(stok)
                os.system('cls')
                Tambahhp_merklain3() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_merklain2()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        os.system('cls')
        print("Inputan negatif silakan isi kembali")
        Tambahhp_merklain2()
    


def Tambahhp_merklain3():
    i = 0
    while i == 0:
        
        print("Nama hp : ", Datahp[0]) 
        print("Harga hp : Rp. ", Datahp[1])
        print("Stok : ", Datahp[2])
        print("Apakah anda ingin menambahkan hp ini? (Y/N)")
        masukan = str.upper(input(":"))

        if masukan == "Y":
            os.system('cls')
            break
        elif masukan == "N":
            os.system('cls')
            i = 0
            while i == 0:

                print("""
                A. Ubah nama hp
                B. Ubah harga hp
                C. Ubah stok hp
                D. Batalkan isi hp baru
                """)
                opsi = str.upper(input(":"))

                if opsi == "A":
                    os.system('cls')
                    Tambahhp_merklain4()
                elif opsi == "B":
                    os.system('cls')
                    Tambahhp_merklain5()
                elif opsi == "C":
                    os.system('cls')
                    Tambahhp_merklain6()
                elif opsi == "D":
                    os.system('cls')
                    Tambahhp_merklain8()
                else:
                    os.system('cls')
                    print("masukan salah")
        else:
            os.system('cls')
            print("masukan salah")
        
    Daftarhp["Oppo"].update({Datahp[0] : Datahp[1]})
    Stokhp["Oppo"].update({Datahp[0] : Datahp[2]})
    Datahp.clear()
    print("Hp berhasil ditambahkan")
    input("Tekan enter untuk kembali ke menu admin")
    os.system('cls')
    main_admin()



def Tambahhp_merklain4():
    Hp_Baru = str.upper(input("Masukan nama hp baru : "))
    if Hp_Baru == "":
        os.system('cls')
        print("Harap masukan inputan dengan benar")
        Tambahhp_merklain4()
    os.system('cls')
    i = 0
    while i == 0:
        print("Nama hp : ", Hp_Baru)
        print("Apakah nama sudah benar? (Y/N)")
        masukan = str.upper(input(":"))
        if masukan == "Y":
            Datahp[0] = Hp_Baru
            os.system('cls')
            Tambahhp_merklain3() 
        elif masukan == "N":
            os.system('cls')
            Tambahhp_merklain4()
        else:
            os.system('cls')
            print("masukan salah")
    

def Tambahhp_merklain5():
    try:
        Harga_hp = int(input("Masukan harga hp baru : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_merklain5()
    os.system('cls')
    if Harga_hp > 0:
        i = 0
        while i == 0:
            print("Harga hp : ", Harga_hp)
            print("Apakah harga sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp[1] = Harga_hp
                os.system('cls')
                Tambahhp_merklain3() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_merklain5()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        os.system('cls')
        print("Inputan negatif silakan isi kembali")
        Tambahhp_merklain5()

def Tambahhp_merklain6():
    try:
        stok = int(input("Stok hp ada berapa? : "))
    except ValueError:
        os.system('cls')
        print("Inputan harus berupa angka bukan huruf")
        Tambahhp_merklain6() 
    if stok > 0:
        i = 0
        while i == 0:
            print("Stok hp : ", stok)
            print("Apakah stok sudah benar? (Y/N)")
            masukan = str.upper(input(":"))
            if masukan == "Y":
                Datahp[2] = stok
                os.system('cls')
                Tambahhp_merklain3() 
            elif masukan == "N":
                os.system('cls')
                Tambahhp_merklain6()
            else:
                os.system('cls')
                print("masukan salah")
    else:
        os.system('cls')
        print("Inputan negatif silakan isi kembali")
        Tambahhp_merklain6()


def Tambahhp_merklain8():
    print("Apakah anda ingin batal isi hp ini? (Y/N)")
    masukan = str.upper(input(":"))
    if masukan == "Y":
        os.system('cls')
        Datahp.clear()

        i = 0
        while i == 0:
            
            print("Operasi berhasil dibatalkan")
            print("A. Kembali ke menu admin")
            print("B. Kembali ke menu tambah hp")
            opsi = str.upper(input(":"))
            if opsi == "A":
                os.system('cls')
                main_admin()
            elif opsi == "B":
                os.system('cls')
                Tambah_hp()
            else:
                os.system('cls')
                print("masukan salah")
    
    elif masukan == "N":
        os.system('cls')
        Tambahhp_merklain3()

    else:
        os.system('cls')
        print("masukan salah")
        Tambahhp_merklain8()


def Edit_hp():
    print("===============================================================")
    print("===============================================================")
    for merk in Merkhp:
        print(merk)
    print("Semua hp")
    print("=========")
    print("Kembali")
    print("Pilih merk hp yang akan diedit (Ketik kembali untuk kembali kemenu admin)")
    masukan = str.lower(input(":"))
    print("===============================================================")

    if masukan == "samsung":
        os.system('cls')
        Edithp_Samsung()
    elif masukan == "oppo":
        os.system('cls')
        Edithp_Oppo()
    elif masukan == "merk lain":
        os.system('cls')
        Edithp_merklain()
    elif masukan == "semua hp":
        os.system('cls')
        Edithp_Semuahp()
    elif masukan == "kembali":
        os.system('cls')
        main_admin()
    else:
        os.system('cls')
        print("masukan salah")
        Edit_hp()

    
def Edithp_Samsung():
    for key in Daftarhp["Samsung"].keys():
        print("%s" % (key))

    print("====================")
    print("Kembali")
    print("Masukan nama hp yang akan diedit (Ketik kembali untuk kembali ke menu sebelumnya) ")
    ubah = str.upper(input(":"))
    if ubah in Daftarhp["Samsung"].keys():
        Datahp.append(ubah)
        os.system('cls')
        Edithp_Samsung1()
    elif ubah == "KEMBALI":
        os.system('cls')
        Edit_hp()
    else:
        os.system('cls')
        print("Masukan inputan yang benar")
        Edithp_Samsung()


def Edithp_Samsung1():
    print("Nama hp : ",Datahp[0])
    print("Harga hp : Rp. ",Daftarhp["Samsung"][Datahp[0]])
    print("Menu edit")
    print("""
        1. Nama Hp
        2. Harga Hp
        3. Edit Nama dan Harga hp
        4. Kembali ke pilih merk hp
        5. Kembali ke menu admin
        """)
    try:
        masukan = int(input(":"))
    except ValueError:
        os.system('cls')
        print("Masukan salah")
        Edithp_Samsung1()
    
    if masukan > 0:
        if masukan == 1:
            os.system('cls')
            Editnama_Samsung()
        elif masukan == 2:
            os.system('cls')
            Editharga_Samsung()
        elif masukan == 3:
            os.system('cls')
            Editnamaharga_Samsung()
        elif masukan == 4:
            Datahp.clear()
            os.system('cls')
            Edit_hp()
        elif masukan == 5:
            Datahp.clear()
            os.system('cls')
            main_admin()
        else:
            os.system('cls')
            print("Inputan kamu salah, silakan coba kembali")
            Edithp_Samsung1()
    else:
        os.system('cls')
        print("Inputan kamu negatif, silakan coba kembali")
        Edithp_Samsung1()

def Editnama_Samsung():
    print("Nama hp lama : ",Datahp[0])
    print("Masukan Nama hp baru (Ketik kembali untuk kembali ke menu sebelumnya) ")
    namahp = str.upper(input(":"))
    if namahp == "":
        os.system('cls')
        print("Mohon isi dengan benar")
        Editnama_Samsung()
    elif namahp == "KEMBALI":
        os.system('cls')
        Edithp_Samsung1()

    
    i = 0
    while i == 0:
        print("Nama hp baru : ",namahp)
        print("Apakah nama sudah benar? (Y/N)")
        nama = str.upper(input(":"))
        if nama == "Y":
            os.system('cls')
            break
        elif nama == "N":
            os.system('cls')
            Editnama_Samsung()
        else:
            os.system('cls')
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            os.system('cls')
            break
        elif Konfirmasi == "N":
            os.system('cls')
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit nama
                D. Kembali ke menu edit
                """)
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    os.system('cls')
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    os.system('cls')
                    Edit_hp()
                elif masukan == "C":
                    os.system('cls')
                    Editnama_Samsung()
                elif masukan == "D":
                    os.system('cls')
                    Edithp_Samsung1()
                else:
                    os.system('cls')
                    print("inputan salah")
        else:
            os.system('cls')
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
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            os.system('cls')
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            os.system('cls')
            main_admin()
        else:
            os.system('cls')
            print("Input salah")


def Editharga_Samsung():
    print("Harga hp lama : Rp. ",Daftarhp["Samsung"][Datahp[0]])
    print("Masukan Harga hp baru (Ketik 000 untuk kembali ke menu sebelumnya)")
    try:
        hargahp = int(input(":"))
    except ValueError:
        os.system('cls')
        print("Masukan angka bukan huruf")
        Editharga_Samsung()
    
    if hargahp > 0:
        print("Harga hp baru : Rp. ",hargahp)
        i = 0
        while i == 0:
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str.upper(input(":"))
            if nama == "Y":
                os.system('cls')
                break
            elif nama == "N":
                os.system('cls')
                Editharga_Samsung()
            else:
                os.system('cls')
                print("Harap input jawaban yang benar")
    elif hargahp == 000:
        os.system('cls')
        Edithp_Samsung1()
    else:
        os.system('cls')
        print("masukan berbentuk negatif")
        Editharga_Samsung()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            os.system('cls')
            break
        elif Konfirmasi == "N":
            os.system('cls')
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit harga
                D. Kembali ke menu edit
                """)
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    os.system('cls')
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    os.system('cls')
                    Edit_hp()
                elif masukan == "C":
                    os.system('cls')
                    Editharga_Samsung()
                elif masukan == "D":
                    os.system('cls')
                    Edithp_Samsung1()
                else:
                    os.system('cls')
                    print("inputan salah")
        else:
            os.system('cls')
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
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            os.system('cls')
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            os.system('cls')
            main_admin()
        else:
            os.system('cls')
            print("Input salah")

def Editnamaharga_Samsung():
    print("Nama hp lama : ",Datahp[0])
    print("Masukan Nama hp baru (Ketik kembali untuk kembali ke menu sebelumnya)")
    namahp = str.upper(input(":"))
    if namahp == "":
        os.system('cls')
        print("Mohon isi dengan benar")
        Editnamaharga_Samsung()
    elif namahp == "KEMBALI":
        os.system('cls')
        Edithp_Samsung1()
    os.system('cls')
    i = 0
    while i == 0:
        print("Nama hp baru : ",namahp)
        print("Apakah nama sudah benar? (Y/N)")
        nama = str.upper(input(":"))
        if nama == "Y":
            os.system('cls')
            break
        elif nama == "N":
            os.system('cls')
            Editnamaharga_Samsung()
        else:
            os.system('cls')
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            os.system('cls')
            break
        elif Konfirmasi == "N":
            os.system('cls')
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit nama
                D. Kembali ke menu edit
                """)
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    os.system('cls')
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    os.system('cls')
                    Edit_hp()
                elif masukan == "C":
                    os.system('cls')
                    Editnamaharga_Samsung()
                elif masukan == "D":
                    os.system('cls')
                    Edithp_Samsung1()
                else:
                    os.system('cls')
                    print("inputan salah")
        else:
            os.system('cls')
            print("inputan salah")
    Datahp.append(namahp)
    Editnamaharga_Samsung1()
            
def Editnamaharga_Samsung1():
    print("Harga hp lama : Rp. ",Daftarhp["Samsung"][Datahp[0]])
    print("Masukan Harga hp baru (Ketik 000 untuk kembali ke menu sebelumnya)")
    try:
        hargahp = int(input(":"))
    except ValueError:
        os.system('cls')
        print("Masukan angka bukan huruf")
        Editnamaharga_Samsung1()
    os.system('cls')
    if hargahp > 0:
        i = 0
        while i == 0:
            print("Harga hp baru : Rp. ",hargahp)
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str.upper(input(":"))
            if nama == "Y":
                os.system('cls')
                break
            elif nama == "N":
                os.system('cls')
                Editnamaharga_Samsung1()
            else:
                os.system('cls')
                print("Harap input jawaban yang benar")
    elif hargahp == 000:
        Datahp.clear()
        os.system('cls')
        Editnamaharga_Samsung()
    else:
        os.system('cls')
        print("masukan berbentuk negatif")
        Editnamaharga_Samsung1()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            os.system('cls')
            break
        elif Konfirmasi == "N":
            os.system('cls')
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit harga
                D. Kembali ke menu edit
                """)
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    os.system('cls')
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    os.system('cls')
                    Edit_hp()
                elif masukan == "C":
                    os.system('cls')
                    Editnamaharga_Samsung1()
                elif masukan == "D":
                    os.system('cls')
                    del Datahp[1]
                    Edithp_Samsung1()
                else:
                    os.system('cls')
                    print("inputan salah")
        else:
            os.system('cls')
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
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            os.system('cls')
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            os.system('cls')
            main_admin()
        else:
            os.system('cls')
            print("Input salah")
    
def Edithp_Oppo():
    for key in Daftarhp["Oppo"].keys():
        print("%s" % (key))

    print("====================")
    print("Kembali")
    print("Masukan nama hp yang akan diedit (Ketik kembali untuk kembali ke menu sebelumnya) ")
    ubah = str.upper(input(":"))
    if ubah in Daftarhp["Oppo"].keys():
        Datahp.append(ubah)
        os.system('cls')
        Edithp_Oppo1()
    elif ubah == "KEMBALI":
        os.system('cls')
        Edit_hp()
    else:
        os.system('cls')
        print("Masukan inputan yang benar")
        Edithp_Oppo()


def Edithp_Oppo1():
    print("Nama hp : ",Datahp[0])
    print("Harga hp : Rp. ",Daftarhp["Oppo"][Datahp[0]])
    print("Menu edit")
    print("""
        1. Nama Hp
        2. Harga Hp
        3. Edit Nama dan Harga hp
        4. Kembali ke pilih merk hp
        5. Kembali ke menu admin
        """)
    try:
        masukan = int(input(":"))
    except ValueError:
        os.system('cls')
        print("Masukan salah")
        Edithp_Oppo1()
    
    if masukan > 0:
        if masukan == 1:
            os.system('cls')
            Editnama_Oppo()
        elif masukan == 2:
            os.system('cls')
            Editharga_Oppo()
        elif masukan == 3:
            os.system('cls')
            Editnamaharga_Oppo()
        elif masukan == 4:
            Datahp.clear()
            os.system('cls')
            Edit_hp()
        elif masukan == 5:
            Datahp.clear()
            os.system('cls')
            main_admin()
        else:
            os.system('cls')
            print("Inputan kamu salah, silakan coba kembali")
            Edithp_Oppo1()
    else:
        os.system('cls')
        print("Inputan kamu negatif, silakan coba kembali")
        Edithp_Oppo1()

def Editnama_Oppo():
    print("Nama hp lama : ",Datahp[0])
    print("Masukan Nama hp baru (Ketik kembali untuk kembali ke menu sebelumnya) ")
    namahp = str.upper(input(":"))
    if namahp == "":
        os.system('cls')
        print("Mohon isi dengan benar")
        Editnama_Oppo()
    elif namahp == "KEMBALI":
        os.system('cls')
        Edithp_Oppo1()

    
    i = 0
    while i == 0:
        print("Nama hp baru : ",namahp)
        print("Apakah nama sudah benar? (Y/N)")
        nama = str.upper(input(":"))
        if nama == "Y":
            os.system('cls')
            break
        elif nama == "N":
            os.system('cls')
            Editnama_Oppo()
        else:
            os.system('cls')
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            os.system('cls')
            break
        elif Konfirmasi == "N":
            os.system('cls')
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit nama
                D. Kembali ke menu edit
                """)
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    os.system('cls')
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    os.system('cls')
                    Edit_hp()
                elif masukan == "C":
                    os.system('cls')
                    Editnama_Oppo()
                elif masukan == "D":
                    os.system('cls')
                    Edithp_Oppo1()
                else:
                    os.system('cls')
                    print("inputan salah")
        else:
            os.system('cls')
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
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            os.system('cls')
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            os.system('cls')
            main_admin()
        else:
            os.system('cls')
            print("Input salah")


def Editharga_Oppo():
    print("Harga hp lama : Rp. ",Daftarhp["Oppo"][Datahp[0]])
    print("Masukan Harga hp baru (Ketik 000 untuk kembali ke menu sebelumnya)")
    try:
        hargahp = int(input(":"))
    except ValueError:
        os.system('cls')
        print("Masukan angka bukan huruf")
        Editharga_Oppo()
    
    if hargahp > 0:
        print("Harga hp baru : Rp. ",hargahp)
        i = 0
        while i == 0:
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str.upper(input(":"))
            if nama == "Y":
                os.system('cls')
                break
            elif nama == "N":
                os.system('cls')
                Editharga_Oppo()
            else:
                os.system('cls')
                print("Harap input jawaban yang benar")
    elif hargahp == 000:
        os.system('cls')
        Edithp_Oppo1()
    else:
        os.system('cls')
        print("masukan berbentuk negatif")
        Editharga_Oppo()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            os.system('cls')
            break
        elif Konfirmasi == "N":
            os.system('cls')
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit harga
                D. Kembali ke menu edit
                """)
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    os.system('cls')
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    os.system('cls')
                    Edit_hp()
                elif masukan == "C":
                    os.system('cls')
                    Editharga_Oppo()
                elif masukan == "D":
                    os.system('cls')
                    Edithp_Oppo1()
                else:
                    os.system('cls')
                    print("inputan salah")
        else:
            os.system('cls')
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
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            os.system('cls')
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            os.system('cls')
            main_admin()
        else:
            os.system('cls')
            print("Input salah")

def Editnamaharga_Oppo():
    print("Nama hp lama : ",Datahp[0])
    print("Masukan Nama hp baru (Ketik kembali untuk kembali ke menu sebelumnya)")
    namahp = str.upper(input(":"))
    if namahp == "":
        os.system('cls')
        print("Mohon isi dengan benar")
        Editnamaharga_Oppo()
    elif namahp == "KEMBALI":
        os.system('cls')
        Edithp_Oppo1()
    os.system('cls')
    i = 0
    while i == 0:
        print("Nama hp baru : ",namahp)
        print("Apakah nama sudah benar? (Y/N)")
        nama = str.upper(input(":"))
        if nama == "Y":
            os.system('cls')
            break
        elif nama == "N":
            os.system('cls')
            Editnamaharga_Oppo()
        else:
            os.system('cls')
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            os.system('cls')
            break
        elif Konfirmasi == "N":
            os.system('cls')
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit nama
                D. Kembali ke menu edit
                """)
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    os.system('cls')
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    os.system('cls')
                    Edit_hp()
                elif masukan == "C":
                    os.system('cls')
                    Editnamaharga_Oppo()
                elif masukan == "D":
                    os.system('cls')
                    Edithp_Oppo1()
                else:
                    os.system('cls')
                    print("inputan salah")
        else:
            os.system('cls')
            print("inputan salah")
    Datahp.append(namahp)
    Editnamaharga_Oppo1()
            
def Editnamaharga_Oppo1():
    print("Harga hp lama : Rp. ",Daftarhp["Oppo"][Datahp[0]])
    print("Masukan Harga hp baru (Ketik 000 untuk kembali ke menu sebelumnya)")
    try:
        hargahp = int(input(":"))
    except ValueError:
        os.system('cls')
        print("Masukan angka bukan huruf")
        Editnamaharga_Oppo1()
    os.system('cls')
    if hargahp > 0:
        i = 0
        while i == 0:
            print("Harga hp baru : Rp. ",hargahp)
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str.upper(input(":"))
            if nama == "Y":
                os.system('cls')
                break
            elif nama == "N":
                os.system('cls')
                Editnamaharga_Oppo1()
            else:
                os.system('cls')
                print("Harap input jawaban yang benar")
    elif hargahp == 000:
        Datahp.clear()
        os.system('cls')
        Editnamaharga_Oppo()
    else:
        os.system('cls')
        print("masukan berbentuk negatif")
        Editnamaharga_Oppo1()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            os.system('cls')
            break
        elif Konfirmasi == "N":
            os.system('cls')
            i = 0
            while i == 0:
                print("""
                Apakah anda ingin kembali ke
                A. Menu Admin
                B. Menu Edit
                C. Kembali ke awal edit harga
                D. Kembali ke menu edit
                """)
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    os.system('cls')
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    os.system('cls')
                    Edit_hp()
                elif masukan == "C":
                    os.system('cls')
                    Editnamaharga_Oppo1()
                elif masukan == "D":
                    os.system('cls')
                    del Datahp[1]
                    Edithp_Oppo1()
                else:
                    os.system('cls')
                    print("inputan salah")
        else:
            os.system('cls')
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
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            os.system('cls')
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            os.system('cls')
            main_admin()
        else:
            os.system('cls')
            print("Input salah")



def Edithp_merklain():
    for key, val in Daftarhp["Merk lain"].items():
        print("%s = %s" % (key,val))

    print("=============")
    print("Kembali")
    print("Masukan nama hp yang akan diedit (Ketik kembali untuk kembali ke menu sebelumnya) ")
    ubah = str.upper(input(":"))
    if ubah in Daftarhp["Merk lain"].keys():
        Datahp.append(ubah)
        Edithp_merklain1()
    elif ubah == "KEMBALI":
        Edit_hp()
    else:
        print("Masukan inputan yang benar")
        Edithp_merklain()


def Edithp_merklain1():
    print("Nama hp : ",Datahp[0])
    print("Harga hp : ",Daftarhp["Merk lain"][Datahp[0]])
    print("Menu edit")
    print("""
        1. Nama Hp
        2. Harga Hp
        3. Edit Nama dan Harga hp
        4. Kembali ke pilih merk hp
        5. Kembali ke menu admin
        """)
    try:
        masukan = int(input(":"))
    except ValueError:
        print("Masukan salah")
        Edithp_merklain1()
    
    if masukan > 0:
        if masukan == 1:
            Editnama_merklain()
        elif masukan == 2:
            Editharga_merklain()
        elif masukan == 3:
            Editnamaharga_merklain()
        elif masukan == 4:
            Datahp.clear()
            Edit_hp()
        elif masukan == 5:
            Datahp.clear()
            main_admin()
        else:
            print("Inputan kamu salah")
            Edithp_merklain1()
    else:
        print("Inputan kamu negatif")
        Edithp_merklain1()

def Editnama_merklain():
    print("Nama hp lama : ",Datahp[0])
    print("Masukan Nama hp baru (Ketik kembali untuk kembali ke menu sebelumnya)")
    namahp = str.upper(input(":"))
    if namahp == "":
        print("Mohon isi dengan benar")
        Editnama_merklain()   
    elif namahp == "KEMBALI":
        Edithp_merklain1()
    print("Nama hp baru : ",namahp)
    i = 0
    while i == 0:
        print("Apakah nama sudah benar? (Y/N)")
        nama = str.upper(input(":"))
        if nama == "Y":
            break
        elif nama == "N":
            Editnama_merklain()
        else:
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
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
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnama_merklain()
                elif masukan == "D":
                    Edithp_merklain1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    
    Daftarhp["Merk lain"][namahp] = Daftarhp["Merk lain"].pop(Datahp[0])
    i = 0
    while i == 0:
        print("Nama hp berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")


def Editharga_merklain():
    print("Harga hp lama : Rp. ",Daftarhp["Merk lain"][Datahp[0]])
    print("Masukan Harga hp baru (Ketik 000 untuk kembali ke menu sebelumnya)")
    try:
        hargahp = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Editharga_merklain()
    
    if hargahp > 0:
        print("Harga hp baru : Rp. ",hargahp)
        i = 0
        while i == 0:
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str.upper(input(":"))
            if nama == "Y":
                break
            elif nama == "N":
                Editharga_merklain()
            else:
                print("Harap input jawaban yang benar")
    elif hargahp == 000:
        Edithp_merklain1()
    else:
        print("masukan berbentuk negatif")
        Editharga_merklain()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
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
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editharga_merklain()
                elif masukan == "D":
                    Edithp_merklain1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    
    Daftarhp["Merk lain"].update({Datahp[0] : hargahp})
    i = 0
    while i == 0:
        print("Harga hp berhasil diubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Datahp.clear()
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")

def Editnamaharga_merklain():
    print("Nama hp lama : ",Datahp[0])
    print("Masukan Nama hp baru (Ketik kembali untuk kembali ke menu sebelumnya)")
    namahp = str.upper(input(":"))
    if namahp == "":
        print("Mohon isi dengan benar")
        Editnamaharga_merklain()
    elif namahp == "KEMBALI":
        Edithp_merklain1()
    print("Nama hp baru : ",namahp)
    i = 0
    while i == 0:
        print("Apakah nama sudah benar? (Y/N)")
        nama = str.upper(input(":"))
        if nama == "Y":
            break
        elif nama == "N":
            Editnamaharga_merklain()
        else:
            print("Harap input jawaban yang benar")
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah nama hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
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
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnamaharga_merklain()
                elif masukan == "D":
                    Edithp_merklain1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    Datahp.append(namahp)
    Editnamaharga_merklain1()
            
def Editnamaharga_merklain1():
    print("Harga hp lama : Rp. ",Daftarhp["Merk lain"][Datahp[0]])
    print("Masukan Harga hp baru (Ketik 000 untuk kembali ke menu sebelumnya)")
    try:
        hargahp = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Editnamaharga_merklain1()
    
    if hargahp > 0:
        print("Harga hp baru : Rp. ",hargahp)
        i = 0
        while i == 0:
            print("Apakah Harga sudah benar? (Y/N)")
            nama = str.upper(input(":"))
            if nama == "Y":
                break
            elif nama == "N":
                Editnamaharga_merklain1()
            else:
                print("Harap input jawaban yang benar")
    elif hargahp == 000:
        Datahp.clear()
        Editnamaharga_merklain()
    else:
        print("masukan berbentuk negatif")
        Editnamaharga_merklain1()
    i = 0
    while i == 0:
        print("apakah anda benar-benar ingin mengubah harga hp ini? (Y/N)")
        Konfirmasi = str.upper(input(":"))
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
                masukan = str.upper(input(""))

                if masukan == "A":
                    Datahp.clear()
                    main_admin()
                elif masukan == "B":
                    Datahp.clear()
                    Edit_hp()
                elif masukan == "C":
                    Editnamaharga_merklain1()
                elif masukan == "D":
                    del Datahp[1]
                    Edithp_merklain1()
                else:
                    print("inputan salah")
        else:
            print("inputan salah")
    
    Daftarhp["Merk lain"][Datahp[1]] = Daftarhp["Merk lain"].pop(Datahp[0])
    Daftarhp["Merk lain"].update({Datahp[1] : hargahp})
    i = 0
    while i == 0:
        print("Nama dan harga hp berhasil di ubah")
        print("""
        Apakah anda ingin kembali ke:
        A. Edit hp
        B. Menu admin
        """)
        masukan1 = str.upper(input(":"))

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

    print("==========")
    print("Kembali")
    print("Masukan nama hp yang akan diedit (Ketik kembali untuk kembali ke menu sebelumnya) ")
    ubah = str.upper(input(":"))
    if ubah in Daftarhp["Samsung"].keys():
        Datahp.append(ubah)
        Edithp_Samsung1()
    elif ubah in Daftarhp["Oppo"].keys():
        Datahp.append(ubah)
        Edithp_Oppo1()
    elif ubah in Daftarhp["Merk lain"].keys():
        Datahp.append(ubah)
        Edithp_merklain1()
    elif ubah == "KEMBALI":
        Edit_hp()
    else:
        print("Masukan inputan yang benar")
        Edithp_Semuahp()

   

def Hapus_hp():
    print("=================================================================")
    for key, val in Daftarhp.items():
        for key2, val2 in val.items():
            print("%s : %s" % (key2,val2))
    print("=================================================================")
    print("Kembali")
    print("=================================================================")
    print("Pilih Hp yang akan dihapus (Ketik kembali untuk kembali ke menu sebelumnya)")
    print("=================================================================")

    masukan = str.upper(input(":"))

    if masukan in Daftarhp["Samsung"].keys():
        print("Nama hp : ",masukan)
        print("Harga hp : Rp. ",Daftarhp["Samsung"][masukan])
        i = 0
        while i == 0:
            print("Apakah anda ingin menghapus ini? ini tidak bisa dikembalikan! (Y/N)")
            konfirmasi = str.upper(input(":"))
            if konfirmasi == "Y":
                del Daftarhp["Samsung"][masukan]
                del Stokhp["Samsung"][masukan]
                print("Data berhasil dihapus!")
                input("Tekan enter untuk kembali ke menu admin")
                main_admin()
            elif konfirmasi == "N":
                i = 0
                while i == 0:
                    print("Operasi dibatalkan, apakah anda ingin kembali ke menu hapus hp atau kembali ke menu admin?")
                    print("A. menu hapus hp")
                    print("B. menu admin")
                    konfirm = str.upper(input(":"))
                    if konfirm == "A":
                        Hapus_hp()
                    elif konfirm == "B":
                        main_admin()
                    else:
                        print("Inputan salah")
            else:
                print("Inputan salah")

    elif masukan in Daftarhp["Oppo"].keys():
        print("Nama hp : ",masukan)
        print("Harga hp : Rp. ",Daftarhp["Oppo"][masukan])
        i = 0
        while i == 0:
            print("Apakah anda ingin menghapus ini? ini tidak bisa dikembalikan! (Y/N)")
            konfirmasi = str.upper(input(":"))
            if konfirmasi == "Y":
                del Daftarhp["Oppo"][masukan]
                del Stokhp["Oppo"][masukan]
                print("Data berhasil dihapus!")
                input("Tekan enter untuk kembali ke menu admin")
                main_admin()
            elif konfirmasi == "N":
                i = 0
                while i == 0:
                    print("Operasi dibatalkan, apakah anda ingin kembali ke menu hapus hp atau kembali ke menu admin?")
                    print("A. menu hapus hp")
                    print("B. menu admin")
                    konfirm = str.upper(input(":"))
                    if konfirm == "A":
                        Hapus_hp()
                    elif konfirm == "B":
                        main_admin()
                    else:
                        print("Inputan salah")
            else:
                print("Inputan salah")
    
    elif masukan in Daftarhp["Merk lain"].keys():
        print("Nama hp : ",masukan)
        print("Harga hp : Rp. ",Daftarhp["Merk lain"][masukan])
        i = 0
        while i == 0:
            print("Apakah anda ingin menghapus ini? ini tidak bisa dikembalikan! (Y/N)")
            konfirmasi = str.upper(input(":"))
            if konfirmasi == "Y":
                del Daftarhp["Merk lain"][masukan]
                del Stokhp["Merk lain"][masukan]
                print("Data berhasil dihapus!")
                input("Tekan enter untuk kembali ke menu admin")
                main_admin()
            elif konfirmasi == "N":
                i = 0
                while i == 0:
                    print("Operasi dibatalkan, apakah anda ingin kembali ke menu hapus hp atau kembali ke menu admin?")
                    print("A. menu hapus hp")
                    print("B. menu admin")
                    konfirm = str.upper(input(":"))
                    if konfirm == "A":
                        Hapus_hp()
                    elif konfirm == "B":
                        main_admin()
                    else:
                        print("Inputan salah")
            else:
                print("Inputan salah")
    
    elif masukan == "KEMBALI":
        main_admin()
    
    else:
        print("Inputan salah")
        Hapus_hp()



def Editspechp():

    print("menu utama edit spec hp")
    print("A. Tampilkan seluruh database spec hp yang tersimpan")
    print("B. Tambah spec hp baru")
    print("C. Edit spechp pada database")
    print("D. Kembali ke menu admin")
    print("Masukan input")
    masukan = str.upper(input(":"))

    if masukan == "A":
        Tampilspechp()
    elif masukan == "B":
        Tambahspechp()
    elif masukan == "C":
        Editspechpada()
    elif masukan == "D":
        main_admin()
    else:
        print("Masukan inputan yang benar")
        Editspechp()


def Tampilspechp():
    for key, val in Spechp["Samsung"].items():
        print(key, val)
    
    for key, val in Spechp["Oppo"].items():
        print(key, val)

    for key, val in Spechp["Merk lain"].items():
        print(key, val)

    input("Tekan enter untuk kembali ke menu spechp")
    Editspechp()


def Tambahspechp():
    for key in Spechp.keys():
        print(key)

    print("========")
    print("Kembali")
    print("pilih merk hp (Ketik kembali untuk kembali ke menu sebelumnya)")
    masukan = str.lower(input(":"))

    if masukan == "samsung":
        Tambahspechp_Samsung()
    elif masukan == "oppo":
        Tambahspechp_Oppo()
    elif masukan == "merk lain":
        Tambahspechp_merklain()
    elif masukan == "kembali":
        Editspechp()
    else:
        print("Masukan salah")
        Tambahspechp()

def Tambahspechp_Samsung():
    print("Nama hp? (Ketik kembali untuk kembali ke menu sebelumnya)")
    Nama = str.upper(input(":"))
    if Nama == "":
        print("harap masukan input")
        Tambahspechp_Samsung()
    elif Nama == "KEMBALI":
        Tambahspechp()

    i = 0
    while i == 0:   
        print("Nama hp : ",Nama)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Nama)
            Tambahspechp_Samsung1()
        elif Masukan == "N":
            Tambahspechp_Samsung()
        else:
            print("Masukan salah")
            
def Tambahspechp_Samsung1():   
    print("Tahun keluar? (Ketik 000 untuk membatalkan isi spechp)")
    try:
        Tahun_Keluar = int(input(":"))
    except ValueError:
        print("Masukan harus berbentuk angka")
        Tambahspechp_Samsung1()
    if Tahun_Keluar > 0:
        i = 0
        while i == 0:   
            print("Tahun keluar : ",Tahun_Keluar)
            print("Apakah Tahun Keluar sudah benar? (Y/N)")
            Masukan = str.upper(input(":"))
            if Masukan == "Y":
                Datahp.append(Tahun_Keluar)
                Tambahspechp_Samsung2()
            elif Masukan == "N":
                Tambahspechp_Samsung1()
            else:
                print("Masukan salah")
    elif Tahun_Keluar == 000:

        i = 0
        while i == 0:

            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung1()
            else:
                print("Masukan salah")

    else:
        print("Masukan bernilai negatif")
        Tambahspechp_Samsung1()

def Tambahspechp_Samsung2():
    print("Versi OS? (Contoh : Android 11, IOS 9)")
    print("ketik batal untuk membatalkan isi spec hp")
    Os = str.upper(input(":"))
    if Os == "":
        print("harap masukan input")
        Tambahspechp_Samsung2()
    elif Os == "BATAL":

        i = 0
        while i == 0:

            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung2()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Versi Os : ",Os)
        print("Apakah Versi OS sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Os)
            Tambahspechp_Samsung3()
        elif Masukan == "N":
            Tambahspechp_Samsung2()
        else:
            print("Masukan salah")


    
def Tambahspechp_Samsung3():
    print("Chipset? (Contoh Snapdragon 870, Helio G80)")
    print("ketik batal untuk membatalkan isi spec hp")
    Chipset = str.upper(input(":"))
    if Chipset == "":
        print("harap masukan input")
        Tambahspechp_Samsung3()
    elif Chipset == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung3()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Chipset : ",Chipset)
        print("Apakah nama Chipset sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Chipset)
            Tambahspechp_Samsung4()
        elif Masukan == "N":
            Tambahspechp_Samsung3()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung4():
    print("CPU? (Contoh Octa-core, Quad-core)")
    print("ketik batal untuk membatalkan isi spec hp")
    Cpu = str.upper(input(":"))
    if Cpu == "":
        print("harap masukan input")
        Tambahspechp_Samsung4()
    
    elif Cpu == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung4()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("CPU : ",Cpu)
        print("Apakah nama CPU sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Cpu)
            Tambahspechp_Samsung5()
        elif Masukan == "N":
            Tambahspechp_Samsung4()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung5():
    print("GPU? (Contoh Mali, Adreno)")
    print("ketik batal untuk membatalkan isi spec hp")
    Gpu = str.upper(input(":"))
    if Gpu == "":
        print("harap masukan input")
        Tambahspechp_Samsung5()
    
    elif Gpu == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung5()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("GPU : ",Gpu)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Gpu)
            Tambahspechp_Samsung6()
        elif Masukan == "N":
            Tambahspechp_Samsung5()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung6():
    print("Display? (Contoh Amoled, IPS PLS)")
    print("ketik batal untuk membatalkan isi spec hp")
    Display = str.upper(input(":"))
    if Display == "":
        print("harap masukan input")
        Tambahspechp_Samsung6()
    
    elif Display == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung6()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Display : ",Display)
        print("Apakah nama Display sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Display)
            Tambahspechp_Samsung7()
        elif Masukan == "N":
            Tambahspechp_Samsung6()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung7():
    print("Total Memori Internal? (Contoh 8 GB, 64 GB)")
    print("ketik batal untuk membatalkan isi spec hp")
    Memori = str.upper(input(":"))
    if Memori == "":
        print("harap masukan input")
        Tambahspechp_Samsung7()
    
    elif Memori == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung7()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Total memori internal : ",Memori)
        print("Apakah Total memori sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Memori)
            Tambahspechp_Samsung8()
        elif Masukan == "N":
            Tambahspechp_Samsung7()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung8():
    print("Total Ram? (Contoh 2 GB, 8 GB)")
    print("ketik batal untuk membatalkan isi spec hp")
    Ram = str.upper(input(":"))
    if Ram == "":
        print("harap masukan input")
        Tambahspechp_Samsung8()
    
    elif Ram == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung8()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Total Ram : ",Ram)
        print("Apakah Total Ram sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Ram)
            Tambahspechp_Samsung9()
        elif Masukan == "N":
            Tambahspechp_Samsung8()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung9():
    print("Kamera? (Contoh 20 MP, 30 MP)")
    print("ketik batal untuk membatalkan isi spec hp")
    Kamera = str.upper(input(":"))
    if Kamera == "":
        print("harap masukan input")
        Tambahspechp_Samsung9()
    
    elif Kamera == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung9()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Kamera : ",Kamera)
        print("Apakah Kamera sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Kamera)
            Tambahspechp_Samsung10()
        elif Masukan == "N":
            Tambahspechp_Samsung9()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung10():
    print("Jaringan? (Contoh 2G/3G/4G/5G)")
    print("ketik batal untuk membatalkan isi spec hp")
    Jaringan = str(input(":"))
    if Jaringan == "":
        print("harap masukan input")
        Tambahspechp_Samsung10()
    
    elif Jaringan == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung10()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Jaringan : ",Jaringan)
        print("Apakah nama Jaringan sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Jaringan)
            Tambahspechp_Samsung11()
        elif Masukan == "N":
            Tambahspechp_Samsung10()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung11():
    print("Kapasitas Baterai? (Contoh 2000 MAH/Baterai tanam, 4500 MAH/Baterai lepas)")
    print("ketik batal untuk membatalkan isi spec hp")
    Baterai = str.upper(input(":"))
    if Baterai == "":
        print("harap masukan input")
        Tambahspechp_Samsung11()
    
    elif Baterai == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Samsung11()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Kapasitas baterai : ",Baterai)
        print("Apakah Kapasitas Baterai sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Baterai)
            Tambahspechp_Samsung12()
        elif Masukan == "N":
            Tambahspechp_Samsung11()
        else:
            print("Masukan salah")

def Tambahspechp_Samsung12():
    Spechp["Samsung"][Datahp[0]] = {"Nama" : Datahp[0], "Tahun Keluar" : Datahp[1], "OS" : Datahp[2], "Chipset" : Datahp[3], "CPU" : Datahp[4], "GPU" : Datahp[5], "Display" : Datahp[6], "Memori Internal" : Datahp[7], "RAM" : Datahp[8], "Kamera" : Datahp[9], "Jaringan" : Datahp[10], "Kapasitas Baterai" : Datahp[11]}
    Datahp.clear()
    print("Data hp berhasil ditambah")
    input("Tekan enter untuk kembali ke menu edit spec hp")
    Editspechp()

def Tambahspechp_Oppo():
    print("Nama hp? (Ketik kembali untuk kembali ke menu sebelumnya)")
    Nama = str.upper(input(":"))
    if Nama == "":
        print("harap masukan input")
        Tambahspechp_Oppo()
    elif Nama == "KEMBALI":
        Tambahspechp()

    i = 0
    while i == 0:   
        print("Nama hp : ",Nama)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Nama)
            Tambahspechp_Oppo1()
        elif Masukan == "N":
            Tambahspechp_Oppo()
        else:
            print("Masukan salah")
            
def Tambahspechp_Oppo1():   
    print("Tahun keluar? (Ketik 000 untuk membatalkan isi spechp)")
    try:
        Tahun_Keluar = int(input(":"))
    except ValueError:
        print("Masukan harus berbentuk angka")
        Tambahspechp_Oppo1()
    if Tahun_Keluar > 0:
        i = 0
        while i == 0:   
            print("Tahun keluar : ",Tahun_Keluar)
            print("Apakah Tahun Keluar sudah benar? (Y/N)")
            Masukan = str.upper(input(":"))
            if Masukan == "Y":
                Datahp.append(Tahun_Keluar)
                Tambahspechp_Oppo2()
            elif Masukan == "N":
                Tambahspechp_Oppo1()
            else:
                print("Masukan salah")
    elif Tahun_Keluar == 000:

        i = 0
        while i == 0:

            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo1()
            else:
                print("Masukan salah")

    else:
        print("Masukan bernilai negatif")
        Tambahspechp_Oppo1()

def Tambahspechp_Oppo2():
    print("Versi OS? (Contoh : Android 11, IOS 9)")
    print("ketik batal untuk membatalkan isi spec hp")
    Os = str.upper(input(":"))
    if Os == "":
        print("harap masukan input")
        Tambahspechp_Oppo2()
    elif Os == "BATAL":

        i = 0
        while i == 0:

            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo2()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Versi Os : ",Os)
        print("Apakah Versi OS sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Os)
            Tambahspechp_Oppo3()
        elif Masukan == "N":
            Tambahspechp_Oppo2()
        else:
            print("Masukan salah")


    
def Tambahspechp_Oppo3():
    print("Chipset? (Contoh Snapdragon 870, Helio G80)")
    print("ketik batal untuk membatalkan isi spec hp")
    Chipset = str.upper(input(":"))
    if Chipset == "":
        print("harap masukan input")
        Tambahspechp_Oppo3()
    elif Chipset == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo3()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Chipset : ",Chipset)
        print("Apakah nama Chipset sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Chipset)
            Tambahspechp_Oppo4()
        elif Masukan == "N":
            Tambahspechp_Oppo3()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo4():
    print("CPU? (Contoh Octa-core, Quad-core)")
    print("ketik batal untuk membatalkan isi spec hp")
    Cpu = str.upper(input(":"))
    if Cpu == "":
        print("harap masukan input")
        Tambahspechp_Oppo4()
    
    elif Cpu == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo4()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("CPU : ",Cpu)
        print("Apakah nama CPU sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Cpu)
            Tambahspechp_Oppo5()
        elif Masukan == "N":
            Tambahspechp_Oppo4()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo5():
    print("GPU? (Contoh Mali, Adreno)")
    print("ketik batal untuk membatalkan isi spec hp")
    Gpu = str.upper(input(":"))
    if Gpu == "":
        print("harap masukan input")
        Tambahspechp_Oppo5()
    
    elif Gpu == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo5()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("GPU : ",Gpu)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Gpu)
            Tambahspechp_Oppo6()
        elif Masukan == "N":
            Tambahspechp_Oppo5()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo6():
    print("Display? (Contoh Amoled, IPS PLS)")
    print("ketik batal untuk membatalkan isi spec hp")
    Display = str.upper(input(":"))
    if Display == "":
        print("harap masukan input")
        Tambahspechp_Oppo6()
    
    elif Display == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo6()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Display : ",Display)
        print("Apakah nama Display sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Display)
            Tambahspechp_Oppo7()
        elif Masukan == "N":
            Tambahspechp_Oppo6()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo7():
    print("Total Memori Internal? (Contoh 8 GB, 64 GB)")
    print("ketik batal untuk membatalkan isi spec hp")
    Memori = str.upper(input(":"))
    if Memori == "":
        print("harap masukan input")
        Tambahspechp_Oppo7()
    
    elif Memori == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo7()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Total memori internal : ",Memori)
        print("Apakah Total memori sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Memori)
            Tambahspechp_Oppo8()
        elif Masukan == "N":
            Tambahspechp_Oppo7()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo8():
    print("Total Ram? (Contoh 2 GB, 8 GB)")
    print("ketik batal untuk membatalkan isi spec hp")
    Ram = str.upper(input(":"))
    if Ram == "":
        print("harap masukan input")
        Tambahspechp_Oppo8()
    
    elif Ram == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo8()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Total Ram : ",Ram)
        print("Apakah Total Ram sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Ram)
            Tambahspechp_Oppo9()
        elif Masukan == "N":
            Tambahspechp_Oppo8()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo9():
    print("Kamera? (Contoh 20 MP, 30 MP)")
    print("ketik batal untuk membatalkan isi spec hp")
    Kamera = str.upper(input(":"))
    if Kamera == "":
        print("harap masukan input")
        Tambahspechp_Oppo9()
    
    elif Kamera == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo9()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Kamera : ",Kamera)
        print("Apakah Kamera sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Kamera)
            Tambahspechp_Oppo10()
        elif Masukan == "N":
            Tambahspechp_Oppo9()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo10():
    print("Jaringan? (Contoh 2G/3G/4G/5G)")
    print("ketik batal untuk membatalkan isi spec hp")
    Jaringan = str(input(":"))
    if Jaringan == "":
        print("harap masukan input")
        Tambahspechp_Oppo10()
    
    elif Jaringan == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo10()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Jaringan : ",Jaringan)
        print("Apakah nama Jaringan sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Jaringan)
            Tambahspechp_Oppo11()
        elif Masukan == "N":
            Tambahspechp_Oppo10()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo11():
    print("Kapasitas Baterai? (Contoh 2000 MAH/Baterai tanam, 4500 MAH/Baterai lepas)")
    print("ketik batal untuk membatalkan isi spec hp")
    Baterai = str.upper(input(":"))
    if Baterai == "":
        print("harap masukan input")
        Tambahspechp_Oppo11()
    
    elif Baterai == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_Oppo11()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Kapasitas baterai : ",Baterai)
        print("Apakah Kapasitas Baterai sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Baterai)
            Tambahspechp_Oppo12()
        elif Masukan == "N":
            Tambahspechp_Oppo11()
        else:
            print("Masukan salah")

def Tambahspechp_Oppo12():
    Spechp["Oppo"][Datahp[0]] = {"Nama" : Datahp[0], "Tahun Keluar" : Datahp[1], "OS" : Datahp[2], "Chipset" : Datahp[3], "CPU" : Datahp[4], "GPU" : Datahp[5], "Display" : Datahp[6], "Memori Internal" : Datahp[7], "RAM" : Datahp[8], "Kamera" : Datahp[9], "Jaringan" : Datahp[10], "Kapasitas Baterai" : Datahp[11]}
    Datahp.clear()
    print("Data hp berhasil ditambah")
    input("Tekan enter untuk kembali ke menu edit spec hp")
    Editspechp()


def Tambahspechp_merklain():
    print("Nama hp? (Ketik kembali untuk kembali ke menu sebelumnya)")
    Nama = str.upper(input(":"))
    if Nama == "":
        print("harap masukan input")
        Tambahspechp_merklain()
    elif Nama == "KEMBALI":
        Tambahspechp()

    i = 0
    while i == 0:   
        print("Nama hp : ",Nama)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Nama)
            Tambahspechp_merklain1()
        elif Masukan == "N":
            Tambahspechp_merklain()
        else:
            print("Masukan salah")
            
def Tambahspechp_merklain1():   
    print("Tahun keluar? (Ketik 000 untuk membatalkan isi spechp)")
    try:
        Tahun_Keluar = int(input(":"))
    except ValueError:
        print("Masukan harus berbentuk angka")
        Tambahspechp_merklain1()
    if Tahun_Keluar > 0:
        i = 0
        while i == 0:   
            print("Tahun keluar : ",Tahun_Keluar)
            print("Apakah Tahun Keluar sudah benar? (Y/N)")
            Masukan = str.upper(input(":"))
            if Masukan == "Y":
                Datahp.append(Tahun_Keluar)
                Tambahspechp_merklain2()
            elif Masukan == "N":
                Tambahspechp_merklain1()
            else:
                print("Masukan salah")
    elif Tahun_Keluar == 000:

        i = 0
        while i == 0:

            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain1()
            else:
                print("Masukan salah")

    else:
        print("Masukan bernilai negatif")
        Tambahspechp_merklain1()

def Tambahspechp_merklain2():
    print("Versi OS? (Contoh : Android 11, IOS 9)")
    print("ketik batal untuk membatalkan isi spec hp")
    Os = str.upper(input(":"))
    if Os == "":
        print("harap masukan input")
        Tambahspechp_merklain2()
    elif Os == "BATAL":

        i = 0
        while i == 0:

            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain2()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Versi Os : ",Os)
        print("Apakah Versi OS sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Os)
            Tambahspechp_merklain3()
        elif Masukan == "N":
            Tambahspechp_merklain2()
        else:
            print("Masukan salah")


    
def Tambahspechp_merklain3():
    print("Chipset? (Contoh Snapdragon 870, Helio G80)")
    print("ketik batal untuk membatalkan isi spec hp")
    Chipset = str.upper(input(":"))
    if Chipset == "":
        print("harap masukan input")
        Tambahspechp_merklain3()
    elif Chipset == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain3()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Chipset : ",Chipset)
        print("Apakah nama Chipset sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Chipset)
            Tambahspechp_merklain4()
        elif Masukan == "N":
            Tambahspechp_merklain3()
        else:
            print("Masukan salah")

def Tambahspechp_merklain4():
    print("CPU? (Contoh Octa-core, Quad-core)")
    print("ketik batal untuk membatalkan isi spec hp")
    Cpu = str.upper(input(":"))
    if Cpu == "":
        print("harap masukan input")
        Tambahspechp_merklain4()
    
    elif Cpu == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain4()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("CPU : ",Cpu)
        print("Apakah nama CPU sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Cpu)
            Tambahspechp_merklain5()
        elif Masukan == "N":
            Tambahspechp_merklain4()
        else:
            print("Masukan salah")

def Tambahspechp_merklain5():
    print("GPU? (Contoh Mali, Adreno)")
    print("ketik batal untuk membatalkan isi spec hp")
    Gpu = str.upper(input(":"))
    if Gpu == "":
        print("harap masukan input")
        Tambahspechp_merklain5()
    
    elif Gpu == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain5()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("GPU : ",Gpu)
        print("Apakah nama sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Gpu)
            Tambahspechp_merklain6()
        elif Masukan == "N":
            Tambahspechp_merklain5()
        else:
            print("Masukan salah")

def Tambahspechp_merklain6():
    print("Display? (Contoh Amoled, IPS PLS)")
    print("ketik batal untuk membatalkan isi spec hp")
    Display = str.upper(input(":"))
    if Display == "":
        print("harap masukan input")
        Tambahspechp_merklain6()
    
    elif Display == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain6()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Display : ",Display)
        print("Apakah nama Display sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Display)
            Tambahspechp_merklain7()
        elif Masukan == "N":
            Tambahspechp_merklain6()
        else:
            print("Masukan salah")

def Tambahspechp_merklain7():
    print("Total Memori Internal? (Contoh 8 GB, 64 GB)")
    print("ketik batal untuk membatalkan isi spec hp")
    Memori = str.upper(input(":"))
    if Memori == "":
        print("harap masukan input")
        Tambahspechp_merklain7()
    
    elif Memori == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain7()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Total memori internal : ",Memori)
        print("Apakah Total memori sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Memori)
            Tambahspechp_merklain8()
        elif Masukan == "N":
            Tambahspechp_merklain7()
        else:
            print("Masukan salah")

def Tambahspechp_merklain8():
    print("Total Ram? (Contoh 2 GB, 8 GB)")
    print("ketik batal untuk membatalkan isi spec hp")
    Ram = str.upper(input(":"))
    if Ram == "":
        print("harap masukan input")
        Tambahspechp_merklain8()
    
    elif Ram == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain8()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Total Ram : ",Ram)
        print("Apakah Total Ram sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Ram)
            Tambahspechp_merklain9()
        elif Masukan == "N":
            Tambahspechp_merklain8()
        else:
            print("Masukan salah")

def Tambahspechp_merklain9():
    print("Kamera? (Contoh 20 MP, 30 MP)")
    print("ketik batal untuk membatalkan isi spec hp")
    Kamera = str.upper(input(":"))
    if Kamera == "":
        print("harap masukan input")
        Tambahspechp_merklain9()
    
    elif Kamera == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain9()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Kamera : ",Kamera)
        print("Apakah Kamera sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Kamera)
            Tambahspechp_merklain10()
        elif Masukan == "N":
            Tambahspechp_merklain9()
        else:
            print("Masukan salah")

def Tambahspechp_merklain10():
    print("Jaringan? (Contoh 2G/3G/4G/5G)")
    print("ketik batal untuk membatalkan isi spec hp")
    Jaringan = str(input(":"))
    if Jaringan == "":
        print("harap masukan input")
        Tambahspechp_merklain10()
    
    elif Jaringan == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain10()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Jaringan : ",Jaringan)
        print("Apakah nama Jaringan sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Jaringan)
            Tambahspechp_merklain11()
        elif Masukan == "N":
            Tambahspechp_merklain10()
        else:
            print("Masukan salah")

def Tambahspechp_merklain11():
    print("Kapasitas Baterai? (Contoh 2000 MAH/Baterai tanam, 4500 MAH/Baterai lepas)")
    print("ketik batal untuk membatalkan isi spec hp")
    Baterai = str.upper(input(":"))
    if Baterai == "":
        print("harap masukan input")
        Tambahspechp_merklain11()
    
    elif Baterai == "BATAL":

        i = 0
        while i == 0:
            
            print("Apakah anda ingin batalkan isi spec hp ini? (Y/N)")
            opsi = str.upper(input(":"))
            if opsi == "Y":
                Datahp.clear()
                print("Operasi berhasil dibatalkan")
                input("Tekan enter untuk kembali ke menu edit spechp")
                Editspechp()
            elif opsi == "N":
                Tambahspechp_merklain11()
            else:
                print("Masukan salah")

    i = 0
    while i == 0:   
        print("Kapasitas baterai : ",Baterai)
        print("Apakah Kapasitas Baterai sudah benar? (Y/N)")
        Masukan = str.upper(input(":"))
        if Masukan == "Y":
            Datahp.append(Baterai)
            Tambahspechp_merklain12()
        elif Masukan == "N":
            Tambahspechp_merklain11()
        else:
            print("Masukan salah")

def Tambahspechp_merklain12():
    Spechp["Merk lain"][Datahp[0]] = {"Nama" : Datahp[0], "Tahun Keluar" : Datahp[1], "OS" : Datahp[2], "Chipset" : Datahp[3], "CPU" : Datahp[4], "GPU" : Datahp[5], "Display" : Datahp[6], "Memori Internal" : Datahp[7], "RAM" : Datahp[8], "Kamera" : Datahp[9], "Jaringan" : Datahp[10], "Kapasitas Baterai" : Datahp[11]}
    Datahp.clear()
    print("Data hp berhasil ditambah")
    input("Tekan enter untuk kembali ke menu edit spec hp")
    Editspechp()

def Editspechpada():
    for key in Spechp.keys():
        print("list merk hp")
        print(key)
        print("=======")
        print("Kembali")
        print("Pilih merk hp (ketik kembali untuk kembali ke menu edit spec hp)")
        masukan = str.lower(input(":"))

        if masukan == "samsung":
            for key in Spechp["Samsung"].keys():
                print(key)
                print("Pilih hp yang akan di edit")
                print("ketik kembali untuk balik ke menu sebelumnya")
                i = 0
                while i == 0:
                    masukan1 = str.upper(input(":"))
                    if masukan1 in Spechp["Samsung"]:
                        Datahp.append(masukan1)
                        Editspechpsamsung()
                    elif masukan1 == "KEMBALI":
                        Editspechpada()
                    else:
                        print("Masukan salah")
        
        elif masukan == "oppo":
            for key in Spechp["Oppo"].keys():
                print(key)
                print("Pilih hp yang akan di edit")
                print("ketik kembali untuk balik ke menu sebelumnya")
                i = 0
                while i == 0:
                    masukan1 = str.upper(input(":"))
                    if masukan1 in Spechp["Oppo"]:
                        Datahp.append(masukan1)
                        Editspechpoppo()
                    elif masukan1 == "KEMBALI":
                        Editspechpada()
                    else:
                        print("Masukan salah")

        elif masukan == "merk lain":
            for key in Spechp["Merk lain"].keys():
                print(key)
                print("Pilih hp yang akan di edit")
                print("ketik kembali untuk balik ke menu sebelumnya")
                i = 0
                while i == 0:
                    masukan1 = str.upper(input(":"))
                    if masukan1 in Spechp["Merk lain"]:
                        Datahp.append(masukan1)
                        Editspechpmerklain()
                    elif masukan1 == "KEMBALI":
                        Editspechpada()
                    else:
                        print("Masukan salah")
        
        elif masukan == "kembali":
            Editspechp()

        else:
            print("Inputan salah")
            Editspechpada()


def Editspechpsamsung():

    print("Menu Edit spec hp")
    print("A. Edit spec hp ")
    print("B. Kembali ke menu edit")
    print("C. Kembali ke menu admin")
    masukan = str.upper(input(":"))

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
        M. Kembali ke menu edit
        """)
        print("pilih huruf yang mau di edit ")
        i = 0
        while i == 0:
            ubah = str.upper(input(":"))

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
                Editspechpsamsung()
            else:
                print("Mohon masukan input dengan benar")

    elif masukan == "B":
        Datahp.clear()
        Editspechp()
    
    elif masukan == "C":
        Datahp.clear()
        main_admin()
    
    else:
        print("Masukan salah")
        Editspechpsamsung()
            
               
def Namaspecsamsung():
    print("Masukan nama baru")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    nama = str.upper(input(":"))
    if nama == "":
        print("masukan nama yang benar")
        Namaspecsamsung()
    elif nama == "KEMBALI":
        Editspechpsamsung()
    print("Nama : ",nama)

    i = 0
    while i == 0:

        print("Apakah sudah benar namanya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Namaspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit nama
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
    Spechp["Samsung"][nama] = Daftarhp["Samsung"].pop(Datahp[0])
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
    
        print("""
        Apakah anda ingin kembali ke:
        A. Edit spec
        B. Menu admin
        """)
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Editspechpsamsung()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")




def Tahunspecsamsung():
    print("Masukan nama baru")
    print("Ketik 000 untuk kembali ke menu sebelumnya")
    try:
        Tahun = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Tahunspecsamsung()
    if Tahun > 0:
        i = 0
        while i == 0:
            print("Tahun : ",Tahun)
            print("Apakah sudah benar tahunnya? (Y/N)")
            Konfirmasi = str.upper(input(":"))
            if Konfirmasi == "Y":
                break
            elif Konfirmasi == "N":
                Tahunspecsamsung()
            else:
                print("Inputan salah")
    
    elif Tahun == 000:
        Editspechpsamsung()

        i = 0
        while i == 0:

            print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
            finalisasi = str.upper(input(":"))
            if finalisasi == "Y":
                break
            elif finalisasi == "N":
                print("""
                A. Kembali ke edit tahun
                B. Kembali ke menu edit
                C. Kembali ke menu admin
                """)
                masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Osspecsamsung():
    print("Masukan nama OS baru (Contoh : Android 11, IOS 9)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Os = str.upper(input(":"))
    if Os == "":
        print("masukan nama yang benar")
        Osspecsamsung()
    elif Os == "KEMBALI":
        Editspechpsamsung()
    print("Os : ",Os)


    i = 0
    while i == 0:

        print("Apakah sudah benar nama Os nya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Osspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit OS
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Chipsetspecsamsung():
    print("Masukan nama chipset baru (Contoh Snapdragon 870, Helio G80)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    chipset = str.upper(input(":"))
    if chipset == "":
        print("masukan nama yang benar")
        Chipsetspecsamsung()
    elif chipset == "KEMBALI":
        Editspechpsamsung()
    print("Chipset : ",chipset)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama chipsetnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Chipsetspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit chipset
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Cpuspecsamsung():
    print("Masukan nama CPU baru (Contoh Octa-core, Quad-core)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Cpu = str.upper(input(":"))
    if Cpu == "":
        print("masukan nama yang benar")
        Cpuspecsamsung()
    elif Cpu == "KEMBALI":
        Editspechpsamsung()
    print("CPU : ",Cpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama CPUnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Cpuspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit cpu
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Gpuspecsamsung():
    print("Masukan nama Gpu baru (Contoh Mali, Adreno)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Gpu = str.upper(input(":"))
    if Gpu == "":
        print("masukan nama yang benar")
        Gpuspecsamsung()
    elif Gpu == "KEMBALI":
        Editspechpsamsung()
    print("GPU : ",Gpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama GPUnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Gpuspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit gpu
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Displayspecsamsung():
    print("Masukan nama tipe Display baru (Contoh Amoled, IPS PLS)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Display = str.upper(input(":"))
    if Display == "":
        print("masukan nama yang benar")
        Displayspecsamsung()
    elif Display == "KEMBALI":
        Editspechpsamsung()
    print("Display : ",Display)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama Displaynya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Displayspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit display
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")



def Memorispecsamsung():
    print("Masukan jumlah memori hp baru (Contoh 8 GB, 64 GB)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Memori = str.upper(input(":"))
    if Memori == "":
        print("masukan nama yang benar")
        Memorispecsamsung()
    elif Memori == "KEMBALI":
        Editspechpsamsung()
    print("Memori Internal : ",Memori)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas memorinya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Memorispecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit memori
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Ramspecsamsung():
    print("Masukan jumlah RAM baru (Contoh 2 GB, 8 GB)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Ram = str.upper(input(":"))
    if Ram == "":
        print("masukan nama yang benar")
        Ramspecsamsung()
    elif Ram == "KEMBALI":
        Editspechpsamsung()
    print("Total RAM : ",Ram)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas RAMnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Ramspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit ram
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Kameraspecsamsung():
    print("Masukan total MP Kamera baru (Contoh 20 MP, 30 MP)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Kamera = str.upper(input(":"))
    if Kamera == "":
        print("masukan nama yang benar")
        Kameraspecsamsung()
    elif Kamera == "KEMBALI":
        Editspechpsamsung()
    print("Kamera : ",Kamera)

    i = 0
    while i == 0:

        print("Apakah sudah benar MP kameranya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Kameraspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit kamera
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Jaringanspecsamsung():
    print("Masukan Support Jaringan baru (Contoh 2G/3G/4G/5G)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Jaringan = str.upper(input(":"))
    if Jaringan == "":
        print("masukan nama yang benar")
        Jaringanspecsamsung()
    elif Jaringan == "KEMBALI":
        Editspechpsamsung()
    print("Jaringan : ",Jaringan)

    i = 0
    while i == 0:

        print("Apakah sudah benar Jaringannya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Jaringanspecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit jaringan
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpsamsung()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Bateraispecsamsung():
    print("Masukan jumlah kapasitas baterai baru (Contoh 2000 MAH/Baterai tanam, 4500 MAH/Baterai lepas)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Baterai = str.upper(input(":"))
    if Baterai == "":
        print("masukan nama yang benar")
        Bateraispecsamsung()
    elif Baterai == "KEMBALI":
        Editspechpsamsung()
    print("Kapasitas Baterai : ",Baterai)

    i = 0
    while i == 0:

        print("Apakah sudah benar jumlah Kapasitas Baterainya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Bateraispecsamsung()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit baterai
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

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
    masukan = str.upper(input(":"))

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
        M. Kembali ke menu edit
        """)
        print("pilih huruf yang mau di edit ")
        i = 0
        while i == 0:
            ubah = str.upper(input(":"))

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
                Editspechpoppo()
            else:
                print("Mohon masukan input dengan benar")

    elif masukan == "B":
        Datahp.clear()
        Editspechp()
    
    elif masukan == "C":
        Datahp.clear()
        main_admin()
    
    else:
        print("Masukan salah")
        Editspechpoppo()
            
               
def Namaspecoppo():
    print("Masukan nama baru")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    nama = str.upper(input(":"))
    if nama == "":
        print("masukan nama yang benar")
        Namaspecoppo()
    elif nama == "KEMBALI":
        Editspechpoppo()
    print("Nama : ",nama)

    i = 0
    while i == 0:

        print("Apakah sudah benar namanya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Namaspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit nama
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
    Spechp["Oppo"][nama] = Daftarhp["Oppo"].pop(Datahp[0])
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
    
        print("""
        Apakah anda ingin kembali ke:
        A. Edit spec
        B. Menu admin
        """)
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Editspechpoppo()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")




def Tahunspecoppo():
    print("Masukan nama baru")
    print("Ketik 000 untuk kembali ke menu sebelumnya")
    try:
        Tahun = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Tahunspecoppo()
    if Tahun > 0:
        i = 0
        while i == 0:
            print("Tahun : ",Tahun)
            print("Apakah sudah benar tahunnya? (Y/N)")
            Konfirmasi = str.upper(input(":"))
            if Konfirmasi == "Y":
                break
            elif Konfirmasi == "N":
                Tahunspecoppo()
            else:
                print("Inputan salah")
    
    elif Tahun == 000:
        Editspechpoppo()

        i = 0
        while i == 0:

            print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
            finalisasi = str.upper(input(":"))
            if finalisasi == "Y":
                break
            elif finalisasi == "N":
                print("""
                A. Kembali ke edit tahun
                B. Kembali ke menu edit
                C. Kembali ke menu admin
                """)
                masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Osspecoppo():
    print("Masukan nama OS baru (Contoh : Android 11, IOS 9)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Os = str.upper(input(":"))
    if Os == "":
        print("masukan nama yang benar")
        Osspecoppo()
    elif Os == "KEMBALI":
        Editspechpoppo()
    print("Os : ",Os)


    i = 0
    while i == 0:

        print("Apakah sudah benar nama Os nya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Osspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit OS
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Chipsetspecoppo():
    print("Masukan nama chipset baru (Contoh Snapdragon 870, Helio G80)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    chipset = str.upper(input(":"))
    if chipset == "":
        print("masukan nama yang benar")
        Chipsetspecoppo()
    elif chipset == "KEMBALI":
        Editspechpoppo()
    print("Chipset : ",chipset)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama chipsetnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Chipsetspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit chipset
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Cpuspecoppo():
    print("Masukan nama CPU baru (Contoh Octa-core, Quad-core)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Cpu = str.upper(input(":"))
    if Cpu == "":
        print("masukan nama yang benar")
        Cpuspecoppo()
    elif Cpu == "KEMBALI":
        Editspechpoppo()
    print("CPU : ",Cpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama CPUnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Cpuspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit cpu
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Gpuspecoppo():
    print("Masukan nama Gpu baru (Contoh Mali, Adreno)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Gpu = str.upper(input(":"))
    if Gpu == "":
        print("masukan nama yang benar")
        Gpuspecoppo()
    elif Gpu == "KEMBALI":
        Editspechpoppo()
    print("GPU : ",Gpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama GPUnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Gpuspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit gpu
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Displayspecoppo():
    print("Masukan nama tipe Display baru (Contoh Amoled, IPS PLS)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Display = str.upper(input(":"))
    if Display == "":
        print("masukan nama yang benar")
        Displayspecoppo()
    elif Display == "KEMBALI":
        Editspechpoppo()
    print("Display : ",Display)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama Displaynya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Displayspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit display
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")



def Memorispecoppo():
    print("Masukan jumlah memori hp baru (Contoh 8 GB, 64 GB)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Memori = str.upper(input(":"))
    if Memori == "":
        print("masukan nama yang benar")
        Memorispecoppo()
    elif Memori == "KEMBALI":
        Editspechpoppo()
    print("Memori Internal : ",Memori)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas memorinya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Memorispecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit memori
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Ramspecoppo():
    print("Masukan jumlah RAM baru (Contoh 2 GB, 8 GB)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Ram = str.upper(input(":"))
    if Ram == "":
        print("masukan nama yang benar")
        Ramspecoppo()
    elif Ram == "KEMBALI":
        Editspechpoppo()
    print("Total RAM : ",Ram)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas RAMnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Ramspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit ram
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Kameraspecoppo():
    print("Masukan total MP Kamera baru (Contoh 20 MP, 30 MP)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Kamera = str.upper(input(":"))
    if Kamera == "":
        print("masukan nama yang benar")
        Kameraspecoppo()
    elif Kamera == "KEMBALI":
        Editspechpoppo()
    print("Kamera : ",Kamera)

    i = 0
    while i == 0:

        print("Apakah sudah benar MP kameranya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Kameraspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit kamera
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Jaringanspecoppo():
    print("Masukan Support Jaringan baru (Contoh 2G/3G/4G/5G)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Jaringan = str.upper(input(":"))
    if Jaringan == "":
        print("masukan nama yang benar")
        Jaringanspecoppo()
    elif Jaringan == "KEMBALI":
        Editspechpoppo()
    print("Jaringan : ",Jaringan)

    i = 0
    while i == 0:

        print("Apakah sudah benar Jaringannya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Jaringanspecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit jaringan
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Bateraispecoppo():
    print("Masukan jumlah kapasitas baterai baru (Contoh 2000 MAH/Baterai tanam, 4500 MAH/Baterai lepas)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Baterai = str.upper(input(":"))
    if Baterai == "":
        print("masukan nama yang benar")
        Bateraispecoppo()
    elif Baterai == "KEMBALI":
        Editspechpoppo()
    print("Kapasitas Baterai : ",Baterai)

    i = 0
    while i == 0:

        print("Apakah sudah benar jumlah Kapasitas Baterainya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Bateraispecoppo()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit baterai
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
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
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpoppo()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Editspechpmerklain():

    print("Menu Edit spec hp")
    print("A. Edit spec hp ")
    print("B. Kembali ke menu edit")
    print("C. Kembali ke menu admin")
    masukan = str.upper(input(":"))

    if masukan == "A":
        for key, val in Spechp["Merk lain"][Datahp[0]].items():
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
        M. Kembali ke menu edit
        """)
        print("pilih huruf yang mau di edit ")
        i = 0
        while i == 0:
            ubah = str.upper(input(":"))

            if ubah == "A":
                Namaspecmerklain()
            elif ubah == "B":
                Tahunspecmerklain()
            elif ubah == "C":
                Osspecmerklain()
            elif ubah == "D":
                Chipsetspecmerklain()
            elif ubah == "E":
                Cpuspecmerklain()
            elif ubah == "F":
                Gpuspecmerklain()
            elif ubah == "G":
                Displayspecmerklain()
            elif ubah == "H":
                Memorispecmerklain()
            elif ubah == "I":
                Ramspecmerklain()
            elif ubah == "J":
                Jaringanspecmerklain()
            elif ubah == "K":
                Kameraspecmerklain()
            elif ubah == "L":
                Bateraispecmerklain()
            elif ubah == "M":
                Editspechp()
            else:
                print("Mohon masukan input dengan benar")

    elif masukan == "B":
        Datahp.clear()
        Editspechp()
    
    elif masukan == "C":
        Datahp.clear()
        main_admin()
    
    else:
        print("Masukan salah")
        Editspechpmerklain()
            
               
def Namaspecmerklain():
    print("Masukan nama baru")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    nama = str.upper(input(":"))
    if nama == "":
        print("masukan nama yang benar")
        Namaspecmerklain()
    elif nama == "KEMBALI":
        Editspechpmerklain()
    print("Nama : ",nama)

    i = 0
    while i == 0:

        print("Apakah sudah benar namanya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Namaspecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit nama
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Namaspecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"Nama" : nama})
    Spechp["Merk lain"][nama] = Daftarhp["Merk lain"].pop(Datahp[0])
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
    
        print("""
        Apakah anda ingin kembali ke:
        A. Edit spec
        B. Menu admin
        """)
        masukan1 = str.upper(input(":"))

        if masukan1 == "A":
            Editspechpmerklain()
        elif masukan1 == "B":
            Datahp.clear()
            main_admin()
        else:
            print("Input salah")




def Tahunspecmerklain():
    print("Masukan nama baru")
    print("Ketik 000 untuk kembali ke menu sebelumnya")
    try:
        Tahun = int(input(":"))
    except ValueError:
        print("Masukan angka bukan huruf")
        Tahunspecmerklain()
    if Tahun > 0:
        i = 0
        while i == 0:
            print("Tahun : ",Tahun)
            print("Apakah sudah benar tahunnya? (Y/N)")
            Konfirmasi = str.upper(input(":"))
            if Konfirmasi == "Y":
                break
            elif Konfirmasi == "N":
                Tahunspecmerklain()
            else:
                print("Inputan salah")
    
    elif Tahun == 000:
        Editspechpmerklain()

        i = 0
        while i == 0:

            print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
            finalisasi = str.upper(input(":"))
            if finalisasi == "Y":
                break
            elif finalisasi == "N":
                print("""
                A. Kembali ke edit tahun
                B. Kembali ke menu edit
                C. Kembali ke menu admin
                """)
                masukan = str.upper(input(":"))
                if masukan == "A":
                    Tahunspecmerklain()
                elif masukan == "B":
                    Editspechpmerklain()
                elif masukan == "C":
                    Datahp.clear()
                    main_admin()
                else:
                    print("Masukan salah")
                
            else:
                print("Inputan salah")

        Spechp["Merk lain"][Datahp[0]].update({"Tahun Keluar" : Tahun})
        print("item berhasil di ubah!")
        i = 0
        while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Osspecmerklain():
    print("Masukan nama OS baru (Contoh : Android 11, IOS 9)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Os = str.upper(input(":"))
    if Os == "":
        print("masukan nama yang benar")
        Osspecmerklain()
    elif Os == "KEMBALI":
        Editspechpmerklain()
    print("Os : ",Os)


    i = 0
    while i == 0:

        print("Apakah sudah benar nama Os nya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Osspecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit OS
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Osspecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"OS" : Os})
    print("item berhasil di ubah!")
    
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Chipsetspecmerklain():
    print("Masukan nama chipset baru (Contoh Snapdragon 870, Helio G80)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    chipset = str.upper(input(":"))
    if chipset == "":
        print("masukan nama yang benar")
        Chipsetspecmerklain()
    elif chipset == "KEMBALI":
        Editspechpmerklain()
    print("Chipset : ",chipset)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama chipsetnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Chipsetspecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit chipset
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Chipsetspecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"Chipset" : chipset})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Cpuspecmerklain():
    print("Masukan nama CPU baru (Contoh Octa-core, Quad-core)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Cpu = str.upper(input(":"))
    if Cpu == "":
        print("masukan nama yang benar")
        Cpuspecmerklain()
    elif Cpu == "KEMBALI":
        Editspechpmerklain()
    print("CPU : ",Cpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama CPUnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Cpuspecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit cpu
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Cpuspecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"CPU" : Cpu})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Gpuspecmerklain():
    print("Masukan nama Gpu baru (Contoh Mali, Adreno)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Gpu = str.upper(input(":"))
    if Gpu == "":
        print("masukan nama yang benar")
        Gpuspecmerklain()
    elif Gpu == "KEMBALI":
        Editspechpmerklain()
    print("GPU : ",Gpu)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama GPUnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Gpuspecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit gpu
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Gpuspecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"GPU" : Gpu})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Displayspecmerklain():
    print("Masukan nama tipe Display baru (Contoh Amoled, IPS PLS)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Display = str.upper(input(":"))
    if Display == "":
        print("masukan nama yang benar")
        Displayspecmerklain()
    elif Display == "KEMBALI":
        Editspechpmerklain()
    print("Display : ",Display)

    i = 0
    while i == 0:

        print("Apakah sudah benar nama Displaynya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Displayspecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit display
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Displayspecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"Display" : Display})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")



def Memorispecmerklain():
    print("Masukan jumlah memori hp baru (Contoh 8 GB, 64 GB)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Memori = str.upper(input(":"))
    if Memori == "":
        print("masukan nama yang benar")
        Memorispecmerklain()
    elif Memori == "KEMBALI":
        Editspechpmerklain()
    print("Memori Internal : ",Memori)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas memorinya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Memorispecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit memori
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Memorispecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"Memori Internal" : Memori})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Ramspecmerklain():
    print("Masukan jumlah RAM baru (Contoh 2 GB, 8 GB)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Ram = str.upper(input(":"))
    if Ram == "":
        print("masukan nama yang benar")
        Ramspecmerklain()
    elif Ram == "KEMBALI":
        Editspechpmerklain()
    print("Total RAM : ",Ram)

    i = 0
    while i == 0:

        print("Apakah sudah benar kapasitas RAMnya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Ramspecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit ram
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Ramspecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"RAM" : Ram})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Kameraspecmerklain():
    print("Masukan total MP Kamera baru (Contoh 20 MP, 30 MP)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Kamera = str.upper(input(":"))
    if Kamera == "":
        print("masukan nama yang benar")
        Kameraspecmerklain()
    elif Kamera == "KEMBALI":
        Editspechpmerklain()
    print("Kamera : ",Kamera)

    i = 0
    while i == 0:

        print("Apakah sudah benar MP kameranya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Kameraspecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit kamera
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Kameraspecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"Kamera" : Kamera})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def Jaringanspecmerklain():
    print("Masukan Support Jaringan baru (Contoh 2G/3G/4G/5G)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Jaringan = str.upper(input(":"))
    if Jaringan == "":
        print("masukan nama yang benar")
        Jaringanspecmerklain()
    elif Jaringan == "KEMBALI":
        Editspechpmerklain()
    print("Jaringan : ",Jaringan)

    i = 0
    while i == 0:

        print("Apakah sudah benar Jaringannya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Jaringanspecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit jaringan
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Jaringanspecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"Jaringan" : Jaringan})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")


def Bateraispecmerklain():
    print("Masukan jumlah kapasitas baterai baru (Contoh 2000 MAH/Baterai tanam, 4500 MAH/Baterai lepas)")
    print("Ketik kembali untuk kembali ke menu sebelumnya")
    Baterai = str.upper(input(":"))
    if Baterai == "":
        print("masukan nama yang benar")
        Bateraispecmerklain()
    elif Baterai == "KEMBALI":
        Editspechpmerklain()
    print("Kapasitas Baterai : ",Baterai)

    i = 0
    while i == 0:

        print("Apakah sudah benar jumlah Kapasitas Baterainya? (Y/N)")
        Konfirmasi = str.upper(input(":"))
        if Konfirmasi == "Y":
            break
        elif Konfirmasi == "N":
            Bateraispecmerklain()
        else:
            print("Inputan salah")


    i = 0
    while i == 0:

        print("Apakah anda yakin untuk mengedit item ini? (Y/N)")
        finalisasi = str.upper(input(":"))
        if finalisasi == "Y":
            break
        elif finalisasi == "N":
            print("""
            A. Kembali ke edit baterai
            B. Kembali ke menu edit
            C. Kembali ke menu admin
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                Bateraispecmerklain()
            elif masukan == "B":
                Editspechpmerklain()
            elif masukan == "C":
                Datahp.clear()
                main_admin()
            else:
                print("Masukan salah")
            
        else:
            print("Inputan salah")

    Spechp["Merk lain"][Datahp[0]].update({"Kapasitas Baterai" : Baterai})
    print("item berhasil di ubah!")
    i = 0
    while i == 0:
        
            print("""
            Apakah anda ingin kembali ke:
            A. Edit spec
            B. Menu admin
            """)
            masukan1 = str.upper(input(":"))

            if masukan1 == "A":
                Editspechpmerklain()
            elif masukan1 == "B":
                Datahp.clear()
                main_admin()
            else:
                print("Input salah")

def stokhp():
    print("Stok hp")
    print("Nama hp : Jumlah stok")
    for key, val in Stokhp.items():
        for key2, val2 in val.items():
            print("%s :" "%s" % (key2,val2))
    
    print("""
    A. Ubah stok hp
    B. Kembali ke menu admin
    """)

    masukan = str.upper(input(":"))

    if masukan == "A":
        i = 0
        while i == 0:
            print("List merk hp")
            for merk in Merkhp:
                print(merk)

            print("Pilih merk hp")
            print("Ketik kembali untuk kembali ke awal menu")
            pilihmerk = str.lower(input(":"))

            if pilihmerk == "samsung":
                stokhpsamsung()
            elif pilihmerk == "oppo":
                stokhpoppo()
            elif pilihmerk == "merk lain":
                stokhpmerklain()
            elif pilihmerk == "kembali":
                stokhp()
            else:
                print("masukan salah")
    elif masukan == "B":
        main_admin()
    else:
        print("Masukan anda salah")
        stokhp()


def stokhpsamsung():
    for key, val in Stokhp["Samsung"].items():
        print("%s : %s" % (key,val))
    print("Pilih nama hp yang akan diubah stoknya")
    print("Ketik kembali untuk kembali ke awal menu")
    masukan = str.upper(input(":"))
    if masukan in Stokhp["Samsung"].keys():
        Datahp.append(masukan)
        stokhpsamsung1()
    elif masukan == "KEMBALI":
        stokhp()
    else:
        print("masukan salah")
        stokhpsamsung()



def stokhpsamsung1():
    print("Masukan jumlah stok")
    print("Ketik 000 untuk kembali ke menu sebelumnya")
    try:
        updatestok = int(input(":"))
    except ValueError:
        print("Masukan harus berbentuk angka")
    if updatestok > 0:
        i = 0
        while i == 0:
            print(updatestok)
            print("apakah jumlah stok sudah benar? (Y/N)")
            konfirmasi = str.upper(input(":"))
            if konfirmasi == "Y":
                Stokhp["Samsung"].update({Datahp[0] : updatestok})
                Datahp.clear()
                print("stok hp berhasil di update")
                input("Tekan enter untuk kembali ke menu stok")
                stokhp()
            elif konfirmasi == "N":
                stokhpsamsung1()
            else:
                print("masukan salah")
    elif updatestok == 000:
        Datahp.clear()
        stokhpsamsung()

    else:
        print("masukan harus yang benar")
        stokhpsamsung1()


def stokhpoppo():
    for key, val in Stokhp["Oppo"].items():
        print("%s : %s" % (key,val))
    print("Pilih nama hp yang akan diubah stoknya")
    print("Ketik kembali untuk kembali ke awal menu")
    masukan = str.upper(input(":"))
    if masukan in Stokhp["Oppo"].keys():
        Datahp.append(masukan)
        stokhpoppo1()
    elif masukan == "KEMBALI":
        stokhp()
    else:
        print("masukan salah")
        stokhpoppo()



def stokhpoppo1():
    print("Masukan jumlah stok")
    print("Ketik 000 untuk kembali ke menu sebelumnya")
    try:
        updatestok = int(input(":"))
    except ValueError:
        print("Masukan harus berbentuk angka")
    if updatestok > 0:
        i = 0
        while i == 0:
            print(updatestok)
            print("apakah jumlah stok sudah benar? (Y/N)")
            konfirmasi = str.upper(input(":"))
            if konfirmasi == "Y":
                Stokhp["Oppo"].update({Datahp[0] : updatestok})
                Datahp.clear()
                print("stok hp berhasil di update")
                input("Tekan enter untuk kembali ke menu stok")
                stokhp()
            elif konfirmasi == "N":
                stokhpoppo1()
            else:
                print("masukan salah")
    elif updatestok == 000:
        Datahp.clear()
        stokhpoppo()

    else:
        print("masukan harus yang benar")
        stokhpoppo1()

def stokhpmerklain():
    for key, val in Stokhp["Merk lain"].items():
        print("%s : %s" % (key,val))
    print("Pilih nama hp yang akan diubah stoknya")
    print("Ketik kembali untuk kembali ke awal menu")
    masukan = str.upper(input(":"))
    if masukan in Stokhp["Merk lain"].keys():
        Datahp.append(masukan)
        stokhpmerklain1()
    elif masukan == "KEMBALI":
        stokhp()
    else:
        print("masukan salah")
        stokhpmerklain()



def stokhpmerklain1():
    print("Masukan jumlah stok")
    print("Ketik 000 untuk kembali ke menu sebelumnya")
    try:
        updatestok = int(input(":"))
    except ValueError:
        print("Masukan harus berbentuk angka")
    if updatestok > 0:
        i = 0
        while i == 0:
            print(updatestok)
            print("apakah jumlah stok sudah benar? (Y/N)")
            konfirmasi = str.upper(input(":"))
            if konfirmasi == "Y":
                Stokhp["Merk lain"].update({Datahp[0] : updatestok})
                Datahp.clear()
                print("stok hp berhasil di update")
                input("Tekan enter untuk kembali ke menu stok")
                stokhp()
            elif konfirmasi == "N":
                stokhpmerklain1()
            else:
                print("masukan salah")
    elif updatestok == 000:
        Datahp.clear()
        stokhpmerklain()

    else:
        print("masukan harus yang benar")
        stokhpmerklain1()


def Hapus_Keuntungan():
    print ("===================================================================================================================")
    print("Apakah anda yakin untuk menghapus jumlah keuntungan hari ini? pastikan anda sudah mencatat jumlah keuntungan hari ini")
    print ("===================================================================================================================")
    konfirmasi = str.lower(input("ya/tidak :"))
    if konfirmasi == "ya":
        Keuntungan["Total_keuntungan"].clear()
        print ("====================")
        print ("Data berhasil di hapus")
        print ("====================")
        kembali_menu()
    elif konfirmasi == "tidak":
        print ("Aksi dihentikan")
        kembali_menu()
    else:
        print("Inputan salah, silakan isi konfimasi kembali")
        Hapus_Keuntungan()

def kembalilogin():
    print("=======================================")
    print("Apakah anda ingin kembali ke menu login? ")
    print("=======================================")
    konfirmasi = str.lower(input("ya/tidak :"))
    if konfirmasi == "ya":
            user_login()
    elif konfirmasi == "tidak":
            print ("Aksi dihentikan")
            kembali_menu()
    else:
            print("Inputan salah, silakan konfirmasi kembali")
            kembalilogin()


def kembali_menu():
    input("Tekan enter untuk kembali")
    main_admin()


def kasir():

    waktu = time.ctime()
    print(waktu)
    print("Menu Kasir")
    print("""
    A. Jual Hp
    B. Beli Hp
    C. Kembali ke login
    """)

    masukan = str.upper(input(":"))

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
    masukan = str.upper(input(":"))

    if masukan == "A":
        jualhpmerk()
    elif masukan == "B":
        jualhpharga()
    elif masukan == "C":
        kasir()
    elif masukan in Daftarhp["Samsung"]:
        Datahp.append(masukan)
        konfirmasibeli()
    elif masukan in Daftarhp["Oppo"]:
        Datahp.append(masukan)
        konfirmasibeli()
    elif masukan in Daftarhp["Merk lain"]:
        Datahp.append(masukan)
        konfirmasibeli()
    else:
        print("masukan salah")
        jualhp()


def jualhpmerk():
    for merk in Merkhp:
        print(merk)
    print("Pilih merk yang di inginkan")
    pilihmerk = str.lower(input(":"))        
    if pilihmerk == "samsung":
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

            masukansamsung = str.upper(input(":"))
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

    elif pilihmerk == "oppo":
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

            masukanoppo = str.upper(input(":"))
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
    elif pilihmerk == "merk lain":
        i = 0
        while i == 0:
            for key,val in Daftarhp["Merk lain"].items():
                print("%s : %s" % (key,val))
            
            print("""
                A. Tampilkan seluruh merk hp
                B. Pilih hp berdasarkan harga
                C. Kembali ke awal

                Ket: Masukan nama hp sesuai di tabel untuk pilih hp yang akan di beli 
            """)

            masukaniphone = str.upper(input(":"))
            if masukaniphone == "A":
                jualhp()
            elif masukaniphone == "B":
                jualhpharga()
            elif masukaniphone == "C":
                kasir()
            elif masukaniphone in Daftarhp["Merk lain"].keys():
                Datahp.append(masukaniphone)
                konfirmasibeli()
            else:
                print("Masukan salah")
                
    else:
        print("masukan anda salah, silakan isi kembali")
        jualhpmerk()
        
        


    
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
        masukan = str.upper(input(":"))
        if masukan == "A":
            print("Apakah anda ingin menjual hp ini? (Y/N)")
            Konfirmasi = str.upper(input(":"))
            if Konfirmasi == "Y":
                if Stokhp["Samsung"][Datahp[0]] > 0:
                    waktu = time.ctime()
                    print(waktu)
                    print("Toko")
                    print("Nama Hp :", Datahp[0])
                    print("Harga Hp :", Daftarhp["Samsung"][Datahp[0]])
                    print("Jumlah Bayar Total : Rp.", Daftarhp["Samsung"][Datahp[0]])
                    print("Terima kasih telah membeli di toko kami")
                    ubah = Stokhp["Samsung"][Datahp[0]] - 1
                    Stokhp["Samsung"].update({Datahp[0] : ubah})
                    Keuntungan["Total_keuntungan"].append(Daftarhp["Samsung"][Datahp[0]])
                    input("Tekan enter untuk kembali ke kasir")
                    Datahp.clear()
                    kasir()
                else:
                    print("Mohon maaf hp ini tidak ada stoknya")
                    Datahp.clear()
                    jualhp()
            
            elif Konfirmasi == "N":
                i = 0
                while i == 0:

                    print("""
                    A. Kembali ke daftar seluruh hp
                    B. Kembali ke kasir
                    """)
                    kembali = str.upper(input(":"))

                    if kembali == "A":
                        Datahp.clear()
                        jualhp()
                    elif kembali == "B":
                        Datahp.clear()
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
            print("masukan salah")
            konfirmasibeli()
    
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
        masukan = str.upper(input(":"))
        if masukan == "A":
            print("Apakah anda ingin menjual hp ini? (Y/N)")
            Konfirmasi = str.upper(input(":"))
            if Konfirmasi == "Y":
                if Stokhp["Oppo"][Datahp[0]] > 0:
                    waktu = time.ctime()
                    print(waktu)
                    print("Toko")
                    print("Nama Hp :", Datahp[0])
                    print("Harga Hp :", Daftarhp["Oppo"][Datahp[0]])
                    print("Jumlah Bayar Total : Rp.", Daftarhp["Oppo"][Datahp[0]])
                    print("Terima kasih telah membeli di toko kami")
                    ubah = Stokhp["Oppo"][Datahp[0]] - 1
                    Stokhp["Oppo"].update({Datahp[0] : ubah})
                    Keuntungan["Total_keuntungan"].append(Daftarhp["Oppo"][Datahp[0]])
                    Datahp.clear()
                    input("Tekan enter untuk kembali ke kasir")
                    kasir()
                else:
                    print("Mohon maaf hp ini tidak ada stoknya")
                    Datahp.clear()
                    jualhp()
            
            elif Konfirmasi == "N":
                i = 0
                while i == 0:

                    print("""
                    A. Kembali ke daftar seluruh hp
                    B. Kembali ke kasir
                    """)
                    kembali = str.upper(input(":"))

                    if kembali == "A":
                        Datahp.clear()
                        jualhp()
                    elif kembali == "B":
                        Datahp.clear()
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
            print("masukan salah")
            konfirmasibeli()

    elif Datahp[0] in Daftarhp["Merk lain"].keys():
        print("Nama Hp :", Datahp[0])
        print("Harga Hp :", Daftarhp["Merk lain"][Datahp[0]])
        try:
            print("Spec hp :", Spechp["Merk lain"][Datahp[0]])
        except KeyError:
            print("Spec hp tidak ada")

        print("Stok Hp :", Stokhp["Merk lain"][Datahp[0]])
        print("""
        A. Jual Hp ini
        B. Pilih Hp lain
        C. Kembali ke awal
        """)
        masukan = str.upper(input(":"))
        if masukan == "A":
            print("Apakah anda ingin menjual hp ini? (Y/N)")
            Konfirmasi = str.upper(input(":"))
            if Konfirmasi == "Y":
                if Stokhp["Merk lain"][Datahp[0]] > 0:
                    waktu = time.ctime()
                    print(waktu)
                    print("Toko")
                    print("Nama Hp :", Datahp[0])
                    print("Harga Hp :", Daftarhp["Merk lain"][Datahp[0]])
                    print("Jumlah Bayar Total : Rp.", Daftarhp["Merk lain"][Datahp[0]])
                    print("Terima kasih telah membeli di toko kami")
                    ubah = Stokhp["Iphone"][Datahp[0]] - 1
                    Stokhp["Merk lain"].update({Datahp[0] : ubah})
                    Keuntungan["Total_keuntungan"].append(Daftarhp["Merk lain"][Datahp[0]])
                    Datahp.clear()
                    input("Tekan enter untuk kembali ke kasir")
                    kasir()
                else:
                    print("Mohon maaf hp ini tidak ada stoknya")
                    Datahp.clear()
                    jualhp()
            
            elif Konfirmasi == "N":
                i = 0
                while i == 0:

                    print("""
                    A. Kembali ke daftar seluruh hp
                    B. Kembali ke kasir
                    """)
                    kembali = str.upper(input(":"))

                    if kembali == "A":
                        Datahp.clear()
                        jualhp()
                    elif kembali == "B":
                        Datahp.clear()
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
            print("masukan salah")
            konfirmasibeli()

    else:
        print("data tidak ada")
                

def jualhpharga():
    Samsung = sorted(Daftarhp["Samsung"].items(), key=lambda x: x[1])
    Oppo = sorted(Daftarhp["Oppo"].items(), key=lambda x: x[1])
    Merklain = sorted(Daftarhp["Merk lain"].items(), key=lambda x: x[1])
    for s in Samsung:
        print(s[0], s[1])
    for o in Oppo:
        print(o[0], o[1])
    for i in Merklain:
        print(i[0], i[1])

    print("""
                A. Tampilkan seluruh merk hp
                B. Pilih hp berdasarkan merk
                C. Kembali ke awal

                Ket: Masukan nama hp sesuai di tabel untuk pilih hp yang akan di beli 
    """)

    masukan = str.upper(input(":"))
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
    elif masukan in Daftarhp["Merk lain"].keys():
        Datahp.append(masukan)
        konfirmasibeli()
    else:
        print("Masukan salah")
        jualhpharga()

    
    
def belihp():
    for i in Merkhp:
        print(i)
    print("Pilih merk hp yang akan dibeli")
    print("Ketik kembali untuk kembali ke awal menu")
    masukan = str.lower(input(":"))
    if masukan == "samsung":
        belihpsamsung()
    elif masukan == "oppo":
        belihpoppo()
    elif masukan == "merk lain":
        belihpmerklain()
    elif masukan == "kembali":
        kasir()
    else:
        print("masukan salah")
        belihp()

def belihpsamsung():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        print("Ketik kembali untuk kembali ke awal menu")
        nama = str.upper(input(":"))
        if nama == "":
            print("mohon masukan input dengan benar")
        elif nama == "KEMBALI":
            belihp()
        else:
            Datahp.append(nama)
            belihpsamsung1()

def belihpsamsung1():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        print("Ketik 000 untuk kembali ke awal menu")
        try:
            harga = int(input(":"))
        except ValueError:
            print("harap masukan angka bukan huruf")
        if harga > 0:
            Datahp.append(harga)
            belihpsamsung2()
        elif harga == 000:
            Datahp.clear()
            belihpsamsung()
        else:
            print("masukan anda negatif atau bukan angka")
        
def belihpsamsung2():
    print("Nama Hp : ", Datahp[0])
    print("Harga hp : ", Datahp[1])
    print("Apakah nama dan harga sudah sesuai? (konfirmasi kepada penjual) (Y/N)")
    finalisasi = str.upper(input(":"))
    if finalisasi == "Y":
        waktu = time.ctime()
        print(waktu)
        print("toko hp")
        print("Nama Hp", Datahp[0])
        print("Harga hp", Datahp[1])
        print("terima kasih telah menjual di sini")
        input("Tekan enter untuk kembali ke menu kasir")
        kasir()

    elif finalisasi == "N":
        i = 0
        while i == 0:
            print("""
            A. Ubah nama
            B. Ubah harga
            C. Batalkan penbelian
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                belihpsamsung3()
            elif masukan == "B":
                belihpsamsung4()
            elif masukan == "C":
                i = 0
                while i == 0:
                    print("Apakah anda yakin untuk membatalkan (Y/N)")
                    batal = str.upper(input(":"))
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
        belihpsamsung2()


def belihpsamsung3():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        nama = str.upper(input(":"))
        if nama == "":
            print("mohon masukan input dengan benar")
        else:
            Datahp[0] = nama
            belihpsamsung2()

def belihpsamsung4():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        try:
            harga = int(input(":"))
        except ValueError:
            print("harap masukan angka bukan huruf")
        if harga > 0:
            Datahp[1] = harga
            belihpsamsung2()
        else:
            print("masukan anda negatif atau bukan angka")


def belihpoppo():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        print("Ketik kembali untuk kembali ke awal menu")
        nama = str.upper(input(":"))
        if nama == "":
            print("mohon masukan input dengan benar")
        elif nama == "KEMBALI":
            belihp()
        else:
            Datahp.append(nama)
            belihpoppo1()

def belihpoppo1():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        print("Ketik 000 untuk kembali ke awal menu")
        try:
            harga = int(input(":"))
        except ValueError:
            print("harap masukan angka bukan huruf")
        if harga > 0:
            Datahp.append(harga)
            belihpoppo2()
        elif harga == 000:
            Datahp.clear()
            belihpoppo()
        else:
            print("masukan anda negatif atau bukan angka")
        
def belihpoppo2():
    print("Nama Hp", Datahp[0])
    print("Harga hp", Datahp[1])
    print("Apakah nama dan harga sudah sesuai? (konfirmasi kepada penjual) (Y/N)")
    finalisasi = str.upper(input(":"))
    if finalisasi == "Y":
        waktu = time.ctime()
        print(waktu)
        print("toko hp")
        print("Nama Hp : ", Datahp[0])
        print("Harga hp : ", Datahp[1])
        print("terima kasih telah menjual di sini")
        input("Tekan enter untuk kembali ke menu kasir")
        kasir()

    elif finalisasi == "N":
        i = 0
        while i == 0:
            print("""
            A. Ubah nama
            B. Ubah harga
            C. Batalkan penbelian
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                belihpoppo3()
            elif masukan == "B":
                belihpoppo4()
            elif masukan == "C":
                i = 0
                while i == 0:
                    print("Apakah anda yakin untuk membatalkan (Y/N)")
                    batal = str.upper(input(":"))
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
        belihpoppo2



def belihpoppo3():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        nama = str.upper(input(":"))
        if nama == "":
            print("mohon masukan input dengan benar")
        else:
            Datahp[0] = nama
            belihpoppo2()

def belihpoppo4():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        try:
            harga = int(input(":"))
        except ValueError:
            print("harap masukan angka bukan huruf")
        if harga > 0:
            Datahp[1] = harga
            belihpoppo2()
        else:
            print("masukan anda negatif atau bukan angka")
                

def belihpmerklain():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        print("Ketik kembali untuk kembali ke awal menu")
        nama = str.upper(input(":"))
        if nama == "":
            print("mohon masukan input dengan benar")
        elif nama == "KEMBALI":
            belihp()
        else:
            Datahp.append(nama)
            belihpmerklain1()

def belihpmerklain1():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        print("Ketik 000 untuk kembali ke awal menu")
        try:
            harga = int(input(":"))
        except ValueError:
            print("harap masukan angka bukan huruf")
        if harga > 0:
            Datahp.append(harga)
            belihpmerklain2()
        elif harga == 000:
            Datahp.clear()
            belihpmerklain()
        else:
            print("masukan anda negatif atau bukan angka")
        
def belihpmerklain2():
    print("Nama Hp : ", Datahp[0])
    print("Harga hp : ", Datahp[1])
    print("Apakah nama dan harga sudah sesuai? (konfirmasi kepada penjual) (Y/N)")
    finalisasi = str.upper(input(":"))
    if finalisasi == "Y":
        waktu = time.ctime()
        print(waktu)
        print("toko hp")
        print("Nama Hp", Datahp[0])
        print("Harga hp", Datahp[1])
        print("terima kasih telah menjual di sini")
        input("Tekan enter untuk kembali ke menu kasir")
        kasir()

    elif finalisasi == "N":
        i = 0
        while i == 0:
            print("""
            A. Ubah nama
            B. Ubah harga
            C. Batalkan penbelian
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                belihpmerklain3()
            elif masukan == "B":
                belihpmerklain4()
            elif masukan == "C":
                i = 0
                while i == 0:
                    print("Apakah anda yakin untuk membatalkan (Y/N)")
                    batal = str.upper(input(":"))
                    if batal == "Y":
                        Datahp.clear()
                        print("pembelian dibatalkan")
                        kasir()
                    elif batal == "N":
                        belihpmerklain2()
                    else:
                        print("masukan salah")
            else:
                print("Masukan salah")
    else:
        print("masukan salah")
        belihpmerklain2()


def belihpmerklain3():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        nama = str.upper(input(":"))
        if nama == "":
            print("mohon masukan input dengan benar")
        else:
            Datahp[0] = nama
            belihpmerklain2()

def belihpmerklain4():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        try:
            harga = int(input(":"))
        except ValueError:
            print("harap masukan angka bukan huruf")
        if harga > 0:
            Datahp[1] = harga
            belihpmerklain2()
        else:
            print("masukan anda negatif atau bukan angka")
    
   


user_login()