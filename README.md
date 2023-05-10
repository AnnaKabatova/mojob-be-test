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
![created](https://github.com/AnnaKabatova/mojob-be-test/assets/80786573/adf1d765-e4aa-4dcb-8f25-624df7cc89f2)
![deleted](https://github.com/AnnaKabatova/mojob-be-test/assets/80786573/ef257d4d-ba98-4d7c-b11a-4f875599152b)
![job_created](https://github.com/AnnaKabatova/mojob-be-test/assets/80786573/48c79f4b-147f-4f48-aa46-9c9a7e02eb2f)
![list-create page](https://github.com/AnnaKabatova/mojob-be-test/assets/80786573/cb9e06c1-6b8f-486e-8dec-90da94ad694f)
![not authenticated](https://github.com/AnnaKabatova/mojob-be-test/assets/80786573/5f5444b9-93cb-4869-a29c-b26e4c361881)
![token page](https://github.com/AnnaKabatova/mojob-be-test/assets/80786573/ab5c88aa-816b-4f99-87e4-97ccf3973445)
![update_page](https://github.com/AnnaKabatova/mojob-be-test/assets/80786573/96e332b2-8606-4348-a2b5-69cef940522e)
![user_applications](https://github.com/AnnaKabatova/mojob-be-test/assets/80786573/f22307e1-0424-4282-884c-37ec275e8d13)
