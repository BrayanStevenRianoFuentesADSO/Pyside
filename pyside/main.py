from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel,QPushButton

# QApplication	Administra la aplicación.
# QMainWindow	Crea la ventana principal.
# QWidget	Crea contenedores visuales.
# QLabel	Muestra texto.
# QPushButton	Crea botones.

app= QApplication()

ventana=QMainWindow()

ventana.setWindowTitle("Primera aplicacion en pyside")

ventana.resize(600,400)

contenedor=QWidget()
ventana.setCentralWidget(contenedor)
ventana.show()

app.exec()