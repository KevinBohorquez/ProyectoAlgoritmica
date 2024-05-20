import tkinter as tk
from tkinter import Tk, Label, Button, Entry, Frame, messagebox, mainloop

import customtkinter
from PIL import Image, ImageTk
import pandas as pd
from customtkinter import *

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        fondounmsm = ImageTk.PhotoImage(file="C:/Users/Kevin/Desktop/Proyecto Algoritmica/bgr.png")
        rutaicono = "C:/Users/Kevin/Desktop/Proyecto Algoritmica/logofisi.png"
        img1 = Image.open(rutaicono)
        img1 = img1.resize((155, 155))

        borde = tk.LabelFrame(self, bg='white', bd=10, font=("Microsoft YaHei UI Light", 15))
        borde.pack(fill="both", expand=True)

        fondazo = tk.Label(borde, image=fondounmsm)
        fondazo.image = fondounmsm
        fondazo.place(x=0, y=0, relwidth=1, relheight=1)

        label_bg = tk.Label(borde, bg="black")
        label_bg.place(y=80, x=475, width=400, height=500)
        canvas = tk.Canvas(label_bg, bg="gray17", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        L1 = tk.Label(borde, fg="gray90", bg="gray17", text="Inicio de Sesion", font=("Microsoft YaHei UI Light", 25))
        L1.place(x=556, y=95)
        Frame(borde, width=345, height=2, bg="gray50").place(x=504, y=155)

        img11 = ImageTk.PhotoImage(img1)
        imagenFisiLogo = tk.Label(borde, image=img11, bg="gray17")
        imagenFisiLogo.image = img11
        imagenFisiLogo.place(x=600, y=165)

        T1 = CTkEntry(borde, placeholder_text="Correo Institucional", font=("Microsoft YaHei UI Light", 15), width=300, height=35, text_color="gray90", bg_color="gray22", fg_color="gray26")
        T1.place(x=530, y=340)
        T2 = CTkEntry(borde, show="*", placeholder_text="Codigo de Estudiante", font=("Microsoft YaHei UI Light", 15), width=300, height=35, text_color="gray90", bg_color="gray22", fg_color="gray26")
        T2.place(x=530, y=390)

        nextsito = tk.Button(borde, text="Next", font=("Microsoft YaHei UI Light", 35), command=lambda: controller.show_frame(MenuOpciones))
        nextsito.place(x=1150, y=550)

        def entrar():

            try:
                df = pd.read_excel('loginDataTEST.xlsx')
                if (str(T1.get()) in df["Correo"].values):
                    if df[df["Correo"] == str(T1.get())]["Codigo"].iloc[0] == int(T2.get()):
                        messagebox.showinfo("Acceso Correcto", "Has ingresado")
                        numFila = df[df["Codigo"] == int(T2.get())]
                        controller.creditos = str(numFila["Creditos"].iloc[0])
                        controller.nombreEstudiante = numFila["Nombre"].iloc[0]
                        controller.FisiCoins = numFila["Dinero"].iloc[0]
                        controller.tipoEstudiante = (numFila["Tipo"].iloc[0])
                        controller.codigoEstudiante = str(int(T2.get()))
                        controller.correoEstudiante = str(T1.get())
                        T1.delete(0, tk.END)
                        T2.delete(0, tk.END)
                        controller.show_frame(MenuOpciones)
                    else:
                        messagebox.showinfo("Acceso Incorrecto", "Codigo incorrecto")
                else:
                    messagebox.showinfo("Acceso Incorrecto", "Correo no existe")
            except FileNotFoundError:
                messagebox.showerror("Error", "El archivo Excel no se encuentra")
        BTN1 = CTkButton(borde, bg_color="gray17", fg_color="SpringGreen2", text="Ingresar", corner_radius=16, text_color="gray90", width=300, height=45, font=("Arial", 20), command=entrar)
        BTN1.place(x=530, y=465)


class MenuOpciones(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        bordeMenu = tk.LabelFrame(self, bg='purple4', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeMenu.pack(fill="both", expand=True)

        label_3 = CTkLabel(bordeMenu, fg_color="magenta4", bg_color="purple4", text="", corner_radius=16, width=390,
                           height=240)
        label_3.place(x=500, y=15)
        label_4 = CTkLabel(bordeMenu, fg_color="purple3", bg_color="magenta4", text="", corner_radius=16, width=370,
                           height=240)
        label_4.place(x=510, y=25)

        textito = CTkLabel(bordeMenu, text="MENU DE OPCIONES", font=("Times New Roman", 30), width=300, height=35, text_color="gold2", bg_color="purple3")
        textito.place(x=550, y=31)

        label_2 = CTkLabel(bordeMenu, fg_color="magenta4", bg_color="purple4", text="", corner_radius=16, width=1180,
                           height=540)
        label_2.place(x=85, y=70)
        label_1 = CTkLabel(bordeMenu, fg_color="purple3", bg_color="magenta4", text="", corner_radius=16, width=1160,
                            height=520)
        label_1.place(x=95, y=80)

        burrito_path = os.path.join(os.path.dirname(__file__), 'burrito.jpg')
        image = customtkinter.CTkImage(light_image= Image.open(burrito_path), size=(250, 147))
        image_label = customtkinter.CTkLabel(bordeMenu, image=image, text='')
        image_label.place(x=555, y=272)

        buttoon = CTkButton(bordeMenu, width=550, bg_color="purple3", text_color="black", corner_radius=16, height=150, fg_color="green4", hover_color="green3",text="Operaciones Bancarias", font=("Microsoft YaHei UI Light", 30), command=lambda: controller.show_frame(InfoUsuario))
        buttoon.place(x=120, y=110)

        buttoon1 = CTkButton(bordeMenu, width=550, bg_color="purple3", text_color="black", corner_radius=16, height=150,  fg_color="red4", hover_color="red2", text="Pagar Servicios", font=("Microsoft YaHei UI Light", 30))
        buttoon1.place(x=690, y=110)

        buttoon2 = CTkButton(bordeMenu, width=420, bg_color="purple3", text_color="black", corner_radius=16, height=150, text="Proximamente:\nQuiosco Virtual", font=("Microsoft YaHei UI Light", 30))
        buttoon2.place(x=120, y=270)

        buttoon3 = CTkButton(bordeMenu, width=420, bg_color="purple3", text_color="black", corner_radius=16, height=150, text="Proximamente:\n Casino", font=("Microsoft YaHei UI Light", 30))
        buttoon3.place(x=820, y=270)

        buttoon4 = CTkButton(bordeMenu, width=550, bg_color="purple3", text_color="black", corner_radius=16, height=150, fg_color="blue4", hover_color="blue", text="Configuracion", font=("Microsoft YaHei UI Light", 30))
        buttoon4.place(x=120, y=430)

        buttoon5 = CTkButton(bordeMenu, width=550, bg_color="purple3", text_color="black", corner_radius=16, height=150, fg_color="yellow4", hover_color="yellow3", text="Prestamos e Inversiones", font=("Microsoft YaHei UI Light", 30))
        buttoon5.place(x=690, y=430)

        volverLogin = tk.Button(bordeMenu, text="Cerrar Sesion", font=("Microsoft YaHei UI Light", 15), command=lambda: controller.show_frame(Login))
        volverLogin.place(x=10, y=627)

class InfoUsuario(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        bordeInfo = tk.LabelFrame(self, bg='gray22', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeInfo.pack(fill="both", expand=True)

        label_bg = CTkLabel(bordeInfo, fg_color="blue", bg_color="gray22", text="", corner_radius=16, width=444, height=590)
        label_bg.place(y=30, x=687)
        label_bg1 = CTkLabel(bordeInfo, fg_color="gray60", bg_color="blue", text="", corner_radius=16, width=420, height=570)
        label_bg1.place(y=40, x=699)

        label_bg2 = CTkLabel(bordeInfo, fg_color="blue", bg_color="gray22", text="", corner_radius=16, width=444, height=590)
        label_bg2.place(y=30, x=215)
        label_bg3 = CTkLabel(bordeInfo, fg_color="gray60", bg_color="blue", text="", corner_radius=16, width=420, height=570)
        label_bg3.place(y=40, x=227)


        bottonsito2 = CTkButton(bordeInfo, text="Mostrar Informacion", bg_color="gray60", fg_color="gray50", width=392, height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15), command= lambda:self.mostrarDatos(controller))
        bottonsito2.place(x=240, y=52)

        bottonsito3 = CTkButton(bordeInfo, text="Consultar Saldo", bg_color="gray60", fg_color="gray50", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15))
        bottonsito3.place(x=240, y=102)

        bottonsito4 = CTkButton(bordeInfo, text="Realizar Retiro", bg_color="gray60", fg_color="gray50", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15))
        bottonsito4.place(x=240, y=152)

        bottonsito5 = CTkButton(bordeInfo, text="Transferencia entre cuentas", bg_color="gray60", fg_color="gray50", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15))
        bottonsito5.place(x=240, y=202)

        Buttona = tk.Button(self, text="Volver", font=("Arial", 15), command=lambda: self.salirPagina())
        Buttona.place(x=50, y=600)

    def mostrarDatos(self, controller):
        self.controller = controller
        self.Label = tk.Label(self, fg="white", bg="gray60", text="Codigo de estudiante: "+str(controller.codigoEstudiante), font=("Microsoft YaHei UI Light", 12))
        self.Label.place(x=710, y=100)
        self.Label2 = tk.Label(self, fg="white", bg="gray60", text="Correo Institucional: "+controller.correoEstudiante, font=("Microsoft YaHei UI Light", 12))
        self.Label2.place(x=710, y=150)
        self.Label3 = tk.Label(self, fg="white", bg="gray60", text="Creditos: "+str(controller.creditos), font=("Microsoft YaHei UI Light", 12))
        self.Label3.place(x=710, y=200)
        self.Label4 = tk.Label(self, fg="white", bg="gray60", text="Nombre del Estudiante: "+controller.nombreEstudiante, font=("Microsoft YaHei UI Light", 11))
        self.Label4.place(x=710, y=250)
        self.Label5 = tk.Label(self, fg="white", bg="gray60", text="Tipo de Estudiante: " + controller.tipoEstudiante, font=("Microsoft YaHei UI Light", 12))
        self.Label5.place(x=710, y=300)
        self.Label6 = tk.Label(self, fg="white", bg="gray60", text="FisiCoins: " + str(controller.FisiCoins), font=("Microsoft YaHei UI Light", 12))
        self.Label6.place(x=710, y=350)
    def salirPagina(self):
        self.controller.show_frame(MenuOpciones)
        self.Label6.destroy()
        self.Label5.destroy()
        self.Label4.destroy()
        self.Label3.destroy()
        self.Label2.destroy()
        self.Label.destroy()


class Aplicacion(tk.Tk):
    FisiCoins = 0
    codigoEstudiante = 0
    nombreEstudiante = ""
    correoEstudiante = ""
    creditos = 0
    tipoEstudiante = ""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.state("zoomed")
        self.title("Aplicacion De Pagos")

        window = tk.Frame(self)
        window.pack(fill="both", expand=True)

        window.grid_rowconfigure(0, minsize=700)
        window.grid_columnconfigure(0, minsize=1365)

        self.frames = {}
        for F in (Login, MenuOpciones, InfoUsuario):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Login)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def modificarFisiCoins(self, nuevoValor):
        self.FisiCoins = nuevoValor

if __name__ == '__main__':
    app = Aplicacion()
    app.mainloop()
