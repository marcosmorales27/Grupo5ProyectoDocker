# Proyecto docker grupo 5
Arquitectura de Microservicios: Frontend, Backend, Base de Datos y Autenticación.

## Instrucciones de Instalación y Ejecución

Siga estos pasos en orden estricto para levantar el proyecto:

1. Descargar y preparar
1. Clone el repositorio o descargue la carpeta.
2. Abra su terminal (CMD o PowerShell).
3. Importante: Navegue hasta entrar en la carpeta del proyecto (donde se encuentra el archivo `docker-compose.yml`).

2. Ejecutar los contenedores
Ejecute el siguiente comando en la terminal para construir y levantar los servicios:
docker compose up --build -d

probar los servicios en navegador

1. Frontend Web servicios 1, 2 y 3 
Ingrese a la siguiente dirección para ver la interfaz gráfica que consume el API y la Base de Datos: http://localhost:8080

2. Servicio de Autenticación servicio 4
Para verificar que el servicio de seguridad responde: http://localhost:5000

3. Administración de Base de Datos
Para ver los datos reales guardados en PostgreSQL, ingrese a: http://localhost:8081

Motor (System): PostgreSQL

Servidor (Server): servicio-2

Usuario (Username): usuario

Contraseña (Password): secreto

Base de datos (Database): mibasedatos
