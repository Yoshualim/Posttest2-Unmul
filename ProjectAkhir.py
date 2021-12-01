import time
import os

Daftarhp = {
    "Samsung" : {
        "SAMSUNG J2" : 1000000,
        "SAMSUNG J1 PRIME" : 2000000,
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
    "Merk lain" : {
        "ADVAN C10" : 3,
        "IPHONE X" : 0,
    }
}
Merkhp = ["Samsung", "Merk lain"]
Datahp = []
Penjualan = []
Pembelian = []
Userlogin = {
        "username_user" : "Yoshua",
        "username_admin" :"Admin",
        "Password_Normal" : 210,
        "Password_Admin" : 6093
            }

def user_login():
    print("=============")
    print("Selamat datang")
    print("toko broku store 2rd")
    print("=============")
    user =str(input("Masukan username :"))
    try:
        Pass =int(input("Masukan password :"))
    except ValueError:
        os.system('cls')
        print("Password berbentuk angka silakan isi ulang")
        user_login()
        
    if user == Userlogin["username_admin"] and Pass == Userlogin["Password_Admin"]:
        os.system('cls')
        print("Login Berhasil")
        main_admin()

    elif user == Userlogin["username_user"] and Pass == Userlogin["Password_Normal"]:
        os.system('cls')
        print("Login Berhasil")
        kasir()
        
    else:
        os.system('cls')
        print("Username atau password anda salah, silakan isi kembali")
        user_login()

def main_admin():

    print("Menu Admin toko broku store 2rd") 
    waktu = time.ctime()
    print(waktu)
    print("======================================")
    print("1. Lihat list Hp")
    print("2. Tambahkan Hp")
    print("3. Edit Hp")
    print("4. Hapus Hp ")
    print("5. Stok hp")
    print("6. Hapus jumlah keuntungan dan penjualan")
    jumlahkeuntungan = sum(Penjualan)
    print("Keuntungan hari ini : Rp.", jumlahkeuntungan)
    jumlahpengeluaran = sum(Pembelian)
    print("Pengeluaran hari ini : Rp.", jumlahpengeluaran)
    total = jumlahkeuntungan - jumlahpengeluaran
    print("Total keuntungan : Rp.", total)
    print("0. Keluar dari menu Admin")
    print ("======================================")

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
        stokhp()
    elif pilihan_menu == ("6"):
        os.system('cls')
        reset()
    elif pilihan_menu == ("0"):
        os.system('cls')
        kembalilogin()        
    else:
        os.system('cls')
        print("Anda salah input silakan coba kembali")
        main_admin()

def List_menuhp():
    print("List HP toko broku store 2rd")
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
        
    Daftarhp["Merk lain"].update({Datahp[0] : Datahp[1]})
    Stokhp["Merk lain"].update({Datahp[0] : Datahp[2]})
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
        3. Kembali ke pilih merk hp
        4. Kembali ke menu admin
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
            Datahp.clear()
            os.system('cls')
            Edit_hp()
        elif masukan == 4:
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
    Stokhp["Samsung"][namahp] = Stokhp["Samsung"].pop(Datahp[0])
   
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
   
def Edithp_merklain():
    for key in Daftarhp["Merk lain"].keys():
        print("%s" % (key))

    print("====================")
    print("Kembali")
    print("Masukan nama hp yang akan diedit (Ketik kembali untuk kembali ke menu sebelumnya) ")
    ubah = str.upper(input(":"))
    if ubah in Daftarhp["Merk lain"].keys():
        Datahp.append(ubah)
        os.system('cls')
        Edithp_merklain1()
    elif ubah == "KEMBALI":
        os.system('cls')
        Edit_hp()
    else:
        os.system('cls')
        print("Masukan inputan yang benar")
        Edithp_merklain()


def Edithp_merklain1():
    print("Nama hp : ",Datahp[0])
    print("Harga hp : Rp. ",Daftarhp["Merk lain"][Datahp[0]])
    print("Menu edit")
    print("""
        1. Nama Hp
        2. Harga Hp
        3. Kembali ke pilih merk hp
        4. Kembali ke menu admin
        """)
    try:
        masukan = int(input(":"))
    except ValueError:
        os.system('cls')
        print("Masukan salah")
        Edithp_merklain1()
    
    if masukan > 0:
        if masukan == 1:
            os.system('cls')
            Editnama_merklain()
        elif masukan == 2:
            os.system('cls')
            Editharga_merklain()
        elif masukan == 3:
            Datahp.clear()
            os.system('cls')
            Edit_hp()
        elif masukan == 4:
            Datahp.clear()
            os.system('cls')
            main_admin()
        else:
            os.system('cls')
            print("Inputan kamu salah, silakan coba kembali")
            Edithp_merklain1()
    else:
        os.system('cls')
        print("Inputan kamu negatif, silakan coba kembali")
        Edithp_merklain1()

def Editnama_merklain():
    print("Nama hp lama : ",Datahp[0])
    print("Masukan Nama hp baru (Ketik kembali untuk kembali ke menu sebelumnya) ")
    namahp = str.upper(input(":"))
    if namahp == "":
        os.system('cls')
        print("Mohon isi dengan benar")
        Editnama_merklain()
    elif namahp == "KEMBALI":
        os.system('cls')
        Edithp_merklain1()

    
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
            Editnama_merklain()
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
                    Editnama_merklain()
                elif masukan == "D":
                    os.system('cls')
                    Edithp_merklain1()
                else:
                    os.system('cls')
                    print("inputan salah")
        else:
            os.system('cls')
            print("inputan salah")
    
    
    Daftarhp["Merk lain"][namahp] = Daftarhp["Merk lain"].pop(Datahp[0])
    Stokhp["Merk lain"][namahp] = Stokhp["Merk lain"].pop(Datahp[0])
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


def Editharga_merklain():
    print("Harga hp lama : Rp. ",Daftarhp["Merk lain"][Datahp[0]])
    print("Masukan Harga hp baru (Ketik 000 untuk kembali ke menu sebelumnya)")
    try:
        hargahp = int(input(":"))
    except ValueError:
        os.system('cls')
        print("Masukan angka bukan huruf")
        Editharga_merklain()
    
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
                Editharga_merklain()
            else:
                os.system('cls')
                print("Harap input jawaban yang benar")
    elif hargahp == 000:
        os.system('cls')
        Edithp_merklain1()
    else:
        os.system('cls')
        print("masukan berbentuk negatif")
        Editharga_merklain()
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
                    Editharga_merklain()
                elif masukan == "D":
                    os.system('cls')
                    Edithp_merklain1()
                else:
                    os.system('cls')
                    print("inputan salah")
        else:
            os.system('cls')
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
            os.system('cls')
            Edit_hp()
        elif masukan1 == "B":
            Datahp.clear()
            os.system('cls')
            main_admin()
        else:
            os.system('cls')
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
        os.system('cls')
        Datahp.append(ubah)
        Edithp_Samsung1()
    elif ubah in Daftarhp["Merk lain"].keys():
        os.system('cls')
        Datahp.append(ubah)
        Edithp_merklain1()
    elif ubah == "KEMBALI":
        os.system('cls')
        Edit_hp()
    else:
        os.system('cls')
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
        os.system('cls')
        i = 0
        while i == 0: 
            print("Nama hp : ",masukan)
            print("Harga hp : Rp. ",Daftarhp["Samsung"][masukan])
            print("Apakah anda ingin menghapus ini? ini tidak bisa dikembalikan! (Y/N)")
            konfirmasi = str.upper(input(":"))
            if konfirmasi == "Y":
                os.system('cls')
                del Daftarhp["Samsung"][masukan]
                del Stokhp["Samsung"][masukan]
                print("Data berhasil dihapus!")
                input("Tekan enter untuk kembali ke menu admin")
                os.system('cls')
                main_admin()
            elif konfirmasi == "N":
                os.system('cls')
                i = 0
                while i == 0:
                    print("Operasi dibatalkan, apakah anda ingin kembali ke menu hapus hp atau kembali ke menu admin?")
                    print("A. menu hapus hp")
                    print("B. menu admin")
                    konfirm = str.upper(input(":"))
                    if konfirm == "A":
                        os.system('cls')
                        Hapus_hp()
                    elif konfirm == "B":
                        os.system('cls')
                        main_admin()
                    else:
                        os.system('cls')
                        print("Inputan salah")
            else:
                os.system('cls')
                print("Inputan salah")
    
    elif masukan in Daftarhp["Merk lain"].keys():
        os.system('cls')
        i = 0
        while i == 0:
            print("Nama hp : ",masukan)
            print("Harga hp : Rp. ",Daftarhp["Merk lain"][masukan])
            print("Apakah anda ingin menghapus ini? ini tidak bisa dikembalikan! (Y/N)")
            konfirmasi = str.upper(input(":"))
            if konfirmasi == "Y":
                os.system('cls')
                del Daftarhp["Merk lain"][masukan]
                del Stokhp["Merk lain"][masukan]
                print("Data berhasil dihapus!")
                input("Tekan enter untuk kembali ke menu admin")
                os.system('cls')
                main_admin()
            elif konfirmasi == "N":
                os.system('cls')
                i = 0
                while i == 0:
                    print("Operasi dibatalkan, apakah anda ingin kembali ke menu hapus hp atau kembali ke menu admin?")
                    print("A. menu hapus hp")
                    print("B. menu admin")
                    konfirm = str.upper(input(":"))
                    if konfirm == "A":
                        os.system('cls')
                        Hapus_hp()
                    elif konfirm == "B":
                        os.system('cls')
                        main_admin()
                    else:
                        os.system('cls')
                        print("Inputan salah")
            else:
                os.system('cls')
                print("Inputan salah")
    
    elif masukan == "KEMBALI":
        os.system('cls')
        main_admin()
    
    else:
        os.system('cls')
        print("Inputan salah")
        Hapus_hp()

def stokhp():
    print("Stok hp toko broku store 2rd")
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
        os.system('cls')
        i = 0
        while i == 0:
            print("List merk hp")
            for merk in Merkhp:
                print(merk)

            print("Pilih merk hp")
            print("Ketik kembali untuk kembali ke awal menu")
            pilihmerk = str.lower(input(":"))

            if pilihmerk == "samsung":
                os.system('cls')
                stokhpsamsung()
            elif pilihmerk == "merk lain":
                os.system('cls')
                stokhpmerklain()
            elif pilihmerk == "kembali":
                os.system('cls')
                stokhp()
            else:
                os.system('cls')
                print("masukan salah")
    elif masukan == "B":
        os.system('cls')
        main_admin()
    else:
        os.system('cls')
        print("Masukan anda salah")
        stokhp()


def stokhpsamsung():
    for key, val in Stokhp["Samsung"].items():
        print("%s : %s" % (key,val))
    print("Pilih nama hp yang akan diubah stoknya")
    print("Ketik kembali untuk kembali ke awal menu")
    masukan = str.upper(input(":"))
    if masukan in Stokhp["Samsung"].keys():
        os.system('cls')
        Datahp.append(masukan)
        stokhpsamsung1()
    elif masukan == "KEMBALI":
        os.system('cls')
        stokhp()
    else:
        os.system('cls')
        print("masukan salah")
        stokhpsamsung()



def stokhpsamsung1():
    print("Masukan jumlah stok")
    print("Ketik 000 untuk kembali ke menu sebelumnya")
    try:
        updatestok = int(input(":"))
    except ValueError:
        os.system('cls')
        print("Masukan harus berbentuk angka")
    if updatestok > 0:
        os.system('cls')
        i = 0
        while i == 0:
            print(updatestok)
            print("apakah jumlah stok sudah benar? (Y/N)")
            konfirmasi = str.upper(input(":"))
            if konfirmasi == "Y":
                os.system('cls')
                Stokhp["Samsung"].update({Datahp[0] : updatestok})
                Datahp.clear()
                print("stok hp berhasil di update")
                input("Tekan enter untuk kembali ke menu stok")
                os.system('cls')
                stokhp()
            elif konfirmasi == "N":
                os.system('cls')
                stokhpsamsung1()
            else:
                os.system('cls')
                print("masukan salah")
    elif updatestok == 000:
        os.system('cls')
        Datahp.clear()
        stokhpsamsung()

    else:
        os.system('cls')
        print("masukan harus yang benar")
        stokhpsamsung1()

def stokhpmerklain():
    for key, val in Stokhp["Merk lain"].items():
        print("%s : %s" % (key,val))
    print("Pilih nama hp yang akan diubah stoknya")
    print("Ketik kembali untuk kembali ke awal menu")
    masukan = str.upper(input(":"))
    if masukan in Stokhp["Merk lain"].keys():
        os.system('cls')
        Datahp.append(masukan)
        stokhpmerklain1()
    elif masukan == "KEMBALI":
        os.system('cls')
        stokhp()
    else:
        os.system('cls')
        print("masukan salah")
        stokhpmerklain()



def stokhpmerklain1():
    print("Masukan jumlah stok")
    print("Ketik 000 untuk kembali ke menu sebelumnya")
    try:
        updatestok = int(input(":"))
    except ValueError:
        os.system('cls')
        print("Masukan harus berbentuk angka")
    if updatestok > 0:
        os.system('cls')
        i = 0
        while i == 0:
            print(updatestok)
            print("apakah jumlah stok sudah benar? (Y/N)")
            konfirmasi = str.upper(input(":"))
            if konfirmasi == "Y":
                os.system('cls')
                Stokhp["Merk lain"].update({Datahp[0] : updatestok})
                Datahp.clear()
                print("stok hp berhasil di update")
                input("Tekan enter untuk kembali ke menu stok")
                os.system('cls')
                stokhp()
            elif konfirmasi == "N":
                os.system('cls')
                stokhpmerklain1()
            else:
                os.system('cls')
                print("masukan salah")
    elif updatestok == 000:
        os.system('cls')
        Datahp.clear()
        stokhpmerklain()

    else:
        os.system('cls')
        print("masukan harus yang benar")
        stokhpmerklain1()

def kembalilogin():
    print("=======================================")
    print("Apakah anda ingin kembali ke menu login? ")
    print("=======================================")
    konfirmasi = str.lower(input("ya/tidak :"))
    if konfirmasi == "ya":
        os.system('cls')
        user_login()
    elif konfirmasi == "tidak":
        os.system('cls')
        print ("Aksi dihentikan")
        kembali_menu()
    else:
        os.system('cls')
        print("Inputan salah, silakan konfirmasi kembali")
        kembalilogin()



def reset():
    print ("===================================================================================================================")
    print("Apakah anda yakin untuk menghapus jumlah keuntungan pembelian dan penjualan hari ini? pastikan anda sudah mencatat jumlah keuntungan hari ini")
    print ("===================================================================================================================")
    konfirmasi = str.lower(input("ya/tidak :"))
    if konfirmasi == "ya":
        os.system('cls')
        Penjualan.clear()
        Pembelian.clear()
        print ("====================")
        print ("Data berhasil di hapus")
        print ("====================")
        kembali_menu()
    elif konfirmasi == "tidak":
        os.system('cls')
        print ("Aksi dihentikan")
        kembali_menu()
    else:
        os.system('cls')
        print("Inputan salah, silakan isi konfimasi kembali")
        reset()

def kembali_menu():
    input("Tekan enter untuk kembali")
    os.system('cls')
    main_admin()


def kasir():

    waktu = time.ctime()
    print(waktu)
    print("toko broku store 2rd")
    print("======================")
    print("Menu Kasir")
    print("""
    A. Jual Hp
    B. Beli Hp
    C. Kembali ke login
    """)

    masukan = str.upper(input(":"))

    if masukan == "A":
        os.system('cls')
        jualhp()
    elif masukan == "B":
        os.system('cls')
        belihp()
    elif masukan == "C":
        os.system('cls')
        user_login()
    else:
        os.system('cls')
        print("Masukan pilihan dengan benar")
        kasir()


def jualhp():
    print("Jual hp")
    print("toko broku store 2rd")
    print("=======================")
    for key, val in Daftarhp.items():
        for key2, val2 in val.items():
            print("%s : " "Rp."" %s" % (key2,val2))
    print("""
    A. Pilih hp berdasarkan merk
    B. Pilih hp berdasarkan harga
    C. Kembali ke awal 
    Ket: Masukan nama hp sesuai di tabel untuk pilih hp yang akan di beli
    """)
    masukan = str.upper(input(":"))

    if masukan == "A":
        os.system('cls')
        jualhpmerk()
    elif masukan == "B":
        os.system('cls')
        jualhpharga()
    elif masukan == "C":
        os.system('cls')
        kasir()
    elif masukan in Daftarhp["Samsung"]:
        os.system('cls')
        Datahp.append(masukan)
        konfirmasibeli()
    elif masukan in Daftarhp["Merk lain"]:
        os.system('cls')
        Datahp.append(masukan)
        konfirmasibeli()
    else:
        os.system('cls')
        print("masukan salah")
        jualhp()


def jualhpmerk():
    print("toko broku store 2rd")
    print("======================")
    for merk in Merkhp:
        print(merk)
    print("Pilih merk yang di inginkan")
    pilihmerk = str.lower(input(":"))        
    if pilihmerk == "samsung":
        os.system('cls')
        i = 0
        while i == 0:
            for key,val in Daftarhp["Samsung"].items():
                print("%s : ""Rp."" %s" % (key,val))
            
            print("""
                A. Tampilkan seluruh merk hp
                B. Pilih hp berdasarkan harga
                C. Kembali ke awal

                Ket: Masukan nama hp sesuai di tabel untuk pilih hp yang akan di beli 
            """)

            masukansamsung = str.upper(input(":"))
            if masukansamsung == "A":
                os.system('cls')
                jualhp()
            elif masukansamsung == "B":
                os.system('cls')
                jualhpharga()
            elif masukansamsung == "C":
                os.system('cls')
                kasir()
            elif masukansamsung in Daftarhp["Samsung"].keys():
                os.system('cls')
                Datahp.append(masukansamsung)
                konfirmasibeli()
            else:
                os.system('cls')
                print("masukan salah")

    elif pilihmerk == "merk lain":
        os.system('cls')
        i = 0
        while i == 0:
            for key,val in Daftarhp["Merk lain"].items():
                print("%s : ""Rp."" %s" % (key,val))
            
            print("""
                A. Tampilkan seluruh merk hp
                B. Pilih hp berdasarkan harga
                C. Kembali ke awal

                Ket: Masukan nama hp sesuai di tabel untuk pilih hp yang akan di beli 
            """)

            masukaniphone = str.upper(input(":"))
            if masukaniphone == "A":
                os.system('cls')
                jualhp()
            elif masukaniphone == "B":
                os.system('cls')
                jualhpharga()
            elif masukaniphone == "C":
                os.system('cls')
                kasir()
            elif masukaniphone in Daftarhp["Merk lain"].keys():
                os.system('cls')
                Datahp.append(masukaniphone)
                konfirmasibeli()
            else:
                os.system('cls')
                print("Masukan salah")
                
    else:
        os.system('cls')
        print("masukan anda salah, silakan isi kembali")
        jualhpmerk()
        
    
def konfirmasibeli():
    if Datahp[0] in Daftarhp["Samsung"].keys():
        print("Nama Hp :", Datahp[0])
        print("Harga Hp : Rp.", Daftarhp["Samsung"][Datahp[0]])
        print("Stok Hp :", Stokhp["Samsung"][Datahp[0]])
        print("""
        A. Jual Hp ini
        B. Pilih Hp lain
        C. Kembali ke awal
        """)
        masukan = str.upper(input(":"))
        if masukan == "A":
            os.system('cls')
            print("Apakah anda ingin menjual hp ini? (Y/N)")
            Konfirmasi = str.upper(input(":"))
            if Konfirmasi == "Y":
                os.system('cls')
                if Stokhp["Samsung"][Datahp[0]] > 0:
                    waktu = time.ctime()
                    print(waktu)
                    print("toko broku store 2rd")
                    print("Nama Hp :", Datahp[0])
                    print("Harga Hp : Rp.", Daftarhp["Samsung"][Datahp[0]])
                    print("Jumlah Bayar Total : Rp.", Daftarhp["Samsung"][Datahp[0]])
                    print("Terima kasih telah membeli di toko kami")
                    ubah = Stokhp["Samsung"][Datahp[0]] - 1
                    Stokhp["Samsung"].update({Datahp[0] : ubah})
                    Penjualan.append(Daftarhp["Samsung"][Datahp[0]])
                    input("Tekan enter untuk kembali ke kasir")
                    Datahp.clear()
                    os.system('cls')
                    kasir()
                else:
                    print("Mohon maaf hp ini tidak ada stoknya")
                    Datahp.clear()
                    jualhp()
            
            elif Konfirmasi == "N":
                os.system('cls')
                i = 0
                while i == 0:

                    print("""
                    A. Kembali ke daftar seluruh hp
                    B. Kembali ke kasir
                    """)
                    kembali = str.upper(input(":"))

                    if kembali == "A":
                        os.system('cls')
                        Datahp.clear()
                        jualhp()
                    elif kembali == "B":
                        os.system('cls')
                        Datahp.clear()
                        kasir()
                    else:
                        os.system('cls')
                        print("Masukan salah silakan coba kembali")


        elif masukan == "B":
            os.system('cls')
            Datahp.clear()
            jualhpmerk()
        elif masukan == "C":
            os.system('cls')
            Datahp.clear()
            jualhp()
        else:
            os.system('cls')
            print("masukan salah")
            konfirmasibeli()

    elif Datahp[0] in Daftarhp["Merk lain"].keys():
        print("Nama Hp :", Datahp[0])
        print("Harga Hp : Rp. ", Daftarhp["Merk lain"][Datahp[0]])
        print("Stok Hp :", Stokhp["Merk lain"][Datahp[0]])
        print("""
        A. Jual Hp ini
        B. Pilih Hp lain
        C. Kembali ke awal
        """)
        masukan = str.upper(input(":"))
        if masukan == "A":
            os.system('cls')
            print("Apakah anda ingin menjual hp ini? (Y/N)")
            Konfirmasi = str.upper(input(":"))
            if Konfirmasi == "Y":
                os.system('cls')
                if Stokhp["Merk lain"][Datahp[0]] > 0:
                    waktu = time.ctime()
                    print(waktu)
                    print("toko broku store 2rd")
                    print("Nama Hp :", Datahp[0])
                    print("Harga Hp : Rp. ", Daftarhp["Merk lain"][Datahp[0]])
                    print("Jumlah Bayar Total : Rp.", Daftarhp["Merk lain"][Datahp[0]])
                    print("Terima kasih telah membeli di toko kami")
                    ubah = Stokhp["Merk lain"][Datahp[0]] - 1
                    Stokhp["Merk lain"].update({Datahp[0] : ubah})
                    Penjualan.append(Daftarhp["Merk lain"][Datahp[0]])
                    Datahp.clear()
                    input("Tekan enter untuk kembali ke kasir")
                    os.system('cls')
                    kasir()
                else:
                    print("Mohon maaf hp ini tidak ada stoknya")
                    Datahp.clear()
                    jualhp()
            
            elif Konfirmasi == "N":
                os.system('cls')
                i = 0
                while i == 0:

                    print("""
                    A. Kembali ke daftar seluruh hp
                    B. Kembali ke kasir
                    """)
                    kembali = str.upper(input(":"))

                    if kembali == "A":
                        os.system('cls')
                        Datahp.clear()
                        jualhp()
                    elif kembali == "B":
                        os.system('cls')
                        Datahp.clear()
                        kasir()
                    else:
                        os.system('cls')
                        print("Masukan salah silakan coba kembali")

        elif masukan == "B":
            os.system('cls')
            Datahp.clear()
            jualhpmerk()
        elif masukan == "C":
            os.system('cls')
            Datahp.clear()
            jualhp()
        else:
            os.system('cls')
            print("masukan salah")
            konfirmasibeli()

    else:
        os.system('cls')
        print("data tidak ada")
                

def jualhpharga():
    print("toko broku store 2rd")
    print("======================")
    Samsung = sorted(Daftarhp["Samsung"].items(), key=lambda x: x[1])
    Merklain = sorted(Daftarhp["Merk lain"].items(), key=lambda x: x[1])
    for s in Samsung:
        print(s[0], s[1])
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
        os.system('cls')
        jualhp()
    elif masukan == "B":
        os.system('cls')
        jualhpmerk()
    elif masukan == "C":
        os.system('cls')
        kasir()
    elif masukan in Daftarhp["Samsung"].keys():
        os.system('cls')
        Datahp.append(masukan)
        konfirmasibeli()
    elif masukan in Daftarhp["Merk lain"].keys():
        os.system('cls')
        Datahp.append(masukan)
        konfirmasibeli()
    else:
        os.system('cls')
        print("Masukan salah")
        jualhpharga()
    
def belihp():
    for i in Merkhp:
        print(i)
    print("Pilih merk hp yang akan dibeli")
    print("Ketik kembali untuk kembali ke awal menu")
    masukan = str.lower(input(":"))
    if masukan == "samsung":
        os.system('cls')
        belihpsamsung()
    elif masukan == "merk lain":
        os.system('cls')
        belihpmerklain()
    elif masukan == "kembali":
        os.system('cls')
        kasir()
    else:
        os.system('cls')
        print("masukan salah")
        belihp()

def belihpsamsung():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        print("Ketik kembali untuk kembali ke awal menu")
        nama = str.upper(input(":"))
        if nama == "":
            os.system('cls')
            print("mohon masukan input dengan benar")
        elif nama == "KEMBALI":
            os.system('cls')
            belihp()
        else:
            os.system('cls')
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
            os.system('cls')
            print("harap masukan angka bukan huruf")
            belihpsamsung1()
        if harga > 0:
            os.system('cls')
            Datahp.append(harga)
            belihpsamsung2()
        elif harga == 000:
            os.system('cls')
            Datahp.clear()
            belihpsamsung()
        else:
            os.system('cls')
            print("masukan anda negatif atau bukan angka")
            belihpsamsung1()
        
def belihpsamsung2():
    print("Nama Hp : ", Datahp[0])
    print("Harga hp : Rp. ", Datahp[1])
    print("Apakah nama dan harga sudah sesuai? (konfirmasi kepada penjual) (Y/N)")
    finalisasi = str.upper(input(":"))
    if finalisasi == "Y":
        os.system('cls')
        waktu = time.ctime()
        print(waktu)
        print("toko broku store 2rd")
        print("Nama Hp :", Datahp[0])
        print("Harga hp : Rp.", Datahp[1])
        Pembelian.append(Datahp[1])
        Datahp.clear()
        print("terima kasih telah menjual di sini")
        input("Tekan enter untuk kembali ke menu kasir")
        os.system('cls')
        kasir()

    elif finalisasi == "N":
        os.system('cls')
        i = 0
        while i == 0:
            print("""
            A. Ubah nama
            B. Ubah harga
            C. Batalkan penbelian
            """)
            masukan = str.upper(input(":"))
            if masukan == "A":
                os.system('cls')
                belihpsamsung3()
            elif masukan == "B":
                os.system('cls')
                belihpsamsung4()
            elif masukan == "C":
                os.system('cls')
                i = 0
                while i == 0:
                    print("Apakah anda yakin untuk membatalkan (Y/N)")
                    batal = str.upper(input(":"))
                    if batal == "Y":
                        os.system('cls')
                        Datahp.clear()
                        print("pembelian dibatalkan")
                        os.system('cls')
                        kasir()
                    elif batal == "N":
                        os.system('cls')
                        belihpsamsung2()
                    else:
                        os.system('cls')
                        print("masukan salah")
            else:
                os.system('cls')
                print("Masukan salah")
    else:
        os.system('cls')
        print("masukan salah")
        belihpsamsung2()


def belihpsamsung3():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        nama = str.upper(input(":"))
        if nama == "":
            os.system('cls')
            print("mohon masukan input dengan benar")
        else:
            os.system('cls')
            Datahp[0] = nama
            belihpsamsung2()

def belihpsamsung4():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        try:
            harga = int(input(":"))
        except ValueError:
            os.system('cls')
            print("harap masukan angka bukan huruf")
            belihpsamsung4()
        if harga > 0:
            os.system('cls')
            Datahp[1] = harga
            belihpsamsung2()
        else:
            os.system('cls')
            print("masukan anda negatif atau bukan angka")    
            belihpsamsung4()            

def belihpmerklain():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        print("Ketik kembali untuk kembali ke awal menu")
        nama = str.upper(input(":"))
        if nama == "":
            os.system('cls')
            print("mohon masukan input dengan benar")
        elif nama == "KEMBALI":
            os.system('cls')
            belihp()
        else:
            os.system('cls')
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
            os.system('cls')
            print("harap masukan angka bukan huruf")
            belihpmerklain1()
        if harga > 0:
            os.system('cls')
            Datahp.append(harga)
            belihpmerklain2()
        elif harga == 000:
            os.system('cls')
            Datahp.clear()
            belihpmerklain()
        else:
            os.system('cls')
            print("masukan anda negatif atau bukan angka")
            belihpmerklain1()
        
def belihpmerklain2():
    print("Nama Hp : ", Datahp[0])
    print("Harga hp : Rp. ", Datahp[1])
    print("Apakah nama dan harga sudah sesuai? (konfirmasi kepada penjual) (Y/N)")
    finalisasi = str.upper(input(":"))
    if finalisasi == "Y":
        os.system('cls')
        waktu = time.ctime()
        print(waktu)
        print("toko broku store 2rd")
        print("Nama Hp : ", Datahp[0])
        print("Harga hp : Rp.", Datahp[1])
        Pembelian.append(Datahp[1])
        Datahp.clear()
        print("terima kasih telah menjual di sini")
        input("Tekan enter untuk kembali ke menu kasir")
        os.system('cls')
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
                os.system('cls')
                belihpmerklain3()
            elif masukan == "B":
                os.system('cls')
                belihpmerklain4()
            elif masukan == "C":
                os.system('cls')
                i = 0
                while i == 0:
                    print("Apakah anda yakin untuk membatalkan (Y/N)")
                    batal = str.upper(input(":"))
                    if batal == "Y":
                        os.system('cls')
                        Datahp.clear()
                        print("pembelian dibatalkan")
                        kasir()
                    elif batal == "N":
                        os.system('cls')
                        belihpmerklain2()
                    else:
                        os.system('cls')
                        print("masukan salah")
            else:
                os.system('cls')
                print("Masukan salah")
    else:
        os.system('cls')
        print("masukan salah")
        belihpmerklain2()


def belihpmerklain3():
    i = 0 
    while i == 0:
        print("Namahp? (pastikan tambahkan nama dengan merknya)")
        nama = str.upper(input(":"))
        if nama == "":
            os.system('cls')
            print("mohon masukan input dengan benar")
        else:
            os.system('cls')
            Datahp[0] = nama
            belihpmerklain2()

def belihpmerklain4():
    i = 0
    while i == 0:
        print("Harga hp? (pastikan sudah di diskusikan dan sepakat antara kedua pihak")
        try:
            harga = int(input(":"))
        except ValueError:
            os.system('cls')
            print("harap masukan angka bukan huruf")
            belihpmerklain4()
        if harga > 0:
            os.system('cls')
            Datahp[1] = harga
            belihpmerklain2()
        else:
            os.system('cls')
            print("masukan anda negatif atau bukan angka")
            belihpmerklain4()
    
user_login()