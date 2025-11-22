# Mkuu Backend API

A Django REST Framework based backend API for the Mkuu platform, providing user authentication and account management functionality.

## Features

- User registration and authentication
- JWT token-based authentication
- RESTful API endpoints
- Social authentication support
- Documentation with Swagger/OpenAPI

## Prerequisites

- Python 3.8+
- PostgreSQL (recommended) or SQLite
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add the following variables:
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3  # For development
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

Once the server is running, you can access the following:

- API Documentation: `http://localhost:8000/swagger/` or `http://localhost:8000/redoc/`
- Admin Interface: `http://localhost:8000/admin/`

## Project Structure

```
backend/
├── accounts/           # User authentication and management app
├── api/                # Main API endpoints
├── core/               # Project configuration
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
```

## Environment Variables

| Variable       | Description                     | Default          |
|----------------|---------------------------------|------------------|
| SECRET_KEY    | Django secret key              | -               |
| DEBUG         | Enable debug mode              | False           |
| DATABASE_URL  | Database connection string     | sqlite:///db.sqlite3 |

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
