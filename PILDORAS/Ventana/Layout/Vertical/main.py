from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QLineEdit, QMessageBox, QVBoxLayout, QWidget)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
     
     # Haremos una diseño responsivo.
     # Aquí podemos una altura minima y un largo fijo.
     # Los botones se ajustan al minimunHeight 
    def inicializarUI(self):
        self.setMinimumHeight(200)
        self.setFixedWidth(200)
        self.setWindowTitle("Layout Vertical")
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
       button1 = QPushButton("Botón 1")
       button2 = QPushButton("Botón 2")
       button3 = QPushButton("Botón 3")
       button4 = QPushButton("Botón 4")
       
       button1.clicked.connect(self.imprimir_nombre_boton)
       button2.clicked.connect(self.imprimir_nombre_boton)
       button3.clicked.connect(self.imprimir_nombre_boton)
       button4.clicked.connect(self.imprimir_nombre_boton)
       

       #Los Layout se posiciona de arriba hacia abajo. (aliniados)
       layout = QVBoxLayout()
       layout.addWidget(button1)
       layout.addWidget(button2)
       layout.addWidget(button3)
       layout.addWidget(button4)
       self.setLayout(layout)
    
    def imprimir_nombre_boton(self):
        # Me regresa la señal del boton cliqueado
        boton = self.sender()
        QMessageBox.information(self,
                                'Boton press',
                                f'Boton Clickeado: {boton.text()}',
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok)
        
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())