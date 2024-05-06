judul_buku = ''
input_judul = input("masukan judul buku : ")
judul_buku = str(input_judul)
print("judul buku : ", judul_buku)

tahun_terbit= 0
input_tahun = input("masukan tahun terbit : ")
tahun_terbit = int(input_tahun)
print('tahun terbit : ', tahun_terbit)

harga_buku = 0
input_harga = input("masukan harga buku : ")
harga_buku = float(input_harga)
print("harga buku : ", harga_buku)

penulis = ''
input_nama = input("masukan nama penulis : ")
penulis = str(input_nama)
print('penulis : ' , penulis)


status_ketersediaan = ''
while True:
    input_ketersediaan = input("Masukkan status ketersediaan (True/False): ").capitalize()
    if input_ketersediaan in ("True", "False"):
        if input_ketersediaan == "True":
            status_ketersediaan = True
            print('status ketersediaan : ' + input_ketersediaan)
        else:
            status_ketersediaan = False
            print('status ketersediaan : ' + input_ketersediaan)
        break
    else:
        print("Input tidak valid. Masukkan True atau False.")

menampilkan_semua_data = input("apakah anda ingin menampilkan semua data yang telah di input? : Ya/Tidak : ")
menampilkan_semua_data = menampilkan_semua_data.capitalize()
if menampilkan_semua_data == 'Ya':
    print()
    print("Informasi Buku Berdasarkan Data Input : ")
    print('Judul Buku : ' , judul_buku)
    print('Tahun terbit : ' , tahun_terbit)
    print('Harga Buku : ' , harga_buku)
    print('penulis : ' , penulis)
    print('status ketersediaan : ' , str(bool(menampilkan_semua_data)))
else:
    print("Baiklah...")
    print("Program Berhenti Sekarang.... ")
    exit()