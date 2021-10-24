# Program fungsisix
# Spesifikasi program : Kumpulan fungsi dan prosedur yang akan dipanggil pada program lain 

# ALGORITMA
# import module os, sys, dan time
import os
import sys
import time

def wait(i):
	# Spesifikasi program : Menahan waktu dengan jumlah detik sesuai dengan argumen

	# KAMUS LOKAL
	# i : float

	# ALGORITMA  
	time.sleep(i)

def exitProgram():
	# Spesifikasi program : Keluar dari program

	# ALGORITMA  
	sys.exit()

def clearScreen():
	# Spesifikasi program : Menghapus semua output yang sudah di-print

	# ALGORITMA  
	os.system('cls') #change to 'clear' when using macOS or linux

def clearLast():
	# Spesifikasi program : Menghapus output yang di-print terakhir

	# ALGORITMA  
	sys.stdout.write('\x1b[1A')
	sys.stdout.write('\x1b[2K')

def getIndex(akun, nim):
	# Spesifikasi program : Mendapatkan indeks NIM di dalam list akun

	# KAMUS LOKAL
	# akun : list
	# nim : int

	# ALGORITMA  
    return akun[0].index(nim)

def absensi(absen, sudah, hari, idx_dihari, idx_matkul, akun, nim, idx):
	# Spesifikasi program : Mencatat absen pada mata kuliah di hari tertentu

	# KAMUS LOKAL
	# akun : list
	# absen, sudah : dictionary
	# idx_dihari, idx_matkul, idx : int
	# hari, nim : string

	# ALGORITMA 
	if(sudah[nim][hari][idx_dihari]):
		print("Anda sudah absen di mata kuliah ini")
		wait(1)
		absensiSimulasi(akun, nim, idx, absen, sudah)
	sudah[nim][hari][idx_dihari] = True
	absen[idx][idx_matkul] += 1
	print("Absen berhasil dicatat!")
	wait(1)
	absensiSimulasi(akun, nim, idx, absen, sudah)

def login():
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
	pilih = int(input("Pilih nomor menu: "))
	if(pilih < 0 or pilih > 3):
		clearScreen()
		print("Menu tidak terdaftar! Silahkan coba lagi")
		pilih = login()
	return(pilih)

def loginAuthentication(akun):
	# Spesifikasi program : Cek apabila kredensial login terdaftar dalam sistem

	# KAMUS LOKAL
	# akun : list
	# success : boolean
	# tries, idx : int
	# nim, pswd : string

	# ALGORITMA 
	success = False
	nim = ''
	pswd = ''
	tries = 0
	while(nim not in akun[0]):
		nim = input("Masukan NIM akun INA: ")
		if(nim not in akun[0]):
			clearLast()
			print("Tidak ada akun yang terdaftar dengan NIM tersebut. Coba lagi!")

	idx = getIndex(akun, nim)
	while(tries < 3):
		tries += 1
		pswd = input("Masukan password anda: ")
		if(pswd == akun[2][idx]):
			success = True
			break
		else:
			clearLast()
			print("Password salah!")
	return(nim, idx, success)

def loginInf(akun, nim, idx, absen, sudahAbsen):
	# Spesifikasi program : Menyimulasikan sistem menu login SIX

	# KAMUS LOKAL
	# akun : list
	# absen, sudahAbsen : dictionary
	# idx, pilihLogin : int
	# nim, nama, nim_baru, pswd_baru, x : string
	# success : boolean

	# ALGORITMA 
	print(idx)
	pilihLogin = login()
	if(pilihLogin == 0):
		print("Dadah, sampai jumpa lagi! :D")
		wait(5)
		exitProgram()

	if(pilihLogin == 1): # Login dengan akun INA
		nim, idx, success = loginAuthentication(akun)
		if(success):
			print("Login berhasil!")
			print("Selamat datang di SI-eks!")
			wait(3)
		try:
			return(0)
		finally:
			SIX(akun, nim, idx, absen, sudahAbsen)

	elif(pilihLogin == 2): # Add account
		print("ADD ACCOUNT")
		nama = input("Masukan nama anda: ")
		nim_baru = input("Masukan NIM ada: ")
		pswd_baru = input("Masukan password anda: ")
		akun[0].append(nim_baru)
		akun[1].append(nama)
		akun[2].append(pswd_baru)
		absen.append([0, 0, 0, 0, 0, 0])
		sudahAbsen[nim_baru] = {"senin" : [False, False, False],
								"selasa" : [False, False, False, False],
								"kamis" : [False, False, False],
								"jumat" : [False]}
		print("\nAkun anda sudah dibuat!")
		x = input("Tekan enter untuk kembali ke menu login")
		loginInf(akun, nim, idx, absensi, sudahAbsen)

	elif(pilihLogin == 3): # Print akun yang terdaftar
		print("NIM\t\tPassword")
		for i in range(len(akun[0])):
			print("{}\t{}".format(akun[0][i], akun[2][i]))
		x = input("Tekan enter untuk kembali ke menu login")
		try:
			return(0)
		finally:
			loginInf(akun, nim, idx, absen, sudahAbsen)

