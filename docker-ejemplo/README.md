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

## 🐳 Instalación de Docker

### macOS

1. Descarga e instala [Docker Desktop para Mac](https://www.docker.com/products/docker-desktop/).
2. Abre el archivo `.dmg` descargado y arrastra Docker a tu carpeta de Aplicaciones.
3. Inicia Docker Desktop desde Aplicaciones y espera a que el icono de Docker esté activo en la barra de menú.
4. Verifica la instalación abriendo una terminal y ejecutando:
   ```sh
   docker --version
   ```

### Linux (Ubuntu)

1. Actualiza los paquetes existentes:
   ```sh
   sudo apt update
   ```
2. Instala los paquetes necesarios:
   ```sh
   sudo apt install apt-transport-https ca-certificates curl software-properties-common
   ```
3. Agrega la clave GPG oficial de Docker:
   ```sh
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```
4. Agrega el repositorio de Docker:
   ```sh
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```
5. Instala Docker Engine:
   ```sh
   sudo apt update
   sudo apt install docker-ce
   ```
6. Verifica la instalación:
   ```sh
   docker --version
   ```

### Windows

1. Descarga e instala [Docker Desktop para Windows](https://www.docker.com/products/docker-desktop/).
2. Ejecuta el instalador y sigue los pasos.
3. Reinicia tu PC si es necesario.
4. Abre Docker Desktop y espera a que esté activo.
5. Verifica la instalación abriendo PowerShell o CMD y ejecutando:
   ```sh
   docker --version
   ```

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

---

## 🛠️ Resolución de errores comunes

### 1. ModuleNotFoundError: No module named 'requests'

**Causa:** Falta instalar la librería `requests` dentro del contenedor Docker.

**Solución:**
- Asegúrate de tener un archivo `requirements.txt` con el contenido:
  ```
  requests
  ```
- Modifica el `Dockerfile` para instalar las dependencias:
  ```dockerfile
  COPY requirements.txt /app/
  RUN pip install --no-cache-dir -r requirements.txt
  ```

---

### 2. ERROR: docker: 'docker buildx build' requires 1 argument

**Causa:** Olvidaste poner el punto (`.`) al final del comando `docker build`.

**Solución:**
- Usa el comando completo:
  ```sh
  docker build -t docker-ejemplo .
  ```
  (¡No olvides el punto al final!)

---

### 3. sudo: apt: command not found

**Causa:** Estás usando comandos de Linux (Ubuntu) en macOS, donde no existe `apt`.

**Solución:**
- En macOS, instala Docker siguiendo solo los pasos de la sección "macOS" del README. No uses comandos `apt` en Mac.

--- 