import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from AnalizadorLexico import AnalizadorLexico
from AnalizadorLexicoCSS import AnalizadorLexicoCss
from AnalizadorLexicoHtml import AnalizadorLexicoHtml
from Analisadorsintactico import AnalizadorLexicoSintactico
import os

class aplicacion:

    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Analizador Lexico")
        self.agregar_menu()
        self.entrada=st.ScrolledText(self.ventana1, width=65, height=25)
        self.entrada.grid(column=0, row=0, padx=15, pady=10)
        self.salida=st.ScrolledText(self.ventana1, width=65, height=25)
        self.salida.grid(column=3, row=0, padx=15, pady=10)
        self.consola=st.ScrolledText(self.ventana1, width=75, height=15)
        self.consola.grid(column=0, row=6, padx=15, pady=10)
        self.ventana1.mainloop()

    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Nuevo", command=self.nuevo)
        opciones1.add_command(label="Abrir", command=self.abrir)
        opciones1.add_command(label="Guardar", command=self.guardar)
        opciones1.add_separator()
        opciones1.add_command(label="salir", command=self.salir)
        menubar1.add_cascade(label="Archivo", menu=opciones1)
        opciones2.add_command(label="Archivos .js", command=self.ejecutarAnalisis)
        opciones2.add_command(label="Archivos .css", command=self.ejecutarAnalisisCss)
        opciones2.add_command(label="Archivos .html", command=self.ejecutarAnalisisHtml)
        opciones2.add_command(label="Archivos .Rmt", command=self.ejecutarAnalisisSintactico)
        menubar1.add_cascade(label="Ejecutar Analisis", menu=opciones2)
        menubar1.add_cascade(label="Salir", command=self.salir)

    def salir(self):
        self.ventana1.destroy()

    def guardar(self):
        nombrearch=fd.asksaveasfilename(filetypes = (("js files","*.js"),("css files","*.css"),("html files","*.html"),("todos los archivos","*.*")), defaultextension = ("*.js","*.css",".html"))
        if nombrearch != '':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.entrada.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("informacion", "los datos fueron guardados en el archivo.")

    def abrir(self):
        nombrearch=fd.askopenfilename(filetypes = (("js files","*.js"),("css files","*.css"),("html files","*.html"),("Rmt files","*.Rmt"),("todos los archivos","*.*")), defaultextension = ("*.js","*.css","*.html","*.Rmt"))
        if nombrearch != '':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.entrada.delete("1.0", tk.END)
            self.entrada.insert("1.0", contenido)

    def nuevo(self):
        self.entrada.delete("1.0", tk.END)

    def ejecutarAnalisis(self):
        Prueba = AnalizadorLexico()
        print("----------------Tabla de Tokens----------------")
        Prueba.analizador(self.entrada.get("1.0", tk.END))
        Prueba.imprimirListaTokens()
        print("\n")
        print("----------------Tabla de Errores----------------")
        Prueba.imprimirListaErrores()
        print("\n")
        Prueba.generarHtml()
        Prueba.generarErrores()
        Prueba.generarArbol()
        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, Prueba.sin_errores)
        self.consola.delete("1.0", tk.END)
        for error in Prueba.listaErrores:
            self.consola.insert(tk.END, "----------------------------------------------------------------------\n")
            self.consola.insert(tk.END, 'TOKEN -> {}  LEXEMA -> {}  FILA -> {}  COLUMNA -> {}  INDICE -> {} \n'.format(error.getTipo(), error.getAuxlex(), error.getFila(), error.getColumna(), error.getIndice()))
            self.consola.insert(tk.END, "----------------------------------------------------------------------\n")
        Prueba.ruta_de_archivo("Salida_Correcta.js")

        #for error in Prueba.listaErrores:
            #self.consola.insert(tk.END, error + "\n")

    def ejecutarAnalisisCss(self):
        Tipocss = AnalizadorLexicoCss()
        print("----------------Tabla de Tokens----------------")
        Tipocss.analizadorCss(self.entrada.get("1.0", tk.END))
        Tipocss.imprimirListaTokensCss()
        print("\n")
        print("----------------Tabla de Errores----------------")
        Tipocss.imprimirListaErroresCss()
        print("\n")
        Tipocss.generarHtml_Css()
        Tipocss.generarErrores_Css()
        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, Tipocss.sin_errores)
        self.consola.delete("1.0", tk.END)
        self.consola.insert(tk.END, Tipocss.salida_consola)
        Tipocss.ruta_de_archivo("Salida_Correcta.css")
        #self.scrolledtext2.config(fg="yellow")

    def ejecutarAnalisisHtml(self):
        Tipo_html = AnalizadorLexicoHtml()
        print("----------------Tabla de Tokens----------------")
        Tipo_html.analizadorHtml(self.entrada.get("1.0", tk.END))
        Tipo_html.imprimirListaTokensHtml()
        print("\n")
        print("----------------Tabla de Errores----------------")
        Tipo_html.imprimirListaErroresHtml()
        print("\n")
        Tipo_html.generarHtml_Html()
        Tipo_html.generarErrores_Html()
        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, Tipo_html.sin_errores)
        self.consola.delete("1.0", tk.END)
        for error in Tipo_html.listaErrores_html:
            self.consola.insert(tk.END, "----------------------------------------------------------------------\n")
            self.consola.insert(tk.END, 'TOKEN -> {}  LEXEMA -> {}  FILA -> {}  COLUMNA -> {}  INDICE -> {} \n'.format(error.getTipo(), error.getAuxlex(), error.getFila(), error.getColumna(), error.getIndice()))
            self.consola.insert(tk.END, "----------------------------------------------------------------------\n")
        Tipo_html.ruta_de_archivo("Salida_Correcta.html")
        #self.scrolledtext2.config(fg="yellow")

    def ejecutarAnalisisSintactico(self):
        Tipo_Sintactico = AnalizadorLexicoSintactico()
        print("----------------Tabla de Tokens----------------")
        Tipo_Sintactico.analizadorSintactico(self.entrada.get("1.0", tk.END))
        Tipo_Sintactico.imprimirListaTokensSintactico()
        print("\n")
        print("----------------Tabla de Errores----------------")
        Tipo_Sintactico.imprimirListaErroresSintactico()
        print("\n")
        Tipo_Sintactico.inicio_sintactico()
        Tipo_Sintactico.generarHtml_Sintactico()
        Tipo_Sintactico.generarErrores_Sintactico()
        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, Tipo_Sintactico.respuesta)
        self.consola.delete("1.0", tk.END)
        for error in Tipo_Sintactico.listaErrores_Sintactico:
            self.consola.insert(tk.END, "----------------------------------------------------------------------\n")
            self.consola.insert(tk.END, 'TOKEN -> {}  LEXEMA -> {}  FILA -> {}  COLUMNA -> {}  INDICE -> {} \n'.format(error.getTipo(), error.getAuxlex(), error.getFila(), error.getColumna(), error.getIndice()))
            self.consola.insert(tk.END, "----------------------------------------------------------------------\n")
        #self.scrolledtext2.config(fg="yellow")

        

