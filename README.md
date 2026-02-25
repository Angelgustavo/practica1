# PRACTICA1G4
CONSTRUCCIÓN DE API 
- Código fuente del API(app.py)
- Base de datos  SQLite( Basedatos.py)
Funcionalidades Implementadas
- GET/usuarios: consulta total de usuarios registrados.
![base de datos local host](db_lh.png)
![local host](db_lh_por_usuario.png)
- POST/usuarios: permite registrar usuarios
![prueba curl local host](curl_lh.png)
- Validación de usuarios:
    -  Validación de datos (cedula de 10 digitos,entero, cedulas ya existentes)
    -  Manejo de errores 400, 404, 409
![prueba curl error](db_lh_iderror.png)
![prueba curl id ya registrado](db_lh_idyaregistrado.png)  
    -  Respuesta en formato JSON
Creatividad:
- Conexión con API externa telegram (@apiUIDEG4bot)
![Conexión Telegram](conexion_telegram.jpg) 
Uso de branches
![Branch dev](branch_dev.png)
Conenerización
![Docker](docker.png)
![creación de imagen y contenedor](le_docker.png)
Despliegue Cloud
![contenedor levantado](con_levantado.jpg)
![url generada](url.publica.jpg)
![pruebas curl url publica](pruebas_curl_up.png)
![base de datos url publica](db_up.png)
