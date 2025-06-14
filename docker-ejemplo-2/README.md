# docker-ejemplo-2 🚀

> **Nueva arquitectura: Tres contenedores en red interna (un server y dos clients) para simular un entorno distribuido y probar concurrencia real.**

---

## 🏗️ Arquitectura de deployment

Este ejemplo está diseñado para mostrar cómo desplegar una aplicación distribuida usando Docker Compose con una red interna y tres contenedores:

- **server**: Un contenedor que ejecuta un servidor Flask (basado en main.py), expone una API REST para agregar y listar tareas (persistidas en tasks.json).
- **client1**: Un contenedor que ejecuta test_operacional.py, el cual interactúa con el server vía HTTP usando la librería requests. Este cliente emula el envío de 100 tareas concurrentes al servidor.
- **client2**: Otro contenedor idéntico a client1, que también emula el envío de 100 tareas concurrentes al servidor.
- Los tres contenedores se comunican únicamente a través de una red interna de Docker definida por docker-compose, sin exponer puertos al host (a menos que quieras acceder a la API desde fuera para pruebas).

El objetivo es emular un escenario donde dos clientes independientes envían muchas tareas al mismo tiempo al servidor, para verificar si el server es capaz de recibir y guardar todas las tareas sin perder ninguna (por condiciones de carrera, concurrencia, etc).

### Requisitos previos
- Tener instalado Docker y Docker Compose.
- No es necesario exponer puertos a la máquina host, salvo que quieras acceder a la API desde fuera.
- El archivo docker-compose.yml orquesta los tres servicios y la red interna.

### ¿Cómo se crea la red interna?

Cuando ejecutas `docker-compose up`, Docker Compose crea automáticamente una red interna (bridge) exclusiva para los servicios definidos en el archivo `docker-compose.yml`.

- Todos los contenedores definidos (server, client1, client2) se conectan a esa red y pueden comunicarse entre sí usando el nombre del servicio como hostname (por ejemplo, `server:9000`).
- No necesitas crear la red manualmente ni exponer puertos al host (a menos que quieras acceder desde fuera).
- La comunicación entre contenedores es privada y segura dentro de esa red.

Esto permite que los clientes puedan hacer peticiones HTTP al servidor simplemente usando la URL `http://server:9000/` desde su propio contenedor.

---

## 🔄 Cambios de arquitectura respecto al ejemplo original

En esta versión, la arquitectura fue rediseñada para simular un entorno distribuido y robusto, ideal para pruebas de concurrencia y despliegue realista:

- **Separación de responsabilidades:**
  - El código se divide en dos roles principales:
    - **server:** Un contenedor dedicado a ejecutar un servidor Flask que expone una API REST para agregar y listar tareas.
    - **clients (client1 y client2):** Contenedores independientes que ejecutan test_operacional.py, enviando tareas concurrentemente al server vía HTTP.

- **Comunicación por red interna Docker:**
  - Los contenedores se comunican exclusivamente a través de una red interna creada automáticamente por Docker Compose.
  - Los clients acceden al server usando su nombre de servicio como hostname (por ejemplo, `http://server:9000`).

- **API REST y concurrencia real:**
  - El server ya no depende de la entrada por consola, sino que expone endpoints HTTP para recibir tareas desde cualquier cliente.
  - Los clients pueden ejecutarse en paralelo y desde diferentes contenedores, simulando usuarios o sistemas independientes.

- **Motivación de los cambios:**
  - Permitir pruebas de concurrencia y condiciones de carrera en un entorno distribuido real.
  - Facilitar la escalabilidad y la integración con otros sistemas o microservicios.
  - Demostrar buenas prácticas de despliegue y comunicación entre servicios en Docker.

---

## 🏗️ Evolución de arquitectura: Monolítica → Distribuida

A continuación se muestra cómo cambió la arquitectura del sistema:

**Arquitectura Monolítica (original):**

