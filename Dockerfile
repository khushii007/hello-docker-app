# Use the official Python image
FROM python:3.9-slim

# Copy our script in
COPY app.py /app.py

# Expose port for K8s
EXPOSE 8080

# Run the HTTP server
CMD ["python", "/app.py"]
