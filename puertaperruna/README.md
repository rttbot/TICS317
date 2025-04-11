# Sistema de Puerta Perruna

Este proyecto simula un sistema de puerta automática para perros, que se abre al detectar un ladrido.

## Instrucciones para Crear la Página de GitHub


3. **Configurar GitHub Pages:**
   - Ve a la configuración del repositorio en GitHub.
   - Busca la sección "GitHub Pages".
   - Selecciona la rama `master` o `main` y la carpeta `/ (root)` para la fuente de la página.
   - Guarda los cambios.

4. **Acceder a la Página:**
   - Una vez configurado, GitHub generará una URL para tu página, generalmente en el formato `https://<tu_usuario>.github.io/<nombre_del_repositorio>/`. 

## Descripción del Proyecto

El sistema de puerta perruna utiliza sensores para detectar ladridos y un actuador para abrir o cerrar la puerta automáticamente. El sistema está diseñado para ser seguro, verificando que no haya movimiento antes de cerrar la puerta. 

## Crear el Archivo index.html

Para crear una página web básica para el sistema de puerta perruna, sigue estos pasos:

1. Crea un archivo llamado `index.html` en el directorio raíz del proyecto.
2. Copia y pega el siguiente código en el archivo `index.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Puerta Perruna</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        .container {
            padding: 20px;
            max-width: 800px;
            margin: auto;
        }
        h1, h2 {
            color: #4CAF50;
        }
        footer {
            text-align: center;
            padding: 10px 0;
            background-color: #333;
            color: white;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>
    <header>
        <h1>Sistema de Puerta Perruna</h1>
    </header>
    <div class="container">
        <h2>Descripción</h2>
        <p>Este proyecto simula un sistema de puerta automática para perros, que se abre al detectar un ladrido. Utiliza sensores para detectar ladridos y un actuador para abrir o cerrar la puerta automáticamente.</p>
        <h2>¿Cómo Funciona?</h2>
        <p>El sistema está diseñado para ser seguro, verificando que no haya movimiento antes de cerrar la puerta. Una vez que se detecta un ladrido, la puerta se abre automáticamente y se cierra cuando es seguro hacerlo.</p>
    </div>
    <footer>
        <p>&copy; 2025 Sistema de Puerta Perruna</p>
    </footer>
</body>
</html>
```

3. Guarda el archivo y súbelo a tu repositorio de GitHub. 