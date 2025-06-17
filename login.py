from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def form():
    return '''
        <form action="/login" method="post">
            <input type="text" name="nm">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/success/<name>')
def success(name):
   return f'Welcome {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success', name=user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success', name=user))

if __name__ == '__main__':
   app.run(debug=True)
