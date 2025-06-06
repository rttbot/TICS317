FROM python:3.13.3-slim

WORKDIR /app

# Copiar requirements.txt e instalar dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY main.py test_operacional.py /app/

CMD ["python", "main.py"]