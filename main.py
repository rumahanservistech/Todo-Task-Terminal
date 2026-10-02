import commands
import gui

# TAMPILKAN LIST SETIAP MEMULAI PROGRAM
# menampilkan = commands.tampilkan_list()

# LOOP 
ulang = True
while ulang:
    # input
    terminal = input("todo : ")
    # INPUT HARUS BERISI SETIDAKNYA SATU NILAI
    if len(terminal) <= 0:
        # JIKA KOSONG, MAKA CETAK FEEDBACK
        print("Masukan perintah harus diisi")
    else:
        # SEBALIKNYA, DEFINISIKAN COMMAND SEBAGAI PECAHAN KATA PERTAMA DARI INPUT
        command = terminal.split()[0]


        # COMMAND ADD / TAMBAHKAN 
        if command == "add":

            # PECAH INPUT TERMINAL MENJADI 2 BAGIAN
            bagian = terminal.split(maxsplit=1)
            # JIKA BAGIAN PECAHAN KURANG DARI 2, MAKA CETAK FEEDBACK
            if len(bagian) < 2:
                print("Gunakan perintah dengan format yang benar =====> [add], [Nama Tugas]")
            else:
                # SEBALIKNYA, DEFINISIKAN BAGIAN KEDUA SEBAGAI ARGUMENT
                _,argument = bagian

                # EKSEKUSI ADD / TAMBAHKAN
                # print(f"{argument} =====> Added to list")
                menambahkan = commands.tambah(argument)


        # COMMAND LIST / TAMPILKAN
        elif command == "list":

            # EKSEKUSI LIST / TAMPILKAN
            menampilkan = commands.tampilkan_list()


        # COMMAND DONE / SELESAI 
        elif command == "done":

            # PECAH INPUT TERMINAL MENJADI 2 BAGIAN
            bagian = terminal.split()
            # JIKA BAGIAN PECAHAN KURANG DARI 2, MAKA CETAK FEEDBACK
            # print(len(bagian))
            if not len(bagian) == 2:
                print("Gunakan perintah dengan format yang benar =====> [done], [ID Tugas, ex:5]")
            else:
                # SEBALIKNYA, DEFINISIKAN BAGIAN KEDUA SEBAGAI NUMBER
                # DEFINISIKAN STATUS, TUGAS SEBAGAI TRUE, UNTUK PENGKONDISIAN PADA FUNGSI EKSEKUSI
                _,number = bagian
                # print(number)
                # status = "perintah_done"
                tugas = "perintah_done"
                # ARGUMENT DIKOSONGKAN
                argument = ""
                if number.isdigit():
                    # print(f"ini adalah angka {number}")

                    # EKSEKUSI DONE / SELESAI
                    mengeksekusi = commands.selesai(number)
                else:
                    mengeksekusi = commands.selesai(number)


        elif command == "undone":

            bagian = terminal.split()
            # print(len(bagian))
            if not len(bagian) == 2:
                print("Gunakan perintah dengan format yang benar =====> [undone], [ID Tugas, ex:5] or [all]")
            else:
                _,number = bagian
                tugas = "perintah_undone"
                argument = ""
                if number.isdigit():
                    # print(f"ini adalah angka {number}")

                    # EKSEKUSI UNDONE / TIDAK SELESAI
                    mengeksekusi = commands.tidak_selesai(number)

                else:
                    mengeksekusi = commands.tidak_selesai(number)


        # COMMAND DEL / HAPUS
        elif command == "del":

            bagian = terminal.split()
            if not len(bagian) == 2:
                print("Gunakan perintah dengan format yang benar =====> [del], [ID Tugas, ex:5]")
            else:
                _,number = bagian
                # status = "perintah_del" 
                tugas = "perintah_del"

                # ARGUMENT DIKOSONGKAN
                argument = ""

                # EKSEKUSI DEL / HAPUS
                mengeksekusi = commands.hapus(number)

        # COMMAND EDIT / SUNTING 
        elif command == "edit":

            # PECAH INPUT TERMINAL MENJADI 3 BAGIAN
            bagian = terminal.split(maxsplit=2)
            # JIKA BAGIAN PECAHAN KURANG DARI 3, MAKA CETAK FEEDBACK
            if not len(bagian) == 3:
                print("Gunakan perintah dengan format yang benar =====> [edit], [ID Tugas, ex:5], [Nama Tugas Baru]")
            else:
                # SEBALIKNYA, DEFINISIKAN BAGIAN KEDUA SEBAGAI NUMBER DAN BAGIAN KETIGA SEBAGAI ARGUMENT
                # DEFINISIKAN STATUS, TUGAS SEBAGAI FALSE, UNTUK PENGKONDISIAN PADA FUNGSI EKSEKUSI
                _,number,argument = bagian
                # status = "perintah_edit"
                tugas = "perintah_edit"

                # EKSEKUSI EDIT / SUNTING
                mengeksekusi = commands.sunting(number,argument)
                

        # COMMAND EXIT / KELUAR
        elif command == "e":
            # menghentikan perulangan dengan mendefinisikan ualng sebagai False
            ulang = False
            # cetak status
            print("Program Closed")


        else:
            print("Please use a Right Command For Help Please Read README.md")
