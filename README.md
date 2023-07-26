# ignite
Ignite website for the USU Ignite program

## To start website
To start website 

create a python virtual environment
```
python -m venv venv
```

activate the virtual environment
```
source venv/bin/activate
```

install depedenices
```
pip install Django Pillow
```

clone the project
```
git clone https://github.com/marksoulier/ignite.git
```

run the server (go to where manage.py is located)
```
python manage.py runserver
```

go to the website that the terminal outputs


Live website being hosted at: ignitengineering.com











Notes:


When starting a new project have the urls set up to run the veiws. Then link the app urls to the main website urls.

to run website start from base directroy and run
```
python manage.py runserver
```

Data base will need to be updated to something bigger like mysql or postgresql. This can be done in the settings.py in ignite folder.

this may be important for managing files
django.contrib.staticfiles 

3 steps for making changes to models 

Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.

models can be applied so several objects can be connected to another object. This is done by using a foreign key.

go to the admin site.
Run the server and add /admin to the url. 
username: admin
password: password



good site for learning the basics: https://docs.djangoproject.com/en/4.2/intro/tutorial01/


views is the way that django shows content to the user.

each view is a python function that takes a web request and returns a web response.

Django will choose a view by examining the URL that’s requested (to be precise, the part of the URL after the domain name).