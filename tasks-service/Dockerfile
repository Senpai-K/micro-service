# Dockerfile для микросервиса управления задачами
FROM python:3.9-slim

WORKDIR /app

COPY requirements_serv.txt .
RUN pip install --no-cache-dir -r requirements_serv.txt

COPY . .

EXPOSE 5001

CMD ["python", "src/task_service.py"]
