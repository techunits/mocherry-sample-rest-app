
# mocherry-sample-rest-app
This app will demonstrate the implementation of an REST based webservice using MoCherry framework. We have also incorporated an initializer command to bootstrap the application with some dummy data to start your tests immediately.

**Demo URL:** http://fake-rest-api.techunits.com

#### Setup Guide
In order to setup this applicaiton you have to go through following steps:
```sh
# create virtual environment
$ python -m venv testenv

# activate virtual environment
$ source testenv/bin/activate

# install required dependencies
$ pip install git+https://github.com/techunits/mocherry.git
$ pip install faker  # this will be required to generate fake dummy data for initializer
```

#### Application Initializer
```sh
$ python manage.py initializer
```

The application is having following components(CRUD)

 - Create article
 - List articles
 - View article details
 - Delete article
