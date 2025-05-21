# Sistema de Reservas para Restaurantes 🍽️

![Interfaz del Sistema](https://via.placeholder.com/800x400.png?text=Captura+del+Sistema+de+Reservas)

Aplicación de escritorio para gestión de reservas en restaurantes, desarrollada en Python con:
- **Tkinter** (Interfaz gráfica)
- **SQLite** (Base de datos)
- **SMTP** (Notificaciones por email)

## 📦 Requisitos Previos
- Python 3.8 o superior
- pip (Gestor de paquetes de Python)
- Conexión a internet (para notificaciones por email)

## 🚀 Instalación Rápida
1. **Descargar el proyecto**:
   ```bash
   git clone https://github.com/tu-usuario/sistema-reservas.git
   cd sistema-reservas
Instalar dependencias:

bash
pip install -r requirements.txt
Ejecutar la aplicación:

bash
python sistema_reservas.py
🔑 Credenciales de Acceso
Usuario: admin

Contraseña: admin (cambiar en producción)

📧 Configuración de Notificaciones por Email
Paso 1: Modificar el código
Edita estas líneas en sistema_reservas.py:

python
self.email_from = "tucorreo@gmail.com"  # Tu dirección Gmail
self.email_pass = "contraseña-de-app"   # Contraseña de aplicación (ver Paso 2)
Paso 2: Generar contraseña de aplicación
Activa Verificación en dos pasos en tu cuenta Google

Crea una Contraseña de aplicación:

Ve a Contraseñas de aplicación

Selecciona: Correo + Windows Computer

Copia la contraseña generada (16 dígitos)

Configuración Gmail

🖥️ Funcionalidades Principales
Módulo	Descripción
Clientes	Registrar, editar y eliminar clientes
Reservas	Gestionar reservas con verificación de disponibilidad
Disponibilidad	Visualizar mesas libres en tiempo real
Historial	Consultar reservas pasadas y filtros
🐛 Solución de Problemas Comunes
Error de autenticación SMTP
log
smtplib.SMTPAuthenticationError: (535, '5.7.8 Username and Password not accepted...')
Solución:

Usar contraseña de aplicación (no la contraseña normal de Gmail)

Verificar que la verificación en 2 pasos esté activada

Mesas no aparecen disponibles
Ejecutar la aplicación como administrador

Verificar que el archivo restaurante.db tenga permisos de escritura

📂 Estructura del Proyecto
sistema_reservas/
├── sistema_reservas.py    # Código principal
├── restaurante.db         # Base de datos (se crea automáticamente)
├── requirements.txt       # Dependencias (tkcalendar)
└── README.md              # Este archivo
⚠️ Notas de Seguridad
Cambiar las credenciales por defecto (admin/admin)

No compartir la contraseña de aplicación de Gmail

Usar entorno virtual para producción

📄 Licencia
MIT License - Libre para uso y modificación

¡Listo para gestionar tu restaurante! 🎉
Para soporte técnico: contacto@tudominio.com