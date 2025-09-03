# ACEest Fitness & Gym Tracker

A simple Flask-based fitness tracking API for DevOps assignment.

## Setup

```bash
git clone <your-repo-url>
cd ACEest_Fitness
pip install -r requirements.txt
python -m aceest_fitness.app
```

The app runs on `http://localhost:5000`.

## Endpoints

- `GET /health` – Health check
- `GET /workouts` – List workouts
- `POST /workouts` – Add a workout (JSON: {workout, duration})
- `GET /workouts/<id>` – Get workout by ID
- `DELETE /workouts/<id>` – Delete workout
- `POST /bmi` – Calculate BMI

## Tests

```bash
pytest -q
```

## Docker

```bash
docker build -t aceest_fitness .
docker run -p 5000:5000 aceest_fitness
```

## CI/CD

This project uses GitHub Actions (`.github/workflows/ci.yml`) to:

1. Run Pytest unit tests
2. Build Docker image

The project uses GitHub Actions to implement a fully automated CI/CD pipeline. The workflow is defined in the file .github/workflows/ci.yml and is triggered automatically on every push or pull request to the main branch.

The pipeline ensures that every code change is validated and containerized consistently before integration. It consists of the following key stages:

# Checkout Code

Uses actions/checkout to pull the latest version of the repository into the workflow runner.

# Set Up Python Environment

Configures Python (version 3.10) using actions/setup-python.

Ensures a consistent runtime environment for installing dependencies and running tests.

Install Dependencies

Installs all project dependencies listed in requirements.txt.

Ensures the application and test framework are ready to run.

# Run Unit Tests

Executes the Pytest test suite to validate the Flask application’s core functionalities (e.g., health check, workout management, BMI calculation).

Any test failure blocks the pipeline, ensuring that only correct code proceeds.

# Build Docker Image

Builds the Docker container for the application using the project’s Dockerfile.

Validates that the application can be packaged consistently across environments.