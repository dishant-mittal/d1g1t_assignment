# d1g1t_assignment

## Overview

This is Django REST assignment for D1g1t.
The app uses Django REST inbuilt UI for getting/posting the json data. There is a very basic customized landing page which I have
created from where you may login to authenticate yourself (If not authenticated already) OR you may get avg. happiness statistics.
You must authenticate yourself and login to post your happiness level for a day. An employee can only post the happiness level only
once per day.
Please use the following json format to post your happiness level (can range from 1-10):
{
"level": 4
}


**Important Note**

I am assuming that whoever wants to install this application is having anaconda installed on his/her system.
Please use the this link for installing anaconda if  : https://docs.anaconda.com/anaconda/install/
Also, you don't need to have any explicit database setup for running this app. It uses sqlite which is the default lightweight
database for Django.
I have used Django's inbuilt authentication which some customizations.

## Directory Structure

- requirmenets.txt: contains all the requirements which would be necessary for operation of this app.
- happiness: App to store and operate on the happiness model.
- teams: App to store and operate on the teams model.
- employees: App to store and operate on the employee model if necessary.
- logs: Contains logs for the entire project. You can change the log levels by setting log levels in settings.py in test_d1g1t app.

## Usage

1. Clone the repo using command:

        git clone git@github.com:dishant-mittal/d1g1t_assignment.git

2. Go inside the directory d1g1t_assignment
3. Initiate a new conda environment and install all the dependencies within it using:

        conda config --append channels conda-forge

        conda create --name env_name --file requirements.txt

4. Activate the environment using:

        source activate env_name

5. Run the following commands:

        python manage.py check

        python manage.py makemigrations employees happiness teams

        python manage.py makemigrations

        python manage.py migrate

        python manage.py test

        python manage.py createsuperuser

6. Enter the credentials and details for the superuser and create it.
7. Type this command for running the django-lightweight server (you may change the port if necessary):

        python manage.py runserver 8080

8. Go the your web browser and enter this URL:

        http://127.0.0.1:8080/admin

9. At this point you can create the additonal Users ---> then create teams ---> then create/assign employees to the teams and users already
created. You may go to the homepage of the website from: http://127.0.0.1:8080/   and start using the app





## Contact Person
- Dishant Mittal (also the author) - dishantmittal31@gmail.com