# Dockerfile for Django backend

# Use the official Python image from Docker Hub
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app
# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y wait-for-it

# Copy the Django project into the container
COPY . /app/

RUN python manage.py makemigrations
# RUN python manage.py migrate

# Expose the port on which Django runs
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["wait-for-it", "db:5432", "--", "python", "manage.py", "migrate"]
