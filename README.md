
## Installation

To get a local copy up and running, follow these simple steps:

Clone the repository:
```bash
git clone https://github.com/seizaku/student_sync.git
```

Navigate to project:
```bash
cd ./student_sync
```

Setup python virtual environment
```bash
pip install pipenv
pipenv shell
```

Install Dependencies:
```bash
pip install requirements.txt
```

Configure settings.py database:
```python
  'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'student_sync_db',
      'USER': 'root',
      'PASSWORD': 'password',
  }
```

Migrate database:
```bash
python manage.py migrate
```

Create super user:
```bash
python manage.py createsuperuser
```

Run the Development Server:
```bash
python manage.py runserver
```