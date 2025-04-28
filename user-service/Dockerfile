# Dockerfile для сервиса пользователя
FROM python:3.9-slim

WORKDIR /app

COPY requirements_user.txt .

RUN pip install --no-cache-dir -r requirements_user.txt

COPY . .

EXPOSE 5002

CMD ["python", "src/user_service.py"]
