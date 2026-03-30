# ---------------- IMPORTACIÓN DE LIBRERÍAS ---------------- #
import tkinter as tk


# ---------------- CLASE PRINCIPAL DE LA APLICACIÓN ---------------- #
class TaskApp:
    def __init__(self, root):

        # ---------------- CONFIGURACIÓN DE LA VENTANA ---------------- #
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        # ---------------- ESTRUCTURA DE DATOS ---------------- #
        self.tasks = []

        # ---------------- CAMPO DE ENTRADA ---------------- #
        tk.Label(root, text="Nueva Tarea:", font=("Arial", 10, "bold")).pack(pady=5)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.add_task_event)

        # ---------------- LISTA DE TAREAS ---------------- #
        tk.Label(root, text="Lista de Tareas:", font=("Arial", 10, "bold")).pack(pady=5)

        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=5)

        # ---------------- BOTONES ---------------- #
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.add_btn = tk.Button(btn_frame, text="Añadir", width=12, command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Completar", width=12, command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar", width=12, command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # ---------------- ATAJOS DE TECLADO ---------------- #
        self.root.bind("<Return>", self.add_task_event)
        self.root.bind("<c>", self.complete_task_event)
        self.root.bind("<C>", self.complete_task_event)
        self.root.bind("<Delete>", self.delete_task_event)
        self.root.bind("<d>", self.delete_task_event)
        self.root.bind("<D>", self.delete_task_event)
        self.root.bind("<Escape>", lambda e: self.root.quit())

    # ---------------- FUNCIONES PRINCIPALES ---------------- #

    # Agregar tarea
    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"text": task, "done": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)

    # Evento tecla Enter
    def add_task_event(self, event):
        self.add_task()

    # Marcar como completada
    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index]["done"] = not self.tasks[index]["done"]
            self.update_listbox()
        except IndexError:
            pass

    # Evento tecla C
    def complete_task_event(self, event):
        self.complete_task()

    # Eliminar tarea
    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.update_listbox()
        except IndexError:
            pass

    # Evento tecla Delete o D
    def delete_task_event(self, event):
        self.delete_task()

    # ---------------- ACTUALIZAR LISTA ---------------- #
    def update_listbox(self):
        self.listbox.delete(0, tk.END)

        for task in self.tasks:
            text = task["text"]

            if task["done"]:
                display_text = "✔ " + text
                self.listbox.insert(tk.END, display_text)
                self.listbox.itemconfig(tk.END, fg="gray")
            else:
                display_text = text
                self.listbox.insert(tk.END, display_text)
                self.listbox.itemconfig(tk.END, fg="black")


# ---------------- BLOQUE PRINCIPAL ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()