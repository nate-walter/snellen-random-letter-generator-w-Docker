# Your existing Dockerfile content
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter Notebook extensions
RUN pip install jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user

# Your existing Dockerfile content continues...
COPY . .

# Add a non-root user and switch to that user
RUN useradd -m myuser

# Modify permissions for the /app directory for myuser
RUN chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Run the Python application
CMD ["jupyter", "notebook", "--ip='0.0.0.0'", "--port=8888", "--no-browser"]
