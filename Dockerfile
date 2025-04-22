#Imagen base de python
FROM python:3.11-slim

#Es para crear un directorio de trabajo dentro del contenedor 
WORKDIR /app

#Para copiar archivos
COPY app/ app/
COPY requirements.txt . 

#Instalar dependencias
RUN pip install -r requirements.txt

# ejecuta el script cuando inicie el contenedor
CMD ["python", "app.py"]