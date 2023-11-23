# Usa la imagen base de Python
FROM python:3.10

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Configura Python para no almacenar en búfer la salida
ENV PYTHONUNBUFFERED 1

# CMD especifica el comando para ejecutar tu aplicación
CMD ["python", "scheduler.py"]
