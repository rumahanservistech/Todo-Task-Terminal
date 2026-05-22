kumpulan_data = ["pahami konsep backend"]
def tambah(argument):
    kumpulan_data.append(argument)

def tampilkan_list():
    for item in kumpulan_data:
        cetaka = print(item)

def selesai(number):
    del kumpulan_data[number]

def sunting(number,argument):
    kumpulan_data[number] = argument
