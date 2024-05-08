# Use the official Python image as a base
FROM python:3.9

# Set environment variables - prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask flask-restx

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
