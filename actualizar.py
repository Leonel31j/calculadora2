import os
import git
import tkinter as tk
from tkinter import messagebox

def actualizar_repositorio():
       repo_url = "https://github.com/tu_usuario/tu_repositorio.git"  # Cambia esto por tu URL de GitHub
       repo_dir = os.path.dirname(os.path.abspath(__file__))  # Directorio actual del script

       try:
           if os.path.exists(os.path.join(repo_dir, ".git")):
               repo = git.Repo(repo_dir)
               origin = repo.remotes.origin
               origin.pull()
               messagebox.showinfo("Actualización", "¡La calculadora se ha actualizado correctamente!")
           else:
               git.Repo.clone_from(repo_url, repo_dir)
               messagebox.showinfo("Actualización", "¡Repositorio clonado correctamente!")
       except Exception as e:
           messagebox.showerror("Error", f"No se pudo actualizar: {str(e)}")

if __name__ == "__main__":
       root = tk.Tk()
       root.withdraw()  # Oculta la ventana principal de Tkinter
       actualizar_repositorio()
   