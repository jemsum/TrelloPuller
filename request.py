import requests
from flask import Flask
app = Flask(__name__)

#TODO need to pull this in from config
#api_url=somestring

@app.route('/hello')
def hello_world():
	return 'hello world!'

@app.route('/')
def index():
	return 'Index page'

@app.route('/trello')
def trello():
	return requests.get(api_url)

if __name__ == '__main__':
	app.run(debug=True)



