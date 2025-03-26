# 🚀 Trabajo-clase 🚀

Este repositorio contiene el trabajo que nos asignó nuestro profesor en clase. El objetivo es configurar y desplegar una aplicación web utilizando Docker Compose.

La aplicación constará de cuatro servicios: una aplicación web, una base de datos PostgreSQL, un servicio de caché Redis y un servidor web Nginx.

## 📋 Objetivo

El objetivo de este proyecto es que los alumnos configuren y desplieguen una aplicación web utilizando Docker Compose. La aplicación constará de cuatro servicios:

1. Una aplicación web
2. Una base de datos PostgreSQL
3. Un servicio de caché Redis
4. Un servidor web Nginx

## 🛠️ Tecnologías

- **Python**: 62.6%
- **Dockerfile**: 37.4%

## 📋 Requisitos

### Servicio Web

- Debe ser una aplicación web simple escrita en Python utilizando Flask.
- El código de la aplicación debe estar en un archivo `app.py`.
- La aplicación debe escuchar en el puerto 5000.
- El contenedor debe construirse a partir de un Dockerfile.
- Montar el código de la aplicación desde el sistema de archivos local.

### Base de Datos (PostgreSQL)

- Utilizar la imagen oficial de PostgreSQL.
- Configurar las variables de entorno para el usuario (`user`), la contraseña (`password`) y la base de datos (`mydatabase`).
- Exponer el puerto 5432.
- Montar un volumen para persistir los datos de la base de datos en `/var/lib/postgresql/data`.

### Servicio de Caché (Redis)

- Utilizar la imagen oficial de Redis.
- Exponer el puerto 6379.

### Servidor Web (Nginx)

- Utilizar la imagen oficial de Nginx.
- Configurar Nginx como un proxy inverso para la aplicación web.
- Exponer el puerto 80.
- Utilizar un archivo de configuración `nginx.conf`.
- Montar el archivo de configuración desde el sistema de archivos local en `/etc/nginx/nginx.conf`.

## 🚀 Uso

1. Clona este repositorio:
    ```sh
    git clone https://github.com/AlfaSenpai/Trabajo-clase.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd Trabajo-clase
    ```
3. Construye y despliega los servicios utilizando Docker Compose:
    ```sh
    docker-compose up --build
    ```

Tu aplicación estará disponible en `http://localhost`.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Sigue estos pasos para contribuir:

1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/mi-feature`).
3. Realiza los cambios necesarios y haz commit (`git commit -am 'Añadir mi feature'`).
4. Realiza un push a la rama (`git push origin feature/mi-feature`).
5. Abre un Pull Request.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 📞 Contacto

Para cualquier consulta, puedes contactarme a través de [GitHub](https://github.com/AlfaSenpai) o traves de mi pagina alfonsofernandeztalaero.es.

¡Gracias por visitar el proyecto! 🎉
