from  flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index File'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/talyta')
def user():
    return 'user talyta'

@app.route('/post/80')
def post():
    return 'Post 80'

if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)

