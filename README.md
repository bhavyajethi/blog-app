# BlogApp 

This is my first Django project as I learn Django. This project is a simple **blog application** where users can create, read, update, and delete blog posts.

## Getting Started

To set up this project on your local machine, follow the steps below.

### Clone the Repository

First, clone this repository to your local system:

```sh
git clone https://github.com/bhavyajethi/blog-app.git
cd blog-app

Install Dependencies
Ensure you have Python 3 and virtualenv installed. Then, create a virtual environment and install dependencies:
# Create virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# OR (Linux/macOS)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Set Up Environment Variables
Create a .env file in the project root directory and add the following:
SECRET_KEY="your-secret-key-here"
DEBUG=True

Apply Migrations
Run database migrations:
python manage.py migrate

Create a Superuser (Optional)
To access the Django admin panel, create a superuser:
python manage.py createsuperuser

Run the Development Server
Start the Django server:
python manage.py runserver


Features
User authentication (Login/Signup)
Create, Read, Update, Delete (CRUD) blog posts
Django Admin Panel

Technologies Used
Django - Web framework
SQLite - Database
Bootstrap - Styling

