# docker-ejemplo 🚀

> **Ejemplo simple de sistema de gestión de tareas en Python, ideal para practicar Docker y pruebas de perfil operacional en TICS317 - Arquitectura de Sistemas.**

---

## 📂 Archivos principales

| Archivo                | Descripción                                                        |
|------------------------|--------------------------------------------------------------------|
| `main.py`              | Aplicación principal para agregar y listar tareas (`tasks.json`).   |
| `Dockerfile`           | Archivo para contenerizar la aplicación.                           |
| `test_operacional.py`  | Script que simula varios usuarios agregando tareas (prueba PoC).   |

---

## 🖥️ Uso local

1. Ejecuta la aplicación:
   ```sh
   python main.py
   ```
2. Sigue las instrucciones para agregar o listar tareas.

---

## 🐳 Uso con Docker

1. **Construye la imagen Docker:**
   ```sh
   docker build -t docker-ejemplo .
   ```
2. **Ejecuta el contenedor:**
   ```sh
   docker run -it -v "$(pwd)":/app docker-ejemplo
   ```
   > Esto permite que el archivo `tasks.json` se guarde en tu máquina local.

---

## 🧪 Prueba operacional

Para simular varios usuarios agregando tareas y verificar el perfil operacional:

- Ejecuta el script de prueba:
  ```sh
  python test_operacional.py
  ```
- O dentro del contenedor:
  ```sh
  docker run -it -v "$(pwd)":/app docker-ejemplo python test_operacional.py
  ```

> El script simula **3 usuarios**, cada uno agregando **5 tareas**. Al final muestra el total de tareas registradas y sus descripciones.

---

## 📝 Notas

- Puedes modificar el número de usuarios o tareas en `test_operacional.py`.
- Este ejemplo es ideal para practicar **despliegue**, **persistencia de datos** y **pruebas de perfil operacional** usando Docker.
- Si tienes dudas, revisa la documentación oficial de [Docker](https://docs.docker.com/).

---

## 📚 Recursos útiles

- [Guía oficial de Docker para Python](https://docs.docker.com/guides/python/containerize/)
- [Full Stack Python: Docker](https://www.fullstackpython.com/docker.html)

---

## ✅ Checklist para tu entrega

- [x] Código funcional
- [x] Dockerfile creado y probado
- [x] Prueba operacional documentada
- [x] README claro y atractivo 