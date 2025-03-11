import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Valor A:").grid(row=0, column=0)
        self.entry_a = tk.Entry(self.root, width=10)
        self.entry_a.grid(row=0, column=1)

        tk.Label(self.root, text="Valor B:").grid(row=1, column=0)
        self.entry_b = tk.Entry(self.root, width=10)
        self.entry_b.grid(row=1, column=1 )

        self.result_label = tk.Label(self.root, text="Resultado: ")
        self.result_label.grid(row=2, column=0)

        buttons = [('+', self.sumar), ('-', self.restar), ('*', self.multiplicar), ('/', self.dividir)]
        for i, (text, command) in enumerate(buttons):
            tk.Button(self.root, text=text, command=command, width=5, padx=15, pady=5, ).grid(row=3, column=i)

    def get_values(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
            return None, None

    def sumar(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            self.result_label.config(text=f"Resultado: {a + b}")

    def restar(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            self.result_label.config(text=f"Resultado: {a - b}")

    def multiplicar(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            self.result_label.config(text=f"Resultado: {a * b}")

    def dividir(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            if b != 0:
                self.result_label.config(text=f"Resultado: {a / b}")
            else:
                messagebox.showerror("Error", "No se puede dividir por cero")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
