def biodata():

    Nama = []
    Namapanggilan = []
    Nim = []
    Univ = []
    Progstu = []
    Angkatan = []
    Tempattanggallahir = []
    Umur = []
    Tempattinggal = []
    Semester = []
    Berat = []
    Tinggi = []
    Citacita = []
    Nomortelp = []



    print("Selamat datang silakan isi biodata dibawah ini")
    print("==============================================")
    Nama = input("Nama lengkap : ") 
    Namapanggilan = input("Nama panggilan : ")
    Nim = int(input("NIM : "))
    Univ = input("Asal Universitas : ")
    Progstu = input("Program studi : ")
    Angkatan = int(input("Angkatan tahun : "))
    Tempattanggallahir = input("Tempat tanggal lahir :")
    Umur = int(input("Umur : ")) 
    Tempattinggal = input("Alamat tempat tinggal : ")
    Semester = int(input("Semester : "))
    Berat = float(input("Berat badan : "))
    Tinggi = float(input("Tinggi badan : "))
    Citacita = input("cita-cita : ")
    Nomortelp = int(input("Nomor telpon : "))

    as_nim =str(Nim)
    as_angkatan =str(Angkatan)
    as_umur =str(Umur)
    as_semester =str(Semester)
    as_berat =str(Berat)
    as_tinggi =str(Tinggi)
    as_nomortelp =str(Nomortelp)

    print("Biodata")
    print("=================================")
    print("Nama : " + Nama)
    print("Namapanggilan : " + Namapanggilan)
    print("Nim : " + as_nim)
    print("Asal Universitas : " + Univ)
    print("Program studi : " + Progstu)
    print("Angkatan tahun : " + as_angkatan)
    print("Tempat Tanggal Lahir : " + Tempattanggallahir)
    print("Umur : " + as_umur)
    print("Alamat Tempat Tinggal : " + Tempattinggal)
    print("Semester : " + as_semester)
    print("Berat Badan : "  + as_berat)
    print("Tinggi Badan : " + as_tinggi)
    print("cita-cita : "  + Citacita)
    print("Nomor Telepon : "  + as_nomortelp)

   
biodata()