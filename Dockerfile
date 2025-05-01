# Use the official Python image
FROM python:3.9-slim

# Copy our script in
COPY app.py /app.py

# Run it
CMD ["python", "/app.py"]
