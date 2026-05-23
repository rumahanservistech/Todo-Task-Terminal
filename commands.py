kumpulan_data = ["pahami konsep backend"]

def tambah(argument):
    kumpulan_data.append(argument)

def tampilkan_list():
    for nomor, nilai in enumerate(kumpulan_data, start=1):
        nomor = int(nomor)
        print(f"{nomor}. {nilai}", "\n")

def selesai(number):
    del kumpulan_data[number]

def sunting(number,argument):
    kumpulan_data[number] = argument
