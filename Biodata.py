def biodata():

    biodata = []


    print("Selamat datang silakan isi biodata dibawah ini")
    print("==============================================")
    Nama = input("Nama lengkap : ") 
    biodata.append(Nama)
    Namapanggilan = input("Nama panggilan : ")
    biodata.append(Namapanggilan)
    Nim = int(input("NIM : "))
    biodata.append(Nim)
    Univ = input("Asal Universitas : ")
    biodata.append(Univ)
    Progstu = input("Program studi : ")
    biodata.append(Progstu)
    Angkatan = int(input("Angkatan tahun : "))
    biodata.append(Angkatan)
    Tempattanggallahir = input("Tempat tanggal lahir :")
    biodata.append(Tempattanggallahir)
    Umur = int(input("Umur : ")) 
    biodata.append(Umur)
    Tempattinggal = input("Alamat tempat tinggal : ")
    biodata.append(Tempattinggal)
    Semester = int(input("Semester : "))
    biodata.append(Semester)
    Berat = float(input("Berat badan : "))
    biodata.append(Berat)
    Tinggi = float(input("Tinggi badan : "))
    biodata.append(Tinggi)
    Citacita = input("cita-cita : ")
    biodata.append(Citacita)
    Nomortelp = int(input("Nomor telpon : "))
    biodata.append(Nomortelp)


    print("Loading......")
    print("=================================")
    print("Biodata anda")
    print("=================================")
    print("Nama : ", biodata[0])
    print("Namapanggilan : ", biodata[1])
    print("Nim : ", biodata[2])
    print("Asal Universitas : ", biodata[3])
    print("Program studi : ", biodata[4])
    print("Angkatan tahun : ", biodata[5])
    print("Tempat Tanggal Lahir : ", biodata[6])
    print("Umur : ", biodata[7])
    print("Alamat Tempat Tinggal : ", biodata[8])
    print("Semester : ", biodata[9])
    print("Berat Badan : ", biodata[10])
    print("Tinggi Badan : ", biodata[11])
    print("cita-cita : ", biodata[12])
    print("Nomor Telepon : ", biodata[13])
    print("===================================")
    print("Terima kasih telah mengunakan program ini!")


   
biodata()