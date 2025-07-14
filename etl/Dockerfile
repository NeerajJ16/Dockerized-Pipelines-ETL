# Use lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ETL script and .env for credentials
COPY pipeline.py .

# Run the ETL script
CMD ["python", "pipeline.py"]
