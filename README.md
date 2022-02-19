# practice_django_todoapp
It's been a while (more than 4 months) since I last programmed. Guess let's restart from the classic old Todo App, but using Django!
<br>
# PREREQUISITES
This project assumes you have the following installed in your machine:
1. Windows Subsystem for Linux 2 (WSL2) or Linux OS (Native/Dual Boot). I'm using Ubuntu 20.04 for this purposes.
2. Python 3.8.x (with `pip3` & `virtualenv` installed)
3. PostgreSQL 12.x
<br>
# IMPORTANT PACKAGES TO INSTALL
1. `django`
2. `djangorestframework` (to help structure the app to be like your typical, JavaScript-based REST-API structure)
3. `django-cors-headers` (to manage the separation of concerns between front & backend, and its basic security configuration)
4. `django-filter` (to help us managing filters when scouring the databases)
5. `coverage` (for testing purposes)
6. `pytz` (for timezone management)
7. `psycopg2-binary` (must install this before installing Python's PostgreSQL package, `psycopg2`)
8. `psycopg2` (this IS the PostgreSQL package for Python)
<br>
# PREPARATIONS
1. Create an empty folder to 'house' the virtual environment necessary for this app (e.g. `my_django_house`)
2. Go to the directory `my_django_house` and generate the virtual environment
    `python3 -m venv .` (the `.` syntax signifies current directory we are visiting)
3. Be sure to be in the same directory as the `bin` file, then activate the virtual environment
    `source ./bin/activate`
4. Install the important packages above in the FOLLOWING ORDERS using `pip3 install` command
5. Setup the Django project for this app (I'm choosing the name `todoapp` as the 'table' for the project itself)
    `django-admin startproject todoapp`
6. Go into the project directory (`todoapp` in this case), be sure to locate `manage.py` and initiate the *proper* app for this backend/API. I'm using the name `todoapp_backend` for this purpose.
    `python3 manage.py startapp todo_backend`. This `todoapp_backend` directory will hosts the `models.py`, `views.py`, `tests.py`, anything we associate with an app's basic structure.
7. Go into `todoapp/settings.py`, and be sure to include the following inside `DATABASES` and `INSTALLED_APPS`:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todoapp_backend.apps.TodoappBackendConfig',
    'rest_framework',
    'corsheaders',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': <your_preferred_database>,
        'USER': <your_preferred_username>,
        'PASSWORD': 'default',
        'HOST': '127.0.0.1' # or other host IP of choice,
        'PORT': 5432 # or other port of choice,
    }
}

```

You are now ready to work on or review the functionalities.

<br>

# ENDPOINTS

## TASKS
1. CREATE: `tasks/create`
    * Method: `POST`
    * URL Params: None
    * Header Params: 
    * Query Params: None
    * Form/Body Params:
        - `title` string (required)
        - `description` string (required)
    * Success Response:
        - Code: 201
        - Example: 
        ```
        {
            "id": 6,
            "title": "whassup",
            "description": "task example",
            "created_at": "2022-02-19T22:16:03.171677+07:00",
            "completed": false,
            "last_modified_at": "2022-02-19T22:16:03.171757+07:00"
        }
        ```
    * Error Response(s):
        - Code: 400
        - Example: `"INVALID ENTRY FORM FIELD(S) INPUT"`

2.  GET ONE: `tasks/<pk>/getOne`
    * Method: `GET`
    * URL Params: `pk` integer
    * Header Params: 
    * Query Params: None
    * Form/Body Params: None
    * Success Response:
        - Code: 200
        - Example: 
        ```
        {
            "id": 6,
            "title": "whassup",
            "description": "task example",
            "created_at": "2022-02-19T22:16:03.171677+07:00",
            "completed": false,
            "last_modified_at": "2022-02-19T22:16:03.171757+07:00"
        }
        ```
    * Error Response(s):
        - Code: 404
        - Example: `"ENTRY NOT FOUND"`

3.  LIST ALL: `tasks/getList`
    * Method: `GET`
    * URL Params: `pk` integer
    * Header Params: 
    * Query Params: None
    * Form/Body Params: None
    * Success Response:
        - Code: 200
        - Example: 
        ```
        [
            {
                "id": 5,
                "title": "example title",
                "description": "hello world",
                "created_at": "2022-02-19T22:16:03.171677+07:00",
                "completed": false,
                "last_modified_at": "2022-02-19T22:16:03.171757+07:00"
            },
            {
                "id": 6,
                "title": "whassup",
                "description": "task example",
                "created_at": "2022-02-19T22:16:03.171677+07:00",
                "completed": false,
                "last_modified_at": "2022-02-19T22:16:03.171757+07:00"
            },
            {
                "id": 4,
                "title": "what is this?",
                "description": "seriously, mate?",
                "created_at": "2022-02-16T22:59:11.054435+07:00",
                "completed": false,
                "last_modified_at": "2022-02-16T23:32:06.902076+07:00"
            }
        ]
        ```

4. UPDATE: `tasks/<pk>/edit`
    * Method: `PUT`
    * URL Params: `pk` integer
    * Header Params: 
    * Query Params: None
    * Form/Body Params:
        - `title` string (optional)
        - `description` string (optional)
    * Success Response:
        - Code: 200
        - Example: 
        ```
        {
            "id": 4,
            "title": "what is this?",
            "description": "task example3",
            "created_at": "2022-02-16T22:59:11.054435+07:00",
            "completed": false,
            "last_modified_at": "2022-02-19T23:12:22.928593+07:00"
        }
        ```
    * Error Response(s):
      1.  Code: 404
          Example: `"ENTRY NOT FOUND"`
      2.  Code: 400
          Example: `"FORBIDDEN INPUT FIELD: ['id', 'created_at']"`

5.  DROP: `tasks/<pk>/drop`
    * Method: `GET`
    * URL Params: `pk` integer
    * Header Params: 
    * Query Params: None
    * Form/Body Params: None
    * Success Response:
        - Code: 204
        - Example: `"DROP ENTRY SUCCESSFUL FOR ID: 4"`
    * Error Response(s):
        - Code: 404
        - Example: `"ENTRY NOT FOUND"`