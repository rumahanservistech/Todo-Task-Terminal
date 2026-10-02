from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Todo")

layout = QVBoxLayout()

label = QLabel("Contoh Catata")

button1 = QPushButton("Tambah")
# def tambahh():
#     label.setText("Menambahkan")
def show_input_popup():
    label.setText("Ditambahkan")
    
button2 = QPushButton("Tampil")
def tampill():
    label.setText("Menampilkan")

button3 = QPushButton("Selesa")
def selesaii():
    label.setText("Menyelesa")
    
button4 = QPushButton("Tidak Selesa")
button5 = QPushButton("Hapus")
button6 = QPushButton("Sunting")
button7 = QPushButton("Kembal")


    
button1.clicked.connect(show_input_popup)
button2.clicked.connect(tampill)
button3.clicked.connect(selesaii)

layout.addWidget(label)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(button3)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
