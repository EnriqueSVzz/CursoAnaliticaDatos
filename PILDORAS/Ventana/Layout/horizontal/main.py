from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QLineEdit, QMessageBox, QHBoxLayout, QWidget)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
     
     # Haremos una diseño responsivo.   
    def inicializarUI(self):
        self.setMinimumWidth(600)
        self.setFixedHeight(80)
        self.setWindowTitle("Layout Horizontal")
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
       correo_label = QLabel('Correo Electronico:')
       correo_input = QLineEdit()
       enviar_button = QPushButton("Enviar")
       
       #Los Layout se posiciona de izquierda a derecha. (aliniados)
       layout = QHBoxLayout()
       layout.addWidget(correo_label)
       layout.addWidget(correo_input)
       layout.addWidget(enviar_button)
       self.setLayout(layout)
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())