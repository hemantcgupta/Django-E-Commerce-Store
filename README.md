# Django E-Commerce Store

## Description
This project is a simple RESTful API built with Django for managing products and categories in a hypothetical e-commerce platform. It provides endpoints for CRUD operations on products and categories, along with user authentication using Django's built-in authentication system and JWT tokens.

## Setup Instructions

### Prerequisites
- Python (3.11.4 or higher)
- Pip (24.0 or higher)
- Django (4.0.1 or higher)
- Django REST Framework (3.14.0 or higher)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/hemantcgupta/Django-E-Commerce-Store.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Django-E-Commerce-Store
   ```
3. **Install dependencies using pip:**
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup
1. **Make migrations:**
   ```bash
   python manage.py makemigrations
   ```
2. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

### Running the Server
Start the Django development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.

### Deploy and Run Server by Bat Files
#### **Step 1: Deploy:**
- **Double-click on RunDeploy.bat to Deploy the project.**
- **This script will automatically create a virtual environment and install the required packages.**
#### **Step 2: Start Server:**
- **Double-click on RunServer.bat to execute the script.**
- **This script will automatically run migrations and start the Django development server.**


## API Endpoints

### Authentication
- **Register a new user:**
  ```
  POST /api/register/
  ```
  Required fields: email, password, name, pincode.
- **Login with email and password:**
  ```
  POST /api/login/
  ```
  Returns JWT token.

### Products
- **List all products:**
  ```
  GET /api/products/
  ```
- **Create a new product:**
  ```
  POST /api/products/
  ```
- **Retrieve details of a product:**
  ```
  GET /api/products/<id>/
  ```
- **Update details of a product:**
  ```
  PUT /api/products/<id>/
  ```
- **Delete a product:**
  ```
  DELETE /api/products/<id>/
  ```

### Categories
- **List all categories:**
  ```
  GET /api/categories/
  ```
- **Create a new category:**
  ```
  POST /api/categories/
  ```
- **Retrieve details of a category:**
  ```
  GET /api/categories/<id>/
  ```
- **Update details of a category:**
  ```
  PUT /api/categories/<id>/
  ```
- **Delete a category:**
  ```
  DELETE /api/categories/<id>/
  ```

## Postman Collection
A Postman collection with sample requests is included in the root folder of the project.
