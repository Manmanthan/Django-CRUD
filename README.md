# Setting up MySQL Database

####Step 1: Create new schema
* Open the MySQL Workbench and create a new schema by clicking the create new schema in the connected server option.
* Select a suitable schema/database name and press apply. This will create the schema and it will appear in the SCHEMAS section of the MySQL workbench.
* In our case the schema name is djangodatabase.

####Step 2: Create authentication user for the schema
* Once the schema is ready create an authentication user and grant privileges to this user.
Create the user by running the following query
> create user dbadmin identified by '12345';
* Grant the privileges by running the following query
> grant all on djangodatabase.* to 'dbadmin'@'%';
* In order to load the newly granted privileges to the user run the following query
> flush privileges;

# Setting up Django Project

####Step 1: Setting up the virtual environment
* Activate your virtual environment and run the following command.
> pip install -r requirements.txt

####Step 2: Installing MySQL Client
* You can install MySQL client directly through pip using the command
> pip install mysqlclient

####Step 3: Updating the Connect String
* Open the settings.py file of the Django project. Update the connection string.
> DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodatabase',
        'USER': 'dbadmin',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

####Step 4: Make Migrations
* Now run the commands
> python manage.py makemigrations

> python manage.py migrate

####Step 5: Run server locally
* Run the following command to run the Django development server.
>python manage.py runserver


# Using the API

####Step 1: Open the REST API
* Open the following link in your browser.
>http://127.0.0.1:8000/

#### Step 2: Use Cases
* To insert, update and select on customers open
> http://127.0.0.1:8000/customers/

* To insert, update and select on products open
> http://127.0.0.1:8000/products/

* To check the order history of given customer open
> http://127.0.0.1:8000/orders/

* Use filter tab to search the customer name.