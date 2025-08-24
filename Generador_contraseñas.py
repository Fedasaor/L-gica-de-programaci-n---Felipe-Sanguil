import tkinter as tk
from tkinter import messagebox
import random
import string

# Función para validar que la longitud sea válida (solo números, entre 1 y 15)
def validar_entrada(texto):
    if texto == "":  # permitir campo vacío momentáneamente
        return True
    if texto.isdigit():  # solo números
        valor = int(texto)
        if 1 <= valor <= 15:  # rango permitido
            return True
        else:
            messagebox.showwarning("Advertencia", "La longitud debe estar entre 1 y 15.")
            return False
    messagebox.showwarning("Advertencia", "Solo se permiten números en la longitud.")
    return False

# Función para generar la contraseña
def generar_contraseña():
    longitud = int(spinbox_longitud.get())
    usar_letras = var_letras.get()
    usar_numeros = var_numeros.get()
    usar_simbolos = var_simbolos.get()

    # Construcción de los caracteres disponibles
    caracteres = ""
    if usar_letras:
        caracteres += string.ascii_letters
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        messagebox.showwarning("Advertencia", "Selecciona al menos un tipo de carácter.")
        return

    contraseña = ""
    while True:
        contraseña = ""
        for _ in range(longitud):
            contraseña += random.choice(caracteres)

        # Validación de seguridad
        if usar_letras and not any(c.isalpha() for c in contraseña):
            continue
        if usar_numeros and not any(c.isdigit() for c in contraseña):
            continue
        if usar_simbolos and not any(c in string.punctuation for c in contraseña):
            continue
        break

    # Mostrar contraseña
    resultado.config(text=contraseña)

    # Guardar en archivo local
    with open("contraseña_generada.txt", "w") as archivo:
        archivo.write(contraseña)


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Generador Seguro de Contraseñas")
ventana.geometry("400x350")
ventana.configure(bg="#e8f0fe")

# Etiqueta de instrucción
tk.Label(ventana, text="Generador seguro de contraseñas", font=("Arial", 18), bg="#e8f0fe").pack(pady=10)

# Longitud
tk.Label(ventana, text="Longitud:", bg="#e8f0fe").pack()

# Validación para el Spinbox (solo 1–15, sin letras ni negativos)
vcmd = (ventana.register(validar_entrada), "%P")
spinbox_longitud = tk.Spinbox(ventana, from_=1, to=15, width=5, validate="key", validatecommand=vcmd)
spinbox_longitud.pack()

# Tipos de caracteres
var_letras = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

tk.Checkbutton(ventana, text="Incluir letras", variable=var_letras, bg="#e8f0fe").pack()
tk.Checkbutton(ventana, text="Incluir números", variable=var_numeros, bg="#e8f0fe").pack()
tk.Checkbutton(ventana, text="Incluir símbolos", variable=var_simbolos, bg="#e8f0fe").pack()

# Botón para generar
tk.Button(ventana, text="Generar Contraseña", command=generar_contraseña, bg="#4CAF50", fg="white").pack(pady=15)

# Resultado
resultado = tk.Label(ventana, text="", font=("Arial", 12), bg="#e8f0fe")
resultado.pack(pady=10)

# Ejecutar aplicación
ventana.mainloop()
