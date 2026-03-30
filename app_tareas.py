import tkinter as tk
from tkinter import messagebox

# Lista para almacenar tareas
tareas = []

# Función para añadir tarea
def agregar_tarea(event=None):
    tarea = entrada.get().strip()
    if tarea != "":
        tareas.append({"texto": tarea, "completada": False})
        actualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese una tarea")

# Función para actualizar lista visual
def actualizar_lista():
    lista.delete(0, tk.END)
    for tarea in tareas:
        if tarea["completada"]:
            lista.insert(tk.END, "✔ " + tarea["texto"])
        else:
            lista.insert(tk.END, "✘ " + tarea["texto"])

# Función para marcar como completada
def completar_tarea():
    try:
        indice = lista.curselection()[0]
        tareas[indice]["completada"] = True
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea")

# Función para eliminar tarea
def eliminar_tarea():
    try:
        indice = lista.curselection()[0]
        tareas.pop(indice)
        actualizar_lista()
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea")

# Evento doble clic (opcional)
def doble_click(event):
    completar_tarea()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Campo de entrada
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

# Evento Enter
entrada.bind("<Return>", agregar_tarea)

# Botones
btn_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar como Completada", command=completar_tarea)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# Evento doble clic
lista.bind("<Double-Button-1>", doble_click)

# Ejecutar aplicación
ventana.mainloop()
