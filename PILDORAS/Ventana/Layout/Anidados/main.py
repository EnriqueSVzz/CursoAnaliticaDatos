from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QLineEdit, QMessageBox, QHBoxLayout, QVBoxLayout, QWidget)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
     
     # Haremos una diseño responsivo.   
    def inicializarUI(self):
        self.setMinimumWidth(600)
        self.setMinimumWidth(400)
        self.setWindowTitle("Layout Nested")
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
        
       #declaremos todas los labels y su input text
       message_label = QLabel('Por favor ingrese sus datos personales')
       
       nombre_label = QLabel('Nombre:')
       nombre_input = QLineEdit()
       apellido_label = QLabel('Apellido:')
       apellido_input = QLineEdit()
       edad_label = QLabel('Edad:')
       edad_input = QLineEdit()
       
       correo_label = QLabel('Correo:')
       correo_input = QLineEdit()
       direccion_label = QLabel('Dirección:')
       direccion_input = QLineEdit()
       telefono_label = QLabel('Telefono:')
       telefono_input = QLineEdit()
       
       enviar_button = QPushButton("Enviar")
       
       '''
       Debemos alinear de la siguiente Manera
       LH.1 = Mensage
       LH.2 = LV.1 (Primeros Datos) y LV.2 (Segundos Datos)
       LH.3 = Botón
       '''
       
       #Armemos los LV
       layoutV1 = QVBoxLayout()
       layoutV1.addWidget(nombre_label)
       layoutV1.addWidget(apellido_label)
       layoutV1.addWidget(edad_label)
       #self.setLayout(layoutV1)
       
       layoutV2 = QVBoxLayout()
       layoutV2.addWidget(nombre_input)
       layoutV2.addWidget(apellido_label)
       layoutV2.addWidget(edad_input)
       #self.setLayout(layoutV2)
       
       layoutV3 = QVBoxLayout()
       layoutV3.addWidget(correo_label)
       layoutV3.addWidget(direccion_label)
       layoutV3.addWidget(telefono_label)
       #self.setLayout(layoutV3)
       
       layoutV4 = QVBoxLayout()
       layoutV4.addWidget(correo_input)
       layoutV4.addWidget(direccion_input)
       layoutV4.addWidget(telefono_input)
       #self.setLayout(layoutV4)
       
       # Armemos los LH
       layoutH1 = QHBoxLayout()
       layoutH1.addWidget(layoutV1)
       layoutH1.addWidget(layoutV2)
       #self.setLayout(layoutH1)
       
       layoutH2 = QHBoxLayout()
       layoutH2.addWidget(layoutV3)
       layoutH2.addWidget(layoutV4)
       #self.setLayout(layoutH2)
       
       layoutHF = QHBoxLayout()
       layoutHF.addWidget(layoutH1)
       layoutHF.addWidget(layoutH2)
       layoutHF.addWidget(enviar_button)
       self.setLayout(layoutHF)
       
       
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())