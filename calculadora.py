import tkinter as tk

class Calculadora:
       def __init__(self, master):
           self.master = master
           master.title("Calculadora")

           self.resultado = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2)
           self.resultado.grid(row=0, column=0, columnspan=4)

           self.crear_botones()

       def crear_botones(self):
           botones = [
               '7', '8', '9', '/',
               '4', '5', '6', '*',
               '1', '2', '3', '-',
               '0', '.', '=', '+'
           ]

           fila = 1
           col = 0
           for boton in botones:
               tk.Button(self.master, text=boton, width=5, height=2, command=lambda b=boton: self.click(b)).grid(row=fila, column=col)
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