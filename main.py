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
        if number.isdigit() and int(number) > 0:
            try:
                number = int(number) - 1
                print(commands.data_dari_file[number], "Done")
            except Exception as e:
                print(f"Can't find list No. {number + 1}")
            else:
                menyelesaikan = commands.selesai(number)
        else:
            print(f"Can't find list '{number}'")

    elif command == "edit":
        none, number, argument = terminal.split(maxsplit=2)
        if number.isdigit() and int(number) > 0:
            try:
                number = int(number) - 1
                print(f"edited list : {commands.data_dari_file[number]} to list : {argument}")
            except Exception as e:
                print(f"Can't find list No. {number + 1}")
            else:
                mengubah = commands.sunting(number,argument)
        else:
            print(f"Can't find list '{number}'")

    elif command == "exit":
        ulang = False
        print("program closed")

    else:
        print("please use a right command for help please read README.md")
