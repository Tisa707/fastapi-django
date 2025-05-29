# FastAPI and Django Integration Experiment

This project is an exploration of using FastAPI and Django together in the same environment to understand their interoperability.

## Technologies Used
- Python 3.9+
- FastAPI
- Django

## How to Run
1. Clone the repo  
2. Create and activate a virtual environment  
3. Install dependencies with `pip install -r requirements.txt`  
4. Run the app using `uvicorn main:app --reload`

## Future Work
- Add shared authentication  
- Improve integration between frameworks



# User Email Generation CRUD Application

This is a simple CRUD (Create, Read, Update, Delete) application built using **FastAPI**, **Django**, and **SQLAlchemy** to manage user email generation. It demonstrates basic backend functionality and provides a RESTful API for user management.

## Features

- **Create**: Add new users with email addresses.
- **Read**: Retrieve user data (email).
- **Update**: Modify existing user details.
- **Delete**: Remove users from the database.

## Technologies Used

- **FastAPI**: For creating the fast, asynchronous REST API.
- **Django**: Used as the main web framework for project structure.
- **SQLAlchemy**: ORM used for database interactions.
- **SQLite**: Database for storing user information (SQLite for local development or PostgreSQL if deployed).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tisa707/fastapi-django.git
   cd fastapi-django
