# Data Ingestion Pipeline for User Metrics

## Overview

This repository contains the implementation of a comprehensive data ingestion pipeline designed to efficiently handle a stream of user metrics. The metrics include `talked_time`, `microphone_used`, `speaker_used`, and `voice_sentiment`. The pipeline ingests this data into a MySQL database using Django as the web framework, ensuring optimal performance and reliability.

## Quick Setup

1. **Prerequisites:** Docker must be installed.
2. **Configuration:** Clone the repo and set up the `.env` file with your MySQL settings.
3. **Running the Project:** Use `docker-compose up --build` to launch the application.

## Features
- **Docker Integration:** Utilizes Docker to create a reproducible development environment, making it easy to share and collaborate on the project without system-specific issues.
- **MySQL Database:** Leverages MySQL for efficient data storage and retrieval, integrated through the `mysqlclient` library specified in the project dependencies.

## Project Structure

- **`docker-compose.yml`**: Orchestrates the Docker containers for the application and MySQL database.
- **`Dockerfile`**: Defines the environment setup for the Django application.
- **`manage.py`**: Django management script for administrative tasks.
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`admin.py`**: Configuration for the Django admin interface.
- **`apps.py`**: Application configuration.
- **`models.py`**: Defines the database schema using Django models.
- **`tests.py`**: Contains tests to validate the application logic.
- **`urls.py`**: URL routing configuration for the Django application.
- **`views.py`**: Implements the logic to handle HTTP requests and responses.


