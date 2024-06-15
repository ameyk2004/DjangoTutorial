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
