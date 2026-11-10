from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFormLayout,
    QLineEdit
)

# QApplication: Administra la aplicación.
# QMainWindow: Crea la ventana principal.
# QWidget: Crea contenedores visuales.
# QPushButton: Crea botones.
# QVBoxLayout: Organiza widgets verticalmente.
# QHBoxLayout: Organiza widgets horizontalmente.
# QGridLayout: Organiza widgets en filas y columnas.
# QFormLayout: Organiza etiquetas y campos de formulario.
# QLineEdit: Permite introducir texto en una línea.

app = QApplication([])

ventana = QMainWindow()

ventana.setWindowTitle("Primera aplicación en PySide")

ventana.resize(600, 400)

# Contenedor principal
contenedor = QWidget()


#Layouts para organizar los widgets
vertical_layout=QVBoxLayout()
horizontal_layout=QHBoxLayout()
grid_layout=QGridLayout()
formulario_layout=QFormLayout()

contenedor.setLayout(vertical_layout)
vertical_layout.addLayout(horizontal_layout)
vertical_layout.addLayout(grid_layout)
vertical_layout.addLayout(formulario_layout)


#Botones horizontales
aceptar_boton=QPushButton("Aceptar")
cancelar_boton=QPushButton("Cancelar")

horizontal_layout.addWidget(aceptar_boton)
horizontal_layout.addWidget(cancelar_boton)


#botones de cuadricula
boton1=QPushButton("boton 1")
boton2=QPushButton("boton 2")
boton3=QPushButton("boton 3")
boton4=QPushButton("boton 4")

grid_layout.addWidget(boton1, 0,0)
grid_layout.addWidget(boton2, 0,1)
grid_layout.addWidget(boton3, 1,0)
grid_layout.addWidget(boton4, 1,1)

#Campos de texto
nombre_etiqueta=QLabel("Nombre")
nombre_campo=QLineEdit()

correo_etiqueta=QLabel("Correo")
correo_campo=QLineEdit()

formulario_layout.addRow(nombre_etiqueta, nombre_campo)
formulario_layout.addRow(correo_etiqueta, correo_campo)

#funcion

def aceptar():
    texto=nombre_campo.text()

    print(texto)
    correo_campo.clear()
    nombre_campo.clear()

aceptar_boton.clicked.connect(aceptar)

# Asignamos el contenedor a la ventana
ventana.setCentralWidget(contenedor)

ventana.show()

app.exec()