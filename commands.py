import json

# OPEN JSON SEBAGAI FILE_BACA
with open("data.json","r") as file_baca:

    # LOAD ATAU BACA DATA_DARI_FILE
    data_dari_file = json.load(file_baca)

#################################################################################################################

# FUNGSI ADD / TAMBAHKAN
def tambah(argument):
    # MENAMBAHKAN ARGUMENT KE DATA_DARI_FILE 
    data_dari_file.append(argument)
    # TULIS DATA_DARI_FILE BARU KE JSON SEBAGAI FILE_TULIS
    with open("data.json","w") as file_tulis:
        # SIMPAN HASIL WRITE KE JSON
        json.dump(data_dari_file, file_tulis, indent=4)


# FUNGSI LIST / TAMPILKAN
def tampilkan_list():
    # COMMAND LIST / TAMPILKAN
    print("\n")
    print("List :")
    # EKSEKUSI LIST / TAMPILKAN
    # TAMBAHKAN PENOMORAN LIST MULAI DARI ANGKA 1 DST SEBAGAI NOMOR 
    for nomor, nilai in enumerate(data_dari_file, start=1):
        nomor = int(nomor)
        # TAMPILKAN LIST DENGAN FORMAT PENOMORAN DAN DATA_DARI_FILE
        print(f"{nomor}. {nilai}", "\n")


# FUNGSI DONE / SELESAI
def selesai(number):
    # HAPUS SEBUAH LIST DARI JSON 
    del data_dari_file[number]
    # SIMPAN HASIL DATA_DARI_FILE BARU KE JSON
    with open("data.json","w") as file_tulis:
        json.dump(data_dari_file, file_tulis, indent=4)


# FUNGSI EDIT / SUNTING
def sunting(number,argument):
    data_dari_file[number] = argument
    with open("data.json","w") as file_tulis:
        json.dump(data_dari_file, file_tulis, indent=4)
        

# FUNGSI VALIDASI INPUT
def validasi_data_int(number):
    # validasi 1 number berupa angka
    if not isinstance(number,str):
        print(f"Can't find list '{number}'")
        print("validasi 1 gagal")
        return True
    else:
        print("validasi 1 lolos")
        # print("validasi 1 lolos")

    # validasi 2, nilai di dalam string harus berupa angka
    if not number.isdigit():
        print(f"Can't find list '{number}'")
        print("validasi 2 gagal")
        return True 
    else:
        print("validasi 2 lolos")
        number = int(number) - 1

    # validasi 3 number lebih dari atau sama dengan nol, dan lebih kecil dari data_dari_file
    if not 0 <= number < len(data_dari_file):
        print(f"Can't find list No.{number + 1}")
        print("validasi 3 gagal")
        return True
    else:
        print("validasi 3 lolos")
        return False

# FUNGSI EKSEKUSI DONE DAN EDIT 
def eksekusi(number,status,tugas,argument):
    # validasi untuk menguji apakah input sesuai dengan kondisi list
    menguji = validasi_data_int(number)
    # validasi mengembalikan nilai berupa True / False
    if menguji == False:
        # pengkondisian jika validasi bernilai false maka kode di bawah akan di eksekusi, sebaliknya kode di bawah tidak akan di eksekusi
        number = int(number) - 1
        # print(f"{commands.data_dari_file[number]} =====> Done")
        # menyelesaikan = commands.selesai(number)
        print(status)
        if tugas == True:
            print(f"{data_dari_file[number]} =====> Done")
            perintah = selesai(number)
        else:
            print(f"{data_dari_file[number]} =====> {argument}")
            perintah = sunting(number,argument)
