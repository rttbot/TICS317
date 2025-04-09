# Instrucciones para levantar SecureShop y Puertaperruna en modo debug

## Levantar SecureShop

SecureShop consta de tres aplicaciones que deben ejecutarse en el siguiente orden:

1. **API (api.py)**: 
   - Asegúrate de tener Python y Flask instalados en tu sistema. Si no los tienes, puedes instalarlos usando:
     ```bash
     pip install flask
     ```
   - Navega al directorio del proyecto SecureShop:
     ```bash
     cd /ruta/a/tu/proyecto/SecureShop
     ```
   - Ejecuta la API en modo debug:
     ```bash
     python api.py
     ```
   - La API debería estar corriendo en `http://localhost:5001`.

2. **Panel de Administración (securesoftware.py)**:
   - Ejecuta el panel de administración en modo debug:
     ```bash
     python securesoftware.py
     ```
   - El panel debería estar corriendo en `http://localhost:5002`.

3. **Tienda (secureshop.py)**:
   - Ejecuta la tienda en modo debug:
     ```bash
     python secureshop.py
     ```
   - La tienda debería estar corriendo en `http://localhost:5003`.

## Levantar Puertaperruna

1. Asegúrate de tener Python instalado en tu sistema.

2. Navega al directorio del proyecto Puertaperruna:
   ```bash
   cd /ruta/a/tu/proyecto/puertaperruna
   ```

3. Para evaluar la ejecución del script `sistema_puerta_perruna.py` en Cursor, puedes establecer puntos de interrupción (breakpoints) de la siguiente manera:
   - Abre el archivo `sistema_puerta_perruna.py` en Cursor.
   - Haz clic en el margen izquierdo junto a la línea de código donde deseas establecer un punto de interrupción. Un punto rojo debería aparecer indicando que el breakpoint está activo.

4. Ejecuta el script en modo debug:
   ```bash
   python -m pdb sistema_puerta_perruna.py
   ```

Este script simula el funcionamiento de un sistema de puerta automática para mascotas y no se ejecuta en un puerto específico. Utiliza los breakpoints para pausar la ejecución y evaluar el estado del programa en Cursor.
