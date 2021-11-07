# Program fungsisix
# Spesifikasi program : Kumpulan fungsi dan prosedur yang akan dipanggil pada program lain 

# ALGORITMA
# import module os, sys, dan time
import os
import sys
import time

def goBackEnter():
    x = input("Tekan enter untuk kembali")
    return 0

def wait(i):
	# Spesifikasi program : Menahan waktu dengan jumlah detik sesuai dengan argumen

	# KAMUS LOKAL
	# i : float

	# ALGORITMA  
	time.sleep(i)

def clearScreen():
	# Spesifikasi program : Menghapus semua output yang sudah di-print

	# ALGORITMA  
	os.system('cls') #change to 'clear' when using macOS or linux

def clearLast():
	# Spesifikasi program : Menghapus output yang di-print terakhir

	# ALGORITMA  
	sys.stdout.write('\x1b[1A')
	sys.stdout.write('\x1b[2K')

def pilihLogin():
	# Spesifikasi program : Memilih menu pada login

	# KAMUS LOKAL
	# pilih : int

	# ALGORITMA 
	print('''
-------------------------------
Selamat datang di SI-eks!
-------------------------------
Pilih menu:
1. Login
2. Daftar Akun
3. Akun yang terdaftar
0. Keluar Program
			''')
	pilih = input("Pilih nomor menu: ")
	if(not(pilih.isnumeric()) or int(pilih) < 0 or int(pilih) > 3):
		clearScreen()
		print("Menu tidak terdaftar! Silahkan coba lagi")
		pilih = pilihLogin()
	return(int(pilih))

def pilihSIX():
    print('''
Pilih menu :
1. Status Mahasiswa
2. Kelas
3. Control Panel
0. Sign out
			''')
    pilih = input("Pilih nomor menu: ")
    if(not(pilih.isnumeric()) or int(pilih) < 0 or int(pilih) > 3):
        clearScreen()
        print("Menu tidak terdaftar! Silahkan coba lagi")
        pilih = pilihSIX()
    return(int(pilih))

def SIX(akun, sudah, absen, idx):
    pilih = 100
    while(pilih != 0):
        pilih = pilihSIX()
        if(pilih == 1):
            statusMahasiswa(akun, absen, idx)
        elif(pilih == 2):
            kelas(sudah, absen, akun, idx)
        elif(pilih == 3):
            controlPanel(akun, idx)

def statusMahasiswa(akun, absen, idx):
    print('''
Data Mahasiswa
Nama\t : {}
NIM\t : {}
'''.format(akun[1][idx], akun[0][idx]))

    print('''
Rekap Absensi Semester 1	
No\tMata Kuliah\t\tKehadiran
1\tFisika Dasar IA\t\t{}%
2\tOlahraga\t\t{}%
3\tTTKI\t\t\t{}%
4\tBahasa Inggris\t\t{}%
5\tPengKom\t\t\t{}%
6\tMatematika IA\t\t{}%
'''.format(round(absen[idx][0]*100/3, 2), round(absen[idx][1]*100/1, 2), round(absen[idx][2]*100/1, 2), round(absen[idx][3]*100/1, 2), round(absen[idx][4]*100/2, 2), round(absen[idx][5]*100/3, 2)))

    goBackEnter()
    clearScreen()

def pilihKelasHari():
    print('''
1. Senin
2. Selasa
3. Rabu
4. Kamis
5. Jumat
0. Go back
	''')
    pilihKelas = input("Pilih nomor menu: ")
    if(not(pilihKelas.isnumeric()) or int(pilihKelas)>5 or int(pilihKelas)<0):
        clearScreen()
        print("Menu tidak tersedia!")
        pilihKelas = pilihKelas()
    return(int(pilihKelas))

def absensi(absen, sudah, akun, hari, idx_dihari, idx_matkul, idx):
    nim = akun[0][idx]
    if(sudah[nim][hari][idx_dihari]):
        print("Anda sudah absen di mata kuliah ini")
        wait(1)
        clearScreen()
    else:
        sudah[nim][hari][idx_dihari] = True
        absen[idx][idx_matkul] += 1
        print("Absen berhasil dicatat!")
        wait(1)
        clearScreen()

