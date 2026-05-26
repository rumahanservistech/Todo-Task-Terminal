import json

kumpulan_data = []

with open("data.json","r") as file_baca:
    data_dari_file = json.load(file_baca)

def tambah(argument):
        data_dari_file.append(argument)
        with open("data.json","w") as file_tulis:
            json.dump(data_dari_file, file_tulis, indent=4)

def tampilkan_list():
        for nomor, nilai in enumerate(data_dari_file, start=1):
            nomor = int(nomor)
            print(f"{nomor}. {nilai}", "\n")

def selesai(number):
        del data_dari_file[number]
        with open("data.json","w") as file_tulis:
            json.dump(data_dari_file, file_tulis, indent=4)

def sunting(number,argument):
        data_dari_file[number] = argument
        with open("data.json","w") as file_tulis:
            json.dump(data_dari_file, file_tulis, indent=4)
