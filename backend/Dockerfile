# 1. Start with an official Python image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the dependency list
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the Flask application files
COPY . .

# 6. Make port 5000 available
EXPOSE 5000

# 7. Start the Flask application
CMD ["python", "app.py"]