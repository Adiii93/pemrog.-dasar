mhs = input("apakah anda mahasiswa teknik? Y/N :")
if mhs == "Y":
    print ("1. teknik informatika\n2. teknik mesin\n3. teknik industri")
    kode = int(input("masukkan kode:"))
    if (kode == 1):
        print ("anda adalah mahasiswa teknik informatika")
    elif (kode == 2):
        print ("anda adlah mahasiswa teknik mesin")
    elif (kode == 3):
        print ("anda adalah mahasiswa teknik industri")
    else :
        print ("tidak ada")
else:
    print ("salah jurusan")
