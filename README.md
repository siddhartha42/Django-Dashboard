# Python-Django Dashboard

The Python-Django dashboard offers essential signup and login features, complete with authentication and password hashing. The system includes checks for unique usernames and emails, allowing users to sign up with roles such as doctor or patient. Additionally, the dashboard provides a convenient profile picture feature.

## Prerequisites

Ensure you have the latest version of Python installed.

## Getting Started

Follow these steps to initialize the project:

# Clone the Repository:
git clone https://github.com/your-username/python-dashboard.git

# Navigate to the Project Directory:
cd python-dashboard

# Set Up a Virtual Environment:
install virtualenv
virtualenv venv
venv/Scripts/activate

# Install Required Packages:
pip install django
pip install pillow

# Apply Database Migrations:
python manage.py makemigrations
python manage.py migrate

# Run the Development Server:
python manage.py runserver

You can now access the dashboard at http://127.0.0.1:8000/.

