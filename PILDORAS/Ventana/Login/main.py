from PyQt6.QtWidgets import (QDialog, QLabel, QPushButton, QLineEdit, QMessageBox)
from PyQt6.QtGui import QPixmap

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.inicializarUI()
        
    def inicializarUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Ventana Principal")
        self.generar_contenido()
    
    def generar_contenido(self):
        imagen_path = 'tigres.jpeg'  # Asegúrate de que está en la misma carpeta
        
        # Verifica si la imagen se carga correctamente
        pixmap = QPixmap(imagen_path)
        
        
        if pixmap.isNull():
            print("La imagen no se cargó. Revisa la ruta o el formato.")
        else:
            print("La imagen se cargó correctamente.")

        if pixmap.isNull():  # isNull() verifica si la imagen no se pudo cargar
            QMessageBox.warning(self, 'Error', f'No se encontró el archivo: {imagen_path}', 
                                QMessageBox.StandardButton.Close)
        else:
            image_label = QLabel(self)  
            image_label.setPixmap(pixmap)  
            image_label.setGeometry(50, 50, pixmap.width(), pixmap.height())  # Posiciona la imagen
            image_label.show()  # Asegura que el QLabel se muestre

