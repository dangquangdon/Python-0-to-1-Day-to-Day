# Part 10: Migration and Deployment

## Migration

As many of you might have notice, since we moved our files to blueprints, we are unable to access the database from command line anymore.

In this part, we will implement some small changes and add data migrations.

1. in `config/dev.py` let's adjust the location of our database `flaskapp.db`, by changing the environment variable:

```python
SQLALCHEMY_DATABASE_URI = f'sqlite:////{os.path.join(os.getcwd(),"flaskapp.db")}'
```

After this, delete the old database file, hopefully you don't have anything too important there.

2. In your `run.py`, modify it like this

```python
from app import create_app

app = create_app('dev')

if __name__ == '__main__':
    app.run()


```

. Open the terminal or command prompt, and install two new extensions:

- `pip install flask-migrate`

- `pip install flask-script`

Then create `manage.py`, let's adjust the content

```python
from app import db
from run import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate = Migrate(app, db, render_as_batch=True)
    else:
        migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__=="__main__":
    manager.run()
```

Flask Migrate will be the version control of your database from now on. If you make any changes such as add columns, modify columns' names and so on, you don't need to delete the old one and create a new one anymore.

Flask Script will give you some more command, we will go through some basic commands together.

3. After the two step above, now you can open your terminal/command prompt, activate your virtualenv and type

`python manage.py` and press `Enter`. You will see that Flask will give you thee options: - `db` to perform database migrations

- `shell` to activate python interpreter inside Flask application context - `runserver` to run flask app

Since we already deleted our old database file, before we can start the app, we have to create a new one.

- run `python manage.py db init`, it will create a folder `migrations` which will store all versions of your database. **only run in the first time**
- next `python manage.py db migrate`, it will start migrating and push the changes to staging area (sound familiar?)
- last `python manage.py db upgrade`, your changes will be taken effect, the new database file will be created if this is the first time running.

Now if you want to start your server, run `python manage.py runserver`

If you want to access your database from terminal and practicing the Flask_SQLAlchemy syntax, run `python manage.py shell` and start importing `User` or `Post` and play around with it

4. From now on, everything you make any changes such as add new tables or columns in your database, you can start runing

   - `python manage.py db migrate`
   - then `python manage.py db upgrade`

5. To get ready for deployment, let's go to `config/prod.py` to setup our production configuration as following

```python
import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)


DEBUG = True
SECRET_KEY = config.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = '587'
MAIL_USE_TLS = True

MAIL_USERNAME = config.get('MAIL_USERNAME')
MAIL_PASSWORD = config.get('MAIL_PASSWORD')

```

In our production, we will set all of the configuration variables in a `json` file

We will also use PostgreSQL for the production database, therefore we will need to save our credential in the `json` file

## Deployment

### Create and access Virtual Machine

As mentioned before, we will deploy this app to a virtual machine on Microsoft Azure cloud service.

