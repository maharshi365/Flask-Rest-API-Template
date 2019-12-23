# Flask-Rest-API-Template
This is a basic flask api template that can be used to build flask applications

# Usage Instructions
## Startup
1. Change directory to Flask_App and then run `python -m pip install -r requirements.txt`
2. Once all requirements are installed do `python run.py`
3. Go to [localhost:5000] for the swagger page

## New Models
1. Database models are defined inside Flask_App/Main/Models
2. They are automatically initialized inside of the database when the application is started

## New Controllers
1. Endpoint controllers are defined inside Flask_App/Main/Controllers
2. api objects must be defined inside of the controller module
3. api objects must be imported inside Flask_App/Main/__init__.py
    1. Import the api object in create_app
    2. Add the api as a namespace to the api for endpoint creation

## New Services
- Services can be defined as needed. They are not needed as part of the Flask Startup


