# Program main
# SIMULASI KERJA SIX
# Spesifikasi program : Program utama simulasi SIX 

# KAMUS
# nama, nim_baru, pswd_baru : string
# pilihLogin : int

# ALGORITMA
# import fungsi, prosedur, dan variabel buatan dari file fungsisix.py dan variables.py
import fungsisix as fs
import variables as var

pilihLogin = 100
while(pilihLogin != 0):
    fs.clearScreen()
    pilihLogin = fs.pilihLogin()
    if(pilihLogin == 1):
        nim = " "
        password = ""
        success = False
        tries = 0
        while(nim not in var.akun[0] or nim == ""):
            nim = input("Masukan NIM akun INA: ")
            if(nim not in var.akun[0]):
                fs.clearLast
                print("Tidak ada akun yang terdaftar dengan NIM tersebut. Coba lagi! (tekan enter untuk kembali)")
            
        idx = var.akun[0].index(nim)
        while(tries < 3):
            tries += 1
            password = input("Masukan password anda: ")
            if(password == var.akun[2][idx]):
                success = True
                break
            fs.clearLast()
            print("Password salah!")

        if(success): fs.SIX(var.akun, var.sudahAbsen, var.absensi, idx)
        else: print("Jika lupa password silahkan hubungi DitSTI")

    elif(pilihLogin == 2):
        print("ADD ACCOUNT")
        nama = input("Masukan nama anda: ")
        nim_baru = input("Masukan NIM ada: ")
        pswd_baru = input("Masukan password anda: ")
        var.akun[0].append(nim_baru)
        var.akun[1].append(nama)
        var.akun[2].append(pswd_baru)
        var.absensi.append([0, 0, 0, 0, 0, 0])
        var.sudahAbsen[nim_baru] = {"senin" : [False, False, False],
                                    "selasa" : [False, False, False, False],
                                    "kamis" : [False, False, False],
                                    "jumat" : [False]}
        print("\nAkun anda sudah dibuat!")
        fs.goBackEnter()

    elif(pilihLogin == 3):
        print("NIM\tPassword")
        for i in range(len(var.akun[0])):
            print("{}\t{}".format(var.akun[0][i], var.akun[2][i]))
        fs.goBackEnter()

# exit program
print("Dadah, sampai jumpa lagi! :D")
fs.wait(1)