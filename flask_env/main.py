from flask import Flask
from flask import render_template

# creates a Flask application, named app
myapp = Flask(__name__)

# a route where we will display content of .txt via an HTML template
@myapp.route('/', defaults={'filename': 'file1.txt'})
@myapp.route('/<filename>')
#@myapp.route('/<filename>')
def content(filename):
	with open(filename,'r', encoding='utf8', errors='ignore') as fl:
            return render_template('content.html', text=fl.read())
# a route where we will display a welcome message via an HTML template
# @myapp.route('/hello/<user>')
# def hello(user):
#     return render_template('index.html', name = user )

# run the application
if __name__ == "__main__":
    myapp.run(debug=True)
