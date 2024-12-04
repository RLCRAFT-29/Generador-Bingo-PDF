import random
from tkinter import Tk, Label, Button, Entry, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_tabla_bingo():
    B = random.sample(range(1, 19), 5)
    I = random.sample(range(19, 37), 5)
    N = random.sample(range(37, 55), 5)
    N[2] = " "  # Espacio libre en el centro
    G = random.sample(range(55, 73), 5)
    O = random.sample(range(73, 91), 5)
    return [B, I, N, G, O]

def guardar_pdf(tablas, filename, imagen):
    try:
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        for index, tabla in enumerate(tablas, start=1):
            # Título del tablero
            c.setFont("Helvetica-Bold", 24)
            c.drawCentredString(width / 2, height - 50, f"BINGO - Tablero {index}")

            # Ajuste para centrar el tablero
            tablero_x_start = (width - 5 * 50) / 2  # Centro horizontal de la página
            tablero_y_start = height / 2 + 50  # Centrado verticalmente, con espacio extra para el título
            cell_width = 50
            cell_height = 50

            # Dibujar letras de "BINGO"
            c.setFont("Helvetica-Bold", 16)
            for i, col in enumerate("BINGO"):
                c.drawString(tablero_x_start + i * cell_width + 15, tablero_y_start + 15, col)

            # Dibujar cuadrícula del tablero
            c.setFont("Helvetica", 14)
            for row in range(5):
                for col in range(5):
                    x = tablero_x_start + col * cell_width
                    y = tablero_y_start - (row + 1) * cell_height
                    c.rect(x, y, cell_width, cell_height)  # Líneas de la cuadrícula
                    value = tabla[col][row]
                    if value != " ":  # Agregar números excepto el espacio vacío
                        c.drawCentredString(x + cell_width / 2, y + cell_height / 2 - 5, str(value))

            # Imagen decorativa en la celda "N" y número del tablero
            img_size = 40
            img_x = tablero_x_start + 2 * cell_width + 5
            img_y = tablero_y_start - 3 * cell_height + 5
            c.drawImage(imagen, img_x, img_y, img_size, img_size)
            c.drawCentredString(img_x + img_size / 2, img_y + img_size / 2 - 5, f"#{index}")

            # Borde decorativo
            c.setLineWidth(2)
            c.rect(tablero_x_start - 5, tablero_y_start - 5 * cell_height - 10, 5 * cell_width + 10, 5 * cell_height + 20)

            c.showPage()  # Nueva página para el siguiente tablero

        c.save()
        print(f"PDF generado con {len(tablas)} tableros en '{filename}'")
    except Exception as e:
        print("Error al generar el PDF:", str(e))

def seleccionar_imagen():
    global imagen_path
    imagen_path = filedialog.askopenfilename(filetypes=[("Imagen", "*.png;*.jpg;*.jpeg")])
    if imagen_path:
        label_imagen.config(text=f"Imagen seleccionada: {imagen_path.split('/')[-1]}")

def generar_bingos():
    try:
        num_paginas = int(entry_paginas.get())
        if num_paginas <= 0:
            label_resultado.config(text="Por favor, ingresa un número positivo.")
            return
        if not imagen_path:
            label_resultado.config(text="Por favor, selecciona una imagen.")
            return

        tablas = [generar_tabla_bingo() for _ in range(num_paginas)]
        guardar_pdf(tablas, "bingo_tableros.pdf", imagen_path)
        label_resultado.config(text=f"PDF generado con {num_paginas} tableros.")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa un número válido.")

# Configurar la interfaz gráfica
root = Tk()
root.title("Generador de Tableros de Bingo")

imagen_path = ""

Label(root, text="Número de tableros:").grid(row=0, column=0, padx=10, pady=10)
entry_paginas = Entry(root)
entry_paginas.grid(row=0, column=1, padx=10, pady=10)

Button(root, text="Seleccionar Imagen", command=seleccionar_imagen).grid(row=1, column=0, columnspan=2, padx=10, pady=10)
label_imagen = Label(root, text="No se ha seleccionado ninguna imagen.")
label_imagen.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

Button(root, text="Generar PDF", command=generar_bingos).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
label_resultado = Label(root, text="")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
