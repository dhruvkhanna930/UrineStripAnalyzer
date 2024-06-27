# Urine Strip Analyzer

This project is a web application designed to analyze images of urine strips, identify up to 10 colors on the strip, and provide analysis results in JSON format. It uses Django for the backend API and React for the frontend interface.

## Features

- **Image Upload**: Users can upload images of urine strips for analysis.
- **Color Identification**: The system identifies up to 10 colors present on the urine strip.
- **JSON Output**: Results are returned in JSON format for easy integration with other systems.

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: React
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

## Installation

### Prerequisites

- Docker
- Docker Compose

### Running the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/dhruvkhanna930/UrineStripAnalyzer.git
   cd UrineStripAnalyzer
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start the containers for the backend, frontend, and PostgreSQL database.

3. Access the application:

   - Backend API: http://localhost:8000/
   - Frontend Interface: http://localhost:3000/

4. Create a superuser to access the Django admin interface:

   ```bash
   docker-compose exec backend python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

5. Access the Django admin interface:

   - URL: http://localhost:8000/admin/
   - Use the superuser credentials created in the previous step.

6. Database Initialization:
    ```bash
   docker-compose exec backend python manage.py makemigrations
   docker-compose exec backend python manage.py migrate
    ```
    Run these if the RUN python manage.py runserver gives error while running docker-compose

## Usage

- **Uploading an Image**: Navigate to the frontend interface, upload an image of a urine strip, and submit it for analysis.
- **Viewing Results**: Results will be displayed on the frontend interface in JSON format.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
