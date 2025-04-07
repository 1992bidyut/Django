# Django with SQLAlchemy Project

This project demonstrates how to integrate SQLAlchemy with Django, and implements both synchronous and asynchronous views along with custom middleware.

## Project Specifications

- Python 3.10
- Django 4.2.7
- SQLAlchemy 1.3.20
- MySQL database
- Custom middleware for request timing
- Sync and async views

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install required packages

```bash
pip install Django==4.2.7
pip install SQLAlchemy==1.3.20
pip install mysqlclient
pip install asgiref
pip install uvicorn
```

### 3. Create MySQL database

```sql
CREATE DATABASE django_sqlalchemy_db;
CREATE USER 'db_user'@'localhost' IDENTIFIED BY 'db_password';
GRANT ALL PRIVILEGES ON django_sqlalchemy_db.* TO 'db_user'@'localhost';
FLUSH PRIVILEGES;
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Initialize SQLAlchemy database

```bash
python manage.py init_sqlalchemy
```

### 6. Run the development server

```bash
# For synchronous WSGI server
python manage.py runserver

# For asynchronous ASGI server
uvicorn djangosqlalchemy.asgi:application --reload
Or
uvicorn djangosqlalchemy.asgi:application --host 127.0.0.1 --port 8000 --reload
```

## Project Structure

```
djangosqlalchemy/
├── core/
│   ├── management/
│   │   └── commands/
│   │       └── init_sqlalchemy.py
│   ├── middleware/
│   │   └── custom_middleware.py
│   ├── templates/
│   │   └── core/
│   │       └── index.html
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── sqlalchemy_models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── djangosqlalchemy/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## API Endpoints

- `GET /`: Main page with documentation
- `GET /sync/`: Synchronous view using SQLAlchemy
- `GET /async/`: Asynchronous view using SQLAlchemy
- `GET /users/`: List all users
- `POST /users/`: Create a new user
- `GET /users/<id>/`: Get a specific user
- `PUT /users/<id>/`: Update a specific user
- `DELETE /users/<id>/`: Delete a specific user

## Custom Middleware

This project includes a custom middleware for timing requests. The middleware adds an `X-Processing-Time` header to responses indicating how long the request took to process.

## Using Both ORMs

This project demonstrates how to use both Django's ORM and SQLAlchemy in the same project:

- Django ORM is used for standard CRUD operations
- SQLAlchemy is used for more complex queries and in both sync and async views

## Performance Comparison

You can compare the performance of synchronous and asynchronous views by accessing:
- `/sync/` - Synchronous view
- `/async/` - Asynchronous view

Both endpoints will return the processing time in the response.