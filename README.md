# Django Template

This is a starter template for Django projects.

## Prerequisites

- Python 3.10 or later
- Virtualenv

## Installation

1. Clone this repository.
2. Create a virtual environment: `$ python3 -m venv venv`
3. Activate the virtual environment: `$ source venv/bin/activate`
4. Install dependencies: `$ pip install -r requirements.txt`

## Development

### Environment

The application runs in multiple environments such as DEV and PROD. All environment variables used in this application are available in the `.env.example` file. Copy it to `.env.local` and configure your own variables.

To load environment variables from both files, run:

    $ source .env
    $ source .env.local

### Database

The first time you run the application, apply the database migrations and create a superuser account:

    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py createsuperuser

### Run server

Start the development server:

    $ python manage.py runserver

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.