import json

# data_dari_file = []

# OPEN JSON SEBAGAI FILE_BACA
with open("data.json","r") as file_baca:

    # LOAD ATAU BACA DATA_DARI_FILE
    data_dari_file = json.load(file_baca)


#################################################################################################################

# FUNGSI ADD / TAMBAHKAN
def tambah(argument):


    # PENGKONDISIAN ID BARU
    # jika data kosong maka id = 1
    if len(data_dari_file) <= 0:
        id_max = 1
        print("data kosong")
    # jika data terisi maka cari id terbesar lalu tambahkan 1 untuk id baru
    else:
        id_pertama = 1
        # membaca dictionary pada list data_dari_file sebagai i
        for i in data_dari_file:
            print(i["id"])
            # dari dictionary yang telah dibaca maka ambil value dari key ["id"], bandingkan dengan id_pertama = 1 sampai id yang terbesar
            if i["id"] > id_pertama:
                # jika id pada list data_dari_file lebih besar, ubah id tersebut menjadi id_pertama untuk dibandingkan
                id_pertama = i["id"]
        id_max = id_pertama + 1
        print("id paling besar : ", id_pertama)
        print("id akhir : ", id_max)
        print("data_ada")

    sebuah_dict = {
        "id":id_max,
        "tugas":argument,
        "selesaikan":False
    }

    # data_dari_file adalah list
    # print(sebuah_dict(argument))
    print(sebuah_dict)
    # MENAMBAHKAN DICTIONARY KE DATA_DARI_FILE 
    data_dari_file.append(sebuah_dict)
    # TULIS DATA_DARI_FILE BARU KE JSON SEBAGAI FILE_TULIS
    with open("data.json","w") as file_tulis:
        # SIMPAN HASIL WRITE KE JSON
        json.dump(data_dari_file, file_tulis, indent=4)


# FUNGSI LIST / TAMPILKAN
def tampilkan_list():
    # COMMAND LIST / TAMPILKAN
    print("\n")
    # print("List :", "\n")

    print(f"| ID |      List Belum      |", "\n")
    for i in data_dari_file:
        if i["selesaikan"] == False:
            tampil_id = i["id"]
            tampil_tugas = i["tugas"]
            print(f"[ {tampil_id} ] {tampil_tugas}", "\n")

    print("\n")

    print(f"| ID |      List Sudah      |", "\n")
    for i in data_dari_file:
        if i["selesaikan"] == True:
            tampil_id = i["id"]
            tampil_tugas = i["tugas"]
            print(f"[ {tampil_id} ] {tampil_tugas}", "\n")

    # for i in data_dari_file:
    #     tampil_id = i["id"]
    #     tampil_tugas = i["tugas"]
    #     # print(tampil_id, tampil_tugas)
    #     print(f"[ {tampil_id} ] {tampil_tugas}", "\n")
    #     # print(i)

    # # EKSEKUSI LIST / TAMPILKAN
    # # TAMBAHKAN PENOMORAN LIST MULAI DARI ANGKA 1 DST SEBAGAI NOMOR 
    # for nomor, nilai in enumerate(data_dari_file, start=1):
    #     nomor = int(nomor)
    #     # TAMPILKAN LIST DENGAN FORMAT PENOMORAN DAN DATA_DARI_FILE
    #     print(f"{nomor}. {nilai}", "\n")
    #

# FUNGSI DONE / SELESAI
def selesai(number):

    # print("input number adalah : ", number)
    for i in data_dari_file:
        if i["id"] == int(number):
            i["selesaikan"] = True
            print(i)

    # print(data_dari_file[number])
    # data_dari_file[number]["selesaikan"] = True
    # print(data_dari_file[number])

    # # HAPUS SEBUAH LIST DARI JSON 
    # del data_dari_file[number]

    # SIMPAN HASIL DATA_DARI_FILE BARU KE JSON
    with open("data.json","w") as file_tulis:
        json.dump(data_dari_file, file_tulis, indent=4)


def hapus(number):

    for nomor, i in enumerate(data_dari_file):
        # print(nomor, i)
        if i["id"] == int(number):
            print(i, nomor)
            nomor_data_dari_file = nomor
    print(nomor_data_dari_file)
    del data_dari_file[nomor_data_dari_file]

    # SIMPAN HASIL DATA_DARI_FILE BARU KE JSON
    with open("data.json","w") as file_tulis:
        json.dump(data_dari_file, file_tulis, indent=4)

    # for i in data_dari_file:
    #     if i["id"] == int(number):
    #         print(f"{i} dihapus")


# FUNGSI EDIT / SUNTING
def sunting(number,argument):

    for i in data_dari_file:
        if i["id"] == int(number):
            # print(i)
            print(f"[ {i["id"]} ] {i["tugas"]} =====> [ {i["id"]} ] {argument}")
            i["tugas"] = argument

    # SIMPAN HASIL DATA_DARI_FILE BARU KE JSON
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
        number = int(number)

    # validasi 3 number lebih dari atau sama dengan nol, dan lebih kecil dari data_dari_file

    for i in data_dari_file:
        # print(i["id"])
        if number == i["id"]:
            print(f"{number} ada")
            print("validasi 3 lolos")
            return False

    return True

    # list_id = []
    # for i in data_dari_file:
    #     # print(i["id"])
    #     list_id.append(i["id"])
    # print(list_id)

    # if not 0 <= number == list_id:
    #     print(f"Can't find list No.{number}")
    #     print("validasi 3 gagal")
    #     return True
    # else:
    #     print("validasi 3 lolos")
    #     return False

# FUNGSI EKSEKUSI DONE DAN EDIT 
def eksekusi(number,status,tugas,argument):
    # validasi untuk menguji apakah input sesuai dengan kondisi list
    menguji = validasi_data_int(number)
    # print("status : ", validasi_data_int(number))
    # validasi mengembalikan nilai berupa True / False
    if menguji == False:
        # pengkondisian jika validasi bernilai false maka kode di bawah akan di eksekusi, sebaliknya kode di bawah tidak akan di eksekusi
        # number = int(number) - 1
        # print(f"{commands.data_dari_file[number]} =====> Done")
        # menyelesaikan = commands.selesai(number)
        print(status)
        # print("tugas : ", tugas)
        if tugas == "perintah_done":
            # print(f"{data_dari_file[int(number)]} =====> Done")
            perintah = selesai(number)
        elif tugas == "perintah_del":
            # print(f"{data_dari_file[int(number)]} =====> Delete")
            perintah = hapus(number)
        elif tugas == "perintah_edit":
            # print(f"{data_dari_file[int(number)]} =====> {argument}")
            perintah = sunting(number,argument)
