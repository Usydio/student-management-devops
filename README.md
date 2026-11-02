# Student Management DevOps Platform

A real-world student management application designed to demonstrate DevOps practices through containerization, automation, and version control.

## Project Overview

This project uses a multi-container architecture to run a student management application.

## Technologies

- Python
- Flask
- PostgreSQL
- HTML
- CSS
- JavaScript
- Nginx
- Docker
- Docker Compose
- Git
- GitHub
- Docker Hub
- GitHub Actions

## Project Architecture

The application consists of four main components:

1. **Frontend:** User interface built with HTML, CSS, and JavaScript.
2. **Backend:** Flask REST API.
3. **Database:** PostgreSQL for storing student records.
4. **Web Server:** Nginx for serving the frontend and routing requests.

Docker Compose will manage the application containers and their communication through a Docker network.

## Project Structure

```text
student-management-devops/
├── backend/
├── frontend/
├── nginx/
├── database/
├── .github/
│   └── workflows/
├── .env.example
├── .gitignore
└── README.md
```

## Project Goals

- Build a student management application.
- Containerize the application using Docker.
- Configure multiple services using Docker Compose.
- Establish communication between containers.
- Use Git and GitHub for version control.
- Publish Docker images to Docker Hub.
- Automate project checks using GitHub Actions.

## Project Status

🚧 Under development
