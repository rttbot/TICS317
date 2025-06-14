# docker-ejemplo-3: Balanceo de carga y manejo de fallas

> Arquitectura de Sistemas: TICS317

---

## 🌐 Introducción: Sistemas distribuidos y controles de salud

En sistemas distribuidos, múltiples servicios o instancias trabajan juntos para ofrecer alta disponibilidad, escalabilidad y tolerancia a fallos. Sin embargo, esto introduce nuevos desafíos:

- **¿Qué pasa si un servidor falla?**
- **¿Cómo sabemos si un servicio está disponible?**
- **¿Cómo detectamos y monitoreamos errores en tiempo real?**

Por eso, es fundamental implementar:
- **Balanceadores de carga:** Distribuyen el tráfico entre varias instancias, mejorando la disponibilidad y el rendimiento.
- **Health checks (/health):** Permiten saber si un servicio está "vivo" y listo para recibir tráfico.
- **Endpoints de monitoreo (/errors/stats, /status):** Permiten observar el estado lógico del sistema, errores recientes y métricas clave.

Estos controles son esenciales para cualquier despliegue distribuido moderno, ya sea en la nube, en contenedores o en servidores físicos.

---

## 🚀 Estructura del sistema

- **Balanceador:** load_balancer.py (puerto 8080)
- **Servidores de tareas:** taskserver.py (server1:5001, server2:5002)
- **Clientes concurrentes:** clientemulator.py (client1, client2)
- **Archivo compartido:** tasks.json
- **Red interna:** ticsnet

---

## 🏗️ Arquitectura (resumida)

```
+---------------------+      HTTP      +---------------------+      HTTP      +---------------------+
|   clientemulator1   | ------------> |   load_balancer     | ----------->  |   taskserver1 (5001)|
+---------------------+                +---------------------+               +---------------------+
|   clientemulator2   | ------------> |   (puerto 8080)     | ----------->  |   taskserver2 (5002)|
+---------------------+                +---------------------+               +---------------------+
```

---

## 📦 Componentes del sistema
- `taskserver.py`: Servidor Flask que maneja tareas y reporta errores.
- `load_balancer.py`: Balanceador de carga que distribuye solicitudes entre varios servidores Flask.
- `clientemulator.py`: Cliente que realiza pruebas de concurrencia y fuerza errores.
- `tasks.json`: Archivo compartido para persistencia de tareas.
- `Dockerfile`: Imagen base para todos los servicios.
- `docker-compose.yml`: Orquestador de todos los servicios y la red interna.

---

## ⚙️ ¿Cómo funciona?
1. El usuario o los clientes acceden a través del balanceador (puerto 8080).
2. El balanceador elige un servidor disponible (5001 o 5002) y reenvía la solicitud.
3. Los servidores procesan la solicitud y responden (agregan/listan tareas, etc.).
4. El balanceador monitorea el estado de los servidores y maneja fallas automáticamente.
5. Los errores HTTP (400, 404, 500) son detectados y registrados para monitoreo.

---

## 🚦 Pasos para correr el sistema

1. **(Opcional) Limpia el archivo de tareas**
   ```sh
   echo "[]" > tasks.json
   ```

2. **Construye y levanta todos los servicios**
   ```sh
   docker-compose up --build
   ```
   Esto construye la imagen y levanta el balanceador, dos taskserver y dos clientemulator en la red interna.

3. **Observa los logs en tiempo real**
   - En la misma terminal, verás los logs de todos los servicios.
   - Si quieres verlos en otra terminal:
     ```sh
     docker-compose logs -f
     ```

4. **Accede a la API y endpoints de monitoreo**
   - Ver tareas:  http://localhost:8080/tareas
   - Estado del balanceador:  http://localhost:8080/health
   - Estado de los servidores:  http://localhost:8080/status

5. **(Opcional) Ingresa a un contenedor para inspeccionar el archivo de tareas**
   ```sh
   docker exec -it server1 /bin/bash
   cat /app/tasks.json
   exit
   ```

6. **(Opcional) Simula una falla**
   - Detén un servidor:
     ```sh
     docker-compose stop server1
     ```
   - El sistema seguirá funcionando y el balanceador redirigirá las solicitudes al server restante.

7. **(Opcional) Baja todos los servicios cuando termines**
   ```sh
   docker-compose down
   ```

---

## 👀 Monitoreo y verificación

- Ver los contenedores activos:
  ```sh
  docker ps
  ```
- Ver el estado de los servicios:
  ```sh
  docker-compose ps
  ```
- Ver la red interna y los contenedores conectados:
  ```sh
  docker network inspect docker-ejemplo-3_ticsnet
  ```
- Ver los procesos dentro de un contenedor:
  ```sh
  docker exec -it server1 ps aux
  ```
- Salir de un contenedor:
  ```sh
  exit
  ```
  o presiona `Ctrl+D`.

---

## 🎯 ¿Qué se espera demostrar?
- Balanceo de carga real entre servidores.
- Persistencia de tareas compartida.
- Manejo y monitoreo de errores HTTP.
- Alta disponibilidad: el sistema sigue funcionando si un servidor falla.
- Observabilidad: puedes ver estadísticas y estado en tiempo real.

---

## 🧩 Consideraciones sobre balanceadores de carga

### Importancia en Arquitecturas Modernas
El balanceador de carga es fundamental para:

- **Escalabilidad horizontal:** Permite añadir más servidores para manejar más tráfico sin cambiar la aplicación.
- **Arquitecturas de microservicios:** Facilita la comunicación entre múltiples servicios independientes.
- **Alta disponibilidad:** Garantiza que el sistema siga funcionando incluso si algunos componentes fallan.
- **Despliegues sin tiempo de inactividad:** Permite actualizar servidores de forma gradual sin interrumpir el servicio.

En sistemas reales, los balanceadores también pueden realizar tareas como terminación de SSL, autenticación, compresión de tráfico y monitoreo avanzado.

### Algoritmos de Distribución de Carga
Aunque en este ejemplo usamos selección aleatoria, existen varios algoritmos comunes:

- **Round Robin:** Distribuye solicitudes secuencialmente entre los servidores. Es simple y efectivo cuando los servidores tienen capacidades similares.
- **Menor número de conexiones:** Envía solicitudes al servidor con menos conexiones activas. Útil cuando las cargas de trabajo varían mucho.
- **Tiempo de respuesta:** Selecciona el servidor con mejor tiempo de respuesta reciente, ideal para sistemas con servidores heterogéneos.
- **Hash IP:** Envía todas las solicitudes de una misma IP al mismo servidor, útil para mantener la afinidad de sesión.
- **Aleatorio:** Como en nuestra implementación, selecciona un servidor al azar. Es simple y puede ser suficiente para sistemas pequeños o pruebas.

> **Nota:** En sistemas de producción, los balanceadores suelen combinar varios de estos algoritmos y monitorear activamente la salud de los servidores para tomar decisiones inteligentes.

---
