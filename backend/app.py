# Important Flask tools
from flask import Flask, jsonify

# Create the Flask application
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Student Management DevOps Platform",
        "status": "success"
    })

# Health check route
@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Student Management API"
    })

# Start the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)