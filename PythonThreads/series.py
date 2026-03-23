import tkinter as tk
from tkinter import scrolledtext
import threading
import math


# -------------------------------------------------
# FUNCIONES MATEMATICAS
# -------------------------------------------------

def es_primo(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# -------------------------------------------------
# CALCULOS
# -------------------------------------------------

def calcular_primos():

    resultado = []
    numero = 2

    while len(resultado) < 100:

        if es_primo(numero):
            resultado.append(numero)

        numero += 1

    text_primos.delete("1.0", tk.END)
    text_primos.insert(tk.END, " ".join(map(str, resultado)))


def calcular_fibonacci():

    a, b = 0, 1
    resultado = []

    for _ in range(100):
        resultado.append(a)
        a, b = b, a + b

    text_fib.delete("1.0", tk.END)
    text_fib.insert(tk.END, " ".join(map(str, resultado)))


def calcular_triangulares():

    resultado = []

    for n in range(1, 101):
        triangular = (n * (n + 1)) // 2
        resultado.append(triangular)

    text_tri.delete("1.0", tk.END)
    text_tri.insert(tk.END, " ".join(map(str, resultado)))


# -------------------------------------------------
# EJECUCION CON HILOS
# -------------------------------------------------

def ejecutar_primos():
    threading.Thread(target=calcular_primos, daemon=True).start()


def ejecutar_fibonacci():
    threading.Thread(target=calcular_fibonacci, daemon=True).start()


def ejecutar_triangulares():
    threading.Thread(target=calcular_triangulares, daemon=True).start()


# -------------------------------------------------
# BOTON REINICIAR
# -------------------------------------------------

def reiniciar():

    text_primos.delete("1.0", tk.END)
    text_fib.delete("1.0", tk.END)
    text_tri.delete("1.0", tk.END)


# -------------------------------------------------
# INTERFAZ GRAFICA
# -------------------------------------------------

root = tk.Tk()
root.title("Series Matemáticas con Hilos")

root.state("zoomed")
root.minsize(900, 500)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)


# -------------------------------------------------
# FRAME PRIMOS
# -------------------------------------------------

frame_primos = tk.LabelFrame(root, text="Primeros 100 números primos")
frame_primos.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

frame_primos.columnconfigure(0, weight=1)
frame_primos.rowconfigure(1, weight=1)

btn_primos = tk.Button(frame_primos, text="Calcular", command=ejecutar_primos)
btn_primos.grid(row=0, column=0, sticky="ew")

text_primos = scrolledtext.ScrolledText(frame_primos)
text_primos.grid(row=1, column=0, sticky="nsew")


# -------------------------------------------------
# FRAME FIBONACCI
# -------------------------------------------------

frame_fib = tk.LabelFrame(root, text="Primeros 100 números Fibonacci")
frame_fib.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

frame_fib.columnconfigure(0, weight=1)
frame_fib.rowconfigure(1, weight=1)

btn_fib = tk.Button(frame_fib, text="Calcular", command=ejecutar_fibonacci)
btn_fib.grid(row=0, column=0, sticky="ew")

text_fib = scrolledtext.ScrolledText(frame_fib)
text_fib.grid(row=1, column=0, sticky="nsew")


# -------------------------------------------------
# FRAME TRIANGULARES
# -------------------------------------------------

frame_tri = tk.LabelFrame(root, text="Primeros 100 números triangulares")
frame_tri.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

frame_tri.columnconfigure(0, weight=1)
frame_tri.rowconfigure(1, weight=1)

btn_tri = tk.Button(frame_tri, text="Calcular", command=ejecutar_triangulares)
btn_tri.grid(row=0, column=0, sticky="ew")

text_tri = scrolledtext.ScrolledText(frame_tri)
text_tri.grid(row=1, column=0, sticky="nsew")


# -------------------------------------------------
# PANEL DE CONTROL INFERIOR
# -------------------------------------------------

frame_control = tk.Frame(root)
frame_control.grid(row=1, column=0, columnspan=3, pady=10)

btn_reiniciar = tk.Button(frame_control, text="Reiniciar", width=15, command=reiniciar)
btn_reiniciar.pack(side=tk.LEFT, padx=20)

btn_salir = tk.Button(frame_control, text="Salir", width=15, command=root.destroy)
btn_salir.pack(side=tk.LEFT, padx=20)


root.mainloop()