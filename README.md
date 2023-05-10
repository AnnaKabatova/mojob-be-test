# Simple Recruitment API
- A simple API service for recruitment, written in Django REST Framework

### Requirements:
1. Endpoint for creating, updating and deleting jobs with job headers
2. Endpoint that returns a job with a fully serialized job header
3. Endpoint that returns all applications for provided user_id
4. Whenever the job is created call method "send_job_created_email", whenever updated - "senf_job_updated_email"
5. All endpoints should be accessible only to authenticated users.
6. Endpoints should use JSON format.

### Technologies to use:
1. Django, Django REST preferable
2. PostgreSQL database

### How to run:
- Copy this repo from github:
```git
git clone https://github.com/AnnaKabatova/mojob-be-test.git
```
- Create venv and activate it through terminal:
```git
python -m venv myvenv

#Windows activaition:
myvenv\Scripts\activate

#Unix or Linux activation:
source myvenv/bin/activate
```
- Copy .env.sample rename it to .env and populate with all required data
- Run migrations to initialize database: ```python manage.py migrate```
- Run the server of app ```python manage.py runserver```
