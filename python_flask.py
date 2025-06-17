#flask 
#Flask is a web application framework written in Python
#web framework represents a collection of libraries and modules that help you build web applications
#It is developed by Armin Ronacher, who leads an international group of Python enthusiasts named Pocco.
#Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects.


#WSGI
#Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development. WSGI is a specification for a universal interface between the web server and the web applications.

#Werkzeug
#It is a WSGI toolkit, which implements requests, response objects, and other utility functions. This enables building a web framework on top of it. The Flask framework uses Werkzeug as one of its bases.

#Jinja2
#Jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages.

#Flask is often referred to as a micro framework. It aims to keep the core of an application simple yet extensible. Flask does not have built-in abstraction layer for database handling, nor does it have form a validation support. Instead, Flask supports the extensions to add such functionality to the application. Some of the popular Flask extensions are discussed later in the tutorial.

####
#steps to perform flask installation
#
### ✅ Setting Up and Running a Flask App in VS Code (Windows + PowerShell)
#
#### 🔹 1. **Check Python Installation**
#
#Open terminal in VS Code:
#
#```powershell
#python --version
#```
#
#Ensure Python is installed and the version is 3.13.x or similar.
#
#---
#
#### 🔹 2. **Create Project Folder Without Spaces (Recommended)**
#
#To avoid issues with paths:
#
#```powershell
#cd D:\
#mkdir Celebal_DS
#cd Celebal_DS
#```
#
#---
#
#### 🔹 3. **Create a Virtual Environment**
#
#```powershell
#python -m venv venv
#```
#
#This creates a `venv` folder containing an isolated Python environment.
#
#---
#
#### 🔹 4. **Fix PowerShell Script Execution Policy**
#
#If activation fails due to permissions, open PowerShell as Administrator and run:
#
#```powershell
#Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
#```
#
#Type `Y` and press Enter.
#
#---
#
#### 🔹 5. **Activate the Virtual Environment**
#
#Back in VS Code terminal:
#
#```powershell
#.\venv\Scripts\Activate.ps1
#```
#
#You should now see `(venv)` in the terminal prompt.
#
#---
#
#### 🔹 6. **Install Flask**
#
#Install Flask inside the virtual environment:
#
#```powershell
#pip install flask
#```
#
#---
#
#### 🔹 7. **Create Your Flask App File**
#
#Create a file named `hello.py` with the following content:
#
#```python
#from flask import Flask
#app = Flask(__name__)
#
#@app.route('/')
#def hello_world():
#    return 'Hello World'
#
#if __name__ == '__main__':
#    app.run(debug=True)
#```
#
#---
#
#### 🔹 8. **Run the Flask App**
#
#```powershell
#python hello.py
#```
#
#Output:
#
#```
# * Running on http://127.0.0.1:5000/
#```
#
#Open this link in your browser to see your app.
#
#---
#
#### 🔹 9. **(Optional) Save Installed Packages**
#
#Create a `requirements.txt` file for your project:
#
#```powershell
#pip freeze > requirements.txt
#### 🔹 10. **Deactivate Virtual Environment**
#
#When you’re done:
#
#```powershell
#deactivate