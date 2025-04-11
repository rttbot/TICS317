# Proyectos: Sistema de Puerta Perruna y SecureShop 

Este repositorio contiene dos proyectos: un sistema de puerta automática para perros y una tienda en línea segura. A continuación, se detallan las instrucciones para configurar y ejecutar cada proyecto.

## Requisitos Previos

- **IDE Recomendado**: Se recomienda utilizar un IDE como Visual Studio Code o PyCharm para facilitar el desarrollo y la depuración.
- **Clonar el Repositorio**: 
  ```bash
  git clone https://github.com/tu_usuario/tu_repositorio.git
  cd tu_repositorio
  ```

## Configuración del Entorno Local

1. **Crear un Entorno Virtual**:
   - Un entorno virtual te permite crear un espacio aislado para tus proyectos de Python, donde puedes instalar paquetes sin afectar el sistema global de Python.
   - Ejecuta el siguiente comando para crear un entorno virtual llamado `venv`:
     ```bash
     python -m venv venv
     ```

2. **Activar el Entorno Virtual**:
   - La activación del entorno virtual varía según el sistema operativo:
     - En Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - En macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Instalar Dependencias**:
   - Asegúrate de que el entorno virtual esté activado antes de instalar las dependencias.
   - Para `puertaperruna`:
     ```bash
     cd TICS317/puertaperruna
     pip install -r requirements.txt
     ```
   - Para `SecureShop`:
     ```bash
     cd TICS317/SecureShop
     pip install -r requirements.txt
     ```

## Sistema de Puerta Perruna

Este proyecto simula un sistema de puerta automática para perros, que se abre al detectar un ladrido.

### Ejecución

1. **Ejecutar el Simulador**:
   - Asegúrate de que el entorno virtual esté activado.
   - Ejecuta el siguiente comando:
     ```bash
     python simulador_bobby.py
     ```

2. **Uso de `pdb` para Depuración**:
   - El script `simulador_bobby.py` incluye un punto de interrupción con `pdb`. Para avanzar en el depurador, utiliza los siguientes comandos:
     - `n`: Ejecuta la siguiente línea de código.
     - `c`: Continúa la ejecución hasta el siguiente punto de interrupción.
     - `q`: Sale del depurador.


## SecureShop

Este proyecto es una aplicación web para una tienda en línea segura.

### Ejecución

1. **Iniciar la Aplicación**:
   - Asegúrate de que el entorno virtual esté activado.
   - Ejecuta el siguiente comando:
     ```bash
     python api.py
     ```

2. **Acceder a la Aplicación**:
   - Abre un navegador web y ve a `http://localhost:5001` para interactuar con la API.

## Notas Finales

- Asegúrate de que el entorno virtual esté activado antes de ejecutar cualquier script.
- Consulta la documentación de cada proyecto para más detalles sobre su funcionamiento y características.
- En lo personal, prefiero el debug del IDE más que por comando.
- Ojo típico errorcillo - fijarse cómo tiene configurado correr python (en mi caso es python3)
