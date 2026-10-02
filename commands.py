import json
import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="todo",
    user="postgres",
    password="643571"
)

print("Berhasil terhubung ke PostgreSQL!")

# conn.close()

# data_dari_file = []

# # OPEN JSON SEBAGAI FILE_BACA
# with open("data.json","r") as file_baca:
#
#     # LOAD ATAU BACA DATA_DARI_FILE
#     data_dari_file = json.load(file_baca)


#################################################################################################################

# FUNGSI ADD / TAMBAHKAN
def tambah(argument):

    cursor = conn.cursor()
    cursor.execute(
        """
        insert into daftar (title)
        values (%s)
        returning id
        """,
        (argument,)
    )

    id_baru = cursor.fetchone()[0]
    
    conn.commit()
    cursor.close()

    print(f"[ {id_baru} ] {argument} =====> Added")


    # # PENGKONDISIAN ID BARU
    # # JIKA LIST DATA_DARI_FILE KOSONG MAKA ID = 1
    # if len(data_dari_file) <= 0:
    #     id_max = 1
    #     # print("data kosong")
    #     # JIKA LIST DATA_DARI_FILE TERISI MAKA ID TERBESAR + 1
    # else:
    #     id_pertama = 1
    #     # BACA SEMUA DICT DALAM LIST
    #     for i in data_dari_file:
    #         # print(i["id"])
    #         # COCOKKAN VALUE KEY ID YANG LEBIH BESAE DARI ID PERTAMA
    #         if i["id"] > id_pertama:
    #             # JIKA VALUE KEY ID LEBIH BESAR DARI ID PERTAMA MAKA UBAH ID PERTAMA DENGAN ID DARI VALUE KEY
    #             id_pertama = i["id"]
    #     # MAKA ID BARU ADALAH ID TERBESAR AKHIR + 1
    #     id_max = id_pertama + 1
    #     # print("id paling besar : ", id_pertama)
    #     # print("id akhir : ", id_max)
    #     # print("data_ada")
    #
    # # DEFINISIKAN DICT BARU SEBAGAI SEBUAH DICT
    # sebuah_dict = {
    #     "id":id_max,
    #     "tugas":argument,
    #     "selesaikan":False
    # }
    #
    # 
    # print(sebuah_dict)
    # # CETAK STATUS
    # print(f"[ {sebuah_dict["id"]} ] {sebuah_dict["tugas"]} =====> Add")
    # # MENAMBAHKAN DICTIONARY KE DATA_DARI_FILE 
    # data_dari_file.append(sebuah_dict)
    #
    # # SIMPAN HASIL DATA_DARI_FILE BARU KE JSON
    # with open("data.json","w") as file_tulis:
    #     json.dump(data_dari_file, file_tulis, indent=4)
    #

# FUNGSI LIST / TAMPILKAN
def tampilkan_list():

    cursor = conn.cursor()

    cursor.execute(
        """
        select * from daftar;
        """
    )
    isi_todo = cursor.fetchall()
    # print(isi_todo)

    print(f"| ID |      List Belum      |", "\n")
    for i in isi_todo:
        if i[2] == False:
            print(f"[ {i[0]} ] {i[1]}")

    print("\n")

    print(f"| ID |      List Sudah      |", "\n")
    for i in isi_todo:
        if i[2] == True:
            print(f"[ {i[0]} ] {i[1]}")

    # print(isi_todo)

    # # COMMAND LIST / TAMPILKAN
    # print("\n")
    #
    # # EKSEKUSI LIST BELUM
    # print(f"| ID |      List Belum      |", "\n")
    # # BACA SEMUA DICT DALAM LIST
    # for i in data_dari_file:
    #     # COCOKKAN DICT MANA SAJA YANG MEMPUNYAI KEY SELESAIKAN DENGAN VALUE FALSE
    #     if i["selesaikan"] == False:
    #         # DEIFINISIKAN VALUE KEY ID SEBAGAI TAMPIL_ID, VALUE KEY TUGAS SEBAGAI TAMPIL_TUGAS
    #         tampil_id = i["id"]
    #         tampil_tugas = i["tugas"]
    #         # CETAK LIST BELUM
    #         print(f"[ {tampil_id} ] {tampil_tugas}", "\n")
    #
    # print("\n")
    #
    # EKSEKUSI LIST SUDAH
    # print(f"| ID |      List Sudah      |", "\n")
    # # BACA SEMUA DICT DALAM LIST
    # for i in data_dari_file:
    #     # COCOKKAN DICT MANA SAJA YANG MEMPUNYAI KEY SELESAIKAN DENGAN VALUE TRUE
    #     if i["selesaikan"] == True:
    #         # DEIFINISIKAN VALUE KEY ID SEBAGAI TAMPIL_ID, VALUE KEY TUGAS SEBAGAI TAMPIL_TUGAS
    #         tampil_id = i["id"]
    #         tampil_tugas = i["tugas"]
    #         # CETAK LIST SUDAH
    #         print(f"[ {tampil_id} ] {tampil_tugas}", "\n")


