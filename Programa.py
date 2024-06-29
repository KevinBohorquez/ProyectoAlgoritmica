import tkinter as tk
from tkinter import Tk, Label, Button, Entry, Frame, messagebox, mainloop

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime  # Importamos datetime para manejar fechas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

import customtkinter
from PIL import Image, ImageTk
import pandas as pd
from customtkinter import *
import random

# importamos las librerias tk, customtkinter, pillow y pandas

# funcion para eliminar los widgets dentro de nuestro labelframe (limpiar los datos que aparecen al presionar un botton)
def eliminar_widgets_labelframe(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# Clase Login, clase hija de la clase Aplicacion
class Login(tk.Frame):

    # Inicializamos la clase, self para referirse a si mismo (el login) y controller se refiere a su clase padre (Aplicacion)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Colocamos el fondo de san marcos
        fondounmsm = ImageTk.PhotoImage(file="bgr.png")
        rutaicono = "logofisi.png"
        img1 = Image.open(rutaicono)
        img1 = img1.resize((155, 155))

        # hacemos el borde, de tipo LabelFrame, que nos ayudara a manejar los widgets (button, label, entry, etc)
        # este borde funciona como una caja invisible que la haremos de las dimensiones de la ventana
        # dentro de el borde pondremos los widgets
        borde = tk.LabelFrame(self, bg='white', bd=10, font=("Microsoft YaHei UI Light", 15))
        borde.pack(fill="both", expand=True)

        # ponemos el fondo de san marcos
        fondazo = tk.Label(borde, image=fondounmsm)
        fondazo.image = fondounmsm
        fondazo.place(x=0, y=0, relwidth=1, relheight=1)

        # el rectangulo gris
        label_bg = tk.Label(borde, bg="black")
        label_bg.place(y=80, x=475, width=400, height=500)
        canvas = tk.Canvas(label_bg, bg="gray17", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        # ponemos el logo de la fisi
        img11 = ImageTk.PhotoImage(img1)
        imagenFisiLogo = tk.Label(borde, image=img11, bg="gray17")
        imagenFisiLogo.image = img11
        imagenFisiLogo.place(x=600, y=165)

        # Escribimos el inicio de sesion con un label
        L1 = tk.Label(borde, fg="gray90", bg="gray17", text="Inicio de Sesion", font=("Microsoft YaHei UI Light", 25))
        L1.place(x=556, y=95)
        Frame(borde, width=345, height=2, bg="gray50").place(x=504, y=155)

        # Hacemos 2 Entry, donde el usuario escribira el texto en pantalla,
        T1 = CTkEntry(borde, placeholder_text="Correo Institucional", font=("Microsoft YaHei UI Light", 15), width=300,
                      height=35, text_color="gray90", bg_color="gray22", fg_color="gray26")
        T1.place(x=530, y=340)
        # En el T2 lo ocultamos con show="*"
        T2 = CTkEntry(borde, show="*", placeholder_text="Contraseña", font=("Microsoft YaHei UI Light", 15), width=300,
                      height=35, text_color="gray90", bg_color="gray22", fg_color="gray26")
        T2.place(x=530, y=390)

        # un boton next para pasar a la siguiente ventana rapido, para testeos, no necesitaras ingresar el usuario
        nextsito = tk.Button(borde, text="Next", font=("Microsoft YaHei UI Light", 35),
                             command=lambda: controller.show_frame(MenuOpciones))
        nextsito.place(x=1150, y=550)

        # definimos la funcion entrar, que se activara al presionar el boton Ingresar
        def entrar():

            try:  # Intentemos leer el archivo excel
                df = pd.read_excel('loginData.xlsx')
                if (str(T1.get()) in df["Correo"].values):  # revisamos si el texto en T1 esta en la columna "Correo" del excel
                    if str(df[df["Correo"] == str(T1.get())]["Contraseña"].iloc[0]) == str(T2.get()):  # sacamos el numero de la fila donde se encuentra
                        # nuestro Correo, sacamos el Codigo de alumno de esa fila y lo igualamos al T2 escrito por el usuario
                        # los messagebox son cuadros emergentes al que les pones un titulo y mensaje
                        messagebox.showinfo("Acceso Correcto", "Has ingresado")
                        # la variable numFila, guardara el numero de la fila donde se encuentra nuestro usuario en el excel
                        numFila = df[df["Correo"] == str(T1.get())]
                        # hacemos que las variables de la clase Aplicacion guarden los datos que estan en el excel
                        controller.creditos = str(numFila["Creditos"].iloc[0])
                        controller.nombreEstudiante = numFila["Nombre"].iloc[0]
                        controller.dni = numFila["DNI"].iloc[0]
                        controller.FisiCoins = numFila["Dinero"].iloc[0]
                        controller.tipoEstudiante = (numFila["Tipo"].iloc[0])
                        controller.codigoEstudiante = numFila["Codigo"].iloc[0]
                        controller.correoEstudiante = str(T1.get())
                        controller.contraseña = str(numFila["Contraseña"].iloc[0])
                        controller.foto = str(numFila["Foto"].iloc[0])
                        # como ya se verifico que es correcto el correo y codigo, borramos lo escrito en los campos T1 y T2
                        T1.delete(0, tk.END)
                        T2.delete(0, tk.END)
                        # pasamos al frame MenuOpciones
                        controller.show_frame(MenuOpciones)
                    else:
                        messagebox.showinfo("Acceso Incorrecto", "Contraseña incorrecta")
                else:
                    messagebox.showinfo("Acceso Incorrecto", "Correo no existe")
            except FileNotFoundError:
                messagebox.showerror("Error", "El archivo Excel no se encuentra")

        # el boton donde dice ingresar :p
        BTN1 = CTkButton(borde, bg_color="gray17", fg_color="SpringGreen2", text="Ingresar", corner_radius=16,
                         text_color="gray90", width=300, height=45, font=("Arial", 20), command=entrar)
        BTN1.place(x=530, y=465)


# clase MenuOpciones, clase hija de la clase Aplicacion
class MenuOpciones(tk.Frame):

    # Inicializamos la clase, self para referirse a si mismo (el login) y controller se refiere a su clase padre (Aplicacion)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # efecto de sobra radial

        # hacemos un bordemenu, con la misma funcionalidad que el borde de Login xd
        bordeMenu = tk.LabelFrame(self, bg='#05171d', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeMenu.pack(fill="both", expand=True)

        # partes del diseño, los rectangulos morados :P

        # rectanculos verticales
        label_3 = CTkLabel(bordeMenu, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=8, width=380,
                           height=240)
        label_3.place(x=505, y=22)
        label_4 = CTkLabel(bordeMenu, fg_color="#01213a", bg_color="#88d398", text="", corner_radius=8, width=370,
                           height=240)
        label_4.place(x=510, y=25)

        textito = CTkLabel(bordeMenu, text="MENÚ", font=("Nunito", 30), width=300, height=35, text_color="#e3f473",
                           bg_color="#01213a")
        textito.place(x=550, y=31)
        # rectanculos horizontales
        label_2 = CTkLabel(bordeMenu, fg_color="#88d398", text="", corner_radius=10, width=1166,
                           height=530)
        label_2.place(x=92, y=75)
        label_1 = CTkLabel(bordeMenu, fg_color="#01213a", bg_color="#88d398", text="", corner_radius=10, width=1160,
                           height=520)
        label_1.place(x=95, y=80)

        # insertamos la imagen de la fisicoin
        burrito_path = os.path.join(os.path.dirname(__file__), 'FISICOIN.png')
        image = customtkinter.CTkImage(light_image=Image.open(burrito_path), size=(210, 147))
        image_label = customtkinter.CTkLabel(bordeMenu, bg_color="#01213a", image=image, text='')
        image_label.place(x=570, y=265)

        # las diferentes tipos de opciones, hover_color cambiar el color cuando el mouse este encima
        # buttoon, tiene un command para ir a Operaciones Bancarias

        # Borde operaciones bancarias
        label_2 = CTkLabel(bordeMenu, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=12, width=534,
                           height=145)
        label_2.place(x=115, y=105)
        # Boton OPERACIONES BANCARIAS
        buttoon = CTkButton(bordeMenu, width=530, bg_color="#88d398", text_color="white", corner_radius=12, height=135,
                            fg_color="#114b5f", hover_color="darkcyan", text="Operaciones Bancarias",
                            font=("Nunito", 35), command=lambda: controller.show_frame(InfoUsuario))
        buttoon.place(x=117, y=110)
        # Borde pagar servicios
        label_2 = CTkLabel(bordeMenu, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=12, width=534,
                           height=145)
        label_2.place(x=688, y=105)
        # Boton PAGAR SERVICIOS
        buttoon1 = CTkButton(bordeMenu, width=530, bg_color="#88d398", text_color="white", corner_radius=12, height=135,
                             fg_color="#114b5f", hover_color="darkcyan", text="Pagar Servicios", font=("Nunito", 35), command=lambda: controller.show_frame(pagarServicios))
        buttoon1.place(x=690, y=110)
        # Boton PROXIMAMENTE QUIOSCO
        buttoon2 = CTkButton(bordeMenu, width=420, bg_color="#01213a", fg_color="#575f61", text_color="black",
                             corner_radius=32, height=150, text="Proximamente:\nQuiosco Virtual",
                             font=("Microsoft YaHei UI Light", 30))
        buttoon2.place(x=120, y=265)
        # Boton PROXIMAMENTE CASINO
        buttoon3 = CTkButton(bordeMenu, width=420, bg_color="#01213a", fg_color="#575f61", text_color="black",
                             corner_radius=32, height=150, text="Proximamente:\n Casino",
                             font=("Microsoft YaHei UI Light", 30))
        buttoon3.place(x=810, y=265)
        # Borde Configuracion
        label_2 = CTkLabel(bordeMenu, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=12, width=534,
                           height=145)
        label_2.place(x=115, y=425)
        # Boton CONFIGURACION
        buttoon4 = CTkButton(bordeMenu, width=530, bg_color="#88d398", text_color="white", corner_radius=12, height=135,
                             fg_color="#114b5f", hover_color="darkcyan", text="Configuracion", font=("Nunito", 35),
                             command=lambda: controller.show_frame(Config))
        buttoon4.place(x=117, y=430)

        # Borde Inversiones
        label_2 = CTkLabel(bordeMenu, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=12, width=534,
                           height=145)
        label_2.place(x=688, y=425)

        # Boton INVERSIONES
        buttoon5 = CTkButton(bordeMenu, width=530, bg_color="#88d398", text_color="white", corner_radius=12, height=135,
                             fg_color="#114b5f", hover_color="darkcyan", text="Prestamos e Inversiones",
                             font=("Nunito", 35), command=lambda: controller.show_frame(Prestamos_Inversiones))
        buttoon5.place(x=690, y=430)

        # cerrar sesion, para volve al login
        volverLogin = tk.Button(bordeMenu, text="Cerrar Sesion", font=("Microsoft YaHei UI Light", 15),
                                command=lambda: controller.show_frame(Login))
        volverLogin.place(x=10, y=627)


# clase InfoUsuario, clase hija de la clase Aplicacion
class InfoUsuario(tk.Frame):
    # Inicializamos la clase, self para referirse a si mismo (el login) y controller se refiere a su clase padre (Aplicacion)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        bordeInfo = tk.LabelFrame(self, bg='#010f4c', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeInfo.pack(fill="both", expand=True)

        # los rectangulos  azul, debajo de donde estar el texto xd
        label_bg = CTkLabel(bordeInfo, fg_color="#0026a3", bg_color="#010f4c", text="", corner_radius=16, width=444,
                            height=590)
        label_bg.place(y=30, x=687)
        label_bg1 = CTkLabel(bordeInfo, fg_color="#0084f1", bg_color="#0026a3", text="", corner_radius=16, width=420,
                             height=570)
        label_bg1.place(y=40, x=699)
        label_bg2 = CTkLabel(bordeInfo, fg_color="#0026a3", bg_color="#010f4c", text="", corner_radius=16, width=444,
                             height=590)
        label_bg2.place(y=30, x=215)
        label_bg3 = CTkLabel(bordeInfo, fg_color="#0084f1", bg_color="#0026a3", text="", corner_radius=16, width=420,
                             height=570)
        label_bg3.place(y=40, x=227)

        # boton, que activa la funcion MostrarInformacio
        bottonsito2 = CTkButton(bordeInfo, text="Consultar Informacion", bg_color="#0084f1", fg_color="#4bb4f6", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15),
                                command=lambda: self.consultarSaldo(controller, respuestaLabelFrame))
        bottonsito2.place(x=240, y=52)
        # el resto de botones, que no hacen nada por el momento
        bottonsito3 = CTkButton(bordeInfo, text="Realizar deposito", bg_color="#0084f1", fg_color="#4bb4f6", width=392, command=lambda: self.RealizarDeposito(controller, respuestaLabelFrame), height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15))
        bottonsito3.place(x=240, y=102)

        bottonsito4 = CTkButton(bordeInfo, text="Realizar Retiro", bg_color="#0084f1", fg_color="#4bb4f6", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15), command=lambda: self.RealizarRetiro(controller, respuestaLabelFrame))
        bottonsito4.place(x=240, y=152)

        bottonsito5 = CTkButton(bordeInfo, text="Transferencia entre cuentas", bg_color="#0084f1", fg_color="#4bb4f6",
                                width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15), command=lambda: self.TransferenciaEntreCuentas(controller, respuestaLabelFrame))
        bottonsito5.place(x=240, y=202)
        # boton para volver, ojo, tiene SalirPagina()
        Buttona = tk.Button(self, text="Volver", font=("Arial", 15),
                            command=lambda: self.salirPagina(respuestaLabelFrame))
        Buttona.place(x=50, y=600)

        # este nuevo labelframe esta dentro de nuestro labelframe BordeInfo
        # su funcion es que dentro de este esten todos los widgets de nuestra opciones, consultar saldo, realizar retiro, etc
        # almacenar los widgets que generen nuestros botones dentro de un labelframe nos facilitara el borrarlos cuando sea necesario
        # con solo llamar a lafuncion eliminar_widgets_labelframe ,podras borrar todos los widgets que generaste dentro de tu botton
        respuestaLabelFrame = tk.LabelFrame(bordeInfo, text="", height=550, width=400, bg="#0084f1",
                                            foreground="gray60",
                                            bd=0, font=("Microsoft YaHei UI Light", 15))
        respuestaLabelFrame.place(x=708, y=53)
        # este labelframe es el segundo rectangulo, a la derechad de las opciones

    # mostrarDatos, funcion que necesita el argumento controller
    def consultarSaldo(self, controller, frame):
        eliminar_widgets_labelframe(frame)
        # limpiamos lo que este dentro de nuestro labelframe, antes de generar nuevos widgets

        self.La1 = CTkLabel(frame, text="Foto De\n Perfil", text_color="#010f4c", fg_color="#0026a3", corner_radius=16, font=("Microsoft YaHei UI Light", 32, "bold"))
        self.La1.place(x=45, y=115)

        self.L1 = CTkLabel(frame, text="", width=168, height=168, fg_color="#0026a3", corner_radius=16)
        self.L1.place(x=210, y=80)
        path = 'fotosPerfil/'+str(controller.foto)+'.jpeg'
        self.img_perfil = os.path.join(os.path.dirname(__file__), path)
        self.image = customtkinter.CTkImage(light_image=Image.open(self.img_perfil), size=(147, 147))
        self.image_label = customtkinter.CTkLabel(frame, bg_color="#01213a", image=self.image, text='')
        self.image_label.place(x=220, y=90)

        self.Lab1 = CTkLabel(frame, text="", width=380, height=60, fg_color="#0026a3", corner_radius=16)
        self.Lab1.place(x=10, y=7)
        self.Lab2 = CTkLabel(frame, corner_radius=16, height=40, fg_color="#4bb4f6", bg_color="#0026a3", text="Consulta de Informacion", text_color="black", font=("Microsoft YaHei UI Light", 30))
        self.Lab2.place(x=20, y=17)

        # escribimos todos los datos llamando a controller.  que es igual a Aplicacion., estamos llamando las variables de Aplicacion
        self.Label4 = tk.Label(frame, fg="white", bg="#0084f1",
                               text="Nombre del Estudiante: " + controller.nombreEstudiante,
                               font=("Microsoft YaHei UI Light", 11))
        self.Label4.place(x=5, y=400)
        self.Label = tk.Label(frame, fg="white", bg="#0084f1",
                              text="Codigo de estudiante: " + str(controller.codigoEstudiante),
                              font=("Microsoft YaHei UI Light", 12))
        self.Label.place(x=5, y=250)
        self.Label2 = tk.Label(frame, fg="white", bg="#0084f1",
                               text="Correo Institucional: " + controller.correoEstudiante,
                               font=("Microsoft YaHei UI Light", 12))
        self.Label2.place(x=5, y=300)
        self.Label3 = tk.Label(frame, fg="white", bg="#0084f1", text="Creditos: " + str(controller.creditos),
                               font=("Microsoft YaHei UI Light", 12))
        self.Label3.place(x=5, y=350)
        self.Label5 = tk.Label(frame, fg="white", bg="#0084f1", text="Tipo de Estudiante: " + controller.tipoEstudiante + "GRADO",
                               font=("Microsoft YaHei UI Light", 12))
        self.Label5.place(x=5, y=450)
        self.Label6 = tk.Label(frame, fg="white", bg="#0084f1", text="FisiCoins: " + str(controller.FisiCoins),
                               font=("Microsoft YaHei UI Light", 12))
        self.Label6.place(x=5, y=500)

    def RealizarDeposito(self, controller, frame):
        eliminar_widgets_labelframe(frame)

        self.controller = controller

        titulo = CTkLabel(frame, text="Realizar Deposito", font=("Microsoft YaHei UI Light", 25), bg_color='#0084f1',
                          fg_color='#0026a3', corner_radius=16, width=310, height=48, text_color="white")
        titulo.place(x=45, y=35)

        self.monto_entry = CTkEntry(frame, placeholder_text="Monto a depositar",
                                    font=("Microsoft YaHei UI Light", 15), width=300, height=41, text_color="gray90",
                                    bg_color="#0084f1", fg_color="gray26")
        self.monto_entry.place(x=45, y= 170)

        boton_confirmar = CTkButton(frame, text="Confirmar Deposito", bg_color="#0084f1", fg_color="SpringGreen2",
                                    width=300, height=45, font=("Arial", 20), command=self.realizar_deposito)
        boton_confirmar.place(x=45, y=400)

        boton_descargar = CTkButton(frame, text="Descargar PDF", bg_color="#0084f1", fg_color="SpringGreen2",
                                    width=300, height=45, font=("Arial", 20), command=self.descargar_pdfDeposito)
        boton_descargar.place(x=45, y=470)

    def realizar_deposito(self):
        try:
            monto = float(self.monto_entry.get())
            if monto <= 0:
                raise ValueError("El monto debe ser positivo")

            if monto > self.controller.FisiCoins:
                messagebox.showerror("Error", "Fondos insuficientes")
            else:
                self.controller.modificarFisiCoinsMas(monto)
                self.generar_factura_pdfDeposito(monto)
                self.pdf_generado = True
                messagebox.showinfo("Éxito", f"Has depositado {monto} FisiCoins")

        except ValueError as ve:
            messagebox.showerror("Error", f"Entrada inválida: {ve}")

        self.monto_entry.delete(0, tk.END)

    def RealizarRetiro(self, controller, frame):
        eliminar_widgets_labelframe(frame)

        self.controller = controller

        titulo = CTkLabel(frame, text="Realizar Retiro", font=("Microsoft YaHei UI Light", 25), bg_color='#0084f1',
                          fg_color='#0026a3', corner_radius=16, width=310, height=48, text_color="white")
        titulo.place(x=45, y=35)

        self.monto_entry = CTkEntry(frame, placeholder_text="Monto a Retirar",
                                    font=("Microsoft YaHei UI Light", 15), width=300, height=41, text_color="gray90",
                                    bg_color="#0084f1", fg_color="gray26")
        self.monto_entry.place(x=45, y=170)

        boton_confirmar = CTkButton(frame, text="Confirmar Retiro", bg_color="#0084f1", fg_color="SpringGreen2",
                                    width=300, height=45, font=("Arial", 20), command=self.realizar_retiro)
        boton_confirmar.place(x=45, y=400)

        boton_descargar = CTkButton(frame, text="Descargar PDF", bg_color="#0084f1", fg_color="SpringGreen2",
                                    width=300, height=45, font=("Arial", 20), command=self.descargar_pdfRetiro)
        boton_descargar.place(x=45, y=470)

    def realizar_retiro(self):
        try:
            monto = float(self.monto_entry.get())
            if monto <= 0:
                raise ValueError("El monto debe ser positivo")

            if monto > self.controller.FisiCoins:
                messagebox.showerror("Error", "Fondos insuficientes")
            else:
                self.controller.modificarFisiCoins(monto)
                self.generar_factura_pdfRetiro(monto)
                self.pdf_generado = True
                messagebox.showinfo("Éxito", f"Has retirado {monto} FisiCoins")

        except ValueError as ve:
            messagebox.showerror("Error", f"Entrada inválida: {ve}")

        self.monto_entry.delete(0, tk.END)
    def generar_factura_pdfDeposito(self, monto):
        try:
            pdf_path = "factura_deposito.pdf"
            doc = SimpleDocTemplate(pdf_path, pagesize=letter)
            elements = []

            # Estilos
            styles = getSampleStyleSheet()
            title_style = styles['Heading1']
            normal_style = styles['Normal']

            # Título del documento
            elements.append(Paragraph("Factura de Deposito de Dinero", title_style))

            # Información del remitente
            elements.append(Paragraph(f"Remitente: {self.controller.nombreEstudiante}", normal_style))
            elements.append(Paragraph(f"Correo Remitente: {self.controller.correoEstudiante}", normal_style))
            elements.append(Paragraph(f"Código de Estudiante: {self.controller.codigoEstudiante}", normal_style))

            # Espacio
            elements.append(Paragraph(" ", normal_style))

            # Información de la transacción
            elements.append(Paragraph(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", normal_style))
            elements.append(Paragraph(f"Monto Depositado: {monto} FisiCoins", normal_style))

            # Tabla de detalles
            data = [
                ["Descripción", "Cantidad"],
                ["Deposito de FisiCoins", f"{monto}"]
            ]
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            elements.append(table)

            # Pie de página
            elements.append(Paragraph("Gracias por usar nuestros servicios.", normal_style))

            # Construir el PDF
            doc.build(elements)
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el PDF: {e}")
            self.pdf_generado = False

    def generar_factura_pdfRetiro(self, monto):
        try:
            pdf_path = "factura_retiro.pdf"
            doc = SimpleDocTemplate(pdf_path, pagesize=letter)
            elements = []

            # Estilos
            styles = getSampleStyleSheet()
            title_style = styles['Heading1']
            normal_style = styles['Normal']

            # Título del documento
            elements.append(Paragraph("Factura de Retiro de Dinero", title_style))

            # Información del remitente
            elements.append(Paragraph(f"Remitente: {self.controller.nombreEstudiante}", normal_style))
            elements.append(Paragraph(f"Correo Remitente: {self.controller.correoEstudiante}", normal_style))
            elements.append(Paragraph(f"Código de Estudiante: {self.controller.codigoEstudiante}", normal_style))

            # Espacio
            elements.append(Paragraph(" ", normal_style))

            # Información de la transacción
            elements.append(Paragraph(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", normal_style))
            elements.append(Paragraph(f"Monto Retirado: {monto} FisiCoins", normal_style))

            # Tabla de detalles
            data = [
                ["Descripción", "Cantidad"],
                ["Deposito de FisiCoins", f"{monto}"]
            ]
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            elements.append(table)

            # Pie de página
            elements.append(Paragraph("Gracias por usar nuestros servicios.", normal_style))

            # Construir el PDF
            doc.build(elements)
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el PDF: {e}")
            self.pdf_generado = False

    def eliminar_pdfDeposito(self):
        pdf_path = "factura_deposito.pdf"
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    def eliminar_pdfRetiro(self):
        pdf_path = "factura_retiro.pdf"
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    def descargar_pdfRetiro(self):
        if not self.pdf_generado:
            messagebox.showerror("Error", "No se ha realizado ningún retiro.")
            return

        pdf_path = "factura_retiro.pdf"
        if os.path.exists(pdf_path):
            os.startfile(pdf_path)
        else:
            messagebox.showerror("Error", "El archivo PDF no existe.")

    def descargar_pdfDeposito(self):
        if not self.pdf_generado:
            messagebox.showerror("Error", "No se ha realizado ningún retiro.")
            return

        pdf_path = "factura_deposito.pdf"
        if os.path.exists(pdf_path):
            os.startfile(pdf_path)
        else:
            messagebox.showerror("Error", "El archivo PDF no existe.")
    def TransferenciaEntreCuentas(self, controller, frame):
        eliminar_widgets_labelframe(frame)
        self.controller = controller

        self.label_transferencia = CTkLabel(frame, text="Transferencia de Dinero", font=("Microsoft YaHei UI Light", 20),
                                       text_color="white", fg_color= "#0026a3", bg_color="#0084f1", width=310, height=48, corner_radius=16)
        self.label_transferencia.place(x=45, y=35)

        self.label_destino = CTkLabel(frame, text="Correo de destino:",
                                      font=("Microsoft YaHei UI Light", 15), text_color="white")
        self.label_destino.place(x=45, y=150)
        self.entry_destino = CTkEntry(frame, width=300)
        self.entry_destino.place(x=45, y=180)

        self.label_monto = CTkLabel(frame, text="Monto a transferir:",
                                    font=("Microsoft YaHei UI Light", 15), text_color="white")
        self.label_monto.place(x=45, y=280)
        self.entry_monto = CTkEntry(frame, width=300)
        self.entry_monto.place(x=45, y=310)

        boton_transferir = CTkButton(frame, text="Transferir", bg_color="#0084f1", fg_color="SpringGreen2",
                                     text_color="gray90", width=300, height=45, corner_radius=8,
                                     font=("Microsoft YaHei UI Light", 20), command=self.realizar_transferencia)
        boton_transferir.place(x=45, y=400)

        boton_descargar = CTkButton(frame, text="Descargar PDF", bg_color="#0084f1",
                                    fg_color="SpringGreen2", text_color="gray90", width=300, height=45, corner_radius=8,
                                    font=("Microsoft YaHei UI Light", 20), command=self.descargar_pdfTransferencia)
        boton_descargar.place(x=45, y=470)

    def realizar_transferencia(self):
        correo_destino = self.entry_destino.get()
        monto = self.entry_monto.get()

        if not correo_destino or not monto:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        try:
            monto = float(monto)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un monto válido.")
            return

        if monto <= 0:
            messagebox.showerror("Error", "El monto debe ser mayor a cero.")
            return

        if monto > self.controller.FisiCoins:
            messagebox.showerror("Error", "Saldo insuficiente.")
            return

        if not self.es_correo_valido(correo_destino):
            messagebox.showerror("Error", "Por favor, ingrese un correo válido.")
            return
        if correo_destino == self.controller.correoEstudiante:
            messagebox.showerror("Error", "No se puede transferir a la misma cuenta.")
            return
        try:
            df = pd.read_excel("loginData.xlsx")
            if correo_destino not in df["Correo"].values:
                messagebox.showerror("Error", "El correo de destino no existe en la base de datos.")
                return
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo no se encuentra.")
            return

        # Aquí se debe realizar la lógica para transferir el dinero
        self.controller.modificarFisiCoins(monto)
        self.generar_factura_pdfTransferencia(correo_destino, monto)
        self.controller.MandarDinero(monto, correo_destino)
        messagebox.showinfo("Éxito", f"Transferencia de {monto} FisiCoins a {correo_destino} realizada con éxito.")

    def es_correo_valido(self, correo):
        import re
        return re.match(r"[^@]+@[^@]+\.[^@]+", correo) is not None

    def descargar_pdfTransferencia(self):
        pdf_path = "factura_transaccion.pdf"
        if os.path.exists(pdf_path):
            os.startfile(pdf_path)
        else:
            messagebox.showerror("Error", "El archivo PDF no existe.")

    def generar_factura_pdfTransferencia(self, correo_destino, monto):
        pdf_path = "factura_transaccion.pdf"
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        elements = []

        # Estilos
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        normal_style = styles['Normal']

        # Título del documento
        elements.append(Paragraph("Factura de Transferencia de Dinero", title_style))

        # Información del remitente
        elements.append(Paragraph(f"Remitente: {self.controller.nombreEstudiante}", normal_style))
        elements.append(Paragraph(f"Correo Remitente: {self.controller.correoEstudiante}", normal_style))
        elements.append(Paragraph(f"Código de Estudiante: {self.controller.codigoEstudiante}", normal_style))

        # Espacio
        elements.append(Paragraph(" ", normal_style))

        # Información de la transacción
        elements.append(Paragraph(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", normal_style))
        elements.append(Paragraph(f"Correo Destinatario: {correo_destino}", normal_style))
        elements.append(Paragraph(f"Monto Transferido: {monto} FisiCoins", normal_style))

        # Tabla de detalles
        data = [
            ["Descripción", "Cantidad"],
            ["Transferencia de FisiCoins", f"{monto}"]
        ]
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(table)

        # Pie de página
        elements.append(Paragraph("Gracias por usar nuestros servicios.", normal_style))

        # Construir el PDF
        doc.build(elements)

    def eliminar_pdfTransferencia(self):
        pdf_path = "factura_transaccion.pdf"
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    # al salir de la pagina, debemos eliminar los Label que creamos en MostrarInformacion
    def salirPagina(self, frame):
        eliminar_widgets_labelframe(frame)  # eliminamos los widgets antes de salir del frame
        self.controller.show_frame(MenuOpciones)  # volvemos al menu de opciones


class Prestamos_Inversiones(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        bordePrest_inv = tk.LabelFrame(self, bg='#05171d', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordePrest_inv.pack(fill="both", expand=True)

        rec_azul1 = CTkLabel(bordePrest_inv, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=16,
                             width=444, height=200)
        rec_azul1.place(y=200, x=687)
        rec_gray1 = CTkLabel(bordePrest_inv, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=16,
                             width=420, height=180)
        rec_gray1.place(y=210, x=699)
        rec_azul2 = CTkLabel(bordePrest_inv, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=16,
                             width=444, height=200)
        rec_azul2.place(y=200, x=215)
        rec_gray2 = CTkLabel(bordePrest_inv, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=16,
                             width=420, height=180)
        rec_gray2.place(y=210, x=227)

        buttonxd = CTkButton(bordePrest_inv, text="Simulación de Préstamo", fg_color="#114b5f", hover_color="darkcyan",
                             font=("Nunito", 35), width=392,
                             height=45, corner_radius=8, command=lambda: controller.show_frame(Prestamos))
        buttonxd.place(x=240, y=275)

        buttonxd1 = CTkButton(bordePrest_inv, text="Inversiones", fg_color="#114b5f", hover_color="darkcyan",
                              font=("Nunito", 35), width=392,
                              height=45, corner_radius=8, command=lambda: controller.show_frame(Inversiones))
        buttonxd1.place(x=710, y=275)

        Buttonb = tk.Button(self, text="Volver", font=("Arial", 15), command=lambda: self.salirPagina())
        Buttonb.place(x=50, y=600)

    def salirPagina(self):
        self.controller.show_frame(MenuOpciones)


class Prestamos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        bordePrest = tk.LabelFrame(self, bg='#05171d', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordePrest.pack(fill="both", expand=True)

        respuestaLabelFrame = tk.LabelFrame(bordePrest, text="", height=550, width=400, bg="#05171d",
                                            foreground="gray60",
                                            bd=0, font=("Microsoft YaHei UI Light", 15))
        respuestaLabelFrame.place(x=708, y=53)

        button_monto = CTkButton(bordePrest, text="Monto del Préstamo", bg_color="#88d398", text_color="white",
                                 fg_color="#114b5f", font=("Nunito", 15), width=392,
                                 height=45, corner_radius=8, command=lambda: self.insertar_monto(controller))
        button_monto.place(x=240, y=150)

        button_tipo_prestamo = CTkButton(bordePrest, text="Tipo de interés", bg_color="#88d398", text_color="white",
                                         fg_color="#114b5f", font=("Nunito", 15), width=392,
                                         height=45, corner_radius=8, command=lambda: self.tipo_prestamo(controller))
        button_tipo_prestamo.place(x=240, y=325)

        button_plazo_prestamo = CTkButton(bordePrest, text="Plazo del Préstamo", bg_color="#88d398", text_color="white",
                                          fg_color="#114b5f", font=("Nunito", 15), width=392,
                                          height=45, corner_radius=8, command=lambda: self.insertar_tiempo(controller))
        button_plazo_prestamo.place(x=240, y=500)

        button_calcular = CTkButton(bordePrest, text="Calcular Cuota", bg_color="#88d398", text_color="white",
                                    fg_color="#114b5f", font=("Nunito", 25), width=150,
                                    height=150, corner_radius=10, command=lambda: self.calcular_cuota())
        button_calcular.place(x=25, y=250)
        Buttonb = tk.Button(self, text="Volver", font=("Arial", 15),
                            command=lambda: self.salirPagina(respuestaLabelFrame))
        Buttonb.place(x=50, y=600)

    def calcular_cuota(self):
        try:
            monto = float(self.entrada_monto.get())
            tasa = 0
            tiempo = 0

            if self.entrada_i_mes_2:
                tasa = float(self.entrada_i_mes_2.get()) / 100
                tiempo = int(self.entrada_tiempo_meses.get())
            elif self.entrada_i_bimestre_2:
                tasa = float(self.entrada_i_bimestre_2.get()) / 100
                tiempo = int(self.entrada_tiempo_meses.get()) // 2
            elif self.entrada_i_trimestre_2:
                tasa = float(self.entrada_i_trimestre_2.get()) / 100
                tiempo = int(self.entrada_tiempo_meses.get()) // 3
            elif self.entrada_i_cuatrimestre_2:
                tasa = float(self.entrada_i_cuatrimestre_2.get()) / 100
                tiempo = int(self.entrada_tiempo_meses.get()) // 4
            elif self.entrada_i_semestre_2:
                tasa = float(self.entrada_i_semestre_2.get()) / 100
                tiempo = int(self.entrada_tiempo_meses.get()) // 6
            elif self.entrada_i_ano_2:
                tasa = float(self.entrada_i_ano_2.get()) / 100
                tiempo = int(self.entrada_tiempo_annos.get())

            cuota_mensual = (monto * tasa * (1 + tasa) ** tiempo) / ((1 + tasa) ** tiempo - 1)
            messagebox.showinfo("Cuota Mensual", f"La cuota mensual es: ${cuota_mensual:.2f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def insertar_monto(self, controller):
        self.controller = controller
        self.entrada_monto = CTkEntry(self, placeholder_text="Ingrese el monto", font=("Microsoft YaHei UI Light", 15),
                                      width=300, height=35, text_color="gray90", bg_color="gray22", fg_color="gray26")
        self.entrada_monto.place(x=750, y=165)

    def tipo_prestamo(self, controller):
        self.controller = controller

        self.frame_tipo = customtkinter.CTkScrollableFrame(self, orientation="vertical", width=200, height=100)
        self.frame_tipo.place(x=750, y=325)
        self.frame_tipo._scrollbar.configure(height=1)

        self.button_i_mes = customtkinter.CTkButton(self.frame_tipo, text="Capitalizable mensualmente",
                                                    bg_color="#88d398", text_color="white", fg_color="#114b5f",
                                                    font=("Nunito", 12), height=28, width=140,
                                                    command=lambda m="mensual": self.button_presionado_capitalizacion(
                                                        m))
        self.button_i_mes.pack(pady=10)
        self.button_i_bimestre = customtkinter.CTkButton(self.frame_tipo, text="Capitalizable bimestralmente",
                                                         bg_color="#88d398", text_color="white", fg_color="#114b5f",
                                                         font=("Nunito", 12), height=28, width=140, command=lambda
                n="bimestral": self.button_presionado_capitalizacion(n))
        self.button_i_bimestre.pack(pady=10)
        self.button_i_trimestre = customtkinter.CTkButton(self.frame_tipo, text="Capitalizable trimestralmente",
                                                          bg_color="#88d398", text_color="white", fg_color="#114b5f",
                                                          font=("Nunito", 12), height=28, width=140, command=lambda
                o="trimestral": self.button_presionado_capitalizacion(o))
        self.button_i_trimestre.pack(pady=10)
        self.button_i_cuatrimestre = customtkinter.CTkButton(self.frame_tipo, text="Capitalizable cuatrimestralmente",
                                                             bg_color="#88d398", text_color="white", fg_color="#114b5f",
                                                             font=("Nunito", 12), height=28, width=140, command=lambda
                p="cuatrimestral": self.button_presionado_capitalizacion(p))
        self.button_i_cuatrimestre.pack(pady=10)
        self.button_i_semestral = customtkinter.CTkButton(self.frame_tipo, text="Capitalizable semestralmente",
                                                          bg_color="#88d398", text_color="white", fg_color="#114b5f",
                                                          font=("Nunito", 12), height=28, width=140, command=lambda
                q="semestral": self.button_presionado_capitalizacion(q))
        self.button_i_semestral.pack(pady=10)
        self.button_i_ano = customtkinter.CTkButton(self.frame_tipo, text="Capitalizable anualmente",
                                                    bg_color="#88d398", text_color="white", fg_color="#114b5f",
                                                    font=("Nunito", 12), height=28, width=140,
                                                    command=lambda r="anual": self.button_presionado_capitalizacion(r))
        self.button_i_ano.pack(pady=10)

    def button_presionado_capitalizacion(self, m):
        self.capitalizacion = [["mensual", False], ["bimestral", False], ["trimestral", False],
                               ["cuatrimestral", False], ["semestral", False], ["anual", False]]
        for i in range(6):
            if (m == self.capitalizacion[i][0]):
                self.capitalizacion[i][1] = True
            else:
                self.capitalizacion[i][1] = False

        self.limpiar_interfaz_anterior()
        self.interes()

    def button_presionado_periodo(self, m):
        self.periodo = [["mes", False], ["año", False]]
        for i in range(2):
            if (m == self.periodo[i][0]):
                self.periodo[i][1] = True
            else:
                self.periodo[i][1] = False

        self.limpiar_interfaz_anterior_2()
        self.tiempo_prestamo()

    def limpiar_interfaz_anterior(self):
        atributos_botones = ['button_i_mes_2', 'button_i_bimestre_2', 'button_i_trimestre_2',
                             'button_i_cuatrimestre_2', 'button_i_semestre_2', 'button_i_ano_2']
        atributos_entradas = ['entrada_i_mes_2', 'entrada_i_bimestre_2', 'entrada_i_trimestre_2',
                              'entrada_i_cuatrimestre_2', 'entrada_i_semestre_2', 'entrada_i_ano_2']
        for attr in atributos_botones + atributos_entradas:
            if hasattr(self, attr):
                widget = getattr(self, attr)
                widget.place_forget()

    def interes(self):
        self.frame_tipo.place_forget()
        self.frame_tipo.update_idletasks()
        self.frame_tipo.update()

        if (self.capitalizacion[0][1] == True):
            self.button_i_mes_2 = customtkinter.CTkButton(self, text="Capitalizable mensualmente", bg_color="#88d398",
                                                          text_color="white", fg_color="#114b5f", font=("Nunito", 12),
                                                          height=28, width=100)
            self.button_i_mes_2.place(x=756, y=351)
            self.entrada_i_mes_2 = CTkEntry(self, placeholder_text="Ingrese el porcentaje de interés mensual",
                                            font=("Microsoft YaHei UI Light", 15), width=300, height=35,
                                            text_color="gray90", bg_color="gray22", fg_color="gray26")
            self.entrada_i_mes_2.place(x=1000, y=351)
        elif (self.capitalizacion[1][1] == True):
            self.button_i_bimestre_2 = customtkinter.CTkButton(self, text="Capitalizable bimestralmente",
                                                               bg_color="#88d398", text_color="white",
                                                               fg_color="#114b5f", font=("Nunito", 12), height=28,
                                                               width=100)
            self.button_i_bimestre_2.place(x=756, y=351)
            self.entrada_i_bimestre_2 = CTkEntry(self, placeholder_text="Ingrese el porcentaje de interés bimestral",
                                                 font=("Microsoft YaHei UI Light", 15), width=300, height=35,
                                                 text_color="gray90", bg_color="gray22", fg_color="gray26")
            self.entrada_i_bimestre_2.place(x=1000, y=351)
        elif (self.capitalizacion[2][1] == True):
            self.button_i_trimestre_2 = customtkinter.CTkButton(self, text="Capitalizable trimestralmente",
                                                                bg_color="#88d398", text_color="white",
                                                                fg_color="#114b5f", font=("Nunito", 12), height=28,
                                                                width=100)
            self.button_i_trimestre_2.place(x=756, y=351)
            self.entrada_i_trimestre_2 = CTkEntry(self, placeholder_text="Ingrese el porcentaje de interés trimestral",
                                                  font=("Microsoft YaHei UI Light", 15), width=300, height=35,
                                                  text_color="gray90", bg_color="gray22", fg_color="gray26")
            self.entrada_i_trimestre_2.place(x=1000, y=351)
        elif (self.capitalizacion[3][1] == True):
            self.button_i_cuatrimestre_2 = customtkinter.CTkButton(self, text="Capitalizable cuatrimestralmente",
                                                                   bg_color="#88d398", text_color="white",
                                                                   fg_color="#114b5f", font=("Nunito", 12), height=28,
                                                                   width=100)
            self.button_i_cuatrimestre_2.place(x=756, y=351)
            self.entrada_i_cuatrimestre_2 = CTkEntry(self,
                                                     placeholder_text="Ingrese el porcentaje de interés cuatrimestral",
                                                     font=("Microsoft YaHei UI Light", 15), width=300, height=35,
                                                     text_color="gray90", bg_color="gray22", fg_color="gray26")
            self.entrada_i_cuatrimestre_2.place(x=1000, y=351)
        elif (self.capitalizacion[4][1] == True):
            self.button_i_semestre_2 = customtkinter.CTkButton(self, text="Capitalizable semestralmente", height=28,
                                                               width=100)
            self.button_i_semestre_2.place(x=756, y=351)
            self.entrada_i_semestre_2 = CTkEntry(self, placeholder_text="Ingrese el porcentaje de interés semestral",
                                                 font=("Microsoft YaHei UI Light", 15), width=300, height=35,
                                                 text_color="gray90", bg_color="gray22", fg_color="gray26")
            self.entrada_i_semestre_2.place(x=1000, y=351)
        elif (self.capitalizacion[5][1] == True):
            self.button_i_ano_2 = customtkinter.CTkButton(self, text="Capitalizable anualmente", height=28, width=100,
                                                          bg_color="#88d398", text_color="white", fg_color="#114b5f",
                                                          font=("Nunito", 12))
            self.button_i_ano_2.place(x=756, y=351)
            self.entrada_i_ano_2 = CTkEntry(self, placeholder_text="Ingrese el porcentaje de interés anual",
                                            font=("Microsoft YaHei UI Light", 15), width=300, height=35,
                                            text_color="gray90", bg_color="gray22", fg_color="gray26")
            self.entrada_i_ano_2.place(x=1000, y=351)

    def insertar_tiempo(self, controller):
        self.controller = controller

        self.frame = customtkinter.CTkScrollableFrame(self, orientation="vertical", width=100, height=100)
        self.frame.place(x=750, y=515)
        self.frame._scrollbar.configure(height=5)

        self.button_meses = customtkinter.CTkButton(self.frame, text="Meses", height=28, width=140,
                                                    command=lambda s="mes": self.button_presionado_periodo(s),
                                                    bg_color="#88d398", text_color="white", fg_color="#114b5f",
                                                    font=("Nunito", 12))
        self.button_meses.pack(pady=10)
        self.button_anos = customtkinter.CTkButton(self.frame, text="Años", height=28, width=140,
                                                   command=lambda t="año": self.button_presionado_periodo(t),
                                                   bg_color="#88d398", text_color="white", fg_color="#114b5f",
                                                   font=("Nunito", 12))
        self.button_anos.pack(pady=10)

    def limpiar_interfaz_anterior_2(self):
        atributos_botones = ['button_mesitos', 'button_annitos']
        atributos_entradas = ['entrada_tiempo_meses', 'entrada_tiempo_annos']
        for attr in atributos_botones + atributos_entradas:
            if hasattr(self, attr):
                widget = getattr(self, attr)
                widget.place_forget()

    def tiempo_prestamo(self):
        self.frame.place_forget()
        self.frame.update_idletasks()
        self.frame.update()

        if (self.periodo[0][1] == True):
            self.button_mesitos = customtkinter.CTkButton(self, text="Meses", height=28, width=100, bg_color="#88d398",
                                                          text_color="white", fg_color="#114b5f", font=("Nunito", 12))
            self.button_mesitos.place(x=756, y=531)
            self.entrada_tiempo_meses = CTkEntry(self, placeholder_text="Ingrese los meses",
                                                 font=("Microsoft YaHei UI Light", 15), width=300, height=35,
                                                 text_color="gray90", bg_color="gray22", fg_color="gray26")
            self.entrada_tiempo_meses.place(x=900, y=531)
        elif (self.periodo[1][1] == True):
            self.button_annitos = customtkinter.CTkButton(self, text="Años", height=28, width=100, bg_color="#88d398",
                                                          text_color="white", fg_color="#114b5f", font=("Nunito", 12))
            self.button_annitos.place(x=756, y=531)
            self.entrada_tiempo_annos = CTkEntry(self, placeholder_text="Ingrese los años",
                                                 font=("Microsoft YaHei UI Light", 15), width=300, height=35,
                                                 text_color="gray90", bg_color="gray22", fg_color="gray26")
            self.entrada_tiempo_annos.place(x=900, y=531)

        self.update()

    def salirPagina(self, frame):
        eliminar_widgets_labelframe(frame)
        self.controller.show_frame(Prestamos_Inversiones)

class Inversiones(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.historial_inversiones = []  # Lista para almacenar el historial de inversiones
        self.configurar_frame()

    def configurar_frame(self):
        bordeInv = tk.LabelFrame(self, bg='#05171d', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeInv.pack(fill="both", expand=True)

        # Etiqueta de selección de tipo de inversión
        label_tipo_inversion = CTkLabel(bordeInv, text="Seleccione tipo de inversión:", fg_color="#88d398",
                                        bg_color="#01213a", corner_radius=16, width=420, height=80,
                                        font=("Microsoft YaHei UI Light", 15))
        label_tipo_inversion.place(x=227, y=20)

        # Botones para seleccionar tipo de inversión
        button_acciones = CTkButton(bordeInv, text="Acciones", fg_color="#114b5f", hover_color="darkcyan",
                                    font=("Nunito", 25), width=200, height=45, corner_radius=8,
                                    command=lambda: self.seleccionar_inversion("Acciones"))
        button_acciones.place(x=400, y=120)

        button_bonos = CTkButton(bordeInv, text="Bonos", fg_color="#114b5f", hover_color="darkcyan",
                                 font=("Nunito", 25), width=200, height=45, corner_radius=8,
                                 command=lambda: self.seleccionar_inversion("Bonos"))
        button_bonos.place(x=400, y=200)

        button_fondos = CTkButton(bordeInv, text="Fondos Mutuos", fg_color="#114b5f", hover_color="darkcyan",
                                  font=("Nunito", 25), width=200, height=45, corner_radius=8,
                                  command=lambda: self.seleccionar_inversion("Fondos Mutuos"))
        button_fondos.place(x=400, y=280)

        # Etiqueta para evaluar riesgos
        label_evaluar_riesgos = CTkLabel(bordeInv, text="Evaluar riesgos:", fg_color="#88d398", bg_color="#01213a",
                                         corner_radius=16, width=420, height=80,
                                         font=("Microsoft YaHei UI Light", 15))
        label_evaluar_riesgos.place(x=227, y=370)

        # Entrada para ingresar el monto a invertir
        self.entrada_monto_invertir = CTkEntry(bordeInv, placeholder_text="Ingrese el monto a invertir",
                                               font=("Microsoft YaHei UI Light", 15), width=300, height=35,
                                               text_color="gray90", bg_color="gray22", fg_color="gray26")
        self.entrada_monto_invertir.place(x=685, y=385)

        # Botón para evaluar riesgos
        button_evaluar_riesgo = CTkButton(bordeInv, text="Evaluar Riesgo", fg_color="#114b5f",
                                          hover_color="darkcyan",
                                          font=("Nunito", 25), width=200, height=45, corner_radius=8,
                                          command=self.evaluar_riesgo)
        button_evaluar_riesgo.place(x=685, y=450)

        # Botón para finalizar la inversión
        button_finalizar = CTkButton(bordeInv, text="Finalizar Inversión", fg_color="#114b5f",
                                     hover_color="darkcyan",
                                     font=("Nunito", 25), width=300, height=45, corner_radius=8,
                                     command=self.finalizar_inversion)
        button_finalizar.place(x=505, y=520)

        # Botón para volver al menú de opciones
        button_volver = tk.Button(self, text="Volver", font=("Arial", 15), command=lambda: self.salir_pagina())
        button_volver.place(x=50, y=600)

        # Botón para ver historial de inversiones
        button_historial = tk.Button(self, text="Ver Historial", font=("Arial", 15), command=self.ver_historial)
        button_historial.place(x=150, y=600)

        # Atributos para almacenar selección y evaluación de riesgos
        self.tipo_inversion = ""
        self.riesgo_evaluado = ""

    def update_frame(self):
        # Actualiza el frame cuando se vuelve a mostrar
        for widget in self.winfo_children():
            widget.destroy()
        self.configurar_frame()

    def seleccionar_inversion(self, tipo):
        # Almacena el tipo de inversión seleccionado y muestra un mensaje
        self.tipo_inversion = tipo
        messagebox.showinfo("Selección de Inversión", f"Ha seleccionado: {tipo}")

    def evaluar_riesgo(self):
        # Simula una evaluación de riesgos
        if self.tipo_inversion == "":
            messagebox.showerror("Error", "Seleccione primero el tipo de inversión.")
            return
        self.riesgo_evaluado = "Bajo" if self.tipo_inversion == "Bonos" else "Alto"
        messagebox.showinfo("Evaluación de Riesgo",
                            f"El riesgo de {self.tipo_inversion} es {self.riesgo_evaluado}.")

    def finalizar_inversion(self):
        # Valida el monto ingresado y finaliza la inversión
        monto = self.entrada_monto_invertir.get()
        if not monto.isdigit():
            messagebox.showerror("Error", "Ingrese un monto válido.")
            return

        monto = float(monto)
        if monto <= 0:
            messagebox.showerror("Error", "Ingrese un monto mayor que cero.")
            return

        if self.tipo_inversion == "":
            messagebox.showerror("Error", "Seleccione primero el tipo de inversión.")
            return

        if self.riesgo_evaluado == "":
            messagebox.showerror("Error", "Evalúe el riesgo antes de finalizar la inversión.")
            return

        # Guarda la inversión en el historial
        self.historial_inversiones.append((self.tipo_inversion, monto, self.riesgo_evaluado))

        # Aquí podrías implementar la lógica para finalizar la inversión
        messagebox.showinfo("Inversión Finalizada",
                            f"Ha invertido {monto} en {self.tipo_inversion} con riesgo {self.riesgo_evaluado}.")

        # Reiniciar variables para futuras inversiones
        self.tipo_inversion = ""
        self.riesgo_evaluado = ""
        self.entrada_monto_invertir.delete(0, tk.END)

    def salir_pagina(self):
        # Muestra el frame de Prestamos_Inversiones
        self.controller.show_frame(Prestamos_Inversiones)

    def ver_historial(self):
        # Muestra el historial de inversiones
        if not self.historial_inversiones:
            messagebox.showinfo("Historial de Inversiones", "No hay inversiones registradas.")
        else:
            historial = "\n".join(
                [f"Tipo: {inv[0]}, Monto: {inv[1]}, Riesgo: {inv[2]}" for inv in self.historial_inversiones])
            messagebox.showinfo("Historial de Inversiones", historial)
def salirPagina(self, frame):
    eliminar_widgets_labelframe(frame)
    self.controller.show_frame(Prestamos_Inversiones)


class Config(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        bordeContra = tk.LabelFrame(self, bg='#20ace8', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeContra.pack(fill="both", expand=True)

        # Rectangulos

        label_bg1 = CTkLabel(bordeContra, fg_color="#25e8e8", bg_color="#20ace8", text="", corner_radius=16, width=979,
                             height=460)
        label_bg1.place(y=40, x=210)

        # Titulo del frame
        self.Label = tk.Label(self, fg="black", bg="#25e8e8", text="Cambiar contraseña ",
                              font=("Microsoft YaHei UI Light", 20, "bold"))
        self.Label.place(x=590, y=90)
        # validar contraseña antigua
        self.Label1 = tk.Label(self, fg="black", bg="#25e8e8", text="Contraseña antigua: ",
                               font=("Microsoft YaHei UI Light", 17))
        self.Label1.place(x=260, y=190)
        self.C1 = CTkEntry(bordeContra, show="*", placeholder_text="Introduzca su contraseña actual",
                           font=("Microsoft YaHei UI Light", 15), width=300, height=35, text_color="black",
                           bg_color="#25e8e8", fg_color="white")
        self.C1.place(x=670, y=190)

        self.nuevaContraLabelFrame = tk.LabelFrame(bordeContra, text="", height=250, width=800, bg="#25e8e8",
                                                   foreground="gray60",
                                                   bd=0, font=("Microsoft YaHei UI Light", 15))
        self.nuevaContraLabelFrame.place(x=230, y=240)

        # boton para volver, ojo, tiene SalirPagina()
        Buttona = tk.Button(bordeContra, text="Volver", font=("Arial", 15),
                            command=lambda: self.salirPagina(self.nuevaContraLabelFrame))
        Buttona.place(x=50, y=600)

        bottonNuevoFrame = CTkButton(bordeContra, text="Validar", text_color="black", bg_color="#25e8e8",
                                     fg_color="gray60",
                                     width=100, height=40, corner_radius=8, font=("Microsoft YaHei UI Light", 16),
                                     command=lambda: self.ValidarContraseñaAntigua(controller))
        bottonNuevoFrame.place(x=1000, y=185)

    def ValidarContraseñaAntigua(self, controller):
        if controller.contraseña == self.C1.get():
            messagebox.showinfo("Correcto", "Contraseña antigua verificada :)")
            self.mostrarCambioContra(controller, self.nuevaContraLabelFrame)
        else:
            messagebox.showinfo("Error", "Contraseña antigua incorrecta")

    def mostrarCambioContra(self, controller, frame):
        eliminar_widgets_labelframe(frame)

        self.Label2 = tk.Label(self, fg="black", bg="#25e8e8", text="Contraseña nueva: ",
                               font=("Microsoft YaHei UI Light", 17))
        self.Label2.place(x=260, y=260)
        self.Label3 = tk.Label(self, fg="black", bg="#25e8e8", text="Reescriba la contraseña: ",
                               font=("Microsoft YaHei UI Light", 17))
        self.Label3.place(x=260, y=330)

        self.C2 = CTkEntry(self, show="*", placeholder_text="Introduzca la nueva contraseña",
                           font=("Microsoft YaHei UI Light", 15), width=300, height=35, text_color="black",
                           bg_color="#25e8e8", fg_color="white")
        self.C2.place(x=680, y=260)
        self.C3 = CTkEntry(self, show="*", placeholder_text="Confirmar nueva contraseña",
                           font=("Microsoft YaHei UI Light", 15), width=300, height=35, text_color="black",
                           bg_color="#25e8e8", fg_color="white")
        self.C3.place(x=680, y=330)

        def enviar():
            df = pd.read_excel('loginData.xlsx', sheet_name='Sheet1')
            df['Contraseña'] = df['Contraseña'].astype(str)
            if len(str(self.C2.get())) >= 8:
                if (self.C2.get()).isalnum():
                    if (self.C2.get()) == (self.C3.get()):
                        filac = df.index[df["Contraseña"] == str(self.C1.get())].tolist()
                        for i in filac:
                            df.at[i, "Contraseña"] = str(self.C2.get())
                        controller.contraseña = str(self.C2.get())
                        df.to_excel("LoginData.xlsx", index=False)
                        messagebox.showinfo("Contraseña cambiada!", "Su nueva contraseña es: {}".format(controller.contraseña))
                        self.C1.delete(0, tk.END)
                        self.C2.delete(0, tk.END)
                        self.C3.delete(0, tk.END)
                        eliminar_widgets_labelframe(frame)
                        controller.show_frame(MenuOpciones)
                    else:
                        messagebox.showinfo("Error", "La confirmación de la nueva contraseña no coincide")
                else:
                    messagebox.showinfo("Error", "La nueva contraseña solo debe contener números y letras.")
            else:
                messagebox.showinfo("Error", "La nueva contraseña debe tener al menos 8 caracteres.")

        # BOTON para cambiar la contraseña
        cambiarcontra = CTkButton(self, text="Enviar", text_color="black", bg_color="#25e8e8", fg_color="gray60",
                                  width=392,
                                  height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 16), command=enviar)
        cambiarcontra.place(x=500, y=420)

    # para el boton volver
    def salirPagina(self, frame):
        eliminar_widgets_labelframe(frame)
        self.controller.show_frame(MenuOpciones)


class pagarServicios(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.service_prices = {}
        bordeMenu = tk.LabelFrame(self, bg='#05171d', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeMenu.pack(fill="both", expand=True)
        # PAGAR SERVICIOS
        self.title = tk.Label(bordeMenu, text="Pagar Servicios", font=("Helvetica", 30), bg="#05171d", fg="white")
        self.title.place(x=530, y=80)

        # elegirr
        self.service_label = tk.Label(bordeMenu, text="Seleccione el servicio a pagar:",
                                      font=("Microsoft YaHei UI Light", 16), bg="#05171d", fg="white")
        self.service_label.place(x=300, y=150)

        self.service_var = tk.StringVar(value="Electricidad")
        self.service_options = ["Electricidad", "Agua", "Internet", "Teléfono", "Gas"]
        for service in self.service_options:
            self.service_prices[service] = random.randint(20, 100)
        self.service_menu = tk.OptionMenu(bordeMenu, self.service_var, *self.service_options,
                                          command=self.update_amount_label)
        self.service_menu.place(x=300, y=200, width=200, height=30)

        # monto a pagar
        self.amount_label = tk.Label(bordeMenu,
                                     text=f"Monto a pagar: {self.service_prices[self.service_var.get()]} fisiCoins",
                                     font=("Microsoft YaHei UI Light", 16), bg="#05171d", fg="white")
        self.amount_label.place(x=300, y=250)
        # saldo actualizado
        self.bolsillo = tk.Label(bordeMenu, fg="white", bg="#0084f1", text="FisiCoins: " + str(controller.FisiCoins),
                                 font=("Microsoft YaHei UI Light", 12))
        self.bolsillo.place(x=300, y=300)

        # Botón de pagar
        self.pay_button = tk.Button(bordeMenu, text="Pagar", command=self.pay_service)
        self.pay_button.place(x=300, y=350)
        Buttona = tk.Button(bordeMenu, text="Volver", font=("Arial", 15),
                            command=lambda: controller.show_frame(MenuOpciones))
        Buttona.place(x=50, y=600)

    def pay_service(self):
        service = self.service_var.get()
        amount = self.service_prices[self.service_var.get()]

        amount = float(amount)
        if amount > self.controller.FisiCoins:
            messagebox.showerror("Error", "Fondos insuficientes")
            return

        messagebox.showinfo("Pago realizado", f"Has pagado {amount} por el servicio de {service}.")
        self.controller.modificarFisiCoins(amount)

    def update_amount_label(self, selected_service):
        self.amount_label.config(text=f"Monto a pagar: {self.service_prices[selected_service]} fisiCoins")


# Clase Aplicacion, donde creamos la ventana por la que pasaran los frames
class Aplicacion(tk.Tk):
    # variables que usaremos
    FisiCoins = 0
    codigoEstudiante = 0
    nombreEstudiante = ""
    correoEstudiante = ""
    creditos = 0
    tipoEstudiante = ""
    contraseña = ""
    dni = 0
    foto = 0
    # inicializamos la clase
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # self.state hace referencia si misma, a Aplicacion, y "zoomed" hace que este en pantalla completa al iniciar
        self.state("zoomed")
        # el titulo de la ventana
        self.title("Aplicacion De Pagos")

        # una ventana en blanco
        # falta revisar esta parte, ojo :u
        window = tk.Frame(self)
        window.pack(fill="both", expand=True)
        window.grid_rowconfigure(0, minsize=700)
        window.grid_columnconfigure(0, minsize=1365)

        # creamos un diccionario llamado frames
        # el diccionario te permite almacenar distintos valores, no solo tipos de datos primitivos
        # como el array en c++, pero con mas capacidades
        self.frames = {}
        for F in (Login, MenuOpciones, InfoUsuario, Config, Prestamos_Inversiones, Prestamos, pagarServicios, Inversiones):  # hacemos que F recorra Login, MenuOpciones, InfoUsuario (hara 3 vueltas xd)
            frame = F(window, self)  # esta parte de aca inicializa las subclases de Aplicacion
            # de esta manera: en la primera vuelta F sera Login, lo que hara
            # frame = Login(window, self) esto creara el Login, lo mismo pasara en la 2da y 3ra vuelta
            # ahora almacenamos frame en el diccionario frames
            self.frames[F] = frame
            # frame.grid es para q funcione xd, no tiene mucha explicacion, si lo quitas no corre
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(
            Login)  # llamamos a showframe(Login) para que al correr el programa, Login sea lo primero en aparecer

    # creamos la funcion show_frame, que traera al frente el frame que queramos
    def show_frame(self, page):
        # al llamar la funcion le daremos el parametro "page", que sera para indicar a que frame queremos cambiar
        frame = self.frames[page]

        # .tkraise hace que el frame se levante sobre el que tenemos en pantalla
        frame.tkraise()

    # llamaremos a la funcion modificarFisicoins cuando lo necesitemos
    # le debemos pasar el nuevoValor como parametro para ser la nueva FisiCoins
    def modificarFisiCoins(self, nuevoValor):
        df = pd.read_excel('loginData.xlsx')
        numFila = df.index[df["Codigo"] == self.codigoEstudiante].tolist()
        numFila = numFila[0]
        FisicoinActual = df.at[numFila, "Dinero"]
        df.at[numFila, "Dinero"] = FisicoinActual - nuevoValor
        self.FisiCoins = FisicoinActual - nuevoValor
        df.to_excel('loginData.xlsx', index=False)

    def modificarFisiCoinsMas(self, nuevoValor):
        df = pd.read_excel('loginData.xlsx')
        numFila = df.index[df["Codigo"] == self.codigoEstudiante].tolist()
        numFila = numFila[0]
        FisicoinActual = df.at[numFila, "Dinero"]
        df.at[numFila, "Dinero"] = FisicoinActual + nuevoValor
        self.FisiCoins = FisicoinActual + nuevoValor
        df.to_excel('loginData.xlsx', index=False)

    def MandarDinero(self, monto, correo):
        df = pd.read_excel('loginData.xlsx')
        numFila = df.index[df["Correo"] == correo].tolist()
        numFila = numFila[0]
        FisicoinActual = df.at[numFila, "Dinero"]
        df.at[numFila, "Dinero"] = FisicoinActual + monto
        df.to_excel('loginData.xlsx', index=False)


# if __name == '__main__' hace que solo se ejecute lo que esta dentro del if
# es como un int main()
if __name__ == '__main__':
    # creamos app, un objeto que sera clase Aplicacion, al hacer esto
    # inicializara Aplicacion, y Aplicacion inicializara las subclases que tiene dentro
    app = Aplicacion()
    # .mainloop para que la ventana no se cierre
    app.mainloop()
