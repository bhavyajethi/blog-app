# **Blog App**
This is my first Django project as I learn Django. This project is a simple **blog application** where users can create, read, update, and delete blog posts.

## **Features**
### User authentication (Login/Signup)
### Create, Read, Update, Delete (CRUD) blog posts
### Django Admin Panel

# **Tech Stack**
Django - Web framework
SQLite - Database
Bootstrap - Styling

## Getting Started

To set up this project on your local machine, follow the steps below.

### Clone the Repository

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/bhavyajethi/Deep-ai-assistant.git
   cd Deep-ai-assistant

2. **Set Up Virtual Environment**:  
   ```bash
   python -m venv venv
   venv\Scripts\activate        # On Windows
   # OR
   source venv/bin/activate     # On macOS/Linux

3. **Install dependencies**:  
   ```bash
     pip install -r requirements.txt

4. **Set Up Environment Variables and follow the steps below**:
  ```bash
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
