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
