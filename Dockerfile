# Usa una imagen oficial de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos y los instala
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Copia el script de entrada
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expone el puerto en el que la aplicación correrá
EXPOSE 9101

# Usa el script de entrada
ENTRYPOINT ["/app/entrypoint.sh"]
