import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QMessageBox, QCheckBox)

from PyQt6.QtGui import QFont, QPixmap 

from registro import RegistrarUsuarioView
from main import MainWindow

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Login")
        self.generar_formulario()
        self.show()
        
    def generar_formulario(self):
        self.is_logged = False
        user_label = QLabel(self)
        user_label.setText("Usuario:")
        user_label.setFont(QFont('Arial',10))
        user_label.move(20,54)
        
        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,50)
        
        password_label = QLabel(self)
        password_label.setText("Contraseña:")
        password_label.setFont(QFont('Arial',10))
        password_label.move(20,86)
        
        self.password_input = QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.move(90,82)
        #Para ver la contraseña como puntos
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        #Check para ver contraseña
        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("Ver contraseña")
        self.check_view_password.move(90,120)
        self.check_view_password.toggled.connect(self.mostrar_contrasena)
        
        #Botones iniciar sesión
        login_button = QPushButton(self)
        login_button.setText("Iniciar sesión")
        login_button.resize(320,24)
        login_button.move(20,140)
        login_button.clicked.connect(self.login)
        
        #Botones registrar
        register_button = QPushButton(self)
        register_button.setText("Registrate")
        register_button.resize(320,24)
        register_button.move(20,180)
        register_button.clicked.connect(self.registrar_usuario)
    
    def mostrar_contrasena(self, clicked):
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
    
    #Acción para Login    
    def login(self):
        users = []
        user_path = 'usuarios.txt'
        try:
            with open(user_path, 'r') as f:
                for line in f:
                    users.append(line.strip("\n"))
            login_information = f"{self.user_input.text()}, {self.password_input.text()}"

            if login_information in users:
                 QMessageBox.information(self, 'Inicio Sesión',
                'Inicio Exitoso', 
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                 self.is_logged = True
                 self.close()
                 self.open_main_window()
            else:
                QMessageBox.warning(self, 'Inicio Sesión',
                                    'Inicio Fallido',
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)
                
        except FileNotFoundError as e:
            QMessageBox.warning(self, 'Error', f' No se encontró el archivo: {str(e)}', 
                                    QMessageBox.StandardButton.Close)
        
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Falló el Login: {str(e)}', 
                                    QMessageBox.StandardButton.Close)

    #Debenser variables de instancia (self) para que funcione
    def registrar_usuario(self):
        self.new_user_form = RegistrarUsuarioView()
        self.new_user_form.show()

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())