# FUNGSI DONE / SELESAI
def selesai(number):

    cursor = conn.cursor()
    cursor.execute(
        """
        update daftar
        set completed = True
        where id = %s
        returning title
        """,
        (number,)
    )
    tugas = cursor.fetchone()[0]
    print(f"[ {number} ] {tugas} =====> Done")
    conn.commit()
    cursor.close()
    # # print(number)

    # if number == "all":
    #     for i in data_dari_file:
    #         if i["selesaikan"] == False:
    #             # print(i)
    #             print(f"[ {i["id"]} ] {i["tugas"]} =====> Done")
    #             i["selesaikan"] = True

    # else:
    #     # BACA SEMUA DICT PADA LIST
    #     for i in data_dari_file:
    #         # COCOKKAN DICT MANA SAJA DENGAN VALUE KEY ID YANG SAMA DENGAN NUMBER
    #         if i["id"] == int(number):

    #             if i["selesaikan"] == True:
    #                 print(f"[ {i["id"]} ] {i["tugas"]} =====> Already Done")

    #             else:
    #                 # CETAK STATUS
    #                 print(f"[ {i["id"]} ] {i["tugas"]} =====> Done")
    #                 # UBAH VALUE KEY SELESAIKAN DENGAN TRUE
    #                 i["selesaikan"] = True

    # # SIMPAN HASIL DATA_DARI_FILE BARU KE JSON
    # with open("data.json","w") as file_tulis:
    #     json.dump(data_dari_file, file_tulis, indent=4)


def tidak_selesai(number):

    cursor = conn.cursor()
    cursor.execute(
        "update daftar set completed = False where id = %s returning title" , (number,)
    )
    tugas = cursor.fetchone()[0]
    print(f"[ {number} ] {tugas} =====> Undone")
    conn.commit()
    cursor.close()


    # # print(number)
    # if number == "all":
    #     for i in data_dari_file:
    #         if i["selesaikan"] == True:
    #             print(f"[ {i["id"]} ] {i["tugas"]} =====> Undone")
    #             i["selesaikan"] = False

    # elif number.isdigit():
    #     for i in data_dari_file:
    #         if i["id"] == int(number):
    #             if i["selesaikan"] == False:
    #                 print(f"[ {i["id"]} ] {i["tugas"]} =====> Already Undone")
    #             else:
    #                 print(f"[ {i["id"]} ] {i["tugas"]} =====> Undone")
    #                 i["selesaikan"] = False

    # else:
    #     print(f"{number}? apa maksud kamu [all]?")

    # # SIMPAN HASIL DATA_DARI_FILE BARU KE JSON
    # with open("data.json","w") as file_tulis:
    #     json.dump(data_dari_file, file_tulis, indent=4)


def hapus(number):
    
    if not number == "all":
        
        cursor = conn.cursor()
        cursor.execute (
            """
            delete from daftar
            where id = %s
            returning title
            """,
            (number,)
        )
        isi_todo = cursor.fetchone()[0]
        
    else:
        cursor = conn.cursor()
        cursor.execute (
            """
            delete from daftar
            returning title
            """
        )
        isi_todo = cursor.fetchall()
        

    conn.commit()
    cursor.close()

    print(f"[ {number} ] {isi_todo} =====> Del")

    # # BACA SEMUA DICT DAN NOMOR PADA LIST
    # for nomor, i in enumerate(data_dari_file):
    #     # print(nomor, i)
    #     # COCOKKAN DICT MANA SAJA DENGAN VALUE KEY ID YANG SAMA DENGAN NUMBER
    #     if i["id"] == int(number):
    #         # print(i, nomor)
    #         # CETAK STATUS
    #         print(f"[ {i["id"]} ] {i["tugas"]} =====> Delete")
    #         # DEIFINISIKAN NOMOR PADA LIST SEBAGAI NOMOR_DATA_DARI_FILE
    #         nomor_data_dari_file = nomor
    # # print(nomor_data_dari_file)
    # # HAPUS DICT PADA LIST SESUAI NOMOR
    # del data_dari_file[nomor_data_dari_file]
    #
    # # SIMPAN HASIL DATA_DARI_FILE BARU KE JSON
    # with open("data.json","w") as file_tulis:
    #     json.dump(data_dari_file, file_tulis, indent=4)
    #

