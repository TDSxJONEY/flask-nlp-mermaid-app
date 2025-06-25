# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app

# Copy your application code to the container
COPY . /app

# Install system dependencies (e.g., for spaCy, transformers, etc.)
RUN apt-get update && apt-get install -y gcc g++ libgomp1 && apt-get clean

# Install Python dependencies as specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Install spaCy model manually
RUN python -m spacy download en_core_web_sm

# Expose the port the app will run on
EXPOSE 5000

# Command to run your app (Flask app)
CMD ["python", "run.py"]
