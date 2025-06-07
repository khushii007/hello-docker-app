FROM python:3.9-slim

COPY app /app
WORKDIR /app

CMD ["python", "main.py"]
