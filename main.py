import commands

# LOOP 
ulang = True
while ulang:
    # input
    terminal = input("todo : ")
    # pecah kata pertama pada input
    command = terminal.split()[0]

    # COMMAND ADD / TAMBAHKAN 
    if command == "add":
        none, argument = terminal.split(maxsplit=1)

        # EKSEKUSI ADD / TAMBAHKAN
        menambahkan = commands.tambah(argument)
        print(f"{argument} =====> Added to list")

    # COMMAND LIST / TAMPILKAN
    elif command == "list":
        print("\n")
        print("List :")
        # EKSEKUSI LIST / TAMPILKAN
        menampilkan = commands.tampilkan_list()

    # COMMAND DONE / SELESAI 
    elif command == "done":
        number = terminal.split()[1]
        
        # validasi untuk menguji apakah input sesuai dengan kondisi list
        menguji = commands.validasi_data_int(number)
        # validasi mengembalikan nilai berupa True / False
        if menguji == False:
            # pengkondisian jika validasi bernilai false maka kode di bawah akan di eksekusi, sebaliknya kode di bawah tidak akan di eksekusi
            number = int(number) - 1
            menyelesaikan = commands.selesai(number)
            print(f"List : {commands.data_dari_file[number]} =====> Done")

    # COMMAND EDIT / SUNTING 
    elif command == "edit":
        none, number, argument = terminal.split(maxsplit=2)

        # validasi untuk menguji apakah input sesuai dengan kondisi list
        menguji = commands.validasi_data_int(number)
        if menguji == False:
            # validasi mengembalikan nilai berupa True / False
            number = int(number) - 1
            mengubah = commands.sunting(number,argument)
            print(f"{commands.data_dari_file[number]} =====> {argument}")

    # COMMAND EXIT / KELUAR
    elif command == "exit":
        # menghentikan perulangan dengan mendefinisikan ualng sebagai False
        ulang = False
        # cetak status
        print("Program Closed")

    else:
        print("Please use a Right Command For Help Please Read README.md")
