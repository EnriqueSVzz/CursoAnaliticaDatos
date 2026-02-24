from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QLineEdit, QMessageBox, QHBoxLayout, QVBoxLayout, QWidget)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()

    def inicializarUI(self):
        self.setMinimumSize(200, 200)
        self.setWindowTitle("Layout Nested")
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
        message_label = QLabel('Por favor ingrese sus datos personales')

        # Labels e inputs
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

        # Layouts verticales
        layoutV1 = QVBoxLayout()
        layoutV1.addWidget(nombre_label)
        layoutV1.addWidget(apellido_label)
        layoutV1.addWidget(edad_label)

        layoutV2 = QVBoxLayout()
        layoutV2.addWidget(nombre_input)
        layoutV2.addWidget(apellido_input)  # Corregido
        layoutV2.addWidget(edad_input)

        layoutV3 = QVBoxLayout()
        layoutV3.addWidget(correo_label)
        layoutV3.addWidget(direccion_label)
        layoutV3.addWidget(telefono_label)

        layoutV4 = QVBoxLayout()
        layoutV4.addWidget(correo_input)
        layoutV4.addWidget(direccion_input)
        layoutV4.addWidget(telefono_input)

        # Layouts horizontales
        layoutH1 = QHBoxLayout()
        layoutH1.addLayout(layoutV1)  # Corregido
        layoutH1.addLayout(layoutV2)  # Corregido

        layoutH2 = QHBoxLayout()
        layoutH2.addLayout(layoutV3)  # Corregido
        layoutH2.addLayout(layoutV4)  # Corregido

        layoutHF = QHBoxLayout()
        layoutHF.addLayout(layoutH1)  # Corregido
        layoutHF.addLayout(layoutH2)  # Corregido

        # Layout para el botón
        #layoutBoton = QHBoxLayout()
        #layoutBoton.addWidget(enviar_button)

        # Layout final
        layoutFinal = QVBoxLayout()
        layoutFinal.addWidget(message_label)
        layoutFinal.addLayout(layoutHF)
        layoutFinal.addWidget(enviar_button)

        self.setLayout(layoutFinal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
