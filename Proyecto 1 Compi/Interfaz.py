import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from AnalizadorLexico import AnalizadorLexico
from AnalizadorLexicoCSS import AnalizadorLexicoCss
import os

class aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Analizador Lexico")
        self.agregar_menu()
        self.scrolledtext1=st.ScrolledText(self.ventana1, width=60, height=30)
        self.scrolledtext1.grid(column=0, row=0, padx=10, pady=10)
        self.scrolledtext2=st.ScrolledText(self.ventana1, width=60, height=30)
        self.scrolledtext2.grid(column=3, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Nuevo", command=self.nuevo)
        opciones1.add_command(label="Abrir", command=self.abrir)
        opciones1.add_command(label="Guardar", command=self.guardar)
        opciones1.add_separator()
        opciones1.add_command(label="salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)
        menubar1.add_cascade(label="Ejecutar Analisis", command = self.ejecutarAnalisis)
        menubar1.add_cascade(label="Salir", command=self.salir)

    def salir(self):
        self.ventana1.destroy()

    def guardar(self):
        nombrearch=fd.asksaveasfilename(filetypes = (("js files","*.js"),("css files","*.css"),("html files","*.html"),("todos los archivos","*.*")), defaultextension = ("*.js","*.css",".html"))
        if nombrearch != '':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.scrolledtext1.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("informacion", "los datos fueron guardados en el archivo.")

    def abrir(self):
        nombrearch=fd.askopenfilename(filetypes = (("js files","*.js"),("css files","*.css"),("html files","*.html"),("todos los archivos","*.*")), defaultextension = ("*.js","*.css",".html"))
        if nombrearch != '':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.scrolledtext1.delete("1.0", tk.END)
            self.scrolledtext1.insert("1.0", contenido)

    def nuevo(self):
        self.scrolledtext1.delete("1.0", tk.END)

    def ejecutarAnalisis(self):
        Prueba = AnalizadorLexico()
        print("----------------Tabla de Tokens----------------")
        Prueba.analizador(self.scrolledtext1.get("1.0", tk.END))
        Prueba.imprimirListaTokens()
        print("\n")
        print("----------------Tabla de Errores----------------")
        Prueba.imprimirListaErrores()
        print("\n")
        Prueba.generarHtml()
        Prueba.generarErrores()
        print("")
        self.scrolledtext2.insert(tk.END, Prueba.guardarcomentario)
        self.scrolledtext2.config(fg="yellow")

        



aplicacion1=aplicacion()

#Prueba = AnalizadorLexico()
PruebaCss = AnalizadorLexicoCss()
PruebaCss.analizarArchivoCss("LexicoCss.css")
print("----------------Tabla de Tokens----------------")
#Prueba.analizarArchivo("ejemplo.js")
#Prueba.analizarArchivo("Entrada.js")
#Prueba.imprimirListaTokens()
PruebaCss.imprimirListaTokensCss()
print("\n")
print("----------------Tabla de Errores----------------")
#Prueba.imprimirListaErrores()
PruebaCss.imprimirListaErroresCss()
print("\n")




