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
        print("\n")
        print("list")
        menampilkan = commands.tampilkan_list()
    elif command == "done":
        number = terminal.split()[1]
        number = int(number) - 1
        print(commands.kumpulan_data[number], "Done")
        menyelesaikan = commands.selesai(number)
    elif command == "edit":
        none, number, argument = terminal.split(maxsplit=2)
        number = int(number) - 1
        print(f"edited list : {commands.kumpulan_data[number]} to list : {argument}")
        mengubah = commands.sunting(number,argument)
    elif command == "exit":
        ulang = False
        print("program closed")
    else:
        print("please use a right command for help please read README.md")
