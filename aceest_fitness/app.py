from flask import Flask, request, jsonify, abort

def create_app():
    app = Flask(__name__)

    # In-memory database for workouts
    db = {"workouts": [], "next_id": 1}

    @app.get("/")
    def index():
        return jsonify({
            "app": "ACEest Fitness & Gym Tracker",
            "version": "1.0.0",
            "endpoints": ["/health", "/workouts", "/bmi"]
        })

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    # View all workouts
    @app.get("/workouts")
    def list_workouts():
        return jsonify(db["workouts"]), 200

    # Add a workout
    @app.post("/workouts")
    def add_workout():
        payload = request.get_json(silent=True) or {}
        workout = payload.get("workout")
        duration = payload.get("duration")

        if not workout or duration is None:
            abort(400, description="Fields 'workout' and 'duration' are required")

        try:
            duration = int(duration)
        except ValueError:
            abort(400, description="'duration' must be a number")

        workout_entry = {
            "id": db["next_id"],
            "workout": workout.strip(),
            "duration": duration
        }
        db["next_id"] += 1
        db["workouts"].append(workout_entry)
        return jsonify(workout_entry), 201

    # Get one workout
    @app.get("/workouts/<int:workout_id>")
    def get_workout(workout_id):
        workout = next((w for w in db["workouts"] if w["id"] == workout_id), None)
        if not workout:
            abort(404, description="Workout not found")
        return jsonify(workout), 200

    # Delete a workout
    @app.delete("/workouts/<int:workout_id>")
    def delete_workout(workout_id):
        workout = next((w for w in db["workouts"] if w["id"] == workout_id), None)
        if not workout:
            abort(404, description="Workout not found")
        db["workouts"].remove(workout)
        return jsonify(workout), 200

    # BMI calculator
    @app.post("/bmi")
    def bmi():
        payload = request.get_json(silent=True) or {}
        try:
            height_cm = float(payload.get("height_cm", 0))
            weight_kg = float(payload.get("weight_kg", 0))
        except (TypeError, ValueError):
            abort(400, description="height_cm and weight_kg must be numbers")

        if height_cm <= 0 or weight_kg <= 0:
            abort(400, description="height_cm and weight_kg must be positive")

        height_m = height_cm / 100.0
        bmi_val = weight_kg / (height_m ** 2)
        category = (
            "Underweight" if bmi_val < 18.5 else
            "Normal" if bmi_val < 25 else
            "Overweight" if bmi_val < 30 else
            "Obese"
        )
        return jsonify({"bmi": round(bmi_val, 2), "category": category}), 200

    return app

# Expose global app
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