def SIX(akun, nim, idx, absen, sudah):
	# Spesifikasi program : Menyimulasikan sistem menu utama SIX

	# KAMUS LOKAL
	# akun : list
	# absen, sudah : dictionary
	# idx, pilihSIX : int
	# nim : string

	# ALGORITMA 
	clearScreen()

	print('''
Pilih menu :
1. Status Mahasiswa
2. Kelas
3. Control Panel
0. Sign out
			''')
	pilihSIX = int(input("Pilih nomor menu: "))
	if(pilihSIX == 1): # status mahasiswa
		statusMahasiswaSimulation(akun, nim, idx, absen, sudah)
	elif(pilihSIX == 2): # absen / kelas
		absensiSimulasi(akun, nim, idx, absen, sudah)
	elif(pilihSIX == 3): # control panel
		controlPanelSimulation(akun, nim, idx, absen, sudah)
	else: # back to login
		try:
			return(0)
		finally:
			loginInf(akun, nim, idx, absen, sudah)

def statusMahasiswaSimulation(akun, nim, idx, absen, sudah):
	# Spesifikasi program : Menyimulasikan sistem menu status mahasiswa (rekap absensi)

	# KAMUS LOKAL
	# akun : list
	# absen, sudah : dictionary
	# idx : int
	# nim, x : string

	# ALGORITMA 
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

	print("Tekan enter untuk kembali ke menu utama")
	x = input()
	try:
		return(0)
	finally:
		SIX(akun, nim, idx, absen, sudah)

def absensiSimulasi(akun, nim, idx, absen, sudah):
	# Spesifikasi program : Memilih mata kuliah yang ingin di-Tandai Hadir

	# KAMUS LOKAL
	# akun : list
	# absen, sudah : dictionary
	# idx, pilihAbsen, pilihMatkul : int
	# nim, x : string

	# ALGORITMA 
	clearScreen()
	print('''
1. Senin
2. Selasa
3. Rabu
4. Kamis
5. Jumat
0. Go back
	''')
	pilihAbsen = int(input("Pilih nomor menu: "))
	while(pilihAbsen>5 or pilihAbsen<0):
		pilihAbsen = int(input("Menu tidak tersedia! Pilih nomor menu: "))
		wait(1)
# SENIN
	if(pilihAbsen==1):
		print('''
1. Fisika Dasar IA
2. Matematika IA
3. Pengenalan Komputasi
	''')
		pilihMatkul = int(input("Pilih nomor mata kuliah: "))
		if(pilihMatkul>3 or pilihMatkul<1):
			absensiSimulasi(akun, nim, idx, absen, sudah)
		else:
			# senin - fisika
			if(pilihMatkul == 1):
				absensi(absen, sudah, "senin", 0, 0, akun, nim, idx)

			# senin - matematika
			elif(pilihMatkul == 2):
				absensi(absen, sudah, "senin", 1, 5, akun, nim, idx)

			# senin - pengkom
			elif(pilihMatkul == 3 and not(sudah[nim]["senin"][2])):
				absensi(absen, sudah, "senin", 2, 4, akun, nim, idx)

