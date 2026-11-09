from flask import Flask, jsonify
import psycopg
from dotenv import load_dotenv
import os

# Load database settings from the .env file
load_dotenv()

# Create Flask application
app = Flask(__name__)


# Connect to PostgreSQL
def get_db_connection():
    return psycopg.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )


# Homepage
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Student Management DevOps Platform",
        "status": "success"
    })


# API health check
@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Student Management API"
    })


# Retrieve all students
@app.route("/api/students", methods=["GET"])
def get_students():
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:

                cursor.execute("""
                    SELECT id, name, age, course
                    FROM students
                    ORDER BY id
                """)

                students = cursor.fetchall()

        result = [
            {
                "id": student[0],
                "name": student[1],
                "age": student[2],
                "course": student[3]
            }
            for student in students
        ]

        return jsonify(result)

    except psycopg.Error:
        app.logger.exception("Database operation failed")
        return jsonify({
            "error": "Database operation failed"
        }), 500


# Start Flask application
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )