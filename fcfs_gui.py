import tkinter as tk
import threading
import random
import time

# -------------------------
# GENERAR 6 PROCESOS
# -------------------------
procesos = [
    {
        "id": i,
        "llegada": 0,
        "rafaga": random.randint(2, 6),
        "io": 0
    }
    for i in range(1, 7)
]

# -------------------------
# INTERFAZ
# -------------------------
root = tk.Tk()
root.title("FCFS con Tabla + Gantt")

canvas = tk.Canvas(root, width=1200, height=500)
canvas.pack()

# -------------------------
# TABLA
# -------------------------
headers = ["PID", "Tiempo de Llegada", "Ráfaga CPU", "Ráfaga E/S"]

for i, h in enumerate(headers):
    canvas.create_text(150 + i*200, 30, text=h, font=("Arial", 10, "bold"))

for i, p in enumerate(procesos):
    y = 60 + i*25
    canvas.create_text(150, y, text=f"P{p['id']}")
    canvas.create_text(350, y, text=p["llegada"])
    canvas.create_text(550, y, text=p["rafaga"])
    canvas.create_text(750, y, text=p["io"])

# -------------------------
# GANTT
# -------------------------
cell_w = 40
cell_h = 40
start_x = 150
start_y = 250

# Etiquetas procesos
for i in range(6):
    canvas.create_text(100, start_y + i*cell_h + 20, text=f"P{i+1}")

timeline = []

def draw_step(t):
    pid = timeline[t]

    if pid is not None:
        fila = pid - 1

        x = start_x + t * cell_w
        y = start_y + fila * cell_h

        canvas.create_rectangle(x, y, x+cell_w, y+cell_h, fill="green")
        canvas.create_text(x+20, y+20, text=f"P{pid}")

    # tiempo
    canvas.create_text(start_x + t*cell_w + 20,
                       start_y + 6*cell_h + 20,
                       text=f"t{t}")

# -------------------------
# SIMULACIÓN FCFS
# -------------------------
def simular():
    tiempo = 0
    cola = procesos.copy()

    while cola:
        proceso = cola.pop(0)

        for _ in range(proceso["rafaga"]):
            timeline.append(proceso["id"])

            root.after(0, draw_step, tiempo)

            tiempo += 1
            time.sleep(0.5)

threading.Thread(target=simular).start()

root.mainloop() 
import tkinter as tk
import threading
import random
import time

# -------------------------
# GENERAR 6 PROCESOS
# -------------------------
procesos = [
    {
        "id": i,
        "llegada": 0,
        "rafaga": random.randint(2, 6),
        "io": 0
    }
    for i in range(1, 7)
]

# -------------------------
# INTERFAZ
# -------------------------
root = tk.Tk()
root.title("FCFS con Tabla + Gantt")

canvas = tk.Canvas(root, width=1200, height=500)
canvas.pack()

# -------------------------
# TABLA
# -------------------------
headers = ["PID", "Tiempo de Llegada", "Ráfaga CPU", "Ráfaga E/S"]

for i, h in enumerate(headers):
    canvas.create_text(150 + i*200, 30, text=h, font=("Arial", 10, "bold"))

for i, p in enumerate(procesos):
    y = 60 + i*25
    canvas.create_text(150, y, text=f"P{p['id']}")
    canvas.create_text(350, y, text=p["llegada"])
    canvas.create_text(550, y, text=p["rafaga"])
    canvas.create_text(750, y, text=p["io"])

# -------------------------
# GANTT
# -------------------------
cell_w = 40
cell_h = 40
start_x = 150
start_y = 250

# Etiquetas procesos
for i in range(6):
    canvas.create_text(100, start_y + i*cell_h + 20, text=f"P{i+1}")

timeline = []

def draw_step(t):
    pid = timeline[t]

    if pid is not None:
        fila = pid - 1

        x = start_x + t * cell_w
        y = start_y + fila * cell_h

        canvas.create_rectangle(x, y, x+cell_w, y+cell_h, fill="green")
        canvas.create_text(x+20, y+20, text=f"P{pid}")

    # tiempo
    canvas.create_text(start_x + t*cell_w + 20,
                       start_y + 6*cell_h + 20,
                       text=f"t{t}")

# -------------------------
# SIMULACIÓN FCFS
# -------------------------
def simular():
    tiempo = 0
    cola = procesos.copy()

    while cola:
        proceso = cola.pop(0)

        for _ in range(proceso["rafaga"]):
            timeline.append(proceso["id"])

            root.after(0, draw_step, tiempo)

            tiempo += 1
            time.sleep(0.5)

threading.Thread(target=simular).start()

root.mainloop()