def kelas(sudah, absen, akun, idx):
    pilih = 100
    while(pilih != 0):
        pilih = pilihKelasHari()
        if(pilih == 1):
            print('''
1. Fisika Dasar IA
2. Matematika IA
3. Pengenalan Komputasi
            ''')
            try:
                pilihMatkul = int(input("Pilih nomor mata kuliah: "))
            except ValueError:
                pass
            if(pilihMatkul>3 or pilihMatkul<1):
                pass
            else:
                # senin - fisika
                if(pilihMatkul == 1):
                    absensi(absen, sudah, akun, "senin", 0, 0, idx)

                # senin - matematika
                elif(pilihMatkul == 2):
                    absensi(absen, sudah, akun, "senin", 1, 5, idx)

                # senin - pengkom
                elif(pilihMatkul == 3):
                    absensi(absen, sudah, akun, "senin", 2, 4, idx)
            clearScreen()

        elif(pilih == 2):
            print('''
1. Pengenalan Komputasi
2. Matematika IA
3. Fisika Dasar IA
4. Olaharaga
            ''')
            try:
                pilihMatkul = int(input("Pilih nomor mata kuliah: "))
            except ValueError:
                pass
            if(pilihMatkul>4 or pilihMatkul<1):
                pass
            else:
                # selasa - pengkom
                if(pilihMatkul == 1):
                    absensi(absen, sudah, akun, "selasa", 0, 4, idx)

                # selasa - matematika
                elif(pilihMatkul == 2):
                    absensi(absen, sudah, akun, "selasa", 1, 5, idx)

                # selasa - fisika
                elif(pilihMatkul == 3):
                    absensi(absen, sudah, akun, "selasa", 2, 0, idx)

                # selasa - olahraga
                elif(pilihMatkul == 4):
                    absensi(absen, sudah, akun, "selasa", 3, 1, idx)
            clearScreen()

        elif(pilih == 3):
            print("Tidak ada kelas di hari Rabu")
            wait(1)
            clearScreen()
    
        elif(pilih == 4):
            print('''
1. Fisika Dasar IA
2. Matematika IA
3. Bahasa Inggris
            ''')
            try:
                pilihMatkul = int(input("Pilih nomor mata kuliah: "))
            except ValueError:
                pass
            if(pilihMatkul>3 or pilihMatkul<1):
                pass
            else:
                # kamis - fisika
                if(pilihMatkul == 1):
                    absensi(absen, sudah, akun, "kamis", 0, 0, idx)

                # kamis - matematika
                if(pilihMatkul == 2):
                    absensi(absen, sudah, akun, "kamis", 1, 5, idx)

                # kamis - bahasa inggris
                if(pilihMatkul == 3):
                    absensi(absen, sudah, akun, "kamis", 2, 3, idx)
            clearScreen()

        elif(pilih == 5):
            print('''
1. Tata Tulis Karya Ilmiah
            ''')
            try:
                pilihMatkul = int(input("Pilih nomor mata kuliah: "))
            except ValueError:
                pass
            if(pilihMatkul>1 or pilihMatkul<1):
                pass
            else:
                # jumat - ttki
                if(pilihMatkul == 1):
                    absensi(absen, sudah, akun, "jumat", 0, 2, idx)
            clearScreen()

def pilihControlPanel(akun, idx):
    print('''
AKUN INA
NIM\t: {}
Password\t: {}

Pilih menu:
1. Ganti password
0. Go back
			'''.format(akun[0][idx], akun[2][idx]))
    pilih = input("Pilih nomor menu: ")
    if(not(pilih.isnumeric()) or int(pilih)>1 or int(pilih)<0):
        clearScreen()
        print("Menu tidak terdaftar! Silahkan coba lagi")
        pilih = pilihControlPanel(akun, idx)
    return(int(pilih))

def gantiPassword(akun, idx):
    newPass = input("Masukan password baru: ")
    akun[2][idx] = newPass
    print("Password berhasil diganti!")
    goBackEnter()
    clearScreen()

def controlPanel(akun, idx):
    pilih = 100
    while(pilih != 0):
        pilih = pilihControlPanel(akun, idx)
        if(pilih == 1):
            gantiPassword(akun, idx)