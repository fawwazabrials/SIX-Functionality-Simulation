import os
import sys
import time

def clearScreen():
	os.system('cls') #change to 'cls' when using windows

def clearLast():
	sys.stdout.write('\x1b[1A')
	sys.stdout.write('\x1b[2K')

def getIndex(akun, nim):
    return akun[0].index(nim)

def absensi(absen, sudah, hari, idx_dihari, idx_matkul, akun, nim, idx):
	if(sudah[nim][hari][idx_dihari]):
		print("Anda sudah absen di mata kuliah ini")
		time.sleep(1)
		absensiSimulasi(akun, nim, idx, absen, sudah)
	sudah[nim][hari][idx_dihari] = True
	absen[idx][idx_matkul] += 1
	print("Absen berhasil dicatat!")
	time.sleep(1)
	absensiSimulasi(akun, nim, idx, absen, sudah)


def login():
	print('''
-------------------------------
Selamat datang di SI-eks!
-------------------------------
Pilih menu:
1. Login
2. Daftar Akun
3. Akun yang terdaftar
			''')
	pilih = int(input("Pilih nomor menu: "))
	if(pilih < 1 or pilih > 3):
		clearScreen()
		print("Menu tidak terdaftar! Silahkan coba lagi")
		pilih = login()
	return(pilih)



def SIX(akun, nim, idx, absen, sudah):
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
	else:
		pass



def statusMahasiswaSimulation(akun, nim, idx, absen, sudah):
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
'''.format(round(absen[idx][0]*100/3, 2), round(absen[idx][1]*100/1, 2),
round(absen[idx][2]*100/1, 2), round(absen[idx][3]*100/1, 2), 
round(absen[idx][4]*100/2, 2), round(absen[idx][5]*100/3, 2)))

	print("Tekan enter untuk kembali ke menu utama")
	pilihStatusMhssw = input()
	SIX(akun, nim, idx, absen, sudah)



def absensiSimulasi(akun, nim, idx, absen, sudah):
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
		time.sleep(1)
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
		time.sleep(1)
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
		time.sleep(1)
		SIX(akun, nim, idx, absen, sudah)


def controlPanelSimulation(akun, nim, idx, absen, sudah):
    pilihCtrl = pilihControlPanel(nim,akun[2][idx])
    if(pilihCtrl == 0):
        SIX(akun, nim, idx, absen, sudah)
    else:
        gantiPass(nim, akun)
        pilihControlPanel(nim,akun[2][idx])

def pilihControlPanel(akun, nim, idx, absen, sudah):
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
        pilihCtrl = pilihControlPanel(nim, akun[2][idx])
    return(pilihCtrl)

def gantiPass(akun, nim, idx, absen, sudah):
    newPass = input("Masukan password baru: ")
    akun[2][idx] = newPass
    print("Password berhasil diganti!")
