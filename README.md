# Quiz App

## Overview
This is a simple Django-based quiz application. The app allows a user to start a new quiz session, answer a set of random multiple-choice questions, and view the results at the end of the quiz.

## Features
- Start a new quiz session
- Get a random set of 3 multiple-choice questions from the database
- Submit answers for all questions at once
- View the total number of questions answered, along with details on correct and incorrect submissions

## Assumptions
- There is only one user.
- Questions are pre-populated in the database.
- The quiz consists of exactly 3 questions per session.

## Requirements
- Python 3.x
- Django 4.x

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yaswanth8895/quiz-app.git
    cd quiz-app
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/quiz/start/` to start a new quiz.

## Usage

1. **Start a new quiz:**
    - Navigate to `http://127.0.0.1:8000/quiz/start/` to start a new quiz session.

2. **Answer questions:**
    - You will be presented with 3 random multiple-choice questions. Select your answers and submit them.

3. **View results:**
    - After submitting your answers, you will be redirected to the results page where you can see the total number of questions answered, along with the number of correct and incorrect answers.

4. **Take a new quiz:**
    - On the results page, click the "Take New Quiz" button to start a new quiz session.

## Adding Questions

1. **Access the admin interface:**
    - Go to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

2. **Add questions:**
    - In the admin interface, click on "Questions" and then "Add Question" to add new questions to the database. Fill in the question text and options, and specify the correct option.

## Project Structure
