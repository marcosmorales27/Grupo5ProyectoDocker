# Proyecto docker grupo 5
Arquitectura: frontend, backend, base de datos y autenticación.

## Instrucciones de instalación y ejecución

1. Descargar y preparar
1. Clone el repositorio o descargue la carpeta.
2. Abre CMD.
3. Importante: Navegue hasta entrar en la carpeta del proyecto (donde se encuentra el archivo `docker-compose.yml`).

2. Ejecutar los contenedores
Ejecute el siguiente comando en la terminal para construir los servicios:
docker compose up --build -d

Probar los servicios en navegador

1. Frontend Web servicios 1, 2 y 3 
Ingrese a la siguiente dirección para ver el API y la Base de Datos: http://localhost:8080

2. Servicio de autenticación servicio 4
Para verificar que el servicio de seguridad: http://localhost:5000

3. Administración de base de datos
Para ver los datos guardados en PostgreSQL, ingrese a: http://localhost:8081

Motor (System): PostgreSQL

Servidor (Server): servicio-2

Usuario (Username): usuario

Contraseña (Password): secreto

Base de datos (Database): mibasedatos
