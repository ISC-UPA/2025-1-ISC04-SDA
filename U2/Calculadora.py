import os
import tkinter as tk
from tkinter import messagebox
import numpy as np
from math import sin as seno, log as ln, log10 as log

class Calculadora:
    def __init__(self, root):
        self.root = root
        root.geometry("800x600")   # x,y
        self.root.title("Calculadora")
        
        self.entry_infix = tk.StringVar()
        self.entry_postfix = tk.StringVar()
        self.entry_result = tk.StringVar()

        self.frameDisplay = tk.Frame(self.root,  bg="#f0f0f0")
        self.frameDisplay.pack(fill='both', expand=True)        
        
        self.frameTeclado = tk.Frame(self.root,  bg="#f0f0f0")
        self.frameTeclado.pack(fill='both', expand=True)        
        
        self.create_Display()
        self.create_Teclado()
        
    def create_Display(self):
        self.label1 = tk.Label(self.frameDisplay, text="Infix: ", font=("Arial", 18))
        self.label1.grid(row=0, column=0, pady=10,  sticky='w') 
        infix = tk.Entry(self.frameDisplay, textvariable=self.entry_infix, font=("Arial", 18), justify="right")
        infix.grid(row=0, column=1, columnspan=4, sticky="we")
        
        self.label2 = tk.Label(self.frameDisplay, text="Postfix: ", font=("Arial", 18))
        self.label2.grid(row=1, column=0, pady=10,  sticky='w')         
        posfix = tk.Entry(self.frameDisplay, textvariable=self.entry_postfix, font=("Arial", 18), justify="right", state="readonly" ) # De solo lectura
        posfix.grid(row=1, column=2, columnspan=4)
        
        self.label3 = tk.Label(self.frameDisplay, text="Result: ", font=("Arial", 18))
        self.label3.grid(row=2, column=0, pady=10,  sticky='w')         
        result = tk.Entry(self.frameDisplay, textvariable=self.entry_result, font=("Arial", 18), justify="right", state="readonly" )
        result.grid(row=2, column=2, columnspan=4, pady=10,  sticky='w')
        
    def create_Teclado(self):
        numero = ['0','1','2','3','4','5','6','7','8','9','.','(-)', 'EXP']
        operador = ['+', '-' , '*' , '/', '^', '(', ')']
        prioridad = {'+':1, '-':1, '*':2, '/':2, '^':3}  
        parentesis = ['(',')']
        funciones = ['sen','cos', 'tan','asen', 'acos', 'atan', 'ln','aln', 'log', 'alog', '10^x', 'e^x', 'sqrt']
        constantes = ['pi', 'e']   
        
        buttons = [
            ('7', '8', '9', '-'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '/'),
            ('0', '.', 'EXP', '=')
        ]
        
        tablero = [['1','2','3'],
                   ['4','X','6'],
                   ['7','8','9'],
                   ['Fin','','']]
        tabla= np.array(tablero)
        

        for i, row in enumerate(buttons):
            for j, button_text in enumerate(row):
                button = tk.Button(self.frameTeclado, text=button_text, font=("Arial", 18),
                                   command=lambda text=button_text: self.on_click(text), width=5, height=2)
                button.grid(row=i, column=j)

    def on_click(self, button_text):
        if button_text == "=":
            try:
                print("Infix: ", self.entry_infix.get())
                expression = self.entry_infix.get()
                result =  round(ln(3.1416/2),4)
                self.entry_result.set(result)
            except Exception:
                messagebox.showerror("Error", "Expresión inválida")
        elif button_text == "C":
            self.entry_infix.set("")
            self.entry_result.set("")
        else:
            self.entry_infix.set(self.entry_infix.get() + " " + button_text)

if __name__ == "__main__":
    os.system('cls')     
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
    os.system('pause')       
    print(seno(3.1416/2))

    
        