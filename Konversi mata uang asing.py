
def menu():

   print("Konversi mata uang rupiah ke mata uang asing")
   print("Pilih mata uang asing yang akan dikonversi  ")
   print("============================================")
   print("1. IDR TO USD")
   print("2. IDR TO SGD")
   print("3. IDR TO EUR")
   print("4. IDR TO JPY")
    
def idrtousd():
    print("============================================")
    idr = float(input("Masukan jumlah mata uang rupiah : "))
    print("============================================")
    usd = 0.000071
    hasil1 = idr * usd
    print(round(hasil1,2))

def idrtosgd():
    print("============================================")
    idr = float(input("Masukan jumlah mata uang rupiah : "))
    print("============================================")
    sgd = 0.000095
    hasil2 = idr * sgd
    print(round(hasil2,2))

def idrtoeur():
    print("============================================")
    eur = 0.000061
    idr = float(input("Masukan jumlah mata uang rupiah : "))
    print("============================================")
    hasil3 = idr * eur
    print(round(hasil3,2))

def idrtojpy():
    print("============================================")
    jpy = 0.0081
    idr = float(input("Masukan jumlah mata uang rupiah : "))
    print("============================================")
    hasil4 = idr * jpy
    print(round(hasil4,2))


menu()
masukan = input("Silakan pilih mata uang yang akan di konversi : ")

if masukan == ("1"):
    idrtousd()
elif masukan == ("2"):
    idrtosgd()
elif masukan == ("3"):
    idrtoeur()
elif masukan == ("4"):
    idrtojpy()
