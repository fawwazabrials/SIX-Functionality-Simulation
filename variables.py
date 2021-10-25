# Program init
# Spesifikasi program : intialisasi variabel-variabel yang akan digunakan
# Kumpulan variabel-variabel yang akan dipanggil pada program lain 

# KAMUS
# akun, absensi : list
# jadwal, sudahAbsen : dictionary
# nim, idx : int
# success : boolean

akun = [
    ["16521085", "16521095", "16521105", "16521115"],
    ["Austin Gabriel Pardosi", "Michael Leon Putra Widhi", "Muhamad Farhan Syakir", "Fawwaz Abrial Saffa"],
    ["pass1", "pass2", "pass3", "pass4"]
]

absensi = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

jadwal = {
    "senin" : [False, False, False],
    "selasa" : [False, False, False, False],
    "kamis" : [False, False, False],
    "jumat" : [False]
}

sudahAbsen= {
    "16521085" : {"senin" : [False, False, False],
    "selasa" : [False, False, False, False],
    "kamis" : [False, False, False],
    "jumat" : [False]},
    "16521095" : {"senin" : [False, False, False],
    "selasa" : [False, False, False, False],
    "kamis" : [False, False, False],
    "jumat" : [False]},
    "16521105" : {"senin" : [False, False, False],
    "selasa" : [False, False, False, False],
    "kamis" : [False, False, False],
    "jumat" : [False]},
    "16521115" : {"senin" : [False, False, False],
    "selasa" : [False, False, False, False],
    "kamis" : [False, False, False],
    "jumat" : [False]}
    }