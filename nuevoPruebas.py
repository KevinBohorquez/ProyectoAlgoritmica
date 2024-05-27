import tkinter as tk
from tkinter import Tk, Label, Button, Entry, Frame, messagebox, mainloop

import customtkinter
from PIL import Image, ImageTk
import pandas as pd
from customtkinter import *
#importamos las librerias tk, customtkinter, pillow y pandas

#Clase Login, clase hija de la clase Aplicacion
class Login(tk.Frame):

    #Inicializamos la clase, self para referirse a si mismo (el login) y controller se refiere a su clase padre (Aplicacion)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Colocamos el fondo de san marcos
        fondounmsm = ImageTk.PhotoImage(file="C:/Users/Kevin/Desktop/Proyecto Algoritmica/bgr.png")
        rutaicono = "C:/Users/Kevin/Desktop/Proyecto Algoritmica/logofisi.png"
        img1 = Image.open(rutaicono)
        img1 = img1.resize((155, 155))

        #hacemos el borde, de tipo LabelFrame, que nos ayudara a manejar los widgets (button, label, entry, etc)
        #este borde funciona como una caja invisible que la haremos de las dimensiones de la ventana
        #dentro de el borde pondremos los widgets
        borde = tk.LabelFrame(self, bg='white', bd=10, font=("Microsoft YaHei UI Light", 15))
        borde.pack(fill="both", expand=True)

        #ponemos el fondo de san marcos
        fondazo = tk.Label(borde, image=fondounmsm)
        fondazo.image = fondounmsm
        fondazo.place(x=0, y=0, relwidth=1, relheight=1)

        #el rectangulo gris
        label_bg = tk.Label(borde, bg="black")
        label_bg.place(y=80, x=475, width=400, height=500)
        canvas = tk.Canvas(label_bg, bg="gray17", highlightthickness=0)
        canvas.pack(fill=tk.BOTH, expand=True)

        #ponemos el logo de la fisi
        img11 = ImageTk.PhotoImage(img1)
        imagenFisiLogo = tk.Label(borde, image=img11, bg="gray17")
        imagenFisiLogo.image = img11
        imagenFisiLogo.place(x=600, y=165)

        #Escribimos el inicio de sesion con un label
        L1 = tk.Label(borde, fg="gray90", bg="gray17", text="Inicio de Sesion", font=("Microsoft YaHei UI Light", 25))
        L1.place(x=556, y=95)
        Frame(borde, width=345, height=2, bg="gray50").place(x=504, y=155)


        #Hacemos 2 Entry, donde el usuario escribira el texto en pantalla,
        T1 = CTkEntry(borde, placeholder_text="Correo Institucional", font=("Microsoft YaHei UI Light", 15), width=300, height=35, text_color="gray90", bg_color="gray22", fg_color="gray26")
        T1.place(x=530, y=340)
        #En el T2 lo ocultamos con show="*"
        T2 = CTkEntry(borde, show="*", placeholder_text="Codigo de Estudiante", font=("Microsoft YaHei UI Light", 15), width=300, height=35, text_color="gray90", bg_color="gray22", fg_color="gray26")
        T2.place(x=530, y=390)

        #un boton next para pasar a la siguiente ventana rapido, para testeos, no necesitaras ingresar el usuario
        nextsito = tk.Button(borde, text="Next", font=("Microsoft YaHei UI Light", 35), command=lambda: controller.show_frame(MenuOpciones))
        nextsito.place(x=1150, y=550)

        #definimos la funcion entrar, que se activara al presionar el boton Ingresar
        def entrar():

            try: #Intentemos leer el archivo excel
                df = pd.read_excel('loginData.xlsx')
                if (str(T1.get()) in df["Correo"].values): #revisamos si el texto en T1 esta en la columna "Correo" del excel
                    if df[df["Correo"] == str(T1.get())]["Codigo"].iloc[0] == int(T2.get()): #sacamos el numero de la fila donde se encuentra
                        # nuestro Correo, sacamos el Codigo de alumno de esa fila y lo igualamos al T2 escrito por el usuario
                        #los messagebox son cuadros emergentes al que les pones un titulo y mensaje
                        messagebox.showinfo("Acceso Correcto", "Has ingresado")
                        #la variable numFila, guardara el numero de la fila donde se encuentra nuestro usuario en el excel
                        numFila = df[df["Codigo"] == int(T2.get())]
                        #hacemos que las variables de la clase Aplicacion guarden los datos que estan en el excel
                        controller.creditos = str(numFila["Creditos"].iloc[0])
                        controller.nombreEstudiante = numFila["Nombre"].iloc[0]
                        controller.FisiCoins = numFila["Dinero"].iloc[0]
                        controller.tipoEstudiante = (numFila["Tipo"].iloc[0])
                        controller.codigoEstudiante = str(int(T2.get()))
                        controller.correoEstudiante = str(T1.get())
                        #como ya se verifico que es correcto el correo y codigo, borramos lo escrito en los campos T1 y T2
                        T1.delete(0, tk.END)
                        T2.delete(0, tk.END)
                        #pasamos al frame MenuOpciones
                        controller.show_frame(MenuOpciones)
                    else:
                        messagebox.showinfo("Acceso Incorrecto", "Codigo incorrecto")
                else:
                    messagebox.showinfo("Acceso Incorrecto", "Correo no existe")
            except FileNotFoundError:
                messagebox.showerror("Error", "El archivo Excel no se encuentra")
        #el boton donde dice ingresar :p
        BTN1 = CTkButton(borde, bg_color="gray17", fg_color="SpringGreen2", text="Ingresar", corner_radius=16, text_color="gray90", width=300, height=45, font=("Arial", 20), command=entrar)
        BTN1.place(x=530, y=465)


