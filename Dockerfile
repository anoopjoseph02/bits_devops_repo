# Base Image
FROM python:3.10-slim

WORKDIR /app

# Copy files and install required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose app in a port
EXPOSE 5000

CMD ["python", "-m", "aceest_fitness.app"]
