
# PySide6 - Notas de aprendizaje

Registro de conceptos, explicaciones, configuraciones, prácticas y errores encontrados durante el aprendizaje de PySide6.

---

# 1. FUNDAMENTOS

## 1.1. ¿Qué es Qt?

Qt es un framework multiplataforma utilizado para desarrollar aplicaciones con interfaces gráficas (GUI), entre otras funcionalidades.

Permite crear ventanas, botones, formularios, menús, tablas y diferentes componentes visuales.

## 1.2. ¿Qué es PySide6?

PySide6 es el conjunto de bindings oficiales de Qt para Python, conocido como Qt for Python.

Los bindings permiten utilizar las funcionalidades de Qt escribiendo código Python.

En otras palabras:

- Qt proporciona las herramientas para desarrollar interfaces gráficas.
- PySide6 permite utilizar esas herramientas desde Python.

## 1.3. ¿Qué es un widget?

Un widget es un componente visual de una interfaz gráfica.

Algunos ejemplos son:

- QPushButton: botón.
- QLabel: etiqueta de texto.
- QLineEdit: campo de entrada de texto.
- QWidget: componente visual que también puede utilizarse como contenedor.

Los widgets pueden contener otros widgets y formar interfaces más complejas.

## 1.4. ¿Qué es un Layout?

Un Layout es un administrador de distribución que organiza los widgets dentro de un contenedor.

Se encarga de distribuir y ajustar los componentes según el espacio disponible.

A diferencia de posicionar manualmente cada componente, los layouts permiten construir interfaces que se adaptan al tamaño de la ventana.

---

# 2. CONFIGURACIÓN DEL ENTORNO

## 2.1. Crear un entorno virtual

Un entorno virtual permite mantener las dependencias de un proyecto separadas de las instalaciones globales de Python y de otros proyectos.

Para crear uno en Windows utilizando PowerShell:

```powershell
py -m venv .venv
```

Esto crea una carpeta llamada `.venv` con el entorno virtual.

## 2.2. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si se activa correctamente, aparecerá `(.venv)` al comienzo de la línea de comandos.

En Linux:

```bash
source .venv/bin/activate
```

## 2.3. Instalar PySide6

Con el entorno virtual activado:

```powershell
py -m pip install PySide6
```

También podemos comprobar la instalación con:

```powershell
py -m pip show PySide6
```

## 2.4. ¿Por qué utilizar `py -m pip`?

En Windows, `py` es el lanzador de Python.

Al ejecutar `py -m pip`, le indicamos a Python que ejecute el módulo pip.

Esto evita depender de que el comando `pip` esté disponible directamente en la variable PATH.

---

# 3. IMPORTAR CLASES DE PYSIDE6

## 3.1. ¿Qué significa importar?

Importar permite utilizar clases, funciones y otros elementos definidos en módulos externos.

