from  flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
<<<<<<< HEAD
app.run(host="0.0.0.0",port=8080,debug=True)

=======
    app.run(host="0.0.0.0",port=8080,debug=True)
>>>>>>> fa440460d39b00e8403f2ae76d5112ed569b6cd1
