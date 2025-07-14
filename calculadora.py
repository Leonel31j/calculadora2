import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.configure(bg="#2C3E50")  # Color de fondo de la ventana (azul oscuro)

        # Configuración del Entry (campo de resultado)
        self.resultado = tk.Entry(
            master,
            width=16,
            font=('Arial', 24),
            borderwidth=2,
            bg="#34495E",  # Fondo del campo
            fg="#ECF0F1",  # Color del texto (blanco)
            insertbackground="#ECF0F1"  # Color del cursor
        )
        self.resultado.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.crear_botones()

    def crear_botones(self):
        botones = [
            ('7', "#3498DB"), ('8', "#3498DB"), ('9', "#3498DB"), ('/', "#E74C3C"),
            ('4', "#3498DB"), ('5', "#3498DB"), ('6', "#3498DB"), ('*', "#E74C3C"),
            ('1', "#3498DB"), ('2', "#3498DB"), ('3', "#3498DB"), ('-', "#E74C3C"),
            ('0', "#3498DB"), ('.', "#3498DB"), ('=', "#2ECC71"), ('+', "#E74C3C")
        ]

        fila = 1
        col = 0
        for texto, color in botones:
            tk.Button(
                self.master,
                text=texto,
                width=5,
                height=2,
                bg=color,  # Fondo del botón
                fg="#ECF0F1",  # Color del texto
                activebackground="#1ABC9C",  # Color al hacer clic
                relief=tk.FLAT,  # Estilo plano
                font=('Arial', 14, 'bold'),
                command=lambda b=texto: self.click(b)
            ).grid(row=fila, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                fila += 1

    def click(self, boton):
        if boton == '=':
            try:
                resultado = eval(self.resultado.get())
                self.resultado.delete(0, tk.END)
                self.resultado.insert(0, str(resultado))
            except Exception as e:
                self.resultado.delete(0, tk.END)
                self.resultado.insert(0, "Error")
        else:
            self.resultado.insert(tk.END, boton)

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()
