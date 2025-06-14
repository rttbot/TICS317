FROM python:3.13.3-slim

WORKDIR /app

# Copiar requirements.txt e instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY taskserver.py clientemulator.py /app/

# Por defecto, ejecuta el server
CMD ["python", "taskserver.py"]