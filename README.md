# Heron's Formula Calculator
A simple webapp to calculate area of a triangle using Heron's formula made using Flask and MySQL. This is made because I was too lazy to do all the calculations on a calculator.

# Getting Started
## Using Docker
### 1. Build the image
Run `docker build -t herons-calculator .` from the directory
### 2. Create a container with the image created
Run `docker run -d -p 8000:8000 herons-calculator`.
You can specify a port of your own.
### 3. Go to http://localhost:8000

> Alternatively, you could run the 'build.sh' script to build and run the docker container automatically. Run `chmod +x build.sh` first to give the file permission to execute.
## Installing manually
### 1. Make sure python is installed
Install [Python](https://python.org) and [pip](https://https://pip.pypa.io/en/stable/installation/)
### 2. Install the requirements
Run `pip install -r requirements.txt` in the git directory
### 3. Start webserver
Run `gunicorn app:app` and open the link shown in your terminal window

That's all you have to do to get this running

# Tech stack
- Flask 
- Bootstrap 5.1.3
- SQLite3