# FUNGSI EDIT / SUNTING
def sunting(number,argument):
    cursor = conn.cursor()
    cursor.execute(
        "select title from daftar where id = %s", (number,)
    )
    tugas = cursor.fetchone()[0] 
    
    cursor.execute(
        "update daftar set title = %s where id = %s", (argument,number,)
    )
    # tugas = cursor.fetchone()[0]
    
    print(f"[ {number} ] {tugas} =====> [ {number} ] {argument}")
    
    conn.commit()
    cursor.close()
    
    # # BACA SEMUA DICT PADA LIST
    # for i in data_dari_file:
    #     # COCOKKAN DICT MANA SAJA DENGAN VALUE KEY ID YANG SAMA DENGAN NUMBER
    #     if i["id"] == int(number):
    #         # print(i)
    #         # CETAK STATUS
    #         print(f"[ {i["id"]} ] {i["tugas"]} =====> [ {i["id"]} ] {argument}")
    #         # UBAH VALUE KEY TUGAS DENGAN ARGUMENT BARU
    #         i["tugas"] = argument

    # # SIMPAN HASIL DATA_DARI_FILE BARU KE JSON
    # with open("data.json","w") as file_tulis:
    #     json.dump(data_dari_file, file_tulis, indent=4)
        

# FUNGSI VALIDASI INPUT
def validasi_data_int(number):

    try:
        number = int(number)
    except ValueError as e:
        print(f"Can't find list '{number}'")
        return True

    # validasi 1 number berupa angka
    if not isinstance(number,int):
        print(f"Can't find list '{number}'")
        # print("validasi 1 gagal")
        return True

    # else:
        # print("validasi 1 lolos")
        # print("validasi 1 lolos")

    # # validasi 2, nilai di dalam string harus berupa angka
    # if not number.isdigit():
    #     print(f"Can't find list '{number}'")
    #     # print("validasi 2 gagal")
    #     return True 
    # else:
    #     # print("validasi 2 lolos")
    #     number = int(number)

    # VALIDASI 3 - MENCARI APAKAH NUMBER SESUAI DENGAN ID DALAM LIST DATA_DARI_FILE
    # BACA SEMUA DICT DAN NOMOR PADA LIST
    for i in data_dari_file:
        # print(i["id"])
        # COCOKKAN VALUE KEY ID MANA YANG SAMA DENGAN NUMBER
        # print(number)
        if number == i["id"]:
            # print(f"{number} ada")
            # print("validasi 3 lolos")
            return False
    
    # JIKA TIDAK ADA YANG SAMA DENGAN NUMBER MAKA NILAI VALIDASI TRUE
    print(f"Can't find list '{number}'")
    return True


# FUNGSI EKSEKUSI DONE DAN EDIT 
def eksekusi(number,tugas,argument):
    # validasi untuk menguji apakah input sesuai dengan kondisi list
    menguji = validasi_data_int(number)
    # validasi mengembalikan nilai berupa True / False
    # JIKA FUNGSI VALIDASI_DATA_INT MENGEMBALIKAN NILAI FALSE MAKA EKSEKUSI AKAN DIJALANKAN
    if menguji == False:
        # pengkondisian jika validasi bernilai false maka kode di bawah akan di eksekusi, sebaliknya kode di bawah tidak akan di eksekusi
        if tugas == "perintah_done":
            perintah = selesai(number)
        elif tugas == "perintah_undone":
            perintah = tidak_selesai(number)
        elif tugas == "perintah_del":
            perintah = hapus(number)
        elif tugas == "perintah_edit":
            perintah = sunting(number,argument)
