from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask App! Try /user/admin or /user/advika'

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return f'Hello {guest} as Guest'

@app.route('/user/<name>')
def hello_user(name):
   if name == 'admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest=name))

if __name__ == '__main__':
   app.run(debug=True)


#➡️ http://127.0.0.1:5000/
#➡️ http://127.0.0.1:5000/user/admin
#➡️ http://127.0.0.1:5000/user/advika