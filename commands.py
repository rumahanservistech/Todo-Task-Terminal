import json

# kumpulan_data = ["pahami konsep backend"]
kumpulan_data = []
# with open("data.json","w") as file_tulis:
    # json.dump(kumpulan_data, file_tulis, indent=4)

with open("data.json","r") as file_baca:
    data_dari_file = json.load(file_baca)

def tambah(argument):
    # with open("data.json","r") as file_baca:
        # data_dari_file = json.load(file_baca)
        # print(data_dari_file)
        data_dari_file.append(argument)
        # print(data_dari_file)
        with open("data.json","w") as file_tulis:
            json.dump(data_dari_file, file_tulis, indent=4)
            # print(data_dari_file)
    # kumpulan_data.append(argument)

def tampilkan_list():
    # with open("data.json","r") as file_baca:
        # data_dari_file = json.load(file_baca)
        # print(data_dari_file)
        for nomor, nilai in enumerate(data_dari_file, start=1):
            nomor = int(nomor)
            print(f"{nomor}. {nilai}", "\n")

def selesai(number):
    # with open("data.json","r") as file_baca:
        # data_dari_file = json.load(file_baca)
        del data_dari_file[number]
        with open("data.json","w") as file_tulis:
            json.dump(data_dari_file, file_tulis, indent=4)

def sunting(number,argument):
     # with open("data.json","r") as file_baca:
        # data_dari_file = json.load(file_baca)
        data_dari_file[number] = argument
        with open("data.json","w") as file_tulis:
            json.dump(data_dari_file, file_tulis, indent=4)

