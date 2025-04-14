# Use Python 3.10 base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install torch==2.0.1 torchvision torchaudio \
    && pip install -r requirements.txt

# Expose the app port
EXPOSE 10000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
