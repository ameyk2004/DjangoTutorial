# DjangoTutorial

## Introduction

Welcome to My Django Tutorials.
`Django`, a high-level Python web framework that encourages rapid development and clean, pragmatic design. Django is known for its "batteries-included" philosophy, providing a lot of built-in features to help developers build robust web applications quickly.

This project serves as a starting point for developing a web application with Django. The instructions below will guide you through setting up the project using pipenv, a dependency manager for Python that aims to combine the best features of pip and virtualenv.


## Project Setup

### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.x (preferably the latest version)
- pip (Python package installer)
- pipenv (Python dependency manager)

### Installation

#### Install pipenv

```bash
pip install pipenv
```

#### Create the Django Project

```bash
django-admin startproject myproject .
```

#### Run the Development Server

Start the development server to ensure everything is set up correctly:

```bash
python manage.py runserver
```
Open your browser and navigate to http://127.0.0.1:8000/ to see the Django welcome page.

### Directory Structure

```csharp
your-repo-name/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── Pipfile
└── Pipfile.lock 
```

### Configure pipenv Interpreter

#### Install pipenv:

```bash
pip install pipenv
```

#### Open Command Palette:

```bash 
Press Cmd + Shift + P.
Select Python Interpreter:
```

- Type Python: Select Interpreter.
- Choose the pipenv interpreter.


#### Open Integrated Terminal:

- Press Ctrl + (backtick) or go to Terminal > New Terminal.
- Activate pipenv shell if needed:

```bash
pipenv shell
```

#### Verify Setup:

Check the Python version:
```bash
python --version
```

## Create a New App

Navigate to the Project Directory

Make sure you are in the root directory of your Django project:

### Create the App

Use the startapp command to create a new app:

```bash
python manage.py startapp myapp
```

Replace myapp with the name of your new app.

### Verify Directory Structure

After running the command, you will see a new directory named myapp created within your project directory. The structure should look something like this:

```csharp
myproject/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
├── manage.py
└── Pipfile
```

### Register the App

To make Django aware of your new app, you need to add it to the INSTALLED_APPS setting in your project's settings file (myproject/settings.py):

```python
# myproject/settings.py

INSTALLED_APPS = [
    ...
    'myapp',
]
```