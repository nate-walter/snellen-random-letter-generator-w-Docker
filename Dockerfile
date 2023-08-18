FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code
COPY . .

# Add a non-root user and switch to that user
RUN useradd -m myuser

# Modify permissions for the /app directory for myuser
RUN chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Run the Python application
CMD ["python", "main.py"]
