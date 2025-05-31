# Entrenamiento de un Modelo de Lenguaje Simple (LLM) con el corpus Brown

> **Nota:** Este proyecto fue probado con **Python 3.11.11**.

Este proyecto permite entrenar un modelo de lenguaje basado en LSTM usando el corpus Brown de NLTK. El modelo y el tokenizer resultantes se pueden usar para generación de texto y otras tareas de NLP.

## Requisitos

- Python 3.8+
- Recomendado: Mac con Apple Silicon (M1/M2) para aprovechar la aceleración por GPU
- Paquetes Python:
  - tensorflow-macos (solo para Mac M1/M2)
  - tensorflow-metal (solo para Mac M1/M2)
  - tensorflow (para otros sistemas)
  - nltk
  - numpy
  - matplotlib
  - joblib

Puedes instalar todas las dependencias usando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

> **Nota:** El archivo `requirements.txt` incluye `tensorflow` por compatibilidad general. Si tienes Mac M1/M2, después de instalar desde `requirements.txt`, ejecuta:
> ```bash
> pip uninstall tensorflow
> pip install tensorflow-macos tensorflow-metal
> ```
> Así tendrás la versión optimizada para tu GPU Apple Silicon.

## Creación y activación del entorno virtual (recomendado)

1. Crea el entorno virtual:
   ```bash
   python3 -m venv venv
   ```
2. Actívalo:
   - En Mac/Linux:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```

## Consideraciones importantes sobre el tamaño de los datos

- **El corpus Brown completo tiene más de 57,000 oraciones.**
- Entrenar con todo el corpus puede consumir mucha memoria RAM y hacer que el proceso se "mate" (killed) en computadoras personales.
- **Para evitar problemas de memoria:**
  - Usa una fracción del corpus, por ejemplo 2,000 a 10,000 oraciones.
  - Reduce el tamaño del batch (`batch_size`) y el número de épocas (`epochs`).
  - Puedes ajustar estos valores en el script `firstLLM.py`:
    ```python
    data = brown.sents()[:2000]  # Usa solo 2,000 oraciones para pruebas
    history = model.fit(X, y, epochs=10, batch_size=32, verbose=1)
    ```

## Instrucciones para entrenar el modelo

1. **(Opcional) Crea y activa un entorno virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Instala las dependencias:**
   ```bash
   pip install tensorflow-macos tensorflow-metal nltk numpy matplotlib joblib
   ```

3. **Ejecuta el script de entrenamiento:**
   ```bash
   python firstLLM.py
   ```

   El script descargará el corpus Brown y las stopwords de NLTK si es la primera vez que se ejecuta.

4. **Ajusta el tamaño de los datos si tienes problemas de memoria:**
   - Edita la línea en `firstLLM.py`:
     ```python
     data = brown.sents()[:2000]  # Prueba con 2,000 oraciones
     ```
   - También puedes reducir el número de épocas y el tamaño del batch:
     ```python
     history = model.fit(X, y, epochs=10, batch_size=32, verbose=1)
     ```

5. **Salida:**
   - El modelo entrenado se guarda como `model.h5`.
   - El tokenizer se guarda como `tokenizer.pkl`.

## Notas adicionales

- Si ves mensajes de advertencia sobre NUMA o el backend de Metal, puedes ignorarlos si el entrenamiento avanza.
- Si el proceso se "mata" o ves errores de memoria, reduce aún más el tamaño de los datos y/o el modelo.
- El script incluye ejemplos de generación de texto y visualización de la precisión del modelo.

---

## ¿Cómo funciona el backend y cómo se conecta el frontend?

### ¿Qué hace el backend?
- El archivo `backend.py` implementa una API REST usando Flask.
- Esta API carga el modelo (`model.h5`) y el tokenizer (`tokenizer.pkl`) entrenados previamente.
- Expone un endpoint (por ejemplo, `/generate`) que recibe una frase semilla (`seed_text`) y un número de palabras a generar (`next_words`).
- El backend utiliza el modelo para generar texto y devuelve la respuesta al frontend o a cualquier cliente HTTP.

### ¿Cómo se conecta el frontend?
- El frontend (puede ser una app web, Postman, o un simple cliente curl) realiza peticiones HTTP POST al endpoint del backend.
- Envía un JSON con la frase semilla y la cantidad de palabras a generar.
- Recibe como respuesta el texto generado por el modelo.

### ¿Quién hace qué?
- **El backend:** Se encarga de cargar el modelo, recibir solicitudes, generar texto y devolver la respuesta.
- **El frontend/cliente:** Solo envía la frase semilla y muestra el resultado al usuario.
- **El modelo:** Es el "cerebro" que predice la siguiente palabra a partir de la frase semilla.

### ¿Cómo levantar todo en diferentes terminales?

1. **Terminal 1: Entrenamiento del modelo (solo la primera vez o cuando quieras reentrenar)**
   ```bash
   python firstLLM.py
   ```
   Esto generará los archivos `model.h5` y `tokenizer.pkl`.

2. **Terminal 2: Levantar el backend**
   ```bash
   python backend.py
   ```
   Esto iniciará el servidor Flask, normalmente en `http://localhost:5000`.

3. **Terminal 3: Probar la API (puedes usar curl, Postman, o un frontend propio)**
   Ejemplo con curl:
   ```bash
   curl -X POST http://localhost:5000/generate \
        -H "Content-Type: application/json" \
        -d '{"seed_text": "The future of AI", "next_words": 10}'
   ```
   Recibirás un JSON con el texto generado.

### ¿Qué chequear?
- Que los archivos `model.h5` y `tokenizer.pkl` existan antes de levantar el backend.
- Que el backend muestre en consola que está corriendo y no haya errores de carga de modelo.
- Que las respuestas de la API sean coherentes y no haya errores HTTP.

### ¿Cómo usar el aplicativo?
- Puedes interactuar con la API desde cualquier cliente HTTP (curl, Postman, tu propio frontend).
- Solo necesitas enviar la frase semilla y el número de palabras a generar.
- El backend responderá con el texto generado por el modelo.

---

¿Dudas o problemas? ¡No dudes en pedir ayuda!