aplicacion1=aplicacion()

#Prueba = AnalizadorLexico()
#PruebaCss = AnalizadorLexicoCss()
#prueba_html = AnalizadorLexicoHtml()
#prueba_Sintactico = AnalizadorLexicoSintactico()
#prueba_html.analizarArchivoHtml("Ejemplo_Html.html")
#PruebaCss.analizarArchivoCss("LexicoCss.css")
#Prueba.analizarArchivo("ejemplo.js")
#prueba_Sintactico.analizarArchivoSintactico("ejemplosintactico.Rmt")
#print("----------------Tabla de Tokens Arbol----------------")
#Prueba.analizarArchivo("ejemplo.js")
#Prueba.analizarArchivo("Entrada.js")
#prueba_html.imprimirListaTokensHtml()
#prueba_Sintactico.imprimirListaErroresSintactico()
#prueba_Sintactico.inicio_sintactico()
#Prueba.imprimirListaTokensArbol()
#PruebaCss.imprimirListaTokensCss()
#print("\n")
#print("----------------Tabla de Errores----------------")
#Prueba.imprimirListaErrores()
#PruebaCss.imprimirListaErroresCss()
#prueba_html.imprimirListaErroresHtml()
#prueba_Sintactico.imprimirListaTokensSintactico()
#print("\n")

#ded = 12
#print("hola",ded,"adios")
#print("hola{}".format(ded))
#print("gogog"+"djdjd")