```
+---------------------+
|   test_operacional  |
|     (simula users)  |
+---------------------+
           |
           v (subproceso)
+---------------------+
|      main.py        |
| (agrega/lista tareas|
|   en consola)       |
+---------------------+
           |
           v (escribe/lee)
+---------------------+
|    tasks.json       |
+---------------------+
```

**Arquitectura Distribuida (actual):**

```
+---------------------+      HTTP POST/GET      +---------------------+
|  clientemulator.py  |-----------------------> |   taskserver.py     |
|    (client1)        |                         |   (Flask API)       |
+---------------------+                         +---------------------+
                                                |  acceso seguro a    |
+---------------------+      HTTP POST/GET      |    tasks.json       |
|  clientemulator.py  |-----------------------> |  (persistencia)     |
|    (client2)        |                         +---------------------+
+---------------------+
```

**Resumen:**
- Antes: Todo ocurría en un solo proceso, con acceso directo al archivo.
- Ahora: Los clientes son procesos independientes (incluso en contenedores distintos), que se comunican con el servidor por HTTP, y el servidor es el único que accede al archivo de manera segura.

---

## 📂 Archivos principales

| Archivo                | Descripción                                                        |
|------------------------|--------------------------------------------------------------------|
| `taskserver.py`        | Aplicación principal (servidor Flask) para agregar y listar tareas (`tasks.json`).   |
| `Dockerfile`           | Archivo para contenerizar la aplicación.                           |
| `clientemulator.py`    | Script que simula el envío masivo de tareas desde cada cliente.    |
| `docker-compose.yml`   | Orquestador de los tres servicios y la red interna.                |

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
---

## 🖥️ Uso local (solo para pruebas rápidas)

1. Ejecuta la aplicación:
   ```sh
   python main.py
   ```
2. Sigue las instrucciones para agregar o listar tareas.

---

## 🐳 Uso con Docker Compose (recomendado)

1. **Construye y levanta los servicios:**
   ```sh
   docker-compose up --build
   ```
   Esto levantará el server y ambos clientes en la misma red interna.

2. **Observa los logs:**
   - El server mostrará las tareas que va recibiendo.
   - Cada cliente enviará 100 tareas y mostrará el resultado de sus envíos.

3. **Verifica el resultado:**
   - Al finalizar, deberías ver en el server un total de 200 tareas (100 de cada cliente).
   - Puedes inspeccionar el archivo `tasks.json` dentro del contenedor server para comprobar que no se perdió ninguna tarea.

---

## 🐳 Ingresar a un contenedor en ejecución

Si necesitas ingresar a alguno de los contenedores (por ejemplo, al server para ver el archivo de tareas):

1. **Lista los contenedores activos:**
   ```sh
   docker ps
   ```
2. **Ingresa al contenedor server:**
   ```sh
   docker exec -it docker-ejemplo-2-server-1 /bin/bash
   ```
   (El nombre puede variar según tu configuración de docker-compose.)

3. **Dentro del contenedor server**, puedes ejecutar comandos como:
   - Listar archivos:
     ```sh
     ls
     ```
   - Ver el contenido de tasks.json:
     ```sh
     cat /app/tasks.json
     ```
   - Ejecutar la aplicación principal (si es necesario):
     ```sh
     python /app/main.py
     ```

4. **Para salir** de la terminal del contenedor, escribe "exit" o presiona Ctrl+D.

---

## 🧪 Prueba operacional distribuida

Para simular la concurrencia real y verificar si el server pierde tareas:

- Cada cliente (client1 y client2) enviará 100 tareas al server usando la API REST.
- El server debe recibir y guardar las 200 tareas (100 de cada cliente) en `tasks.json`.
- Al finalizar, revisa el total de tareas registradas en el server.

### Diferencia: ¿Por qué podrían perderse tareas? (Condiciones de carrera y concurrencia)

Cuando varios clientes (contenedores) intentan agregar tareas al mismo tiempo, el servidor debe manejar correctamente la concurrencia. Si dos o más procesos intentan escribir en el archivo `tasks.json` simultáneamente y no hay un mecanismo de protección (como un bloqueo de archivo), pueden ocurrir **condiciones de carrera**.