#clase MenuOpciones, clase hija de la clase Aplicacion
class MenuOpciones(tk.Frame):

    #Inicializamos la clase, self para referirse a si mismo (el login) y controller se refiere a su clase padre (Aplicacion)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #hacemos un bordemenu, con la misma funcionalidad que el borde de Login xd
        bordeMenu = tk.LabelFrame(self, bg='purple4', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeMenu.pack(fill="both", expand=True)

        #partes del diseño, los rectangulos morados :p
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

        #insertamos la imagen del burrito
        burrito_path = os.path.join(os.path.dirname(__file__), 'burrito.jpg')
        image = customtkinter.CTkImage(light_image= Image.open(burrito_path), size=(250, 147))
        image_label = customtkinter.CTkLabel(bordeMenu, image=image, text='')
        image_label.place(x=555, y=272)

        #las diferentes tipos de opciones, hover_color cambiar el color cuando el mouse este encima
        #buttoon, tiene un command para ir a Operaciones Bancarias
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

        #cerrar sesion, para volve al login
        volverLogin = tk.Button(bordeMenu, text="Cerrar Sesion", font=("Microsoft YaHei UI Light", 15), command=lambda: controller.show_frame(Login))
        volverLogin.place(x=10, y=627)

#clase InfoUsuario, clase hija de la clase Aplicacion
class InfoUsuario(tk.Frame):
    # Inicializamos la clase, self para referirse a si mismo (el login) y controller se refiere a su clase padre (Aplicacion)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        bordeInfo = tk.LabelFrame(self, bg='gray22', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeInfo.pack(fill="both", expand=True)

        #los rectangulos gris y azul, debajo de donde estar el texto xd
        label_bg = CTkLabel(bordeInfo, fg_color="blue", bg_color="gray22", text="", corner_radius=16, width=444, height=590)
        label_bg.place(y=30, x=687)
        label_bg1 = CTkLabel(bordeInfo, fg_color="gray60", bg_color="blue", text="", corner_radius=16, width=420, height=570)
        label_bg1.place(y=40, x=699)
        label_bg2 = CTkLabel(bordeInfo, fg_color="blue", bg_color="gray22", text="", corner_radius=16, width=444, height=590)
        label_bg2.place(y=30, x=215)
        label_bg3 = CTkLabel(bordeInfo, fg_color="gray60", bg_color="blue", text="", corner_radius=16, width=420, height=570)
        label_bg3.place(y=40, x=227)

        #boton, que activa la funcion MostrarInformacio
        bottonsito2 = CTkButton(bordeInfo, text="Mostrar Informacion", bg_color="gray60", fg_color="gray50", width=392, height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15), command= lambda:self.mostrarDatos(controller))
        bottonsito2.place(x=240, y=52)
        #el resto de botones, que no hacen nada por el momento
        bottonsito3 = CTkButton(bordeInfo, text="Consultar Saldo", bg_color="gray60", fg_color="gray50", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15))
        bottonsito3.place(x=240, y=102)

        bottonsito4 = CTkButton(bordeInfo, text="Realizar Retiro", bg_color="gray60", fg_color="gray50", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15))
        bottonsito4.place(x=240, y=152)

        bottonsito5 = CTkButton(bordeInfo, text="Transferencia entre cuentas", bg_color="gray60", fg_color="gray50", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15))
        bottonsito5.place(x=240, y=202)
        #boton para volver, ojo, tiene SalirPagina()
        Buttona = tk.Button(self, text="Volver", font=("Arial", 15), command=lambda: self.salirPagina())
        Buttona.place(x=50, y=600)

    #mostrarDatos, funcion que necesita el argumento controller
    def mostrarDatos(self, controller):
        self.controller = controller
        #escribimos todos los datos llamando a controller.  que es igual a Aplicacion., estamos llamando las variables de Aplicacion
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

    #al salir de la pagina, debemos eliminar los Label que creamos en MostrarInformacion
    def salirPagina(self):
        self.controller.show_frame(MenuOpciones)
        self.Label6.destroy()
        self.Label5.destroy()
        self.Label4.destroy()
        self.Label3.destroy()
        self.Label2.destroy()
        self.Label.destroy()