- Go to [Microsoft Azure](https://azure.microsoft.com/en-us/) to register a free account (with \$200 credit for free) then login the portal
- Once you're in Microsoft Azure Portal, you will see a lot of products/services they offer.
- Click the `Virtual Machines` service, and `Add` a new virtual machine and fill in all the fields required.
- The important one you should pay attention is `*Image`, choose `Ubuntu Server 18.04 LTS`, and click to the `*Size` change it to the cheapest one you find in the table.
- In the `ADMINISTRATOR ACCOUNT` fields, choose `Password` and then create your `username` and `password`
- In the `INBOUND PORT RULES` and choose `Allow selected ports`. In the next field, choose `SSH`
- Click `Next` to go to the next settings
- We won't change any of these, just keep clicking `Next` to the end, which is `Review + create`
- After reviewing all the information, click `Create`
- Wait for it !

We will connect to this Virtual machine via SSH connection. If you're on MacOS or Linux, you're fine. But if you're on Windows, please follow this tutorial to [install PuTTY](https://www.ssh.com/ssh/putty/windows/install)

Once you get the notification from Microsoft Azure that it has finished creating a virtual machine for you, click `Go to Source`

- In there, you will see some information about your virtual machine.
- Click `Connect` and copy the last field `Login using VM local account`
- If you're using PuTTY, you just need to copy the `Public IP adress` that you see in the dashboard, then paste it to `Host Name (or IP address)` field and click `Open`
- If you're using MacOS or Linux, just paste what you've copy from `Login using VM local account` to your terminal
- Say `yes`
- Then give the password that you've created in `ADMINISTRATOR ACCOUNT` fields before
- Now you have successfully logged into your virtual machine and you can use it.

### Basic configuration

- First, let's run `sudo apt update` and after it's finished, run `sudo apt upgrade` to get the system up to date. This might take a few minutes
- Next, run `sudo nano /etc/hosts`, when nano opens the `hosts` file, below the `localhost`, add a new line and write down your VM public IP address and your VM name, separated by a `space` (follow the format of the line above it)
- Back to Microsoft Azure Portal, In your Dashboard, find `Networking` in the sidebar and click it
- In the `Inbound port rules` tab, click the button `Add inbound port`.
- Keep the default values in the first 3 fields, in `Destination port Ranges`, put `5000`
- Protocol `TCP`
- Action `Allow`
- Name `Port_5000`
- Click `Add`

We open the port `5000` of our VM to be able to see the test version of our app before we actually public it to the public port `80`

**Install pip**

- `sudo apt install python3-pip`
- `sudo apt install virtualenv`

**Install PostgreSQL**

- `sudo apt install postgresql postgresql-contrib`

**Login to PostgreSQL and create database and user**

- `sudo -u postgres psql` This command will let you to log in to postgres CLI (Command Line Interface)
- `postgres=# create database your_db_name;` - to create your database
- `postgres=# create user your_name with encrypted password 'your_password';`
- `postgres=# grant all privileges on database your_db_name to your_name`;

### Transferring files to VM

Keep the terminal that you logged in the VM open, and open a NEW TERMINAL. Then navigate to your project folder and activate the virtual environment

- Once you're in your virtual environment, type `pip freeze > requirements.txt`
- A new text file called `requirements.txt` will be created which contains all of the libraries/extensions that we've installed and used for this project.

1. Simple option:

   - For simplicity, you can push this project to your github account. Recommended to do this if you're using Windows

2. Command line option:

   - **This option is only for MacOS and Linux.**
   - In your terminal after creating the `requirements.txt`, move back 1 level `cd ..` , run the following command to transfer your project to your virtual machine:
     `scp -r flaskApp/ username@your.public.ip.address:~/flaskApp`

- Back to your VM terminal, type `ls` to check if the files have been moved there.
- Move into the project folder, and create a virtualenv for it with `virtualenv -p python3 venv`
- run `pip install -r requirements.txt` to install all dependencies of our application

### Setup configuration file

Since our app will not running with the `dev.py` configuration anymore, because we are trying to put it to production. Therefore we will need to setup the `prod.py`.

If in the `dev.py` we set the Environment Variables to store our credentials, in the `prod.py` we actually could do the same, however, we will apply a new way.

- In your VM terminal, let's create a new file called `config.json` with the following command:
  - `sudo touch /etc/config.json`
  - in the `config.json` you are going to write a `json` file like this:
    ```json
    {
      "SECRET_KEY": "your secret key",
      "SQLALCHEMY_DATABASE_URI": "postgresql://user:pass@localhost/dbname",
      "MAIL_USERNAME": "you email",
      "MAIL_PASSWORD": "your password"
    }
    ```
- use `cat run.py` to check the content of the script, if our `config_tye` is still `dev`, we need to use `nano` to change it to `prod`
- run our `python manage.py` command to migrate/upgrade the database, and check `python manage.py runserver` to see if the server is running properly. Fix any errors it shows
- If there's no error, let's make a test to see if we can access to our app from the internet
- We will test it with the command `export FLASK_APP=run.py` , then `flask run --host=0.0.0.0`
- Now open your browser, and put VM ip address there like this `your.public.ip.address:5000`
  - If you can see your app, it've almost done!
  - If you cannot see it, check the errors and fix them.
  - In our VM settings, we've opened the port 5000 therefore now we can access it. If you omit `:5000` it will access port `80` by default, which we haven't opened it yet. We will open port `80` for public access after we finish testing our app.
  - Test all of the functionalities that we've created so far to make sure they're working fine.

### Install Nginx and Gunicorn

- If you've tested and fixed all possible erros, we will install `nginx` and `gunicorn`. Make sure you're still in `(venv)` of your VM terminal

- `sudo apt install nginx`
- `pip install gunicorn`

**In a nutshell**

- **Nginx** will handle serving the static files such as HTML, CSS, etc
- **Gunicorn** will handle the python code when the information is passed by Nginx

#### Nginx Configuration

- Remove the default configuration of Nginx: `sudo rm /etc/nginx/sites-enabled/default`
- Create a new configuration file: `sudo nano /etc/nginx/sites-enabled/flaskapp`

  ```nginx
  server {
      listen 80;
      server_name 40.113.113.213;

      location /static {
          alias /home/your_name/flaskApp/app/static;
  }

      location / {
          proxy_pass http://localhost:8000;
          include /etc/nginx/proxy_params;
          proxy_redirect off;
      }
  }
  ```

- We tell `nginx` to listen to the request comming from `port 80` and set the server name to our VM IP address
- We specify so that `nginx` knows where to find the static file to serve
- Then if there is any thing that need to deal with Python, `nginx` will pass it to `gunicorn` which runs at `port 8000` by default.
- We will have to go back to Microsoft Azure Portal to open `port 80` up. The same as we've done to open `port 5000`, we just change the port value to `80` this time. And also we will set `5000` to `Deny`
- Restart nginx server `sudo systemctl restart nginx`
- So now if you open your browser and put your VM IP address, you will recieve Nginx errer message, so our nginx is running. We can actually try to access our css file type adding the path to the url.

### Start Gunicorn

- To start Gunicorn, run `gunicorn -w 3 run:app`
- `-w 3` means that gunicorn is going to us `3 workers`. See [gunicorn's documentation](https://gunicorn.org/#docs) for more details. Basically, the number of workers is calculated as `2*(number of cores)+1`. In order to know the number of cores your machine is having, type `nproc --all`
- `run:app` means we run `run.py` and the app name is `app` because we name it `app = create_app('prod')` in the `run.py`
- So now after we run `gunicorn -w 3 run:app` you will be able to access your app using IP address.
- However, now we are running it in the foreground, if we turn off the terminal, our app is turned off as well. So what we are going to do next, is to set it up so that it will running in the background.
- We are going to install `supervisor` by `sudo apt install supervisor`
- `sudo nano /etc/supervisor/conf.d/flaskapp.conf` to set up the configuration file.

  ```
  [program:flaskapp]
  directory=/home/your_name/flaskApp
  command=/home/your_name/flaskApp/venv/bin/gunicorn -w 3 run:app
  user=your_name
  autostart=true
  autorestart=true
  stopasgroup=true
  killasgroup=true
  stderr_logfile=/var/log/flaskapp/flaskapp.err.log
  stdout_logfile=/var/log/flaskapp/flaskapp.out.log
  ```

  - We name our program is flaskapp and set the directory that our app is located
  - run the command with gunicorn
  - set auto start and restart if it's crash
  - write the err log and process log to files so that we can comeback and check it anytime

- Now we have to create those log files with follow commands:

  - `sudo mkdir -p /var/log/flaskapp`
  - `sudo touch /var/log/flaskapp/flaskapp.err.log`
  - `sudo touch /var/log/flaskapp/flaskapp.out.log`

- Let's restart out supervisor `sudo supervisorctl reload`

- Now if we reload the page, it's running.

**One note**
Nginx has a default setting with file upload. If you upload a profile picture that is over 2Mbm it will throw an error. Luckily, we can change that:

- `sudo nano /etc/nginx/nginx.conf`
- Scroll down to `http {...`, below the `types_hash_max_size 2048` add a new line `client_max_body_size 5M;` to set the limit to 5Mb, if you want it to be bigger, feel free to change. However, if you remember, our app will automatically resize the picture so that it won't be too big anyway.
- `sudo systemctl restart nginx`

# CONGRATULATION, YOU NOW HAVE A COMPLETE FUNCTIONAL WEBSITE RUNNING

If you have a domain name, we can replace the IP address with the domain name, and setup SSL (https) for it. You can check the instruction in my next note.
