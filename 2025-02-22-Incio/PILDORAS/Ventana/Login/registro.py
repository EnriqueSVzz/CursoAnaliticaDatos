from PyQt6.QtWidgets import (QDialog, QLabel, QPushButton, QLineEdit, QMessageBox)
from PyQt6.QtGui import QFont

class RegistrarUsuarioView(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.generar_formulario()
        
    def generar_formulario(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("Registrar Usuario")
        
        # Label Usuario
        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial', 10))
        user_label.move(20, 44)
        
        # TextField Usuario
        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 40)
        
        # Label Password
        password_1_label = QLabel(self)
        password_1_label.setText("Password:")
        password_1_label.setFont(QFont('Arial', 10))
        password_1_label.move(20, 74)
        
        # TextField Password
        self.password_1_input = QLineEdit(self)
        self.password_1_input.resize(250, 24)
        self.password_1_input.move(90, 70)
        self.password_1_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        # Label Confirmar Password
        password_2_label = QLabel(self)
        password_2_label.setText("Password (Second Time):")
        password_2_label.setFont(QFont('Arial', 10))
        password_2_label.move(20, 104)
        
        # TextField Confirmar Password
        self.password_2_input = QLineEdit(self)
        self.password_2_input.resize(250, 24)
        self.password_2_input.move(90, 100)
        self.password_2_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        # Botón para crear usuario
        create_button = QPushButton(self)
        create_button.setText("Crear")
        create_button.resize(150, 32)
        create_button.move(20, 170)
        create_button.clicked.connect(self.crear_usuario)
        
        # Botón para cancelar
        cancel_button = QPushButton(self)
        cancel_button.setText("Cancelar")
        cancel_button.resize(150, 32)
        cancel_button.move(170, 170)
        cancel_button.clicked.connect(self.cancelar_creacion)

    def cancelar_creacion(self):
        """ Cierra la ventana de diálogo """
        self.close()
    
    def crear_usuario(self):
        """ Crea un usuario y lo guarda en un archivo """
        user_path = "usuarios.txt"
        usuario = self.user_input.text().strip()
        password1 = self.password_1_input.text().strip()
        password2 = self.password_2_input.text().strip()
        
        if not usuario or not password1 or not password2:
            QMessageBox.warning(self, 'Error', 'Por favor ingrese datos válidos', 
                                QMessageBox.StandardButton.Close)
        elif password1 != password2:
            QMessageBox.warning(self, 'Error', 'Las contraseñas no coinciden', 
                                QMessageBox.StandardButton.Close)
        else:
            try:
                with open(user_path, 'a') as f:  # ✅ Cambiado de 'r' a 'a' (append)
                    f.write(f"{usuario}, {password1}\n")
                
                QMessageBox.information(self, 'Éxito', 'Usuario registrado correctamente', 
                                        QMessageBox.StandardButton.Ok)
                self.close()  # ✅ Cierra la ventana después de registrar

            except Exception as e:
                QMessageBox.warning(self, 'Error', f'No se pudo abrir la base de datos: {str(e)}', 
                                    QMessageBox.StandardButton.Close)
