# ¿Qué es Qt y qué es PySide6?

Qt es un framework para desarrollar aplicaciones con interfaces gráficas.

PySide6 es el conjunto de bindings oficiales de Qt para Python. Es decir, permite utilizar las funcionalidades de Qt escribiendo código Python.

# QApplication

Es el objeto que administra la aplicación gráfica.

Entre sus responsabilidades están:
- Inicializar la aplicación.
- Gestionar los eventos.
- Coordinar el ciclo de vida de la interfaz.

# Crear y ejecutar nuestro entorno virtual

```Powershell

py -m venv .venv

.\.venv\Scripts\Activate.ps1

# deberia aparecer (.venv) en consola
```
# instalar pyside

py -m pip install PySide6

# importar pyside



# Errores y soluciones

```bash
bash: pip: command not found

Significa que Git Bash no encuentra el ejecutable pip.

**intentar con py en lugar de python**
```

### Comprobar tener python y pip instalados

```bash
bash: py --version

(Version de python)

py -m pip --version

(version de pip)

```

## intentar instalar pyside de nuevo

py -m pip install PySide6

```bash:
TypeError: 'PySide6.QtWidgets.QMainWindow.setCentralWidget' called with wrong argument types:
  PySide6.QtWidgets.QMainWindow.setCentralWidget(ObjectType)
Supported signatures:
  PySide6.QtWidgets.QMainWindow.setCentralWidget(widget: PySide6.QtWidgets.QWidget, 

# puede significar que no agregamos los parentesis a un metodo
```