# SELASA
	elif(pilihAbsen==2):
		print('''
1. Pengenalan Komputasi
2. Matematika IA
3. Fisika Dasar IA
4. Olaharaga
	''')
		pilihMatkul = int(input("Pilih nomor mata kuliah: "))
		if(pilihMatkul>4 or pilihMatkul<1):
			absensiSimulasi(akun, nim, idx, absen, sudah)
		else:
			# selasa - pengkom
			if(pilihMatkul == 1):
				absensi(absen, sudah, "selasa", 0, 4, akun, nim, idx)

			# selasa - matematika
			elif(pilihMatkul == 2):
				absensi(absen, sudah, "selasa", 1, 5, akun, nim, idx)

			# selasa - fisika
			elif(pilihMatkul == 3):
				absensi(absen, sudah, "selasa", 2, 0, akun, nim, idx)

			# selasa - olahraga
			elif(pilihMatkul == 4):
				absensi(absen, sudah, "selasa", 3, 1, akun, nim, idx)

# RABU
	elif(pilihAbsen==3):
		print("Tidak ada absen di hari Rabu")
		wait(1)
		absensiSimulasi(akun, nim, idx, absen, sudah)

# KAMIS
	elif(pilihAbsen==4):
		print('''
1. Fisika Dasar IA
2. Matematika IA
3. Bahasa Inggris
	''')
		pilihMatkul = int(input("Pilih nomor mata kuliah: "))
		if(pilihMatkul>3 or pilihMatkul<1):
			absensiSimulasi(akun, nim, idx, absen, sudah)
		else:
			# kamis - fisika
			if(pilihMatkul == 1):
				absensi(absen, sudah, "kamis", 0, 0, akun, nim, idx)

			# kamis - matematika
			if(pilihMatkul == 2):
				absensi(absen, sudah, "kamis", 1, 5, akun, nim, idx)

			# kamis - bahasa inggris
			if(pilihMatkul == 3):
				absensi(absen, sudah, "kamis", 2, 3, akun, nim, idx)

# JUMAT
	elif(pilihAbsen==5):
		print('''
1. Tata Tulis Karya Ilmiah
	''')
		pilihMatkul = int(input("Pilih nomor mata kuliah: "))
		if(pilihMatkul>1 or pilihMatkul<1):
			absensiSimulasi(akun, nim, idx, absen, sudah)
		else:
			# jumat - ttki
			if(pilihMatkul == 1):
				absensi(absen, sudah, "jumat", 0, 2, akun, nim, idx)
	else:
		wait(1)
		try:
			return(0)
		finally:
			SIX(akun, nim, idx, absen, sudah)


def controlPanelSimulation(akun, nim, idx, absen, sudah):
	# Spesifikasi program : Menyimulasikan sistem menu status control panel (ubah password)

	# KAMUS LOKAL
	# akun : list
	# absen, sudah : dictionary
	# idx, pilihCtrl : int
	# nim: string

	# ALGORITMA 
	pilihCtrl = pilihControlPanel(akun, nim, idx, absen, sudah)
	if(pilihCtrl == 0):
		try:
			return(0)
		finally:
			SIX(akun, nim, idx, absen, sudah)
	elif(pilihCtrl == 1):
		gantiPass(akun, nim, idx, absen, sudah)
		pilihControlPanel(akun, nim, idx, absen, sudah)

def pilihControlPanel(akun, nim, idx, absen, sudah):
	# Spesifikasi program : Memilih menu pada control panel

	# KAMUS LOKAL
	# akun : list
	# absen, sudah : dictionary
	# idx, pilihCtrl : int
	# nim: string

	# ALGORITMA 
    clearScreen()
    print('''
AKUN INA
NIM\t: {}
Password\t: {}

Pilih menu:
1. Ganti password
0. Go back
			'''.format(nim, akun[2][idx]))
    pilihCtrl = int(input("Pilih nomor menu: "))
    if(pilihCtrl>1 or pilihCtrl<0):
        clearScreen()
        print("Menu tidak terdaftar! Silahkan coba lagi")
        pilihCtrl = pilihControlPanel(nim, akun[2][idx], idx, absen, sudah)
    return(pilihCtrl)

def gantiPass(akun, nim, idx, absen, sudah):
	# Spesifikasi program : Mengganti password INA

	# KAMUS LOKAL
	# akun : list
	# absen, sudah : dictionary
	# idx : int
	# nim, newPass, x : string

	# ALGORITMA 
	newPass = input("Masukan password baru: ")
	akun[2][idx] = newPass
	print("Password berhasil diganti!")
	x = input("Tekan enter untuk kembali")
	controlPanelSimulation(akun, nim, idx, absen, sudah)
