# Vehicle CRUD Web App with APIs


This project is a Django web application that provides a user interface and APIs for performing CRUD (Create, Read, Update, Delete) operations on vehicles. It supports different user roles, including super admin, admin, and regular user.
#
#
## swagger : localhost:8000/swagger/
### All api's list in the swagger
#
#
## Introduction

The Vehicle CRUD Web App allows users to manage vehicles by providing functionalities to create, retrieve, update, and delete vehicle records. It is built using Django, a Python web framework, and provides a user-friendly interface along with APIs for programmatic access.

# Installation


Follow the steps below to set up and run the project locally:

Clone the repository: git clone <repository-url>
Change into the project directory: cd vehicle-crud-web-app
Create and activate a virtual environment: python -m venv env (Windows) or python3 -m venv env (macOS/Linux). Activate the environment using the appropriate command for your operating system.
Install the dependencies: pip install -r requirements.txt
Set up the database: python manage.py migrate
Run the development server: python manage.py runserver
The web app will be accessible at http://localhost:8000.

Usage
Web Interface
Access the web app in your browser: http://localhost:8000
Sign up for a new account or log in if you already have one.
User Roles:
### Super Admin: Super admins have the highest level of access and can perform all actions.
### Admin: Admins can manage vehicle records, including creating, updating, and deleting vehicles.
### User: Regular users can view vehicle records but cannot make any changes.
### APIs
The web app also provides APIs for programmatic access. Below are the available endpoints:

## GET /api/vehicles: Retrieve a list of all vehicles.
## GET /api/vehicles/{id}: Retrieve details of a specific vehicle by ID.
## POST /api/vehicles: Create a new vehicle record (requires admin access).
## PUT /api/vehicles/{id}: Update the details of a vehicle by ID (requires admin access).
## DELETE /api/vehicles/{id}: Delete a vehicle by ID (requires admin access).
Ensure you include the appropriate headers and request body when using the APIs.



### Project Structure


The project follows a typical Django project structure:

manage.py: The Django project management script.
vehiclecrud/: The main Django project directory.
settings.py: Project settings including database configuration, installed apps, and middleware.
urls.py: URL configuration for the project.
vehicles/: Django app directory for managing vehicles.
models.py: Defines the database model for vehicles.
views.py: Contains the logic for handling web requests and rendering templates.
serializers.py: Converts Django model instances to JSON for API responses.
urls.py: URL configuration for the vehicle app.




Contact
For any questions or inquiries, please contact sreejeshas33@gmail.com