Por ejemplo:

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
```

Estamos importando tres clases desde el módulo `QtWidgets` de PySide6.

Algunas clases que hemos conocido:

| Clase | Función |
|---|---|
| QApplication | Administra la aplicación gráfica. |
| QMainWindow | Proporciona la estructura de una ventana principal. |
| QWidget | Componente visual y contenedor. |
| QLabel | Muestra texto. |
| QPushButton | Crea botones. |
| QLineEdit | Permite introducir texto en una línea. |
| QVBoxLayout | Organiza widgets verticalmente. |
| QHBoxLayout | Organiza widgets horizontalmente. |
| QGridLayout | Organiza widgets en filas y columnas. |
| QFormLayout | Organiza etiquetas y campos de formulario. |

---

# 4. APLICACIÓN Y CICLO DE EVENTOS

## 4.1. QApplication

QApplication es el objeto que administra una aplicación gráfica basada en Qt Widgets.

Entre sus responsabilidades están:

- Inicializar la aplicación.
- Gestionar los eventos.
- Coordinar el funcionamiento de la interfaz gráfica.
- Administrar el ciclo de vida de la aplicación.

Normalmente se crea una única instancia de QApplication por aplicación.

Ejemplo:

```python
app = QApplication([])
```

Los paréntesis crean una instancia de la clase.

El argumento `[]` representa una lista vacía de argumentos de línea de comandos.

## 4.2. Event Loop

El Event Loop o ciclo de eventos es el mecanismo que permite que la aplicación procese los eventos mientras está funcionando.

Algunos ejemplos de eventos son:

- Clics del mouse.
- Pulsaciones del teclado.
- Redimensionamiento de ventanas.
- Cierre de ventanas.

## 4.3. app.exec()

```python
app.exec()
```

Este método inicia el ciclo de eventos de la aplicación.

Sin él, la aplicación no mantiene el procesamiento normal de eventos de la interfaz.

Es importante recordar que `show()` y `exec()` cumplen funciones diferentes:

- `show()`: muestra la ventana.
- `exec()`: inicia el ciclo de eventos.

---

# 5. VENTANAS Y WIDGETS

## 5.1. Clases e instancias

Una clase es una definición que establece cómo se comportarán los objetos.

Una instancia es un objeto concreto creado a partir de una clase.

Ejemplo:

```python
ventana = QMainWindow()
```

- `QMainWindow`: es la clase.
- `QMainWindow()`: crea una instancia.
- `ventana`: es la variable que almacena esa instancia.

Los paréntesis `()` permiten ejecutar el constructor de la clase y crear el objeto.

## 5.2. QMainWindow

QMainWindow es una clase especializada para crear la ventana principal de una aplicación.

Proporciona una estructura que puede incluir:

- Barra de menús.
- Barra de herramientas.
- Widget central.
- Barra de estado.
- Áreas acoplables.

No es simplemente un contenedor común, sino una ventana principal con una estructura definida.

## 5.3. QWidget

QWidget es una clase base de los componentes visuales de Qt.

También puede utilizarse para crear contenedores donde colocamos otros widgets y layouts.

Ejemplo:

```python
contenedor = QWidget()
```

## 5.4. setCentralWidget()

```python
ventana.setCentralWidget(contenedor)
```

Establece el widget que ocupará el área central de un QMainWindow.

QMainWindow utiliza este método para recibir su contenido principal.

## 5.5. setWindowTitle()

```python
ventana.setWindowTitle("Primera aplicación en PySide")
```

Establece el título que aparecerá en la barra superior de la ventana.

## 5.6. resize()

```python
ventana.resize(600, 400)
```

Establece el tamaño inicial de la ventana.

- 600: ancho.
- 400: alto.

Las dimensiones se expresan en píxeles lógicos de Qt.

## 5.7. show()

```python
ventana.show()
```

Hace visible la ventana.

---

# 6. LAYOUTS Y DISTRIBUCIÓN DE WIDGETS

## 6.1. ¿Qué hacen los Layouts?

Los layouts administran la posición y distribución de los widgets dentro de un contenedor.

Permiten que la interfaz se adapte cuando cambia el tamaño de la ventana.

Un QWidget solamente puede tener un layout principal instalado directamente.

Sin embargo, ese layout puede contener otros layouts.

## 6.2. QVBoxLayout

Organiza los widgets verticalmente, de arriba hacia abajo.

Ejemplo:

```python
layout = QVBoxLayout()
```

Se utiliza para organizar elementos como:

- Menús verticales.
- Paneles.
- Listas de opciones.
- Grupos de botones.

## 6.3. QHBoxLayout

Organiza los widgets horizontalmente, de izquierda a derecha.

Ejemplo:

```python
layout = QHBoxLayout()
```

Se utiliza para:

- Barras de herramientas.
- Botones de navegación.
- Grupos de botones horizontales.

## 6.4. QGridLayout

Organiza los widgets mediante filas y columnas.

Ejemplo:

```python
grid = QGridLayout()
```

Su método addWidget() permite indicar la posición del widget:

```python
grid.addWidget(widget, fila, columna)
```

Ejemplo de distribución:

| | Columna 0 | Columna 1 |
|---|---|---|
| Fila 0 | Botón A | Botón B |
| Fila 1 | Botón C | Botón D |

## 6.5. QFormLayout

Está especializado en organizar formularios.

Ejemplo:

```python
formulario = QFormLayout()
```

Permite relacionar etiquetas con campos de entrada utilizando:

```python
formulario.addRow("Nombre:", campo_nombre)
```

Es útil para formularios de registro y edición de información.

## 6.6. Instalar un Layout: setLayout()

```python
contenedor.setLayout(layout)
```

Instala un layout en un QWidget.

Un contenedor solo puede tener un layout principal.

## 6.7. Agregar widgets: addWidget()

```python
layout.addWidget(boton)
```

Agrega un widget al layout.

Cada llamada agrega un widget.

Si tenemos varios widgets, podemos utilizar varias llamadas o recorrer una lista mediante un bucle for.

## 6.8. Agregar layouts: addLayout()

```python
layout_principal.addLayout(layout_secundario)
```

Permite incorporar un layout dentro de otro.

Esto permite combinar diferentes tipos de distribución.

Por ejemplo:

- Un QVBoxLayout principal.
- Un QHBoxLayout dentro del principal.
- Un QGridLayout dentro del principal.
- Un QFormLayout dentro del principal.

## 6.9. Espaciado: setSpacing()

```python
layout.setSpacing(20)
```

Establece la distancia entre los widgets consecutivos de un layout.

El valor representa píxeles lógicos.

## 6.10. Márgenes: setContentsMargins()

Permite controlar la separación entre los elementos del layout y los bordes de su contenedor.

Recibe cuatro argumentos:

```python
layout.setContentsMargins(10, 10, 10, 10)
```

El orden es:

1. Izquierda.
2. Arriba.
3. Derecha.
4. Abajo.

## 6.11. Alineación: setAlignment()

Permite establecer la alineación de los widgets dentro del layout.

Para utilizar las opciones de alineación necesitamos importar Qt desde PySide6.QtCore.

Algunas opciones son:

- Qt.AlignmentFlag.AlignLeft
- Qt.AlignmentFlag.AlignRight
- Qt.AlignmentFlag.AlignCenter
- Qt.AlignmentFlag.AlignTop
- Qt.AlignmentFlag.AlignBottom

---

# 7. ERRORES Y SOLUCIONES

## 7.1. Error: bash: pip: command not found

### Problema

Git Bash no encuentra el ejecutable pip mediante el comando directo.

Esto no significa necesariamente que Python o pip no estén instalados.

### Solución

En Windows podemos utilizar:

```powershell
py -m pip --version
```

Para instalar paquetes:

```powershell
py -m pip install PySide6
```

## 7.2. Error: setCentralWidget() called with wrong argument types

### Problema

Qt esperaba recibir una instancia de QWidget, pero recibió un objeto de tipo incorrecto.

Una causa frecuente es escribir:

```python
contenedor = QWidget
```

En lugar de:

```python
contenedor = QWidget()
```

En el primer caso estamos guardando una referencia a la clase.

En el segundo estamos creando una instancia de QWidget.

### Solución

Comprobar que estamos creando correctamente el objeto antes de pasarlo a setCentralWidget().

## 7.3. Error: llamar un método sin paréntesis

Por ejemplo:

```python
app.exec
```

Esto solamente hace referencia al método, pero no lo ejecuta.

La forma correcta es:

```python
app.exec()
```

Los paréntesis permiten realizar la llamada al método.

---

# 8. ESTADO ACTUAL DEL APRENDIZAJE

## Conceptos estudiados

- [x] Qt y PySide6.
- [x] Entornos virtuales.
- [x] Instalación de PySide6.
- [x] Importación de clases.
- [x] Clases e instancias.
- [x] QApplication.
- [x] Event Loop.
- [x] QMainWindow.
- [x] QWidget.
- [x] QLabel y QPushButton (conocidos).
- [x] QVBoxLayout.
- [x] QHBoxLayout.
- [x] QGridLayout.
- [x] QFormLayout (introducción).
- [x] addWidget().
- [x] addLayout().
- [x] setLayout().
- [x] setSpacing().

## Próximos temas

- [ ] QLineEdit y entrada de datos.
- [ ] QTextEdit.
- [ ] QCheckBox.
- [ ] QComboBox.
- [ ] QSpinBox.
- [ ] Señales y slots (Signals & Slots).
- [ ] Eventos e interacción con botones.
- [ ] Diálogos y ventanas secundarias.
- [ ] Diseño y estilos con QSS.
- [ ] Model/View y tablas.
- [ ] Organización del código y arquitectura.

---

**Nota:** Este documento es un registro de aprendizaje. Los ejemplos y conceptos se irán ampliando conforme avancemos en PySide6.
