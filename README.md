# Garden Diary API

![API welcome message](assets/Printscreens/API/welcome-message.jpg)

[Garden diaries API](https://garden-diary-api.herokuapp.com/)

[Garden diaries frontend website](https://garden-diary.herokuapp.com/)

## Table of contents
- [Garden diaries API](#garden-diary-api)
- [Project](#project)
    - [Objective](#objective)
    - [Site user goal](#site-user-goal)
    - [Site owner goal](#site-owner-goal)
- [Technology](#technology)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
- [Project management](#project-management)
    - [Github project board, user stories, issues and milestones](#github-project-board-user-stories-issues-and-milestones)
- [Features](#features)
    - [Profiles](#profiles)
    - [Posts](#posts)
    - [Likes](#likes)
    - [Comments](#comments)
    - [Followers](#followers)
    - [Plants](#plants)
    - [Tasks](#items)
    - [Items](#items)
- [Testing](#testing)
    - [Automated tests](#automated-tests)
    - [Manual testing](#manual-testing)
    - [PEP8 Python linter](#pep8-python-linter)
- [Deployment](#deployment)
    - [Github & Gitpod](#github--gitpod)
    - [Create a Django rest framework project](#create-a-django-rest-framework-project)
    - [ElephantSQL](#elephantsql)
    - [Heroku](#heroku)
- [Credits](#credits)

# Project

## Objective
The objective of this project was to create the backend API for a fifth portfolio submission for Code Institutes fullstack developer program.
Among following the projects assessment criteria, the API needed to be built using Django rest framework and other appropriate dependencies, and connected to a separate [frontend website](https://garden-diary.herokuapp.com/).
The application needed to have complete CRUD (create, read, update and delete) functionality for users to work with data from the API.

**The project is partly based on the Code Institute Django rest framework course material**, using some of the code provided there, with additional functionality added by me.

# Technology

## Languages
- Python
- Git

## Framework
- Django rest framework
- Django

## Other software and dependencies
- Cloudinary
- Pillow
- psycopg2
- Gunicorn
- Django Allauth

# Project management

## Github project board, user stories, issues and milestones
Garden Diaries was developed using an agile methodology, using Github issues and projectboard to track tasks during the project.

- [User stories](https://github.com/EmelieMarkkanen/p5-garden-diary-api/issues)
- [Project board](https://github.com/users/EmelieMarkkanen/projects/6/views/1)

# Features
Garden diaries API consists of eight apps, with their own unique model, views, urls and serializers.

A superuser can log in through the Django adminsite to access the backend and administer the User model. 
Other user can access the API data through https://garden-diary-api.herokuapp.com/ and the corresponding url for each API endpoint. 

- [Profiles](https://garden-diary-api.herokuapp.com/profiles/)
- [Posts](https://garden-diary-api.herokuapp.com/posts/)
- [Likes](https://garden-diary-api.herokuapp.com/likes/)
- [Comments](https://garden-diary-api.herokuapp.com/comments/)
- [Followers](https://garden-diary-api.herokuapp.com/followers/)
- Plants: the plants data is only accessible to the owner of the plant post, and can be accessed through the frontend website.
- Tasks: the task data is only accessible to the owner of the task post, and can be accessed through the frontend website.
- Items: the item data is only accessible to the owner of the item post, and can be accessed through the frontend website.

# Testing

## Automated tests
A limited amount of automated testing have been made for this API project, where I instead focused on the manual testing through the frontend Garden Diaries application. 
Due to time constraints I have added a few automated tests to the Plants [model](plants/test_models.py) and [views](plants/tests_views.py).

In the future I would add automated tests to all sections, as well as test the API through for example **[Postman API platform](https://www.postman.com/)**.

## Manual testing
Manual testing was done through the Django Rest Framework admin site throughout development. Manual testing have also been done through the [Garden diary frontend website](https://garden-diary.herokuapp.com/), by sending and fetching data from the API throughout development.

All API endpoints pass manual testing by posting, retrieving, updating and deleting posts via the frontend website, as well as through the Django rest framework admin site. 

Manual testing report from the frontend can be read **[here](https://github.com/EmelieMarkkanen/p5-garden-diary/blob/main/TESTING.md)**.

## PEP8 python linter
I used the [Code Institute Python linter](https://pep8ci.herokuapp.com/#) to test all [Garden diary API python code](assets/Printscreens). Some errors with too long lines and trailing whitespaces were corrected.

Results from linter can be found **[here](assets/Printscreens)**.

# Deployment

## Github & Gitpod
I created a repository in Github, named it ´p5-garden-diary-api´, and used the template [Code-Institute-Org/ci-full-template](https://github.com/Code-Institute-Org/ci-full-template).

- Once the repository is created, click the green button to the right (Gitpod) to open a new Gitpod workspace. 
- To open and work on the project it is best to open the workspace from Gitpod workspaces (rather than Github), this will open your previous workspace rather than creating a new one. You should pin the workspace. 
- Committing changes should be done often and should have clear messages. Use the following commands to make your commits:
    - `git add .`: adds all modified files to a staging area
    - `git commit -m "A message explaining your commit"`: commits all changes to a local repository.
    - `git push`: pushes all your committed changes to your Github repository.
- While working on the project I used the Gitpod development server to view the website in action. To start the development server run the following command: `Python3 manage.py runserver`. 

## Create a Django rest framework project
- Install Django and supporting libraries. I've used Gunicorn, Cloudinary and psycopg2, Pillow and Allauth to start. 
- In the terminal of the Gitpod workspace type django-admin startproject 'project_name' - project_name is desired project name
- In the terminal of the Gitpod workspace type python3 manage.py startapp 'app_name' - app_name is desired app name 
- Create a Requirements.txt file (type pip3 freeze --local > requirements.txt), a env.py file and Procfile on the top level of the project directory. 
- In settings.py add the installed apps names into the installed apps array variable and save the file.
- Move the SECRET KEY to the env.py file, and add the DATABASE URL, ALLOWED_HOST, DEV and CLOUDINARY URL as well. 
- Migrate changes by using the command python3 manage.py migrate.

## Elephant SQL
- Log into ElephantSQL or create new account.
- Click to create new instance and set up the plan by giving it a name, I selected the tiny turtle plan. 
- Select a region (data center) closest to your location. 
- Click review, check that all the details are correct and then click create instance. 
- Return to the ElephantSQL dashboard and click on the database instance name for the project.
- Copy the ElephantSQL database URL that begin with 'postgres://' using the copy icon. 

## Heroku
- Log into Heroku or create an account.
- Click ´New´ create new heroku app. Give the app an app name and select your region, I chose Europe. 
- Open the app settings tab and click ´Reveal config vars´
- Add a config var called ´DATABASE_URL´ and paste in the ElephantSQL database URL
- Add the config var ´SECRET KEY´ with the secret key from the Django app settings.py file. It is recommended to create a new secret key for safety purposes. 
- Add the config vars ´CLOUDINARY_URL´, ´DATABASE_URL´, ´ALLOWED_HOST´, ´CLIENT_ORIGIN´, ´CLIENT_ORIGIN_DEV´ and ´DISABLE_COLLECTSTATIC´. 
- Under the project deploy tab, select GitHub for the deployment method. Search for the repository name and click connect. Scroll down to the manual deployment section and click deploy branch. Make sure you have the main branch selected. 

# Credits
- [Heroku](https://heroku.com/)
- [ElephantSQL](https://www.elephantsql.com/)
- [Django Project](https://www.djangoproject.com/)
- [Django packages](https://djangopackages.org/)
- [Django snippets](https://djangosnippets.org/)
- [Cloudinary](https://cloudinary.com/)