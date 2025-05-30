from PyQt6.QtWidgets import (QApplication, QLabel, QPushButton, QLineEdit, 
                             QMessageBox, QHBoxLayout, QVBoxLayout, QWidget,
                             QGridLayout,QTextEdit)
import sys

'''
==================
Pantalla (2 Filas *4 Columnas)
==================

[   CE    ]     [<--]   [+]
[7]     [8]     [9]     [/]
[4]     [5]     [6]     [*]
[1]     [2]     [3]     [-]
[0]     [00]    [.]     [=]

'''


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.primer_valor = ''
        self.segundo_valor = ''
        self.pointer_flag = '1'
        self.after_equal = False
        self.after_operator = False

    def inicializarUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Calculadora")
        self.generar_interfaz()
        self.show()
    
    def generar_interfaz(self):
        #Establecemos la pantalla
        self.pantalla = QTextEdit()
        self.pantalla.setDisabled(True)
        
        #creamos los botones de la calculadora
        button_1 = QPushButton("1")
        button_2 = QPushButton("2")
        button_3 = QPushButton("3")
        button_4 = QPushButton("4")
        button_5 = QPushButton("5")
        button_6 = QPushButton("6")
        button_7 = QPushButton("7")
        button_8 = QPushButton("8")
        button_9 = QPushButton("9")
        button_0 = QPushButton("0")
        button_00 = QPushButton("00")
        button_punto = QPushButton(".")
        
        # Eventos
        button_1.clicked.connect(self.ingresar_datos)
        button_2.clicked.connect(self.ingresar_datos)
        button_3.clicked.connect(self.ingresar_datos)
        button_4.clicked.connect(self.ingresar_datos)
        button_5.clicked.connect(self.ingresar_datos)
        button_6.clicked.connect(self.ingresar_datos)
        button_7.clicked.connect(self.ingresar_datos)
        button_8.clicked.connect(self.ingresar_datos)
        button_9.clicked.connect(self.ingresar_datos)
        button_0.clicked.connect(self.ingresar_datos)
        button_00.clicked.connect(self.ingresar_datos)
        button_punto.clicked.connect(self.ingresar_datos)
        
        #creamos nuestros botones de operaciones
        button_suma = QPushButton("+")
        button_resta = QPushButton("-")
        button_multiplicacion = QPushButton("*")
        button_division = QPushButton("/")
        
        #Eventos de operadores
        button_suma.clicked.connect(self.insertar_operador)
        button_resta.clicked.connect(self.insertar_operador)
        button_multiplicacion.clicked.connect(self.insertar_operador)
        button_division.clicked.connect(self.insertar_operador)
        
        #botones de procesamiento
        button_ce = QPushButton("CE")
        button_borrar = QPushButton("<--")
        button_resultado = QPushButton("=")
        
        #Creamos nuestro GridLayout.
        #Es un plano cartesiano como EXcel.
        self.main_grid = QGridLayout()
        # (atributi, posicion_inicial_x, posicion_iniciar_y, cantidad de columnas, cantidad de filas)
        self.main_grid.addWidget(self.pantalla,0,0,2,4)
        
        #Nos posicionamos la tercera fila, primera fila y hacemos que mida 2 columnas
        self.main_grid.addWidget(button_ce,2,0,1,2)
        
        #Solos nos posicionamos en la columna x,y
        #aquí estamos insertando hacia la izquierda
        self.main_grid.addWidget(button_borrar,2,2)
        self.main_grid.addWidget(button_suma,2,3)
        
        self.main_grid.addWidget(button_7,3,0)
        self.main_grid.addWidget(button_8,3,1)
        self.main_grid.addWidget(button_9,3,2)
        self.main_grid.addWidget(button_division,3,3)
        
        self.main_grid.addWidget(button_4,4,0)
        self.main_grid.addWidget(button_5,4,1)
        self.main_grid.addWidget(button_6,4,2)
        self.main_grid.addWidget(button_multiplicacion,4,3)
        
        self.main_grid.addWidget(button_1,5,0)
        self.main_grid.addWidget(button_2,5,1)
        self.main_grid.addWidget(button_3,5,2)
        self.main_grid.addWidget(button_resta,5,3)
        
        self.main_grid.addWidget(button_0,6,0)
        self.main_grid.addWidget(button_00,6,1)
        self.main_grid.addWidget(button_punto,6,2)
        self.main_grid.addWidget(button_resultado,6,3)
        
        #Cargamos nuestro Grid
        self.setLayout(self.main_grid)
    
    def ingresar_datos(self):
        # Función para detectar de donde viene el evento.
        boton_text = self.sender().text()
        if self.pointer_flag == "1":
            self.primer_valor += boton_text
        else:
            self.segundo_valor += boton_text
            self.pantalla.setText(self.pantalla.toPlainText() + boton_text)
    
    def insertar_operador(self):
        # Función para detectar de donde viene el evento.
        boton_text = self.sender().text()
        self.operador= boton_text
        self.pointer_flag = "2"
        
        self.pantalla.setText(self.pantalla.toPlainText()+ ' ' + boton_text + ' ')
        self.after_operador = True
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
