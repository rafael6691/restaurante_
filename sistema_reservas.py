import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import smtplib
from datetime import datetime
from tkcalendar import DateEntry

class SistemaReservas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Reservas - Restaurante")
        self.root.geometry("1000x600")
        
        # Conexión a la base de datos
        self.conn = sqlite3.connect('restaurante.db')
        self.crear_tablas()
        self.insertar_mesas_iniciales()
        
        # Configuración de email (EDITAR CON TUS DATOS)
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.email_from = "raortiz1209@gmail.com"
        self.email_pass = "344901@=$"
        
        # Interfaz de login
        self.frame_login = ttk.Frame(self.root)
        ttk.Label(self.frame_login, text="Usuario:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_usuario = ttk.Entry(self.frame_login)
        self.entry_usuario.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(self.frame_login, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_contraseña = ttk.Entry(self.frame_login, show="*")
        self.entry_contraseña.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Button(self.frame_login, text="Ingresar", command=self.validar_login).grid(row=2, columnspan=2, pady=10)
        self.frame_login.pack(pady=100)
    
    def crear_tablas(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes (
                        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        correo TEXT UNIQUE NOT NULL,
                        telefono TEXT)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Mesas (
                        id_mesa INTEGER PRIMARY KEY AUTOINCREMENT,
                        capacidad INTEGER NOT NULL,
                        estado TEXT DEFAULT 'disponible')''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS Reservas (
                        id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_cliente INTEGER,
                        id_mesa INTEGER,
                        fecha TEXT NOT NULL,
                        hora TEXT NOT NULL,
                        personas INTEGER NOT NULL,
                        estado TEXT DEFAULT 'confirmada',
                        FOREIGN KEY(id_cliente) REFERENCES Clientes(id_cliente),
                        FOREIGN KEY(id_mesa) REFERENCES Mesas(id_mesa))''')
        self.conn.commit()
    
    def insertar_mesas_iniciales(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Mesas")
        if cursor.fetchone()[0] == 0:
            capacidades = [2, 2, 4, 4, 6, 6, 8]
            for cap in capacidades:
                cursor.execute("INSERT INTO Mesas (capacidad) VALUES (?)", (cap,))
            self.conn.commit()
    
    def validar_login(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        if usuario == "admin" and contraseña == "admin":
            self.mostrar_interfaz_principal()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
    
    def mostrar_interfaz_principal(self):
        self.frame_login.pack_forget()
        
        # Menú lateral
        self.menu_frame = ttk.Frame(self.root, width=200)
        self.menu_frame.pack(side="left", fill="y")
        
        botones = [
            ("Clientes", self.mostrar_clientes),
            ("Reservas", self.mostrar_reservas),
            ("Disponibilidad", self.mostrar_disponibilidad),
            ("Historial", self.mostrar_historial),
            ("Cerrar Sesión", self.cerrar_sesion)
        ]
        
        for texto, comando in botones:
            ttk.Button(self.menu_frame, text=texto, command=comando, width=20).pack(pady=5)
        
        # Área de contenido
        self.contenido_frame = ttk.Frame(self.root)
        self.contenido_frame.pack(side="right", fill="both", expand=True)
    
    # Resto de métodos (gestión de clientes, reservas, etc.) 
    # [Se mantiene la lógica completa de gestión como en el código original]

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaReservas(root)
    root.mainloop()