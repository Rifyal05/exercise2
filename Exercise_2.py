# exercise
# Buatlah sebuah program Python untuk menyimpan informasi tentang sebuah buku. Buku tersebut memiliki atribut sebagai berikut: Judul buku Tahun terbit Harga Penulis Ketersediaan di perpustakaan Simpan juga data berbentuk list Tipe Data yang Digunakan: String, Integer, Float, Boolean, List

judul_buku= ''
input_judul = input('masukan judul buku : ')
judul_buku= str(input_judul)
print("Judul buku : " , judul_buku)

tahun_terbit= 0
input_tahun= input('masukan tahun terbit : ')
tahun_terbit= int(input_tahun)
print('tahun terbit :', tahun_terbit)

harga_buku= 0
input_harga= float(input('Masukan harga buku : '))
harga_buku= float(input_harga)
print('Harga buku adalah : ', harga_buku)

penulis= ''
input_penulis= input('masukan nama penulis : ')
penulis= str(input_penulis)
print('Nama Penulis : ' + penulis)

status_ketersediaan = ''
input_status = bool(input('Masukan informasi ketersediaan : (True/False) : '))
status_ketersediaan = bool(input_status)
print('status ketersediaan : ' + str(bool(status_ketersediaan)))

input_ketersediaan = input('apakah ingin menampilkan data lengkap? : Ya/Tidak : ')
input_ketersediaan = input_ketersediaan.capitalize()

if input_ketersediaan == 'Ya':
    print()
    print('Informasi lengkap dari buku : ')
    print('Judul Buku   : ', judul_buku)
    print('Tahun Terbit : ', tahun_terbit)
    print('Harga buku   : ' , harga_buku)
    print('penulis      : ', penulis )
    print('ketersediaan : ' , str(bool(status_ketersediaan)))
else:
    print("Baiklah")
