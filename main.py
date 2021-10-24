import fungsisix as fs

# background work
akun = [
    ["16521085", "16521095", "16521105", "16521115", "test"],
    ["Austin Gabriel Pardosi", "Michael Leon Putra Widhi", "Muhamad Farhan Syakir", "Fawwaz Abrial Saffa", "admin"],
    ["pass1", "pass2", "pass3", "pass4", "test"]
]

absensi = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

jadwal = {
    "senin" : [False, False, False],
    "selasa" : [False, False, False, False],
    "kamis" : [False, False, False],
    "jumat" : [False]
}

sudahAbsen = {
    "16521085" : jadwal,
    "16521095" : jadwal,
    "16521105" : jadwal,
    "16521115" : jadwal,
    "test" : jadwal
    }

# login screen
pilihLogin = fs.login()
if(pilihLogin == 1): #Login dengan akun INA
    nim = ''
    pswd = ''
    tries = 0

    # Check ada akun terdaftar atau tidak
    while(nim not in akun[0]):
        nim = input("Masukan NIM akun INA: ")
        if(nim not in akun[0]):
            fs.clearLast()
            print("Tidak ada akun yang terdaftar dengan NIM tersebut. Coba lagi!")

    idx = fs.getIndex(akun, nim)
    while(tries < 3):
        tries += 1
        pswd = input("Masukan password anda: ")
        if(pswd != akun[2][idx]):
            fs.clearLast()
            print("Password salah!")
        else:
            print("Login berhasil!\n\n")
            break

    fs.SIX(akun, nim, idx, absensi, sudahAbsen)