# Django-project1

Deployed on heroku 
https://shareyourproject.herokuapp.com


# How to use this repo

> Clone the repo

> Outside the folder create a virtual environment 

    virtualenv venv

> Activate virtual env

    venv\Scripts\activate (on Windows)
    
> cd into the main folder. You'll see a requirements folder. Install the requirements.

    pip install -r requirements.txt
    
>  Run the server

    python manage.py runserver 

# Any changes in model class should be saved with -

    python manage.py makemigrations
    python manange.py migrate
    
# Layout information

> Project name: dj1

> App name: products

> template location: products/templates
