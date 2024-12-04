
# Generador de Tableros de Bingo 🟢

Este proyecto genera tableros de bingo en formato PDF con opciones de personalización a través de una interfaz gráfica interactiva. Los tableros incluyen una imagen decorativa en la celda central de la columna "N" y están numerados en cada página.

## Características
- Genera múltiples tableros de bingo (5x5) con numeración automática.
- Añade una imagen decorativa en el centro del tablero.
- Interfaz gráfica para seleccionar el número de tableros y la imagen decorativa.
- Los tableros están centrados en la página con un título claro en la parte superior.

---

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes elementos:

1. **Python 3.8 o superior**: Puedes descargarlo desde [python.org](https://www.python.org/).
2. **Bibliotecas necesarias**:
    - `reportlab`: Para generar el archivo PDF con el tablero de bingo.
    - `tkinter`: Para la interfaz gráfica (generalmente incluido en Python por defecto).

---

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto:

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/generador-bingo.git
cd generador-bingo
```

### 2. Crear un entorno virtual (opcional)
Para asegurarte de que no haya conflictos con otras instalaciones de Python, puedes crear un entorno virtual:
```bash
python -m venv env
source env/bin/activate    # En Linux/MacOS
env\Scriptsctivate       # En Windows
```

### 3. Instalar las dependencias
Asegúrate de tener las dependencias necesarias instaladas ejecutando el siguiente comando:
```bash
pip install reportlab
```

### 4. Ejecutar el programa
Ejecuta el script con el siguiente comando:
```bash
python generador_bingo.py
```

---

## Uso

1. Al ejecutar el programa, se abrirá una interfaz gráfica donde puedes ingresar la cantidad de tableros de bingo que deseas generar.
2. En la interfaz:
   - **Número de tableros**: Ingresa cuántos tableros quieres generar en el archivo PDF.
   - **Seleccionar Imagen**: Selecciona una imagen decorativa que se incluirá en la celda central del tablero.
   - **Generar PDF**: Haz clic en "Generar PDF" para crear el archivo `bingo_tableros.pdf`.

3. El archivo PDF generado tendrá los tableros de bingo, cada uno numerado y con una imagen en la celda central.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto:
1. Haz un fork del repositorio.
2. Realiza tus cambios en una nueva rama.
3. Envía un Pull Request con una descripción clara de tus mejoras.
