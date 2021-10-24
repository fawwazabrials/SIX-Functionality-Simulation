import fungsisix as fs
import init as var
import time
import sys

# login screen
pilihLogin = fs.login()
if(pilihLogin == 0):
    print("Dadah, sampai jumpa lagi! :D")
    fs.wait(5)
    fs.exitProgram()

if(pilihLogin == 1): # Login dengan akun INA
    var.nim, var.idx, var.success = fs.loginAuthentication(var.akun)
    if(var.success):
        print("Login berhasil!")
        print("Selamat datang di SI-eks!")
        fs.wait(2)
    fs.SIX(var.akun, var.nim, var.idx, var.absensi, var.sudahAbsen)

elif(pilihLogin == 2): # Add account
    print("ADD ACCOUNT")
    nama = input("Masukan nama anda: ")
    nim_baru = input("Masukan NIM ada: ")
    pswd_baru = input("Masukan password anda: ")
    var.akun[0].append(nim_baru)
    var.akun[1].append(nama)
    var.akun[2].append(pswd_baru)
    var.absensi.append([0, 0, 0, 0, 0, 0])
    var.sudahAbsen[nim_baru] = var.jadwal
    print("\nAkun anda sudah dibuat!")
    x = input("Tekan enter untuk kembali ke menu login")
    fs.loginInf(var.akun, var.nim, var.idx, var.absensi, var.sudahAbsen)


elif(pilihLogin == 3): # Print akun yang terdaftar
    print("NIM\t\tPassword")
    for i in range(len(var.akun[0])):
        print("{}\t{}".format(var.akun[0][i], var.akun[2][i]))
    x = input("Tekan enter untuk kembali ke menu login")
    fs.loginInf(var.akun, var.nim, var.idx, var.absensi, var.sudahAbsen)