- **Condición de carrera:** Es un problema que ocurre cuando el resultado de una operación depende del orden o la sincronización de múltiples procesos o hilos. En este caso, si dos clientes escriben al mismo tiempo, una escritura puede sobrescribir a la otra y se pierden tareas.
- **Ejemplo:** Si client1 y client2 envían tareas al mismo tiempo y el servidor no protege el acceso al archivo, puede que solo se guarden algunas de las tareas, y el total final sea menor a la suma esperada (por ejemplo, menos de 200).
- **Solución:** El servidor debe implementar un mecanismo de bloqueo (file lock) para asegurar que solo un proceso escriba en el archivo a la vez, evitando así la pérdida de datos.

**En resumen:**
- Si el servidor maneja bien la concurrencia, no se pierde ninguna tarea.
- Si hay condiciones de carrera, el total de tareas guardadas será menor al esperado.

---

## 🧪 Explicación de la prueba

- **Concurrencia real:**  
  Al tener dos contenedores clientes independientes, ambos pueden enviar tareas al mismo tiempo, simulando un entorno distribuido real.
- **clientemulator.py:**  
  Cada cliente ejecuta este script, que envía 100 tareas al server usando peticiones HTTP (requests).
- **Verificación:**  
  Si el server maneja correctamente la concurrencia y el acceso al archivo, no se perderá ninguna tarea. Si hay problemas de concurrencia, el total será menor a 200.

---

## 📝 Notas

