import commands
# routing


# loop

ulang = True
while ulang:
    # input
    terminal = input("todo : ")
    command = terminal.split()[0]

    if command == "add":
        none, argument = terminal.split(maxsplit=1)
        menambahkan = commands.tambah(argument)
        print(argument)
        print("added to list")
    elif command == "list":
        print("list")
        menampilkan = commands.tampilkan_list()
    elif command == "done":
        number = int(terminal.split()[1])
        menyelesaikan = commands.selesai(number)
        print("Done")
    elif command == "edit":
        none, number, argument = terminal.split(maxsplit=2)
        number = int(number)
        mengubah = commands.sunting(number,argument)
        print("edited list : lama to list : baru")
    elif command == "exit":
        ulang = False
        print("program closed")
    else:
        print("please use a right command for help please read README.md")