#Clase Aplicacion, donde creamos la ventana por la que pasaran los frames
class Aplicacion(tk.Tk):
    #variables que usaremos
    FisiCoins = 0
    codigoEstudiante = 0
    nombreEstudiante = ""
    correoEstudiante = ""
    creditos = 0
    tipoEstudiante = ""

    #inicializamos la clase
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self.state hace referencia si misma, a Aplicacion, y "zoomed" hace que este en pantalla completa al iniciar
        self.state("zoomed")
        #el titulo de la ventana
        self.title("Aplicacion De Pagos")

        #una ventana en blanco
        #falta revisar esta parte, ojo :u
        window = tk.Frame(self)
        window.pack(fill="both", expand=True)
        window.grid_rowconfigure(0, minsize=700)
        window.grid_columnconfigure(0, minsize=1365)


        #creamos un diccionario llamado frames
        #el diccionario te permite almacenar distintos valores, no solo tipos de datos primitivos
        #como el array en c++, pero con mas capacidades
        self.frames = {}
        for F in (Login, MenuOpciones, InfoUsuario): #hacemos que F recorra Login, MenuOpciones, InfoUsuario (hara 3 vueltas xd)
            frame = F(window, self)  # esta parte de aca inicializa las subclases de Aplicacion
            #de esta manera: en la primera vuelta F sera Login, lo que hara
            #frame = Login(window, self) esto creara el Login, lo mismo pasara en la 2da y 3ra vuelta
            #ahora almacenamos frame en el diccionario frames
            self.frames[F] = frame
            #frame.grid es para q funcione xd, no tiene mucha explicacion, si lo quitas no corre
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Login) #llamamos a showframe(Login) para que al correr el programa, Login sea lo primero en aparecer

    #creamos la funcion show_frame, que traera al frente el frame que queramos
    def show_frame(self, page):
        #al llamar la funcion le daremos el parametro "page", que sera para indicar a que frame queremos cambiar
        frame = self.frames[page]
        #.tkraise hace que el frame se levante sobre el que tenemos en pantalla
        frame.tkraise()

    #llamaremos a la funcion modificarFisicoins cuando lo necesitemos
    #le debemos pasar el nuevoValor como parametro para ser la nueva FisiCoins
    def modificarFisiCoins(self, nuevoValor):
        self.FisiCoins = nuevoValor

#if __name == '__main__' hace que solo se ejecute lo que esta dentro del if
#es como un int main()
if __name__ == '__main__':
    #creamos app, un objeto que sera clase Aplicacion, al hacer esto
    #inicializara Aplicacion, y Aplicacion inicializara las subclases que tiene dentro
    app = Aplicacion()
    #.mainloop para que la ventana no se cierre
    app.mainloop()