- Puedes modificar el número de tareas enviadas por cada cliente editando `clientemulator.py`.
- Este ejemplo es ideal para practicar **despliegue distribuido**, **persistencia de datos concurrente** y **pruebas de robustez operacional** usando Docker Compose.
- Si tienes dudas, revisa la documentación oficial de [Docker](https://docs.docker.com/).

---

## 📚 Recursos útiles

- [Guía oficial de Docker para Python](https://docs.docker.com/guides/python/containerize/)
- [Full Stack Python: Docker](https://www.fullstackpython.com/docker.html)
- [Documentación de Docker Compose](https://docs.docker.com/compose/)

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

## 🐳 Dockerfile multi-rol y uso con Docker Compose

- El Dockerfile está diseñado para servir tanto al server como a los clientes:
  - Por defecto, ejecuta `python taskserver.py` (el servidor Flask).
  - Cuando se usa en los servicios de cliente, Docker Compose sobreescribe el comando para ejecutar `python clientemulator.py`.
- Así, se reutiliza la misma imagen para todos los servicios, facilitando el mantenimiento y la construcción.
- El archivo `requirements.txt` incluye tanto Flask (para el server) como requests (para los clientes).

En el archivo `docker-compose.yml` se define qué comando ejecuta cada servicio.

---

## 📄 Ejemplo de docker-compose.yml

```yaml
version: '3.8'
services:
  server:
    build: .
    container_name: taskserver
    restart: unless-stopped
    networks:
      - ticsnet
    volumes:
      - ./tasks.json:/app/tasks.json
    # Exponer el puerto solo si quieres acceder desde fuera
    ports:
      - "9000:9000"
  client1:
    build: .
    command: ["python", "clientemulator.py"]
    depends_on:
      - server
    networks:
      - ticsnet
  client2:
    build: .
    command: ["python", "clientemulator.py"]
    depends_on:
      - server
    networks:
      - ticsnet
networks:
  ticsnet:
    driver: bridge
```

- **server**: Levanta el servidor Flask en el puerto 9000 y monta el archivo de tareas para persistencia.
- **client1 y client2**: Ejecutan el emulador de cliente, enviando tareas concurrentemente al server.
- Todos los servicios usan la misma imagen, pero los clientes sobreescriben el comando para ejecutar el emulador.
- Todos los servicios están en la red interna `ticsnet` y pueden comunicarse usando los nombres de servicio.

---

## 🚦 Guía rápida de prueba

1. (Opcional) Limpia el archivo de tareas antes de comenzar:
   ```sh
   echo "[]" > tasks.json
   ```

2. Levanta todos los servicios (server y clientes):
   ```sh
   docker-compose up --build
   ```
   - Observa los logs para ver cómo los clientes envían tareas concurrentemente al server.

3. (Opcional) Ingresa al contenedor del server para inspeccionar el archivo de tareas:
   ```sh
   docker exec -it taskserver /bin/bash
   cat /app/tasks.json
   ```

4. Para salir del contenedor, escribe:
   ```sh
   exit
   ```
   o presiona `Ctrl+D`.

5. (Opcional) Cuando termines, baja todos los servicios:
   ```sh
   docker-compose down
   ```

---

## 👀 Monitoreo y verificación de los contenedores y la red

### 1. Ver los contenedores activos
```sh
docker ps
```

### 2. Ver los logs de todos los servicios en tiempo real
```sh
docker-compose logs -f
```
- Para ver solo los logs de un servicio específico:
  ```sh
  docker-compose logs -f server
  ```

### 3. Verificar que los contenedores están en la red privada
```sh
docker network ls
```
Busca el nombre de la red (por ejemplo, `docker-ejemplo-2_ticsnet`), luego:
```sh
docker network inspect docker-ejemplo-2_ticsnet
```
Verás los contenedores conectados a esa red.

### 4. Ver el estado de los servicios en Compose
```sh
docker-compose ps
```

### 5. (Opcional) Ver los procesos dentro de un contenedor
```sh
docker exec -it taskserver ps aux
```

---

## 🎤 Guía para cápsula de 5 minutos: Explicación de la arquitectura distribuida

### 1. ¿De qué trata el problema?
- Simular un sistema de gestión de tareas donde múltiples clientes agregan tareas concurrentemente a un servidor.
- El objetivo es probar la robustez y la persistencia de datos bajo concurrencia real, como ocurriría en sistemas distribuidos.

### 2. ¿Cómo fue diseñado?
- Se rearquitecturó el sistema original monolítico a una arquitectura distribuida usando Docker Compose.
- Ahora hay tres contenedores:
  - **taskserver.py**: Servidor Flask que expone una API REST para agregar y listar tareas.
  - **clientemulator.py (client1 y client2)**: Clientes que simulan usuarios enviando tareas concurrentemente al server vía HTTP.
- Todos los contenedores se comunican solo por una red interna de Docker.

### 3. ¿Qué mostrar del código o README?
- Abre el README y muestra:
  - El diagrama ASCII de la evolución de arquitectura.
  - La sección de arquitectura de deployment y el ejemplo de docker-compose.yml.
- Abre `taskserver.py` y muestra los endpoints Flask (`/tareas` GET y POST) y el uso de file lock.
- Abre `clientemulator.py` y muestra cómo se envían tareas concurrentemente usando requests y threads.

### 4. ¿Cómo se levanta el sistema?
- (Opcional) Limpia el archivo de tareas:
  ```sh
  echo "[]" > tasks.json
  ```
- Levanta los servicios:
  ```sh
  docker-compose up --build
  ```

### 5. ¿Qué pasa y qué revisar?
- Observa los logs en tiempo real:
  - Los clientes envían tareas concurrentemente.
  - El server recibe y guarda las tareas en `tasks.json`.
- Verifica el archivo de tareas:
  ```sh
  docker exec -it taskserver /bin/bash
  cat /app/tasks.json
  exit
  ```
- Espera ver el número total de tareas igual a la suma de las enviadas por ambos clientes (por ejemplo, 200).

### 6. ¿Qué espero y qué demuestro?
- Que todas las tareas se guardan correctamente (no hay pérdida por condiciones de carrera).
- Que la comunicación es solo interna: los clientes y el server solo se ven entre sí dentro de la red privada de Docker.
- Si intentas acceder a la API desde fuera (sin exponer el puerto), no es posible.
- Puedes mostrar la red interna y los contenedores conectados con:
  ```sh
  docker network inspect docker-ejemplo-2_ticsnet
  ```

--- 