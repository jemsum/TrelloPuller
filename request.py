import requests
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
	return 'hello world!'

@app.route('/')
def index():
	return 'Index page'

@app.route('/trello')
def trello():
	return requests.get("https://api.trello.com/1/members/me/boards?key=9e1653a1c004bdbd293f9cf2eb88ea30&token=b7321a6f13e34ca5050a7241f8ba64b41f8799245dcf0a9d26dbe6ec2fb50cd8")

if __name__ == '__main__':
	app.run(debug=True)



