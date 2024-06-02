import tkinter as tk
from tkinter import Tk, Label, Button, Entry, Frame, messagebox, mainloop

import customtkinter
from PIL import Image, ImageTk
import pandas as pd
from customtkinter import *
#importamos las librerias tk, customtkinter, pillow y pandas

#funcion para eliminar los widgets dentro de nuestro labelframe (limpiar los datos que aparecen al presionar un botton)
def eliminar_widgets_labelframe(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#Clase Login, clase hija de la clase Aplicacion
class Login(tk.Frame):

    #Inicializamos la clase, self para referirse a si mismo (el login) y controller se refiere a su clase padre (Aplicacion)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Colocamos el fondo de san marcos
        fondounmsm = ImageTk.PhotoImage(file="bgr.png")
        rutaicono = "logofisi.png"
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
        T2 = CTkEntry(borde, show="*", placeholder_text="Contraseña", font=("Microsoft YaHei UI Light", 15), width=300, height=35, text_color="gray90", bg_color="gray22", fg_color="gray26")
        T2.place(x=530, y=390)

        #un boton next para pasar a la siguiente ventana rapido, para testeos, no necesitaras ingresar el usuario
        nextsito = tk.Button(borde, text="Next", font=("Microsoft YaHei UI Light", 35), command=lambda: controller.show_frame(MenuOpciones))
        nextsito.place(x=1150, y=550)

        #definimos la funcion entrar, que se activara al presionar el boton Ingresar
        def entrar():

            try: #Intentemos leer el archivo excel
                df = pd.read_excel('loginData.xlsx')
                if (str(T1.get()) in df["Correo"].values): #revisamos si el texto en T1 esta en la columna "Correo" del excel
                    if str(df[df["Correo"] == str(T1.get())]["Contraseña"].iloc[0]) == str(T2.get()): #sacamos el numero de la fila donde se encuentra
                        # nuestro Correo, sacamos el Codigo de alumno de esa fila y lo igualamos al T2 escrito por el usuario
                        #los messagebox son cuadros emergentes al que les pones un titulo y mensaje
                        messagebox.showinfo("Acceso Correcto", "Has ingresado")
                        #la variable numFila, guardara el numero de la fila donde se encuentra nuestro usuario en el excel
                        numFila = df[df["Correo"] == str(T1.get())]
                        #hacemos que las variables de la clase Aplicacion guarden los datos que estan en el excel
                        controller.creditos = str(numFila["Creditos"].iloc[0])
                        controller.nombreEstudiante = numFila["Nombre"].iloc[0]
                        controller.dni = numFila["DNI"].iloc[0]
                        controller.FisiCoins = numFila["Dinero"].iloc[0]
                        controller.tipoEstudiante = (numFila["Tipo"].iloc[0])
                        controller.codigoEstudiante = numFila["Codigo"].iloc[0]
                        controller.correoEstudiante = str(T1.get())
                        controller.contraseña = str(numFila["Contraseña"].iloc[0])
                        #como ya se verifico que es correcto el correo y codigo, borramos lo escrito en los campos T1 y T2
                        T1.delete(0, tk.END)
                        T2.delete(0, tk.END)
                        #pasamos al frame MenuOpciones
                        controller.show_frame(MenuOpciones)
                    else:
                        messagebox.showinfo("Acceso Incorrecto", "Contraseña incorrecta")
                else:
                    messagebox.showinfo("Acceso Incorrecto", "Correo no existe")
            except FileNotFoundError:
                messagebox.showerror("Error", "El archivo Excel no se encuentra")
        #el boton donde dice ingresar :p
        BTN1 = CTkButton(borde, bg_color="gray17", fg_color="SpringGreen2", text="Ingresar", corner_radius=16, text_color="gray90", width=300, height=45, font=("Arial", 20), command=entrar)
        BTN1.place(x=530, y=465)


#clase MenuOpciones, clase hija de la clase Aplicacion
#clase MenuOpciones, clase hija de la clase Aplicacion
class MenuOpciones(tk.Frame):

    #Inicializamos la clase, self para referirse a si mismo (el login) y controller se refiere a su clase padre (Aplicacion)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #efecto de sobra radial

        #hacemos un bordemenu, con la misma funcionalidad que el borde de Login xd
        bordeMenu = tk.LabelFrame(self, bg='#05171d', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeMenu.pack(fill="both", expand=True)



        #partes del diseño, los rectangulos morados :P

        #rectanculos verticales
        label_3 = CTkLabel(bordeMenu, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=8, width=380,
                           height=240)
        label_3.place(x=505, y=22)
        label_4 = CTkLabel(bordeMenu, fg_color="#01213a", bg_color="#88d398", text="", corner_radius=8, width=370,
                           height=240)
        label_4.place(x=510, y=25)

        textito = CTkLabel(bordeMenu, text="MENÚ", font=("Nunito", 30), width=300, height=35, text_color="#e3f473", bg_color="#01213a")
        textito.place(x=550, y=31)
        #rectanculos horizontales
        label_2 = CTkLabel(bordeMenu, fg_color="#88d398", text="", corner_radius=10, width=1166,
                           height=530)
        label_2.place(x=92, y=75)
        label_1 = CTkLabel(bordeMenu, fg_color="#01213a", bg_color="#88d398", text="", corner_radius=10, width=1160,
                            height=520)
        label_1.place(x=95, y=80)

        #insertamos la imagen de la fisicoin
        burrito_path = os.path.join(os.path.dirname(__file__), 'FISICOIN.png')
        image = customtkinter.CTkImage(light_image= Image.open(burrito_path), size=(210, 147))
        image_label = customtkinter.CTkLabel(bordeMenu, bg_color="#01213a", image=image, text='')
        image_label.place(x=570, y=265)

        #las diferentes tipos de opciones, hover_color cambiar el color cuando el mouse este encima
        #buttoon, tiene un command para ir a Operaciones Bancarias

            #Borde operaciones bancarias
        label_2 = CTkLabel(bordeMenu, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=12, width=534,
                           height=145)
        label_2.place(x=115, y=105)
            #Boton OPERACIONES BANCARIAS
        buttoon = CTkButton(bordeMenu, width=530, bg_color="#88d398", text_color="white", corner_radius=12, height=135, fg_color="#114b5f", hover_color="darkcyan",text="Operaciones Bancarias", font=("Nunito", 35), command=lambda: controller.show_frame(InfoUsuario))
        buttoon.place(x=117, y=110)
             #Borde pagar servicios
        label_2 = CTkLabel(bordeMenu, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=12, width=534,
                           height=145)
        label_2.place(x=688, y=105)
             #Boton PAGAR SERVICIOS
        buttoon1 = CTkButton(bordeMenu, width=530, bg_color="#88d398", text_color="white", corner_radius=12, height=135,  fg_color="#114b5f", hover_color="darkcyan", text="Pagar Servicios", font=("Nunito", 35))
        buttoon1.place(x=690, y=110)
             #Boton PROXIMAMENTE QUIOSCO
        buttoon2 = CTkButton(bordeMenu, width=420, bg_color="#01213a", fg_color="#575f61", text_color="black", corner_radius=32, height=150, text="Proximamente:\nQuiosco Virtual", font=("Microsoft YaHei UI Light", 30))
        buttoon2.place(x=120, y=265)
             #Boton PROXIMAMENTE CASINO
        buttoon3 = CTkButton(bordeMenu, width=420, bg_color="#01213a", fg_color="#575f61", text_color="black", corner_radius=32, height=150, text="Proximamente:\n Casino", font=("Microsoft YaHei UI Light", 30))
        buttoon3.place(x=810, y=265)
        #Borde Configuracion
        label_2 = CTkLabel(bordeMenu, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=12, width=534,
                           height=145)
        label_2.place(x=115, y=425)
        #Boton CONFIGURACION
        buttoon4 = CTkButton(bordeMenu, width=530, bg_color="#88d398", text_color="white", corner_radius=12, height=135, fg_color="#114b5f",  hover_color="darkcyan", text="Configuracion", font=("Nunito", 35), command=lambda: controller.show_frame(Config))
        buttoon4.place(x=117, y=430)

        #Borde Inversiones
        label_2 = CTkLabel(bordeMenu, fg_color="#88d398", bg_color="#01213a", text="", corner_radius=12, width=534,
                           height=145)
        label_2.place(x=688, y=425)

        #Boton INVERSIONES
        buttoon5 = CTkButton(bordeMenu, width=530, bg_color="#88d398", text_color="white", corner_radius=12, height=135,  fg_color="#114b5f", hover_color="darkcyan", text="Prestamos e Inversiones", font=("Nunito", 35))
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
        bordeInfo = tk.LabelFrame(self, bg='#010f4c', bd=10, font=("Microsoft YaHei UI Light", 15))
        bordeInfo.pack(fill="both", expand=True)

        #los rectangulos gris y azul, debajo de donde estar el texto xd
        label_bg = CTkLabel(bordeInfo, fg_color="#0026a3", bg_color="#010f4c", text="", corner_radius=16, width=444, height=590)
        label_bg.place(y=30, x=687)
        label_bg1 = CTkLabel(bordeInfo, fg_color="#0084f1", bg_color="#0026a3", text="", corner_radius=16, width=420, height=570)
        label_bg1.place(y=40, x=699)
        label_bg2 = CTkLabel(bordeInfo, fg_color="#0026a3", bg_color="#010f4c", text="", corner_radius=16, width=444, height=590)
        label_bg2.place(y=30, x=215)
        label_bg3 = CTkLabel(bordeInfo, fg_color="#0084f1", bg_color="#0026a3", text="", corner_radius=16, width=420, height=570)
        label_bg3.place(y=40, x=227)

        #boton, que activa la funcion MostrarInformacio
        bottonsito2 = CTkButton(bordeInfo, text="Consultar Saldo", bg_color="#0084f1", fg_color="#4bb4f6", width=392, height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15), command= lambda:self.consultarSaldo(controller, respuestaLabelFrame))
        bottonsito2.place(x=240, y=52)
        #el resto de botones, que no hacen nada por el momento
        bottonsito3 = CTkButton(bordeInfo, text="Realizar deposito", bg_color="#0084f1", fg_color="#4bb4f6", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15))
        bottonsito3.place(x=240, y=102)

        bottonsito4 = CTkButton(bordeInfo, text="Realizar Retiro", bg_color="#0084f1", fg_color="#4bb4f6", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15))
        bottonsito4.place(x=240, y=152)

        bottonsito5 = CTkButton(bordeInfo, text="Transferencia entre cuentas", bg_color="#0084f1", fg_color="#4bb4f6", width=392,
                                height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 15))
        bottonsito5.place(x=240, y=202)
        #boton para volver, ojo, tiene SalirPagina()
        Buttona = tk.Button(self, text="Volver", font=("Arial", 15), command=lambda: self.salirPagina(respuestaLabelFrame))
        Buttona.place(x=50, y=600)

        #este nuevo labelframe esta dentro de nuestro labelframe BordeInfo
        #su funcion es que dentro de este esten todos los widgets de nuestra opciones, consultar saldo, realizar retiro, etc
        #almacenar los widgets que generen nuestros botones dentro de un labelframe nos facilitara el borrarlos cuando sea necesario
        #con solo llamar a lafuncion eliminar_widgets_labelframe ,podras borrar todos los widgets que generaste dentro de tu botton
        respuestaLabelFrame = tk.LabelFrame(bordeInfo, text="", height=550, width=400, bg="#0084f1", foreground="gray60",
                                            bd=0, font=("Microsoft YaHei UI Light", 15))
        respuestaLabelFrame.place(x=708, y=53)
        #este labelframe es el segundo rectangulo, a la derechad de las opciones

    #mostrarDatos, funcion que necesita el argumento controller
    def consultarSaldo(self, controller, frame):
        eliminar_widgets_labelframe(frame)
        #limpiamos lo que este dentro de nuestro labelframe, antes de generar nuevos widgets
        
        self.controller = controller
        #escribimos todos los datos llamando a controller.  que es igual a Aplicacion., estamos llamando las variables de Aplicacion
        self.Label = tk.Label(frame, fg="white", bg="gray60", text="Codigo de estudiante: "+str(controller.codigoEstudiante), font=("Microsoft YaHei UI Light", 12))
        self.Label.place(x=0, y=0)
        self.Label2 = tk.Label(frame, fg="white", bg="gray60", text="Correo Institucional: "+controller.correoEstudiante, font=("Microsoft YaHei UI Light", 12))
        self.Label2.place(x=0, y=50)
        self.Label3 = tk.Label(frame, fg="white", bg="gray60", text="Creditos: "+str(controller.creditos), font=("Microsoft YaHei UI Light", 12))
        self.Label3.place(x=0, y=100)
        self.Label4 = tk.Label(frame, fg="white", bg="gray60", text="Nombre del Estudiante: "+controller.nombreEstudiante, font=("Microsoft YaHei UI Light", 11))
        self.Label4.place(x=0, y=150)
        self.Label5 = tk.Label(frame, fg="white", bg="gray60", text="Tipo de Estudiante: " + controller.tipoEstudiante, font=("Microsoft YaHei UI Light", 12))
        self.Label5.place(x=0, y=200)
        self.Label6 = tk.Label(frame, fg="white", bg="gray60", text="FisiCoins: " + str(controller.FisiCoins), font=("Microsoft YaHei UI Light", 12))
        self.Label6.place(x=0, y=250)

    #al salir de la pagina, debemos eliminar los Label que creamos en MostrarInformacion
    def salirPagina(self, frame):
        eliminar_widgets_labelframe(frame) #eliminamos los widgets antes de salir del frame
        self.controller.show_frame(MenuOpciones) #volvemos al menu de opciones


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

        self.nuevaContraLabelFrame = tk.LabelFrame(bordeContra, text="", height=250, width=800, bg="#25e8e8", foreground="gray60",
                                            bd=0, font=("Microsoft YaHei UI Light", 15))
        self.nuevaContraLabelFrame.place(x=230, y=240)

        # boton para volver, ojo, tiene SalirPagina()
        Buttona = tk.Button(bordeContra, text="Volver", font=("Arial", 15), command=lambda: self.salirPagina(self.nuevaContraLabelFrame))
        Buttona.place(x=50, y=600)

        bottonNuevoFrame = CTkButton(bordeContra, text="Validar", text_color="black", bg_color="#25e8e8", fg_color="gray60",
                width=100, height=40, corner_radius=8, font=("Microsoft YaHei UI Light", 16),
                command= lambda: self.ValidarContraseñaAntigua(controller))
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
             if len(str(self.C2.get())) >= 8:
                if (self.C2.get()).isalnum():
                    if (self.C2.get()) == (self.C3.get()):
                        df = pd.read_excel('loginData.xlsx')
                        df['Contraseña'] = df['Contraseña'].astype(str)
                        numFila = df[df["Contraseña"] == str(self.C1.get())]
                        indiceFila = numFila.index[0]
                        df.loc[indiceFila, "Contraseña"] = str(self.C2.get())
                        df.to_excel("LoginData.xlsx", index=False)
                        controller.contraseña = str(self.C2.get())
                        messagebox.showinfo("Contraseña cambiada!", "Su nueva contraseña es: {}".format(controller.contraseña))
                        eliminar_widgets_labelframe(frame)
                    else:
                        messagebox.showinfo("Error", "La confirmación de la nueva contraseña no coincide")
                else:
                    messagebox.showinfo("Error", "La nueva contraseña solo debe contener números y letras.")
             else:
                messagebox.showinfo("Error", "La nueva contraseña debe tener al menos 8 caracteres.")


        # BOTON para cambiar la contraseña
        cambiarcontra = CTkButton(self, text="Enviar", text_color="black", bg_color="#25e8e8", fg_color="gray60",
                                  width=392,
                                  height=45, corner_radius=8, font=("Microsoft YaHei UI Light", 16), command= enviar)
        cambiarcontra.place(x=500, y=420)

    # para el boton volver
    def salirPagina(self, frame):
        eliminar_widgets_labelframe(frame)
        self.controller.show_frame(MenuOpciones)

#Clase Aplicacion, donde creamos la ventana por la que pasaran los frames
class Aplicacion(tk.Tk):
    #variables que usaremos
    FisiCoins = 0
    codigoEstudiante = 0
    nombreEstudiante = ""
    correoEstudiante = ""
    creditos = 0
    tipoEstudiante = ""
    contraseña = ""
    dni = 0

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
        for F in (Login, MenuOpciones, InfoUsuario, Config): #hacemos que F recorra Login, MenuOpciones, InfoUsuario (hara 3 vueltas xd)
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
