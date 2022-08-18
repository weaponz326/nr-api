# NrApi

Each netRink suite is given its own seperate django project
All the the projects share the same virtual environment and the same dependencies
This is advantageous in this particular case beceause all the projects use the same dependencies

However, each project will be deployed seperately on a seperate server

## Comands

To create a new project for a suite, navigate to the `projects` folder and create the the project there
```bash
django-admin startproject project_name
```

To run a project, navigate to the root of the project containing the `manage.py` file and run the project
```bash
py manage.py runserver
```

To run a project on a specific port
eg: let's run a project on port '8001' instead of the default port `8000`
```bash
py manage.py runserver 8001
```

To create an app for a project, navigate to the root of the project containing the `manage.py` file and create the project
```bash
py manage.py startapp app_name
```

To create an app in a sub directory, specify the path to the directory as an option
```bash
py manage.py startapp apps/app_name
```


