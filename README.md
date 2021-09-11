# What we need🤓🤓
 1. Install **Visual Studio Code**. Yup, the blue one 🤑.
    1. I recommend have installed a [Django Extension](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django) for the instructions being recognized in VSCode.
    2. Also, this [Jinja](https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja) extension helps when we use some instructions on a _static file_.
    3. I almost forgot 😬 It's obvious but we need also the python extension it shows as _recommended_.
Note: If you are too lazy here is a [bundle](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack) with the necessary extensions.
2. Install [Python](https://www.python.org/downloads/) 
2. Install [Django](https://docs.djangoproject.com/en/3.2/intro/install/)
# How to start🤔🤔
After cloning the reposity and opening the project in VisualStudio Code. We'll see this structure and where we have the follow archives.
![Structure of the project](https://i.imgur.com/qJJbWF2.png).

In the first part We have a folder named _bidding_ here is stored our project. And then I'm going to talk about de folder ***Scripts*** It's not always necessary having this folder but to avoid some issues It's better to have a virtual enviroment.
Here is stored some scripts for emulate an eviroment and execute it.

VisualStudio Code way
----
It's the easy way, after opening the project you need to find in the bottom bar somethink like _python_ and select the interpreter wich has a _bidding: venv_ write on it an select it. Or you can type _Ctrl + Shift + P_ and select the interpreter.

It's common to not do this step, but I write it just in case.

If you can do it then We have the same issue 🥴🥴

Commands way
----
### With PowerShell
Open a new terminal with _Ctrl + Shift + ñ_

Type ***bidding\Scripts\Activate.bat***
If it dont work. CRY...
Naah 🤡🤡

### CMD Terminal
Here it's something curious in my case PowerShell doesn't work hahaha so if I write some instructions I need to change the _PowerShell_ terminal to a _cmd_ terminal (We do this just with typing _cmd_). 

The way to execute this project we need to open a new terminal _Ctrl + Shift + ñ_. 

And type ***bidding\Scripts\activate.bat*** 

Finally having activated our virtual environment we type 

***python manage.py runserver*** And we'll have our project running on a local host that we can acceess just going to a favourite web browser and wirte on it http://127.0.0.1:8000/

**NOTE: TO KILL THE PROCESS WE HAVE TO PUSH THIS KEYS IN THE TERMINAL _Ctrl + C_ **
